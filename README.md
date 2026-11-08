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

| Label                 | Score range           | The exact text a reader sees                                                                                                                      |
| --------------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| high-confidence human | 0.00 <= score < 0.35  | This writing shows patterns associated with human writing, but its authorship cannot be confirmed.                                                |
| unsure                | 0.35 <= score <= 0.65 | We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result. |
| high-confidence AI    | 0.65 < score <= 1.00  | This writing shows patterns associated with AI-generated text, but this is not proof that AI was used.                                            |

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

| Sample        | Combined score | Result |
| ------------- | -------------: | ------ |
| AI-generated  |        0.62425 | unsure |
| Human-natural |        0.46860 | unsure |
| Human-plain   |        0.56985 | unsure |
| AI-edited     |        0.63465 | unsure |

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


**Moment 3 - Unit 8 adversarial evaluation**

- **What I asked for:** AI assistance with test commands, attack interpretation, acceptance criteria, and Git verification.
- **What came back:** PowerShell checks, before-and-after comparisons, and documentation suggestions.
- **What I changed:** I ran and reviewed the tests, retained the measured failures, verified audit records, and did not claim that input validation improved detection accuracy.
<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 5 per minute, 50 per day

**Why those numbers and not others:**

<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

I chose 5 submissions per minute and 50 submissions per day because Provenance Guard is designed for writers submitting their work for evaluation, not for high-volume automated processing. A legitimate writer submitting a few pieces of work per hour should be able to use the service without reaching these limits.

The 5-per-minute limit makes rapid automated probing more difficult by restricting how quickly a script can submit variations to discover the detector's classification thresholds. The 50-per-day limit further restricts sustained probing while providing enough capacity for normal use. These limits are more restrictive than 10 per minute and 100 per day, but the tradeoff is that legitimate users making many submissions in a short period may receive HTTP 429 responses.

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

Per creator_id, with a fallback to the caller's IP address when a usable creator_id is unavailable.

This allows the system to enforce limits separately for different creators, even when they share the same IP address. However, because the creator_id is supplied by the caller rather than verified through authentication, an attacker could bypass the limit by repeatedly changing creator IDs. Requests without a usable creator_id are grouped by IP address, which can cause unrelated users sharing an address to affect each other's limits.

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

Command:

python run_attacks.py --flood 15

Actual output from November 4, 2026, at 9:05 PM:

============================================================
200 200 200 200 200 429 429 429 429 429 429 429 429 429 429
============================================================

The test submitted 15 requests using the same creator_id (flood_tester). The first 5 requests returned HTTP 200, and the remaining 10 returned HTTP 429.

This confirms that the configured per-minute rate limit was enforced during the test.

Evidence: results/flood_2026-11-04_2105.md

---

## Attack Run — Before

Command: `python run_attacks.py --set ".\attack_set" --label before`

Baseline: November 4, 2026, 9:30 PM.
The run executed 56 attacks against the Flask service.

Verdict criteria:

- Evasion: AI-origin text classified human or unsure is BROKE for avoiding an AI label.
- False positive: human-origin text classified AI is BROKE; human or unsure is HELD.
- Prompt injection: BROKE requires observed instruction takeover or corrupted protected output.
- Malformed input: crashes or inappropriate classification of non-prose are BROKE.
- Flood: enforcing the configured rate limit is HELD.

| ID      | Family             | Targeting                                              | Status | Content ID       | Guess  | Score | Verdict |
| ------- | ------------------ | ------------------------------------------------------ | ------ | ---------------- | ------ | ----- | ------- |
| EV01    | evasion            | signal two: typos raise word variety                   | 200    | `c_aff500ba6d6e` | human  | 0.319 | BROKE   |
| EV02    | evasion            | signal two: broken-up sentences raise length spread    | 200    | `c_fe2218076cc3` | unsure | 0.441 | BROKE   |
| EV03    | evasion            | signal two: a pasted quotation changes the shape       | 200    | `c_7e6b63d2356e` | unsure | 0.527 | BROKE   |
| EV04    | evasion            | signal one: unusual words raise perplexity             | 200    | `c_f7a51e4d31f1` | unsure | 0.538 | BROKE   |
| EV05    | evasion            | both signals: heavy human editing pass                 | 200    | `c_4b45a0015fdb` | human  | 0.326 | BROKE   |
| EV06    | evasion            | signal two: one very long sentence and one very short  | 200    | `c_175b621c331e` | unsure | 0.440 | BROKE   |
| EV07    | evasion            | signal two: padding with punctuation                   | 200    | `c_bd33524b9736` | unsure | 0.543 | BROKE   |
| EV08    | evasion            | signal one: text below the token window                | 200    | `c_6ae440c515ec` | unsure | 0.373 | BROKE   |
| EV09    | evasion            | both: AI text with a human opening paragraph bolted on | 200    | `c_0ad31cba1464` | unsure | 0.543 | BROKE   |
| EV10    | evasion            | signal two: repeated stanza structure                  | 200    | `c_1182d5fc1b27` | ai     | 0.754 | HELD    |
| FP01    | false_positive     | plain, clear human writing with no flourishes          | 200    | `c_d902875e2548` | unsure | 0.512 | HELD    |
| FP02    | false_positive     | human writing in a formal register                     | 200    | `c_419344fa426e` | unsure | 0.607 | HELD    |
| FP03    | false_positive     | a non-native English speaker writing carefully         | 200    | `c_32299e808d66` | unsure | 0.622 | HELD    |
| FP04    | false_positive     | a student essay written to a rubric                    | 200    | `c_74594823d9c4` | unsure | 0.621 | HELD    |
| FP05    | false_positive     | technical documentation written by a person            | 200    | `c_6ebf99ed9e41` | unsure | 0.644 | HELD    |
| FP06    | false_positive     | a person imitating a formal template                   | 200    | `c_0270b4b0f28e` | unsure | 0.632 | HELD    |
| FP07    | false_positive     | human writing that repeats a phrase deliberately       | 200    | `c_ae620d91a769` | unsure | 0.637 | HELD    |
| FP08    | false_positive     | very short genuine human submission                    | 200    | `c_615bbed45706` | unsure | 0.411 | HELD    |
| PI01    | prompt_injection   | instruction to ignore the check                        | 200    | `c_8d8c828e3a94` | unsure | 0.398 | HELD    |
| PI02    | prompt_injection   | instruction disguised as a system message              | 200    | `c_01e600d660d4` | human  | 0.267 | HELD    |
| PI03    | prompt_injection   | instruction wrapped in the writer's voice              | 200    | `c_1c176ed89549` | unsure | 0.505 | HELD    |
| PI04    | prompt_injection   | attempt to make the label text hostile                 | 200    | `c_bfbb083710fc` | unsure | 0.450 | HELD    |
| PI05    | prompt_injection   | attempt to inject into the audit log                   | 200    | `c_c1184080f3ff` | unsure | 0.510 | HELD    |
| PI06    | prompt_injection   | instruction plus real human text                       | 200    | `c_2085bc802a52` | unsure | 0.484 | HELD    |
| MF01    | malformed          | text is only whitespace                                | 400    | `—`              | —      | —     | HELD    |
| MF02    | malformed          | text is a single character                             | 500    | `—`              | —      | —     | BROKE   |
| MF03    | malformed          | text is control characters                             | 200    | `c_5d42660f6659` | human  | 0.250 | BROKE   |
| MF04    | malformed          | text is only punctuation                               | 200    | `c_da10d2502a2a` | human  | 0.256 | BROKE   |
| MF05    | malformed          | text is a very long single word                        | 200    | `c_f37247f290fa` | ai     | 0.749 | BROKE   |
| MF06    | malformed          | text is emoji only                                     | 200    | `c_e8bc7dbb8b22` | ai     | 0.748 | BROKE   |
| MF07    | malformed          | text is right-to-left script                           | 200    | `c_dad02eadbd2f` | ai     | 0.703 | HELD    |
| MF08    | malformed          | text is 60,000 characters                              | 200    | `c_7835e87435b7` | ai     | 0.789 | HELD    |
| RQ01    | malformed          | no text field at all                                   | 400    | `—`              | —      | —     | HELD    |
| RQ02    | malformed          | no creator_id                                          | 200    | `c_505f9657d082` | unsure | 0.370 | HELD    |
| RQ03    | malformed          | text is a number                                       | 400    | `—`              | —      | —     | HELD    |
| RQ04    | malformed          | text is a list                                         | 400    | `—`              | —      | —     | HELD    |
| RQ05    | malformed          | text is null                                           | 400    | `—`              | —      | —     | HELD    |
| RQ06    | malformed          | creator_id is an object                                | 200    | `c_d80ca1245ed5` | human  | 0.275 | BROKE   |
| RQ07    | malformed          | body is a JSON array, not an object                    | 400    | `—`              | —      | —     | HELD    |
| RQ08    | malformed          | body is unparseable JSON                               | 400    | `—`              | —      | —     | HELD    |
| RQ09    | malformed          | body is empty                                          | 400    | `—`              | —      | —     | HELD    |
| RQ10    | malformed          | body is form-encoded, not JSON                         | 429    | `—`              | —      | —     | HELD    |
| RQ11    | malformed          | body is JSON claiming to be plain text                 | 429    | `—`              | —      | —     | HELD    |
| RQ12    | malformed          | deeply nested JSON                                     | 400    | `—`              | —      | —     | HELD    |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator                  | 200    | `c_be369c5219a4` | human  | 0.264 | HELD    |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator                  | 200    | `c_666d6dd7ca5c` | human  | 0.264 | HELD    |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator                  | 200    | `c_2d53b4faae53` | human  | 0.264 | HELD    |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator                  | 200    | `c_53762739de3c` | human  | 0.264 | HELD    |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator                  | 200    | `c_ca6008a5bac5` | human  | 0.264 | HELD    |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator                  | 429    | `—`              | —      | —     | HELD    |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator                  | 429    | `—`              | —      | —     | HELD    |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator                  | 429    | `—`              | —      | —     | HELD    |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator                  | 429    | `—`              | —      | —     | HELD    |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator                  | 429    | `—`              | —      | —     | HELD    |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator                  | 429    | `—`              | —      | —     | HELD    |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator                  | 429    | `—`              | —      | —     | HELD    |

**Ten audit log entries from the run**

```json
[
  {
    "combined_score": 0.31915,
    "content_id": "c_aff500ba6d6e",
    "creator_id": "attacker_EV01",
    "guess": "human",
    "label": "This writing shows patterns associated with human writing, but its authorship cannot be confirmed.",
    "model_score": 0.1635,
    "status": "decided",
    "style_score": 0.4748,
    "timestamp": "2026-11-05T02:30:10+00:00"
  },
  {
    "combined_score": 0.32585,
    "content_id": "c_4b45a0015fdb",
    "creator_id": "attacker_EV05",
    "guess": "human",
    "label": "This writing shows patterns associated with human writing, but its authorship cannot be confirmed.",
    "model_score": 0.3212,
    "status": "decided",
    "style_score": 0.3305,
    "timestamp": "2026-11-05T02:30:11+00:00"
  },
  {
    "combined_score": 0.75415,
    "content_id": "c_1182d5fc1b27",
    "creator_id": "attacker_EV10",
    "guess": "ai",
    "label": "This writing shows patterns associated with AI-generated text, but this is not proof that AI was used.",
    "model_score": 0.9792,
    "status": "decided",
    "style_score": 0.5291,
    "timestamp": "2026-11-05T02:30:12+00:00"
  },
  {
    "combined_score": 0.6223000000000001,
    "content_id": "c_32299e808d66",
    "creator_id": "attacker_FP03",
    "guess": "unsure",
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
    "model_score": 0.8051,
    "status": "decided",
    "style_score": 0.4395,
    "timestamp": "2026-11-05T02:30:12+00:00"
  },
  {
    "combined_score": 0.2668,
    "content_id": "c_01e600d660d4",
    "creator_id": "attacker_PI02",
    "guess": "human",
    "label": "This writing shows patterns associated with human writing, but its authorship cannot be confirmed.",
    "model_score": 0.2044,
    "status": "decided",
    "style_score": 0.3292,
    "timestamp": "2026-11-05T02:30:13+00:00"
  },
  {
    "combined_score": 0.51,
    "content_id": "c_c1184080f3ff",
    "creator_id": "attacker_PI05",
    "guess": "unsure",
    "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
    "model_score": 0.6401,
    "status": "decided",
    "style_score": 0.3799,
    "timestamp": "2026-11-05T02:30:13+00:00"
  },
  {
    "creator_id": "attacker_MF01",
    "event": "rejected",
    "reason": "invalid_or_empty_text",
    "status": "rejected",
    "timestamp": "2026-11-05T02:30:13+00:00"
  },
  {
    "combined_score": 0.25,
    "content_id": "c_5d42660f6659",
    "creator_id": "attacker_MF03",
    "guess": "human",
    "label": "This writing shows patterns associated with human writing, but its authorship cannot be confirmed.",
    "model_score": 0.0,
    "status": "decided",
    "style_score": 0.5,
    "timestamp": "2026-11-05T02:30:13+00:00"
  },
  {
    "combined_score": 0.7484500000000001,
    "content_id": "c_e8bc7dbb8b22",
    "creator_id": "attacker_MF06",
    "guess": "ai",
    "label": "This writing shows patterns associated with AI-generated text, but this is not proof that AI was used.",
    "model_score": 0.9969,
    "status": "decided",
    "style_score": 0.5,
    "timestamp": "2026-11-05T02:30:14+00:00"
  },
  {
    "creator_id": "attacker_flood",
    "event": "rejected",
    "limit": "5 per 1 minute",
    "reason": "rate_limited",
    "status": "rejected",
    "timestamp": "2026-11-05T02:30:16+00:00"
  }
]
```

The ten records include evasion, false-positive, prompt-injection, malformed-input, and rate-limit evidence.

**The single worst outcome** — the one I'd least want to explain to a writer whose work got caught by it:

MF02 submitted a one-character text value, "a", and received HTTP 500.
The scoring workflow raised `ValueError: Text is too short to score — a few sentences at least.`
The route did not convert this into a controlled client error.
The response exposed Werkzeug debugger HTML instead of the expected JSON response.

This is a service reliability and error-handling failure. A writer submitting insufficient text should receive a clear validation message, not an internal server error.

Other baseline weaknesses included AI-origin evasions classified human or unsure, non-prose submissions receiving confident labels, and acceptance of an object-valued creator_id.

MF07 was processed without crashing, but the reliability of its classification on right-to-left text is not established.
MF08 was processed without crashing; no maximum-length requirement was confirmed.
RQ10 and RQ11 returned HTTP 429, so their content-type validation was not independently established.

Evidence: `results/attack_run_2026-11-04_2130_before.md`

---

## Run Log and Verdicts

**Submission input policy:** The maximum submission length is 2,000
characters, configured through `MAX_TEXT_LENGTH` in `config.py`.
The `/submit` endpoint rejects oversized, empty, whitespace-only,
and incorrectly typed text with HTTP 400.

Five acceptance criteria were evaluated across three trials each.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
| --- | --- | --- | --- | --- | --- |
| 1. Human false positives | At most 1/10 high-confidence AI labels | 0/10 | 0/10 | 0/10 | PASS |
| 2. AI?human separation | AI mean minus human mean >= +0.20 | +0.0339 | +0.0339 | +0.0339 | FAIL |
| 3. Label coverage | `human`, `unsure`, and `ai` observed | Only `unsure` | Only `unsure` | Only `unsure` | FAIL |
| 4. Appeal processing | 10/10 accepted with matching audit entries | 10/10 | 10/10 | 10/10 | PASS |
| 5. Invalid input handling | 10/10 HTTP 4xx, valid recovery request succeeds | 10/10 | 10/10 | 10/10 | PASS |

### Evaluation evidence

- Criteria 1?3 baseline:
  `results/run_2026-11-08_1506_before.md`
- Criteria 4?5 baseline:
  `results/run_extended_2026-11-08_150941_before.md`
- Criteria 4?5 after the input-validation fix:
  `results/run_extended_2026-11-08_151919_after.md`

**Actual recorded score values:** The baseline evaluator measured
mean combined AI-likelihood scores of 0.47027 for human writing and
0.50414 for AI writing. The difference was +0.03387, below the
required +0.20. All 20 texts received the `unsure` label.

### Diagnoses

**Criterion 2 ? score separation:** The detector combines a GPT-2
perplexity signal and a stylometric signal. Their combined output did
not reliably distinguish the original human and AI evaluation groups.
The problem occurs in the signal and combining stages, not in the
HTTP route.

**Criterion 3 ? label coverage:** The resulting scores remained
between the configured human and AI thresholds. The label-mapping
stage therefore returned `unsure` for every evaluated text. The
thresholds were reachable in principle, but the observed evaluation
set did not reach them.

**Criterion 5 ? initial failure:** The original route accepted
a 2,001-character submission. The route lacked enforcement of the
documented 2,000-character maximum. Adding explicit input validation
resolved this measured failure.

---

## The Improvement

**What I changed:** I introduced a documented maximum submission
length of 2,000 characters and enforced it at the `/submit` route
before invoking the detector.

**Which diagnosis pointed at it:** The baseline invalid-input
evaluation accepted an oversized submission. The problem was
missing route validation, not model scoring.

**Verification:** After the fix, all ten predefined invalid-input
cases returned HTTP 4xx in each of three trials. Each trial also
verified that a subsequent valid submission succeeded.

### Independent scoring experiment

I investigated whether changing the stylometric signal to emphasize
sentence-length variation and weighting it at 70%, with GPT-2 at 30%,
would improve AI?human separation.

On the original evaluation set, the offline candidate appeared
promising: its estimated separation was +0.2320, with zero
high-confidence AI labels among the original ten human samples.

I then evaluated the unchanged candidate on five additional,
independently supplied human-written paragraphs (H11?H15) and five
new AI-generated paragraphs (A11?A15).

| Metric | Current scoring | Proposed 70/30 scoring |
| --- | ---: | ---: |
| Mean human AI-likelihood | 0.6227 | 0.7126 |
| Mean AI AI-likelihood | 0.5421 | 0.7093 |
| AI?human separation | -0.0806 | -0.0033 |
| Human false positives | 1/5 | 4/5 |
| All three labels observed | No | No |

**Decision:** I rejected the proposed scoring modification because
it increased false accusations of verified human writing and failed
to demonstrate useful separation on the independent samples.
The existing scoring implementation remains unchanged.

### Attack Run ? After

The corrected input-validation behavior is supported by the
extended acceptance report. A complete post-change adversarial
attack-suite result is not claimed here unless separately recorded.

**Did it help?** Yes, for oversized submissions: the original
failure became a consistent HTTP 400 rejection. It did not resolve
the detector's score-separation and label-coverage limitations.

---

## What's Still Broken

### Remaining detector limitations

**Criterion 2 ? AI?human separation:** The measured difference
between the AI and human evaluation groups was only +0.03387,
below the required +0.20. The existing GPT-2 perplexity and
stylometric signals do not provide sufficient separation on
the tested samples.

**Criterion 3 ? label coverage:** All 20 original evaluation
texts received the `unsure` label in each of the three trials.
The score distribution did not reach the configured thresholds
for the `human` and `ai` labels.

**Independent validation:** A proposed scoring modification
initially appeared promising on the original dataset but
incorrectly labeled four of five additional verified human
texts as AI-generated. The modification was rejected.

### Remaining adversarial weaknesses

The baseline adversarial evaluation identified AI-origin
evasion texts that received `human` or `unsure` classifications,
as well as unreliable confident classifications for some
non-prose inputs.

The service also needs further validation of Unicode handling,
content-type enforcement, and adversarial robustness. The
existing evidence does not establish that these problems
have all been resolved.

### What I would improve next

I would collect a larger and more diverse dataset of verified
human and AI writing, including informal writing, technical
writing, different languages, and edited AI-generated text.

I would then calibrate scoring thresholds on a development
dataset and evaluate the final configuration on a separate,
previously unseen test set.

Additional improvements would include clearer handling of
unsupported input formats, stronger request validation,
and automated regression tests for known adversarial cases.

**The trade I'd make if this ran for real:**

I would prioritize reducing false accusations of human
authors, even if that means allowing more AI-generated text
to receive an `unsure` label. Human writers bear the
greater immediate cost when a detector incorrectly
presents their original work as AI-generated.

---


### Milestone 6 - Final remaining failures

The 56-case after-run report has been manually interpreted using
the original attack objectives. RQ10 and RQ11 are INCONCLUSIVE
because HTTP 429 prevented direct content-type validation.

#### Evasion cases still BROKE

| Case | Problem | Next improvement |
| --- | --- | --- |
| EV01 | Typos change vocabulary diversity | Test typo normalization |
| EV02 | Fragmented sentences change length variation | Improve segmentation |
| EV03 | Quoted passages distort style features | Analyze quotations separately |
| EV04 | Unusual vocabulary changes perplexity | Calibrate across genres |
| EV05 | Heavy human editing masks AI origin | Test mixed-authorship writing |
| EV06 | Extreme sentence lengths distort statistics | Use robust dispersion |
| EV07 | Punctuation padding alters features | Normalize excessive punctuation |
| EV08 | Short passages lack sufficient context | Require a reliable token window |
| EV09 | Human opening masks AI-origin content | Add passage-level scoring |

EV10 remained HELD because it received an AI classification.

#### Other remaining weaknesses

- MF03: Control-character-only input was accepted; reject non-prose.
- MF04: Punctuation-only input was classified; require meaningful text.
- MF06: Emoji-only input was labeled AI; reject unsupported input.
- RQ06: Object-valued creator_id was accepted; enforce string validation.
- RQ10/RQ11: HTTP 429 obscured content-type behavior; retest without rate-limit interference.
- Rate limiting: Caller-controlled creator IDs permit rotation; require authenticated identity.

#### Missed acceptance criteria

**Criterion 2 - MISSED:** AI-human score separation remained
+0.03387 versus the +0.20 target. I would calibrate the
model and stylometric signals using a larger labeled corpus
and validate any new weights on independent samples.

**Criterion 3 - MISSED:** The evaluation produced only `unsure`
labels, not all three required labels. I would inspect score
distributions and recalibrate thresholds while monitoring
false-positive accusations.

I stopped after the targeted input-validation improvement
because further scoring changes would make attribution of
improvements difficult, and earlier experimental reweighting
performed poorly on held-out human writing.

#### Production trade-off

I would prioritize fewer false accusations of genuine human
writers, even if that allows more AI-generated text to remain
undetected. Writers avoid unfair penalties, while reviewers
and institutions bear the cost of additional manual review
and less definitive automated detection.

The detector should be advisory, not proof of authorship.

#### Ten actual audit log entries

The following ten entries are taken from the real audit log,
including rejected requests, appeals, and completed decisions.

```jsonl
{"timestamp":"2026-11-08T20:44:00+00:00","creator_id":"ext_ce85aa760e_t3_invalid_7","event":"rejected","status":"rejected","reason":"invalid_or_empty_text"}
{"timestamp":"2026-11-08T20:44:01+00:00","creator_id":"ext_ce85aa760e_t3_invalid_8","event":"rejected","status":"rejected","reason":"invalid_or_empty_text"}
{"timestamp":"2026-11-08T20:44:01+00:00","creator_id":"unknown","event":"rejected","status":"rejected","reason":"rate_limited","limit":"5 per 1 minute"}
{"timestamp":"2026-11-08T20:44:01+00:00","creator_id":"ext_ce85aa760e_t3_invalid_10","event":"rejected","status":"rejected","reason":"text_exceeds_maximum_length"}
{"timestamp":"2026-11-08T20:44:00+00:00","content_id":"c_c530b380c8c3","creator_id":"ext_ce85aa760e_t3_appeal_9","event":"appeal","status":"under_review","reasoning":"Valid appeal evaluation trial 3, case 9."}
{"timestamp":"2026-11-08T20:44:00+00:00","content_id":"c_a7fd44ae1ef4","creator_id":"ext_ce85aa760e_t3_appeal_10","event":"appeal","status":"under_review","reasoning":"Valid appeal evaluation trial 3, case 10."}
{"timestamp":"2026-11-08T20:44:01+00:00","content_id":"c_b6e1df86ee1c","creator_id":"ext_ce85aa760e_t3_recovery_7","guess":"unsure","model_score":0.5746,"style_score":0.4751,"combined_score":0.52485,"label":"We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.","status":"decided"}
{"timestamp":"2026-11-08T20:44:01+00:00","content_id":"c_be9f67254418","creator_id":"ext_ce85aa760e_t3_recovery_8","guess":"unsure","model_score":0.5746,"style_score":0.4751,"combined_score":0.52485,"label":"We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.","status":"decided"}
{"timestamp":"2026-11-08T20:44:01+00:00","content_id":"c_17ea8fd9d892","creator_id":"ext_ce85aa760e_t3_recovery_9","guess":"unsure","model_score":0.5746,"style_score":0.4751,"combined_score":0.52485,"label":"We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.","status":"decided"}
{"timestamp":"2026-11-08T20:44:01+00:00","content_id":"c_0140bb499589","creator_id":"ext_ce85aa760e_t3_recovery_10","guess":"unsure","model_score":0.5746,"style_score":0.4751,"combined_score":0.52485,"label":"We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.","status":"decided"}
```

---

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
       [x] Repository URL submitted — WRITE IT DOWN


---

## Unit 8 Milestone 4 - Verdicts and Diagnoses

The five original acceptance criteria in `criteria.md` remain
unchanged. Each target must hold in all three trials.

### Acceptance verdicts

| Criterion | Target | Trial 1 | Trial 2 | Trial 3 | Verdict |
| --- | --- | --- | --- | --- | --- |
| 1. Human false positives | At most 1/10 | 0/10 | 0/10 | 0/10 | **MET** |
| 2. AI-human separation | At least +0.20 | +0.0339 | +0.0339 | +0.0339 | **MISSED** |
| 3. Label coverage | All three labels | unsure only | unsure only | unsure only | **MISSED** |
| 4. Valid appeals | 10/10 | 10/10 | 10/10 | 10/10 | **MET** |
| 5. Invalid input and recovery | 10/10 | 10/10 | 10/10 | 10/10 | **MET** |

### How each verdict was decided

**1 - MET:** No high-confidence AI accusation occurred among
the ten verified human texts in any trial.

**2 - MISSED:** The average AI-minus-human combined score was
+0.03387 in each trial, below the required +0.20.

**3 - MISSED:** All twenty evaluation texts were labeled
`unsure` in every trial. Neither `human` nor `ai` appeared.

**4 - MET:** All ten valid appeals succeeded with matching
`under_review` audit entries in each trial.

**5 - MET after the fix:** All ten invalid submissions returned
HTTP 4xx and valid submissions continued succeeding in each
post-fix trial. The baseline had missed because an oversized
submission was accepted.

### Root causes of missed criteria

**Criterion 2 - Signals one and two; combining rule:**
GPT-2 perplexity and stylometric features did not distinguish
the human and AI groups sufficiently. Their equally weighted
combination yielded overlapping scores and a group-average
difference of only +0.03387. The evidence does not establish
which individual signal contributed most.

**Criterion 3 - Combining rule; label mapping:**
All combined scores remained between the 0.35 human threshold
and the 0.65 AI threshold. Consequently, label mapping
assigned `unsure` to every text. The underlying scoring
weakness is related to criterion 2.

### Broken attack diagnoses

The baseline attack report is
`results/attack_run_2026-11-04_2130_before.md`.

| Attack | Result | Stage | Mechanism |
| --- | --- | --- | --- |
| EV01 | human, 0.319 | Signal two | Typos alter measured word variety |
| EV02 | unsure, 0.441 | Signal two | Sentence fragmentation changes length spread |
| EV03 | unsure, 0.527 | Signal two | Quotation insertion changes style features |
| EV04 | unsure, 0.538 | Signal one | Unusual words can raise perplexity |
| EV05 | human, 0.326 | Both signals | Human editing changes predictability and style |
| EV06 | unsure, 0.440 | Signal two | Unequal sentence lengths change spread |
| EV07 | unsure, 0.543 | Signal two | Punctuation padding changes style measurements |
| EV08 | unsure, 0.373 | Signal one | Short/token-window behavior weakens evidence |
| EV09 | unsure, 0.543 | Both signals | A human opening changes AI-origin text statistics |

These mechanisms describe the features targeted by the
attacks; individual causal contributions were not verified
through controlled ablation experiments.

**EV10 - HELD:** Repeated-stanza text received `ai` (0.754).

**MF02 - BROKE at baseline:** A one-character submission
returned HTTP 500. Stage: route/error handling. Mechanism:
the detector's exception was not converted into HTTP 4xx.
The later validation fix addressed short invalid input.

**RQ10/RQ11 - Inconclusive:** Both received HTTP 429.
Rate limiting prevented independent content-type validation.

### Shared failure pattern

Seven of nine broken evasion cases targeted stylometric
features or both signals; EV04 and EV08 targeted the model
signal. Surface-level text transformations can therefore
reduce the reliability of AI-origin classification.

The missed score-separation and label-coverage criteria
also share a weak-discrimination problem.

### Criterion review and surprising result

No original criterion was revised because every target
was measurable. Lowering missed targets would conceal
the failures.

Criterion 2 surprised me most. I expected at least +0.20
separation but measured +0.03387.

An opposing argument is that any positive difference
demonstrates separation. However, the explicit target
was +0.20 in every trial, so the recorded result is MISSED.

### Milestone 4 conclusion

**3 MET, 2 MISSED.**

The detector met its original false-positive target,
appeal target, and corrected invalid-input target.
It missed AI-human score separation and label coverage.

I would prioritize reducing false accusations of genuine
writers while improving discrimination on independently
verified evaluation samples.

---


---

## Unit 8 Milestone 5 - One Improvement and Re-evaluation

### Selected improvement

The single selected improvement is submission-length validation
at the `/submit` route.

- **Stage:** Route/input validation
- **Files:** `app.py`, `config.py`
- **Limit:** 2,000 characters
- **Mechanism:** Reject oversized text with HTTP 400 before
  invoking the detection signals.
- **Reason:** The original invalid-input evaluation accepted
  a 2,001-character submission with HTTP 200.
- **Scope:** No changes to model weights, stylometric features,
  scoring thresholds, or label mapping.

The validation was implemented and committed during Milestone 3.
Milestone 5 re-evaluates that same change rather than adding
another modification.

### Before and after - acceptance criteria

| Criterion | Original before | Full after | Outcome |
| --- | --- | --- | --- |
| 1. Human false positives | 0/10 in all 3 trials | 0/10 in all 3 trials | MET, unchanged |
| 2. AI-human score separation | +0.03387, target +0.20 | Still below target | MISSED |
| 3. Label coverage | Only `unsure` in all 3 trials | Only `unsure` in all 3 trials | MISSED |
| 4. Valid appeals | 10/10 in all 3 trials | 10/10 in all 3 trials | MET, unchanged |
| 5. Invalid inputs and recovery | Initial baseline 9/10 | 10/10 in all 3 trials | MET after fix |

Criterion 5's original baseline failed because an oversized
submission was accepted. Its corrected post-fix result passed.
The later full evaluation also reported PASS.

A malformed-JSON probe received HTTP 429 during the later
extended evaluation; this satisfies the observed HTTP 4xx
requirement but does not independently prove that malformed
JSON was rejected by the parser rather than rate limiting.

### Before and after - full attack set

Both attack runs contain 56 cases. The full case-by-case
reports are retained as evidence.

| Attack or group | Before | After | Interpretation |
| --- | --- | --- | --- |
| EV01 | `human` | `human` | Evasion remains effective |
| EV02-EV04 | `unsure` | `unsure` | Evasions remain unresolved |
| EV05 | `human` | `human` | Evasion remains effective |
| EV06-EV09 | `unsure` | `unsure` | Evasions remain unresolved |
| EV10 | `ai` | `ai` | Detector held |
| MF02 | HTTP 500 | HTTP 400 | Invalid-input handling improved |
| RQ10-RQ11 | HTTP 429 | HTTP 429 | Content-type behavior remains unproven |
| Oversized evaluation probe | HTTP 200 at baseline | HTTP 400 | Selected improvement worked |

The attack runner requires manual interpretation of its
outcomes. A question mark in the report is not an automatic
pass or failure.

### Complete evidence

**Before:**

- [Full attack run - before](results/attack_run_2026-11-04_2130_before.md)
- [Criteria 1-3 - before](results/run_2026-11-08_1506_before.md)
- [Criteria 4-5 - original baseline](results/run_extended_2026-11-08_150941_before.md)

**After:**

- [Full attack run - after](results/attack_run_2026-11-08_1543_after.md)
- [Criteria 1-3 - after](results/run_2026-11-08_1543_after.md)
- [Criteria 4-5 - after](results/run_extended_2026-11-08_154353_after.md)

### Did the improvement help?

**Yes, for the specific input-validation failure.**
The oversized submission is now rejected with HTTP 400
instead of being accepted with HTTP 200.

The change did **not** solve AI-human score separation,
label coverage, or the nine identified evasion cases.

MF02 also improved from HTTP 500 to HTTP 400, but the
evidence does not isolate the character-limit check as
the cause of that particular improvement.

### Trade-off and remaining limitations

The 2,000-character limit protects the route from
oversized submissions, but also prevents legitimate
writers from submitting longer documents in one request.

This improvement addresses input handling, not detection
accuracy. The scoring limitations and adversarial
evasion vulnerabilities remain.

**Milestone 5 verdict:** The targeted validation
improvement helped, with a documented length restriction
and no demonstrated improvement in classification accuracy.

---

<!-- ═════════════════════════════════════════════════════════════════════
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
