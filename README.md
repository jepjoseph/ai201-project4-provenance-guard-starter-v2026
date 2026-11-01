# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

1. **Receive the submission:** The writer sends their text and creator ID to the `POST /submit` endpoint in `app.py`. The endpoint checks that the submitted text is valid.

2. **Analyze the text with the model:** `detector.py` processes the submitted text using a local language model and returns a model-based detection score.

3. **Analyze the writing style:** `stylometry.py` examines sentence-length variation, vocabulary diversity, and punctuation usage to calculate a writing-style detection score.

4. **Combine the two signals:** `scoring.py::combine_signals` combines the model score and writing-style score into one overall score, using the weights defined in `config.py`.

5. **Determine the classification:** The scoring logic compares the combined score with the thresholds in `config.py` and assigns one of three classifications: high-confidence human, unsure, or high-confidence AI. The classification is converted into a reader-friendly label.

6. **Record the decision:** `audit.py` saves the submission's content ID, creator ID, detection scores, classification, and decision status in `logs/audit.jsonl` for future review or appeal.

7. **Return the result:** The `/submit` endpoint sends a JSON response containing the content ID, guess, confidence score, label text, model score, and style score. The writing site can display the label to the reader.

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:**
detector.py::model_signal uses a local language model to measure text predictability through perplexity. Lower perplexity means the model finds the text easier to predict. The function converts perplexity into a score between 0 and 1, where a higher score indicates more AI-like writing.

**Why that might differ between human and AI writing:**
AI-generated text often follows predictable word patterns because language models generate text by selecting likely next tokens. Human writing may contain unexpected word choices, unusual sentence structures, and less predictable expressions. These differences can affect perplexity.

**What it can't see:**
The model cannot determine who actually wrote the text. A human using simple vocabulary, short sentences, or repetitive expressions may receive an AI-like score. This can particularly affect people writing in a second language or deliberately using straightforward wording. Conversely, AI-generated text containing unusual vocabulary or unexpected expressions may appear more human-like to the detector.

### Signal two — the style signal

**What it measures:**
stylometry.py is designed to measure statistical properties of writing, including sentence-length variation, vocabulary diversity, and punctuation density. These measurements will be combined into a style score between 0 and 1, where higher values indicate writing that appears more AI-like.

**Why that might differ between human and AI writing:**
Human and AI-generated writing may differ in sentence structure, word variety, and punctuation patterns. For example, human writing may contain sentences of very different lengths, while some AI-generated writing may use more consistent sentence structures. These patterns can provide clues, but they are not reliable proof of authorship.

**What it can't see:**
The style signal cannot understand the meaning of the text or identify its actual author. Adding typos, changing punctuation, splitting sentences, or inserting quotations can change its measurements without changing who wrote the text. A human writer with a consistent writing style could also receive an AI-like score.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:**
I combine the model and stylometry signals using an equally weighted average. Both scores range from 0 to 1, with higher values indicating more AI-like patterns. If the signals disagree, their average reflects that uncertainty rather than automatically favoring an AI accusation. This score is not proof of authorship.

**The numbers:**
Combined score = (0.50 * model_score) + (0.50 * style_score). The model signal contributes 50%, and the style signal contributes 50%. These initial weights will be evaluated using the four Milestone 4 calibration samples.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**

In my four-sample calibration, Sample A was AI-generated. The model signal returned 0.8081, while the stylometry signal returned 0.4404. The two signals differed by 0.3677.

Using the equal-weighted rule, the combined score was 0.6242. With the current thresholds of 0.35 for human and 0.65 for AI, this score falls into the unsure range rather than receiving a high-confidence AI label.

The human-written samples also received unsure-range scores: Sample B scored 0.4686 and Sample C scored 0.5698. The edited AI sample, Sample D, scored 0.6347.

The average combined score was approximately 0.6295 for the two AI-origin samples and 0.5192 for the two human-origin samples, a difference of about 0.1103.

This preliminary calibration does not meet my acceptance criterion requiring at least 0.20 average separation across three trials with 10 human and 10 AI samples. It also does not demonstrate that all three labels are reachable. I am keeping the current weights and thresholds provisional rather than claiming that the detector has been validated.

The split illustrates why neither signal should be treated as proof of authorship. An unsure decision allows uncertain cases to avoid an automatic high-confidence accusation.

---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human |  |  |
| unsure |  |  |
| high-confidence AI |  |  |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "...", "creator_id": "..."}'
```

```json

```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "...", "reasoning": "..."}'
```

```json

```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json

```

---

## How I Used AI

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
