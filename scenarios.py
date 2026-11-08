"""Evaluation scenarios for AI201 Unit 8 Milestone 3."""

import json
from pathlib import Path


SAMPLES_DIR = Path(__file__).resolve().parent / "samples"


def load_samples(filename):
    """Load and validate a ten-sample evaluation dataset."""
    path = SAMPLES_DIR / filename

    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    samples = data["samples"]

    if len(samples) != 10:
        raise ValueError(f"{filename}: expected exactly 10 samples")

    ids = set()

    for sample in samples:
        sample_id = sample["id"]
        text = sample["text"]

        if not isinstance(sample_id, str) or not sample_id.strip():
            raise ValueError(f"{filename}: invalid sample ID")

        if sample_id in ids:
            raise ValueError(f"{filename}: duplicate sample ID {sample_id}")

        if not isinstance(text, str) or not text.strip():
            raise ValueError(f"{filename}: empty or invalid text")

        ids.add(sample_id)

    return samples


HUMAN_SAMPLES = load_samples("human_eval_10.json")
AI_SAMPLES = load_samples("ai_eval_10.json")

HUMAN_TEXTS = [sample["text"] for sample in HUMAN_SAMPLES]
AI_TEXTS = [sample["text"] for sample in AI_SAMPLES]


SCENARIOS = [
    {
        "name": "human_false_positive",
        "criterion": 1,
        "texts": HUMAN_TEXTS,
    },
    {
        "name": "ai_human_separation",
        "criterion": 2,
        "texts": HUMAN_TEXTS + AI_TEXTS,
    },
    {
        "name": "label_coverage",
        "criterion": 3,
        "texts": HUMAN_TEXTS + AI_TEXTS,
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
