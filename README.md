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

The combined score ranges from 0 to 1. A higher score means
the writing exhibits more AI-like patterns. It is not a
verified probability of AI authorship.

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 <= score < 0.35 | This writing shows patterns associated with human writing, but its authorship cannot be confirmed. |
| unsure | 0.35 <= score <= 0.65 | We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result. |
| high-confidence AI | 0.65 < score <= 1.00 | This writing shows patterns associated with AI-generated text, but this is not proof that AI was used. |

**Why I worded the "unsure" one this way:**

The detector cannot verify who actually wrote a piece of text.
I wanted the unsure label to explain that limitation clearly,
without making the writer feel accused of using AI. A person
may have written the entire submission themselves, even when
the detector finds patterns that resemble AI-generated writing.

---

## Sample Run

The following results come from the real detector workflow
tested on November 1, 2026, using the existing calibration
samples. The requests were sent through Flask's test client,
rather than through a separately running curl server.
The audit log was temporarily redirected during testing.

**A submission**

Request:

```json
{
  "text": "Debugging a React and Express Application: what I learned\n\nLong time programmer but somewhat new to react/express/javascript. I'm building a site for practice and One page I'm having trouble with is pulling data from another site doing some calculations and then pulling more data. I like this design as it puts the work in the api and the react app can concentrate on display. The trouble is that the other site is slow and I think the react app is timeing out, its kinda of hard to debug because everytime I sit to debug it then everything works. Bot overall its not a great design because the looping in the api is open ended so I can't predict how long it will take.\n\nBack in the old days with a TCP socket I'd have the server send a heartbeat back every second and sent the timeout to 2 seconds. Here I don't think HTTP has anyway to do that. Also I don't see anyway to set or adjust any timeouts. I could break this up into multiple smaller requests but that doesn't seem to fix the core issue of not controlling the timeout and makes the overall design worse.\n\nGoogling around has been rough so many versions of fetch over the years. I'm using a react app and express and keeping it as vanilla as possible.",
  "creator_id": "calibration-sample_B_human_natural.txt"
}
```

Response (HTTP 200):

```json
{
  "combined_score": 0.4686,
  "confidence": 0.4686,
  "content_id": "c_4ed32b18aab0",
  "guess": "unsure",
  "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
  "model_score": 0.4853,
  "style_score": 0.4519
}
```

**An appeal**

Request:

```json
{
  "content_id": "c_4ed32b18aab0",
  "reasoning": "This is my own writing. I would like the classification reviewed."
}
```

Response (HTTP 200):

```json
{
  "content_id": "c_4ed32b18aab0",
  "message": "Your appeal has been recorded for review.",
  "status": "under_review"
}
```

**Audit log entries**

```json
[
  {
    "combined_score": 0.4686,
    "content_id": "c_4ed32b18aab0",
    "creator_id": "calibration-sample_B_human_natural.txt",
    "guess": "unsure",
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
    "model_score": 0.4853,
    "status": "decided",
    "style_score": 0.4519,
    "timestamp": "2026-11-01T19:20:35+00:00"
  },
  {
    "content_id": "c_4ed32b18aab0",
    "creator_id": "calibration-sample_B_human_natural.txt",
    "event": "appeal",
    "reasoning": "This is my own writing. I would like the classification reviewed.",
    "status": "under_review",
    "timestamp": "2026-11-01T19:20:35+00:00"
  }
]
```

**Calibration observations**

| Sample | Combined score | Result |
|---|---:|---|
| AI-generated | 0.62425 | unsure |
| Human-natural | 0.46860 | unsure |
| Human-plain | 0.56985 | unsure |
| AI-edited | 0.63465 | unsure |

All four real submissions received the unsure label.
Controlled-score tests confirmed that all three label branches
are reachable, but this four-sample run did not demonstrate
all three outcomes with real detector inputs.

---

## How I Used AI

**Moment 1 - Building and testing the scoring system**

- **What I asked for:** I asked AI to help me implement the stylometry functions and combine their results with the model-based detection score. I also wanted to understand how to test the scoring system using different human-written and AI-generated samples.
- **What came back:** AI suggested Python implementations for measuring sentence-length variation, vocabulary diversity, and punctuation density. It also helped me create PowerShell scripts to inspect the project, test the functions, and compare the scores.
- **What I changed:** I ran the implementations and tests in my development environment and reviewed the results. The four calibration samples all received the `unsure` classification, so I kept that limitation in the README rather than claiming that the detector could reliably distinguish human and AI writing.

**Moment 2 - Implementing appeals and audit logging**

- **What I asked for:** I asked AI to help me finish the `/appeal` endpoint while preserving the existing project structure and audit functions. I wanted appeals to work only for existing submissions and to keep the original classification unchanged.
- **What came back:** AI suggested request validation, checking existing content IDs through `audit.entries_for()`, and recording appeals through `audit.log_appeal()`. It also provided scripts to test successful submissions, invalid appeals, and audit history.
- **What I changed:** I applied the implementation, ran the API tests, and verified the results. I confirmed that valid appeals returned `under_review`, invalid requests were rejected, and the original decisions remained in the audit log. I also tested the workflow using the actual detector and documented the results.

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

       [x] criteria.md has five numbered criteria, each naming a target
       [x] Each has a reason underneath
       [x] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [x] Two signals that measure DIFFERENT things, each with a named blind spot
       [x] Three label variants, all reachable, written out in full
       [x] POST /appeal changes status and writes to the log
       [x] Signals and Scoring names scoring.py::combine_signals
       [x] Sample Run: a submission AND an appeal, as pasted text
       [x] At least four new commits
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
