# Extended acceptance evaluation — after

- Run ID: `c7dcc33cfe`
- Timestamp: `2026-11-08T20:19:19.653388+00:00`
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
  "run_id": "c7dcc33cfe",
  "timestamp": "2026-11-08T20:19:19.653388+00:00",
  "service": "http://127.0.0.1:5000",
  "trials": [
    {
      "trial": 1,
      "appeals": [
        {
          "case": 1,
          "content_id": "c_3b781a62617a",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_3b781a62617a",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_3b781a62617a",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 2,
          "content_id": "c_ab52cc04a84e",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_ab52cc04a84e",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_ab52cc04a84e",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 3,
          "content_id": "c_3c937ae2fc08",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_3c937ae2fc08",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_3c937ae2fc08",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 4,
          "content_id": "c_c5b88cc20c59",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_c5b88cc20c59",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_c5b88cc20c59",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 5,
          "content_id": "c_f33bdbd2b18e",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_f33bdbd2b18e",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_f33bdbd2b18e",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 6,
          "content_id": "c_b489cd74c945",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_b489cd74c945",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_b489cd74c945",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 7,
          "content_id": "c_95fb05b2c905",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_95fb05b2c905",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_95fb05b2c905",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 8,
          "content_id": "c_d803320d90c9",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_d803320d90c9",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_d803320d90c9",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 9,
          "content_id": "c_cb9b9e7b9412",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_cb9b9e7b9412",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_cb9b9e7b9412",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 10,
          "content_id": "c_f8bd02f30bcc",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_f8bd02f30bcc",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_f8bd02f30bcc",
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
              "content_id": "c_70d094e28ef0",
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
              "content_id": "c_9a9c523b9322",
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
              "content_id": "c_2abed9287293",
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
              "content_id": "c_0d45ae049bb7",
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
              "content_id": "c_157e01d12a19",
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
              "content_id": "c_f7afc1ffc2de",
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
              "content_id": "c_6e460ad1599f",
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
              "content_id": "c_b7d62776ebad",
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
              "content_id": "c_e23e35224cc0",
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
              "content_id": "c_f28e7ca557e5",
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
          "content_id": "c_3f1aa361d0ca",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_3f1aa361d0ca",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_3f1aa361d0ca",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 2,
          "content_id": "c_684b753f9576",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_684b753f9576",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_684b753f9576",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 3,
          "content_id": "c_2d6c4d75dcdf",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_2d6c4d75dcdf",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_2d6c4d75dcdf",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 4,
          "content_id": "c_703d6da9a135",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_703d6da9a135",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_703d6da9a135",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 5,
          "content_id": "c_39f6cc147ec5",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_39f6cc147ec5",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_39f6cc147ec5",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 6,
          "content_id": "c_9d6475008489",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_9d6475008489",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_9d6475008489",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 7,
          "content_id": "c_704454cdf701",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_704454cdf701",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_704454cdf701",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 8,
          "content_id": "c_3f33fad87646",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_3f33fad87646",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_3f33fad87646",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 9,
          "content_id": "c_e3fc58f2a569",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_e3fc58f2a569",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_e3fc58f2a569",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 10,
          "content_id": "c_bab3a9ab593b",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_bab3a9ab593b",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_bab3a9ab593b",
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
              "content_id": "c_145952321e75",
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
              "content_id": "c_cb405e1793b1",
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
              "content_id": "c_82391df47d5b",
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
              "content_id": "c_81f9d1d6a198",
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
              "content_id": "c_130e9e6407ab",
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
              "content_id": "c_63e4a575d070",
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
              "content_id": "c_1b9efecc2416",
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
              "content_id": "c_4141758cb5d9",
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
              "content_id": "c_28e9ae36b4cd",
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
              "content_id": "c_df1d43040a5f",
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
          "content_id": "c_46e9ec861897",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_46e9ec861897",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_46e9ec861897",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 2,
          "content_id": "c_b0989f642dc1",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_b0989f642dc1",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_b0989f642dc1",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 3,
          "content_id": "c_fbea1a7e3185",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_fbea1a7e3185",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_fbea1a7e3185",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 4,
          "content_id": "c_27c85c39c884",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_27c85c39c884",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_27c85c39c884",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 5,
          "content_id": "c_1f7e39f72a2a",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_1f7e39f72a2a",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_1f7e39f72a2a",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 6,
          "content_id": "c_fae9807b1b9b",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_fae9807b1b9b",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_fae9807b1b9b",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 7,
          "content_id": "c_c398a45f1a07",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_c398a45f1a07",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_c398a45f1a07",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 8,
          "content_id": "c_dc242b4425e3",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_dc242b4425e3",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_dc242b4425e3",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 9,
          "content_id": "c_790a90fce915",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_790a90fce915",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_790a90fce915",
              "message": "Your appeal has been recorded for review.",
              "status": "under_review"
            }
          },
          "matching_audit_entries": 1,
          "pass": true
        },
        {
          "case": 10,
          "content_id": "c_6d29197211cc",
          "submission": {
            "status": 200,
            "response": {
              "combined_score": 0.52485,
              "confidence": 0.52485,
              "content_id": "c_6d29197211cc",
              "guess": "unsure",
              "label": "We cannot reliably determine whether this writing was created by a person or AI. No conclusion about authorship should be drawn from this result.",
              "model_score": 0.5746,
              "style_score": 0.4751
            }
          },
          "appeal": {
            "status": 200,
            "response": {
              "content_id": "c_6d29197211cc",
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
              "content_id": "c_9f9e7ba2783c",
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
              "content_id": "c_15f1a7fef9c9",
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
              "content_id": "c_241c3bd972e7",
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
              "content_id": "c_aca58909d833",
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
              "content_id": "c_5c02c41e46a0",
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
              "content_id": "c_894128403915",
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
              "content_id": "c_28ab3fb814ae",
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
              "content_id": "c_55dc59e757d4",
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
              "content_id": "c_45fd6f318301",
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
              "content_id": "c_e90e597bd95d",
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
