# Extended acceptance evaluation — after

- Run ID: `ce85aa760e`
- Timestamp: `2026-11-08T20:43:53.471920+00:00`
- Trials: 3
- Existing detector and configuration unchanged

## Trial summary

| Trial | Appeals | Invalid 4xx + recovery |
|---|---|---|
| 1 | 10/10 | 10/10 |
| 2 | 10/10 | 10/10 |
| 3 | 10/10 | 10/10 |

## Verdicts

- Criterion 4: **PASS**
- Criterion 5 observed requests: **PASS**
- Criterion 5 full acceptance: **PASS**

The oversized case uses 2001 characters as a provisional probe. This is not a documented maximum.

## Raw evidence

```json
{
  "run_id": "ce85aa760e",
  "timestamp": "2026-11-08T20:43:53.471920+00:00",
  "service": "http://127.0.0.1:5000",
  "trials": [
    {
      "trial": 1,
      "appeals": [
        {
          "case": 1,
          "content_id": "c_ac146f42de11",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_ac146f42de11",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_ac146f42de11",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 2,
          "content_id": "c_380ae09a46bd",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_380ae09a46bd",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_380ae09a46bd",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 3,
          "content_id": "c_1968ef6b1a33",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_1968ef6b1a33",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_1968ef6b1a33",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 4,
          "content_id": "c_3c653519e228",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_3c653519e228",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_3c653519e228",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 5,
          "content_id": "c_b594da8c0803",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_b594da8c0803",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_b594da8c0803",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 6,
          "content_id": "c_583835dcf2e1",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_583835dcf2e1",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_583835dcf2e1",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 7,
          "content_id": "c_2257af192c85",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_2257af192c85",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_2257af192c85",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 8,
          "content_id": "c_91d2359a669e",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_91d2359a669e",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_91d2359a669e",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 9,
          "content_id": "c_9c23b19259d8",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_9c23b19259d8",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_9c23b19259d8",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 10,
          "content_id": "c_ed9bcc603292",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_ed9bcc603292",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_ed9bcc603292",
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
              "content_id": "c_5e9104222be0",
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
              "content_id": "c_d2afcf34b778",
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
              "content_id": "c_a1fa930130cf",
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
              "content_id": "c_2c80469353b3",
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
              "content_id": "c_e29b2842e3b8",
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
              "content_id": "c_6568d0fd5649",
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
              "content_id": "c_26e516619d8d",
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
              "content_id": "c_15fd71e65a32",
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
            "status": 429,
            "response": {
              "error": "rate_limited",
              "limit": "5 per 1 minute",
              "message": "Too many submissions. Try again shortly."
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_5d90b11b5ec5",
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
          "case": "oversized_probe",
          "invalid": {
            "status": 400,
            "response": {
              "error": "bad_request",
              "message": "Text must not exceed 2000 characters."
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_ac205899605c",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "rejected_with_4xx": true,
          "recovered": true,
          "pass": true
        }
      ],
      "criterion_4_pass": true,
      "criterion_5_observed_checks_pass": true
    },
    {
      "trial": 2,
      "appeals": [
        {
          "case": 1,
          "content_id": "c_5a421b159467",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_5a421b159467",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_5a421b159467",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 2,
          "content_id": "c_7b0f1782c4c9",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_7b0f1782c4c9",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_7b0f1782c4c9",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 3,
          "content_id": "c_837fdf0c6810",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_837fdf0c6810",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_837fdf0c6810",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 4,
          "content_id": "c_fbab71627ead",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_fbab71627ead",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_fbab71627ead",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 5,
          "content_id": "c_8c2cd648bc99",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_8c2cd648bc99",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_8c2cd648bc99",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 6,
          "content_id": "c_e8454c950343",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_e8454c950343",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_e8454c950343",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 7,
          "content_id": "c_cfe8d4c2f3b1",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_cfe8d4c2f3b1",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_cfe8d4c2f3b1",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 8,
          "content_id": "c_026baee63c15",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_026baee63c15",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_026baee63c15",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 9,
          "content_id": "c_e4b650764bae",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_e4b650764bae",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_e4b650764bae",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 10,
          "content_id": "c_1a21ef8347d9",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_1a21ef8347d9",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_1a21ef8347d9",
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
              "content_id": "c_c0482fc2e7c0",
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
              "content_id": "c_b20786e253d6",
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
              "content_id": "c_bc5e7ddd8559",
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
              "content_id": "c_f5cef1cf434d",
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
              "content_id": "c_45eeab6fb4e7",
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
              "content_id": "c_8395b9b92dab",
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
              "content_id": "c_09e6d21de70b",
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
              "content_id": "c_14f643f0347c",
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
            "status": 429,
            "response": {
              "error": "rate_limited",
              "limit": "5 per 1 minute",
              "message": "Too many submissions. Try again shortly."
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_6b524443c3cd",
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
          "case": "oversized_probe",
          "invalid": {
            "status": 400,
            "response": {
              "error": "bad_request",
              "message": "Text must not exceed 2000 characters."
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_23da4416b2c3",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "rejected_with_4xx": true,
          "recovered": true,
          "pass": true
        }
      ],
      "criterion_4_pass": true,
      "criterion_5_observed_checks_pass": true
    },
    {
      "trial": 3,
      "appeals": [
        {
          "case": 1,
          "content_id": "c_c6e3825a34f8",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_c6e3825a34f8",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_c6e3825a34f8",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 2,
          "content_id": "c_871cf94c07e1",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_871cf94c07e1",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_871cf94c07e1",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 3,
          "content_id": "c_b59c0f2f1f5f",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_b59c0f2f1f5f",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_b59c0f2f1f5f",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 4,
          "content_id": "c_8858307b999d",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_8858307b999d",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_8858307b999d",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 5,
          "content_id": "c_8f96a99e9ef1",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_8f96a99e9ef1",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_8f96a99e9ef1",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 6,
          "content_id": "c_ce68e79c8d74",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_ce68e79c8d74",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_ce68e79c8d74",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 7,
          "content_id": "c_da21d8391240",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_da21d8391240",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_da21d8391240",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 8,
          "content_id": "c_0d1ce2ea72d8",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_0d1ce2ea72d8",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_0d1ce2ea72d8",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 9,
          "content_id": "c_c530b380c8c3",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_c530b380c8c3",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_c530b380c8c3",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 10,
          "content_id": "c_a7fd44ae1ef4",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_a7fd44ae1ef4",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_a7fd44ae1ef4",
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
              "content_id": "c_68e4fea00ecf",
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
              "content_id": "c_2243fffb5b66",
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
              "content_id": "c_cea7587ef10e",
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
              "content_id": "c_6225982bbee7",
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
              "content_id": "c_aa6a601c7899",
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
              "content_id": "c_c3253ff41b37",
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
              "content_id": "c_b6e1df86ee1c",
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
              "content_id": "c_be9f67254418",
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
            "status": 429,
            "response": {
              "error": "rate_limited",
              "limit": "5 per 1 minute",
              "message": "Too many submissions. Try again shortly."
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_17ea8fd9d892",
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
          "case": "oversized_probe",
          "invalid": {
            "status": 400,
            "response": {
              "error": "bad_request",
              "message": "Text must not exceed 2000 characters."
            }
          },
          "recovery": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_0140bb499589",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "rejected_with_4xx": true,
          "recovered": true,
          "pass": true
        }
      ],
      "criterion_4_pass": true,
      "criterion_5_observed_checks_pass": true
    }
  ],
  "notes": [
    "Existing application configuration was not modified.",
    "2001 characters is a provisional oversized probe, not an established documented maximum.",
    "Criterion 5 cannot receive a complete PASS without a documented and enforced maximum length."
  ],
  "verdicts": {
    "criterion_4": "PASS",
    "criterion_5_observed_requests": "PASS",
    "criterion_5_full_acceptance": "PASS"
  }
}
```
