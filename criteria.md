# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. Limit false accusations against human writers

Across each of three trials using the same 10 independently verified human-written samples, no more than 1 sample may receive a high-confidence AI label in any trial.

**Why this target:**
A false AI accusation can unfairly harm a genuine writer, so the system should prioritize avoiding false positives over detecting every AI-generated submission.

---

## 2. Maintain measurable score separation
Across each of three trials using the same 10 independently verified human-written samples and 10 AI-generated samples, the average combined AI-likelihood score of the AI-generated group must exceed the average combined score of the human-written group by at least 0.20.

**Why this target:**
A minimum score difference of 0.20 helps demonstrate that the model and writing-style signals can distinguish between clearly human-written and AI-generated text. This target focuses on measurable score separation without requiring every individual submission to be classified correctly, which supports the system's conservative approach to avoiding false accusations.

---

## 3. Ensure all three classifications are reachable

Across each of three trials using the same fixed test set, the system must produce all three classifications—high-confidence human, unsure, and high-confidence AI—at least once per trial.

**Why this target:**

All three classifications must be reachable because the system needs to distinguish clear human writing, uncertain cases, and strongly AI-like writing. The unsure classification is especially important because it prevents borderline scores from automatically becoming accusations. If one classification never appears, the thresholds or scoring rules may not be working as intended.
---

## 4. Ensure every valid appeal is recorded

Across each of three trials, all 10 valid appeals submitted with existing content IDs and non-empty reasoning must receive a successful confirmation and produce an audit-log appeal entry with the matching content ID and status `under_review`.

**Why this target:**

Every valid appeal must be recorded because the detector can incorrectly classify genuine human writing as AI-generated. Losing an appeal could leave a writer without a documented way to challenge that decision. Requiring all 10 appeals to succeed ensures that the review process is dependable rather than allowing occasional failures.
---

## 5. Reject invalid submissions without interrupting the service

Across each of three trials using the same 10 predefined invalid submissions, all 10 must receive a controlled HTTP 4xx response. After each invalid submission, a valid submission must still receive a successful response, confirming that the service remains operational.

The invalid test set must include missing text, empty text, whitespace-only text, incorrect data types, malformed JSON, and text exceeding the documented maximum allowed length.

**Why this target:**

Invalid submissions should be rejected consistently because missing, malformed, or excessively large text can cause processing errors or unreliable AI-likelihood scores. Requiring all 10 invalid submissions to receive controlled responses ensures that bad input does not interrupt the service or affect subsequent valid submissions.
---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
