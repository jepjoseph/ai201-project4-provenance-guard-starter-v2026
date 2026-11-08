#!/usr/bin/env python3
"""Unit 8 Milestone 3: appeal and invalid-submission baseline evaluation."""

import argparse
import datetime as dt
import json
import uuid
from pathlib import Path

import requests
import config

ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"

VALID_TEXT = (
    "During a programming assignment, I reviewed the requirements, "
    "tested the implementation with several examples, and documented "
    "the results. When a test failed, I inspected the input and output "
    "before making a small correction. This process helped me understand "
    "how careful validation improves the reliability of software systems."
)


def invalid_cases():
    return [
        ("missing_text", {}),
        ("empty_text", {"text": ""}),
        ("whitespace_only", {"text": "   \t  "}),
        ("null_text", {"text": None}),
        ("numeric_text", {"text": 123}),
        ("boolean_text", {"text": True}),
        ("array_text", {"text": ["hello"]}),
        ("object_text", {"text": {"value": "hello"}}),
        ("malformed_json", None),
        ("oversized_probe", {"text": "A" * (config.MAX_TEXT_LENGTH + 1)}),
    ]


def send(session, url, body, creator, timeout, malformed=False):
    try:
        if malformed:
            response = session.post(
                url,
                data='{"text": "unfinished"',
                headers={"Content-Type": "application/json"},
                timeout=timeout,
            )
        else:
            payload = dict(body)
            payload["creator_id"] = creator
            response = session.post(url, json=payload, timeout=timeout)

        try:
            data = response.json()
        except ValueError:
            data = {"raw_response": response.text[:500]}

        return {"status": response.status_code, "response": data}
    except requests.RequestException as exc:
        return {"status": None, "error": str(exc)}


def audit_entries():
    path = config.AUDIT_LOG
    if not path.exists():
        return []
    entries = []
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            entries.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return entries


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--label", default="before")
    parser.add_argument(
        "--url",
        default=f"http://{config.HOST}:{config.PORT}",
    )
    parser.add_argument("--timeout", type=float, default=120)
    args = parser.parse_args()

    if args.trials != 3:
        raise SystemExit("Acceptance evaluation requires exactly 3 trials.")

    health = requests.get(f"{args.url}/health", timeout=10)
    health.raise_for_status()
    health_data = health.json()
    if not health_data.get("ok") or not health_data.get("rate_limiting"):
        raise SystemExit("Health check or rate-limiting verification failed.")

    RESULTS.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    run_id = uuid.uuid4().hex[:10]
    now = dt.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    path = RESULTS / f"run_extended_{now}_{args.label}.md"

    report = {
        "run_id": run_id,
        "timestamp": dt.datetime.now(dt.timezone.utc).isoformat(),
        "service": args.url,
        "trials": [],
        "notes": [
            "Existing application configuration was not modified.",
            "2001 characters is a provisional oversized probe, "
            "not an established documented maximum.",
            "Criterion 5 cannot receive a complete PASS without "
            "a documented and enforced maximum length.",
        ],
    }

    for trial_number in range(1, args.trials + 1):
        print(f"\n=== TRIAL {trial_number}/3 ===", flush=True)
        prefix = f"ext_{run_id}_t{trial_number}"
        trial = {
            "trial": trial_number,
            "appeals": [],
            "invalid_inputs": [],
        }

        # Criterion 4: ten real submissions followed by ten appeals.
        for index in range(1, 11):
            creator = f"{prefix}_appeal_{index}"
            submission = send(
                session,
                f"{args.url}/submit",
                {"text": VALID_TEXT},
                creator,
                args.timeout,
            )
            content_id = submission.get("response", {}).get("content_id")

            if submission["status"] == 200 and content_id:
                try:
                    response = session.post(
                        f"{args.url}/appeal",
                        json={
                            "content_id": content_id,
                            "reasoning": (
                                f"Valid appeal evaluation trial "
                                f"{trial_number}, case {index}."
                            ),
                        },
                        timeout=args.timeout,
                    )
                    appeal = {
                        "status": response.status_code,
                        "response": response.json(),
                    }
                except (requests.RequestException, ValueError) as exc:
                    appeal = {"status": None, "error": str(exc)}
            else:
                appeal = {
                    "status": None,
                    "error": "Original submission did not succeed.",
                }

            matching = [
                entry for entry in audit_entries()
                if entry.get("content_id") == content_id
                and entry.get("event") == "appeal"
                and entry.get("status") == "under_review"
            ] if content_id else []

            passed = (
                submission["status"] == 200
                and appeal["status"] == 200
                and appeal.get("response", {}).get("content_id") == content_id
                and appeal.get("response", {}).get("status") == "under_review"
                and bool(matching)
            )

            trial["appeals"].append({
                "case": index,
                "content_id": content_id,
                "submission": submission,
                "appeal": appeal,
                "matching_audit_entries": len(matching),
                "pass": passed,
            })
            print(f"  Appeal {index}/10: {'PASS' if passed else 'FAIL'}",
                  flush=True)

        # Criterion 5: ten predefined invalid requests, each followed
        # immediately by a valid request using a distinct creator ID.
        for index, (name, body) in enumerate(invalid_cases(), 1):
            invalid_creator = f"{prefix}_invalid_{index}"
            invalid = send(
                session,
                f"{args.url}/submit",
                body,
                invalid_creator,
                args.timeout,
                malformed=(name == "malformed_json"),
            )

            recovery = send(
                session,
                f"{args.url}/submit",
                {"text": VALID_TEXT},
                f"{prefix}_recovery_{index}",
                args.timeout,
            )

            rejected = (
                isinstance(invalid["status"], int)
                and 400 <= invalid["status"] < 500
            )
            recovered = (
                recovery["status"] == 200
                and bool(recovery.get("response", {}).get("content_id"))
            )

            trial["invalid_inputs"].append({
                "case": name,
                "invalid": invalid,
                "recovery": recovery,
                "rejected_with_4xx": rejected,
                "recovered": recovered,
                "pass": rejected and recovered,
            })

            print(
                f"  Invalid {index}/10 ({name}): "
                f"HTTP {invalid['status']}, "
                f"recovery {recovery['status']}",
                flush=True,
            )

        trial["criterion_4_pass"] = all(
            row["pass"] for row in trial["appeals"]
        )
        trial["criterion_5_observed_checks_pass"] = all(
            row["pass"] for row in trial["invalid_inputs"]
        )
        report["trials"].append(trial)

    criterion_4 = all(
        t["criterion_4_pass"] for t in report["trials"]
    )
    criterion_5_checks = all(
        t["criterion_5_observed_checks_pass"]
        for t in report["trials"]
    )

    report["verdicts"] = {
        "criterion_4": "PASS" if criterion_4 else "FAIL",
        "criterion_5_observed_requests": (
            "PASS" if criterion_5_checks else "FAIL"
        ),
        "criterion_5_full_acceptance": (
            "PASS"
            if criterion_5_checks else "FAIL"
        ),
    }

    lines = [
        "# Extended acceptance evaluation — " + args.label,
        "",
        f"- Run ID: `{run_id}`",
        f"- Timestamp: `{report['timestamp']}`",
        "- Trials: 3",
        "- Existing detector and configuration unchanged",
        "",
        "## Trial summary",
        "",
        "| Trial | Appeals | Invalid 4xx + recovery |",
        "|---|---|---|",
    ]

    for trial in report["trials"]:
        appeals_passed = sum(x["pass"] for x in trial["appeals"])
        invalid_passed = sum(x["pass"] for x in trial["invalid_inputs"])
        lines.append(
            f"| {trial['trial']} | {appeals_passed}/10 | "
            f"{invalid_passed}/10 |"
        )

    lines += [
        "",
        "## Verdicts",
        "",
        f"- Criterion 4: **{report['verdicts']['criterion_4']}**",
        "- Criterion 5 observed requests: "
        f"**{report['verdicts']['criterion_5_observed_requests']}**",
        "- Criterion 5 full acceptance: "
        f"**{report['verdicts']['criterion_5_full_acceptance']}**",
        "",
        "The oversized case uses 2001 characters as a provisional probe. "
        "This is not a documented maximum.",
        "",
        "## Raw evidence",
        "",
        "```json",
        json.dumps(report, indent=2, ensure_ascii=False),
        "```",
        "",
    ]

    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nReport: {path}")
    print("Criterion 4:", report["verdicts"]["criterion_4"])
    print(
        "Criterion 5 observed:",
        report["verdicts"]["criterion_5_observed_requests"],
    )
    print(
        "Criterion 5 full:",
        report["verdicts"]["criterion_5_full_acceptance"],
    )


if __name__ == "__main__":
    main()