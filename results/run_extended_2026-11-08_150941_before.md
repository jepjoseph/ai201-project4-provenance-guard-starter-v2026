# Extended acceptance evaluation — before

- Run ID: `be262e1e8c`
- Timestamp: `2026-11-08T20:09:41.070181+00:00`
- Trials: 3
- Existing detector and configuration unchanged

## Trial summary

| Trial | Appeals | Invalid 4xx + recovery |
|---|---|---|
| 1 | 10/10 | 9/10 |
| 2 | 10/10 | 9/10 |
| 3 | 10/10 | 9/10 |

## Verdicts

- Criterion 4: **PASS**
- Criterion 5 observed requests: **FAIL**
- Criterion 5 full acceptance: **FAIL**

The oversized case uses 2001 characters as a provisional probe. This is not a documented maximum.

## Raw evidence

```json
{
  "run_id": "be262e1e8c",
  "timestamp": "2026-11-08T20:09:41.070181+00:00",
  "service": "http://127.0.0.1:5000",
  "trials": [
    {
      "trial": 1,
      "appeals": [
        {
          "case": 1,
          "content_id": "c_ecd492704aba",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_ecd492704aba",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_ecd492704aba",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 2,
          "content_id": "c_ca77903ec3ea",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_ca77903ec3ea",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_ca77903ec3ea",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 3,
          "content_id": "c_550ea21d258f",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_550ea21d258f",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_550ea21d258f",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 4,
          "content_id": "c_4b532437e51a",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_4b532437e51a",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_4b532437e51a",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 5,
          "content_id": "c_cfd1881fe2e3",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_cfd1881fe2e3",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_cfd1881fe2e3",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 6,
          "content_id": "c_ab32fa7e9af1",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_ab32fa7e9af1",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_ab32fa7e9af1",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 7,
          "content_id": "c_a35640eca11d",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_a35640eca11d",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_a35640eca11d",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 8,
          "content_id": "c_a7c6d05529cf",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_a7c6d05529cf",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_a7c6d05529cf",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 9,
          "content_id": "c_31e1cc6f5c24",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_31e1cc6f5c24",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_31e1cc6f5c24",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 10,
          "content_id": "c_6cb582138b81",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_6cb582138b81",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_6cb582138b81",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        }
      ],
      "invalid_inputs": [
        {
          "case": "missing_text",
          "invalid": {
            "status": 400,
            "response": {
              "error": "bad_request",
              "message": "Send JSON with a non-empty \"text\"."
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_02e7b37eea67",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "rejected_with_4xx": true,
          "recovered": true,
          "pass": true
        },
        {
          "case": "empty_text",
          "invalid": {
            "status": 400,
            "response": {
              "error": "bad_request",
              "message": "Send JSON with a non-empty \"text\"."
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_cd7a79fe99ca",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "rejected_with_4xx": true,
          "recovered": true,
          "pass": true
        },
        {
          "case": "whitespace_only",
          "invalid": {
            "status": 400,
            "response": {
              "error": "bad_request",
              "message": "Send JSON with a non-empty \"text\"."
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_71addb6dfa11",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "rejected_with_4xx": true,
          "recovered": true,
          "pass": true
        },
        {
          "case": "null_text",
          "invalid": {
            "status": 400,
            "response": {
              "error": "bad_request",
              "message": "Send JSON with a non-empty \"text\"."
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_a636fad0e5e9",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "rejected_with_4xx": true,
          "recovered": true,
          "pass": true
        },
        {
          "case": "numeric_text",
          "invalid": {
            "status": 400,
            "response": {
              "error": "bad_request",
              "message": "Send JSON with a non-empty \"text\"."
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_0594162b1e3e",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "rejected_with_4xx": true,
          "recovered": true,
          "pass": true
        },
        {
          "case": "boolean_text",
          "invalid": {
            "status": 400,
            "response": {
              "error": "bad_request",
              "message": "Send JSON with a non-empty \"text\"."
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_c4312163c18b",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "rejected_with_4xx": true,
          "recovered": true,
          "pass": true
        },
        {
          "case": "array_text",
          "invalid": {
            "status": 400,
            "response": {
              "error": "bad_request",
              "message": "Send JSON with a non-empty \"text\"."
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_422c0b3c79f4",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "rejected_with_4xx": true,
          "recovered": true,
          "pass": true
        },
        {
          "case": "object_text",
          "invalid": {
            "status": 400,
            "response": {
              "error": "bad_request",
              "message": "Send JSON with a non-empty \"text\"."
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_68c186a02010",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "rejected_with_4xx": true,
          "recovered": true,
          "pass": true
        },
        {
          "case": "malformed_json",
          "invalid": {
            "status": 400,
            "response": {
              "error": "bad_request",
              "message": "Send a JSON object containing non-empty text."
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_8c72db7d0758",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "rejected_with_4xx": true,
          "recovered": true,
          "pass": true
        },
        {
          "case": "oversized_probe_2001_chars",
          "invalid": {
            "status": 200,
            "response": {
              "combined_score": 0.7486999999999999,
              "confidence": 0.7486999999999999,
              "content_id": "c_f1ccb3ac68e5",
              "guess": "ai",
              "label": "This writing shows patterns associated with AI-generated text, but this is not proof that AI was used.",
              "model_score": 0.9974,
              "style_score": 0.5
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_3d9f96ec1077",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "rejected_with_4xx": false,
          "recovered": true,
          "pass": false
        }
      ],
      "criterion_4_pass": true,
      "criterion_5_observed_checks_pass": false
    },
    {
      "trial": 2,
      "appeals": [
        {
          "case": 1,
          "content_id": "c_92e274f12bfb",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_92e274f12bfb",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_92e274f12bfb",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 2,
          "content_id": "c_2c42ee21d4ef",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_2c42ee21d4ef",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_2c42ee21d4ef",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 3,
          "content_id": "c_c3ba60ebff70",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_c3ba60ebff70",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_c3ba60ebff70",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 4,
          "content_id": "c_804587fcb69a",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_804587fcb69a",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_804587fcb69a",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 5,
          "content_id": "c_ca1b61ca6898",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_ca1b61ca6898",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_ca1b61ca6898",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 6,
          "content_id": "c_b942cf3858d7",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_b942cf3858d7",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_b942cf3858d7",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 7,
          "content_id": "c_08e64625b353",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_08e64625b353",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_08e64625b353",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 8,
          "content_id": "c_a7039a1a2937",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_a7039a1a2937",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_a7039a1a2937",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 9,
          "content_id": "c_c800b0ce0490",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_c800b0ce0490",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_c800b0ce0490",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 10,
          "content_id": "c_bed1ddd1e05a",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_bed1ddd1e05a",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_bed1ddd1e05a",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        }
      ],
      "invalid_inputs": [
        {
          "case": "missing_text",
          "invalid": {
            "status": 400,
            "response": {
              "error": "bad_request",
              "message": "Send JSON with a non-empty \"text\"."
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_e8e23d5baa5f",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "rejected_with_4xx": true,
          "recovered": true,
          "pass": true
        },
        {
          "case": "empty_text",
          "invalid": {
            "status": 400,
            "response": {
              "error": "bad_request",
              "message": "Send JSON with a non-empty \"text\"."
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_0ecf88d14464",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "rejected_with_4xx": true,
          "recovered": true,
          "pass": true
        },
        {
          "case": "whitespace_only",
          "invalid": {
            "status": 400,
            "response": {
              "error": "bad_request",
              "message": "Send JSON with a non-empty \"text\"."
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_cfd068aefdc3",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "rejected_with_4xx": true,
          "recovered": true,
          "pass": true
        },
        {
          "case": "null_text",
          "invalid": {
            "status": 400,
            "response": {
              "error": "bad_request",
              "message": "Send JSON with a non-empty \"text\"."
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_cd29da0139ef",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "rejected_with_4xx": true,
          "recovered": true,
          "pass": true
        },
        {
          "case": "numeric_text",
          "invalid": {
            "status": 400,
            "response": {
              "error": "bad_request",
              "message": "Send JSON with a non-empty \"text\"."
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_73406c55eace",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "rejected_with_4xx": true,
          "recovered": true,
          "pass": true
        },
        {
          "case": "boolean_text",
          "invalid": {
            "status": 400,
            "response": {
              "error": "bad_request",
              "message": "Send JSON with a non-empty \"text\"."
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_ace80197f698",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "rejected_with_4xx": true,
          "recovered": true,
          "pass": true
        },
        {
          "case": "array_text",
          "invalid": {
            "status": 400,
            "response": {
              "error": "bad_request",
              "message": "Send JSON with a non-empty \"text\"."
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_7d83a48daea5",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "rejected_with_4xx": true,
          "recovered": true,
          "pass": true
        },
        {
          "case": "object_text",
          "invalid": {
            "status": 400,
            "response": {
              "error": "bad_request",
              "message": "Send JSON with a non-empty \"text\"."
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_bde2a0eeb85b",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "rejected_with_4xx": true,
          "recovered": true,
          "pass": true
        },
        {
          "case": "malformed_json",
          "invalid": {
            "status": 400,
            "response": {
              "error": "bad_request",
              "message": "Send a JSON object containing non-empty text."
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_5f2c92908847",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "rejected_with_4xx": true,
          "recovered": true,
          "pass": true
        },
        {
          "case": "oversized_probe_2001_chars",
          "invalid": {
            "status": 200,
            "response": {
              "combined_score": 0.7486999999999999,
              "confidence": 0.7486999999999999,
              "content_id": "c_75bd68fbcb71",
              "guess": "ai",
              "label": "This writing shows patterns associated with AI-generated text, but this is not proof that AI was used.",
              "model_score": 0.9974,
              "style_score": 0.5
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_f6d608a303fe",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "rejected_with_4xx": false,
          "recovered": true,
          "pass": false
        }
      ],
      "criterion_4_pass": true,
      "criterion_5_observed_checks_pass": false
    },
    {
      "trial": 3,
      "appeals": [
        {
          "case": 1,
          "content_id": "c_59f60717f073",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_59f60717f073",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_59f60717f073",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 2,
          "content_id": "c_29a3444c0d44",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_29a3444c0d44",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_29a3444c0d44",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 3,
          "content_id": "c_22706b53cb83",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_22706b53cb83",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_22706b53cb83",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 4,
          "content_id": "c_b15659183d08",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_b15659183d08",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_b15659183d08",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 5,
          "content_id": "c_184c825cd318",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_184c825cd318",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_184c825cd318",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 6,
          "content_id": "c_a3b83ac21edd",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_a3b83ac21edd",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_a3b83ac21edd",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 7,
          "content_id": "c_554bfeaa517f",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_554bfeaa517f",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_554bfeaa517f",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 8,
          "content_id": "c_5ed50ba53e82",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_5ed50ba53e82",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_5ed50ba53e82",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 9,
          "content_id": "c_7cb0f19ab2c4",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_7cb0f19ab2c4",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_7cb0f19ab2c4",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 10,
          "content_id": "c_7ff0829cdade",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_7ff0829cdade",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_7ff0829cdade",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        }
      ],
      "invalid_inputs": [
        {
          "case": "missing_text",
          "invalid": {
            "status": 400,
            "response": {
              "error": "bad_request",
              "message": "Send JSON with a non-empty \"text\"."
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_e623600e56d9",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "rejected_with_4xx": true,
          "recovered": true,
          "pass": true
        },
        {
          "case": "empty_text",
          "invalid": {
            "status": 400,
            "response": {
              "error": "bad_request",
              "message": "Send JSON with a non-empty \"text\"."
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_df38a8f76e24",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "rejected_with_4xx": true,
          "recovered": true,
          "pass": true
        },
        {
          "case": "whitespace_only",
          "invalid": {
            "status": 400,
            "response": {
              "error": "bad_request",
              "message": "Send JSON with a non-empty \"text\"."
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_b9c329588281",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "rejected_with_4xx": true,
          "recovered": true,
          "pass": true
        },
        {
          "case": "null_text",
          "invalid": {
            "status": 400,
            "response": {
              "error": "bad_request",
              "message": "Send JSON with a non-empty \"text\"."
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_c69d5c77d97c",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "rejected_with_4xx": true,
          "recovered": true,
          "pass": true
        },
        {
          "case": "numeric_text",
          "invalid": {
            "status": 400,
            "response": {
              "error": "bad_request",
              "message": "Send JSON with a non-empty \"text\"."
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_a6aaea840374",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "rejected_with_4xx": true,
          "recovered": true,
          "pass": true
        },
        {
          "case": "boolean_text",
          "invalid": {
            "status": 400,
            "response": {
              "error": "bad_request",
              "message": "Send JSON with a non-empty \"text\"."
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_7abe602799f4",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "rejected_with_4xx": true,
          "recovered": true,
          "pass": true
        },
        {
          "case": "array_text",
          "invalid": {
            "status": 400,
            "response": {
              "error": "bad_request",
              "message": "Send JSON with a non-empty \"text\"."
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_fd5884212dbd",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "rejected_with_4xx": true,
          "recovered": true,
          "pass": true
        },
        {
          "case": "object_text",
          "invalid": {
            "status": 400,
            "response": {
              "error": "bad_request",
              "message": "Send JSON with a non-empty \"text\"."
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_99630a7ffd05",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "rejected_with_4xx": true,
          "recovered": true,
          "pass": true
        },
        {
          "case": "malformed_json",
          "invalid": {
            "status": 400,
            "response": {
              "error": "bad_request",
              "message": "Send a JSON object containing non-empty text."
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_84317bfbc07f",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "rejected_with_4xx": true,
          "recovered": true,
          "pass": true
        },
        {
          "case": "oversized_probe_2001_chars",
          "invalid": {
            "status": 200,
            "response": {
              "combined_score": 0.7486999999999999,
              "confidence": 0.7486999999999999,
              "content_id": "c_474dab937aff",
              "guess": "ai",
              "label": "This writing shows patterns associated with AI-generated text, but this is not proof that AI was used.",
              "model_score": 0.9974,
              "style_score": 0.5
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_b91f21be497b",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "rejected_with_4xx": false,
          "recovered": true,
          "pass": false
        }
      ],
      "criterion_4_pass": true,
      "criterion_5_observed_checks_pass": false
    }
  ],
  "notes": [
    "Existing application configuration was not modified.",
    "2001 characters is a provisional oversized probe, not an established documented maximum.",
    "Criterion 5 cannot receive a complete PASS without a documented and enforced maximum length."
  ],
  "verdicts": {
    "criterion_4": "PASS",
    "criterion_5_observed_requests": "FAIL",
    "criterion_5_full_acceptance": "FAIL"
  }
}
```
