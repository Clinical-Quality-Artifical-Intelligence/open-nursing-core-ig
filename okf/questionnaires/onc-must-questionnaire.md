---
type: "FHIR Questionnaire (SDC)"
title: "MUST (Malnutrition Universal Screening Tool)"
description: "SDC questionnaire for the Malnutrition Universal Screening Tool: three step scores and the total. Coded items extract to Observations using the ONC MUST component codes; assembling them into the single component-based ONCMUSTScore Observation is the capturing app's responsibility."
resource: "https://opennursingcoreig.com/Questionnaire/onc-must-questionnaire"
tags: [fhir, nursing, questionnaire]
timestamp: 2026-07-11T14:13:20Z
---

# MUST (Malnutrition Universal Screening Tool)

SDC questionnaire for the Malnutrition Universal Screening Tool: three step scores and the total. Coded items extract to Observations using the ONC MUST component codes; assembling them into the single component-based ONCMUSTScore Observation is the capturing app's responsibility.

# Items

| linkId | Text | Type | Required |
|--------|------|------|----------|
| `must-bmi` | Step 1 — BMI score (0 = BMI >20 · 1 = BMI 18.5–20 · 2 = BMI <18.5) | integer | yes |
| `must-weight-loss` | Step 2 — Unplanned weight loss in past 3–6 months (0 = <5% · 1 = 5–10% · 2 = >10%) | integer | yes |
| `must-acute-disease` | Step 3 — Acute disease effect (2 = acutely ill AND no nutritional intake for >5 days, or l | integer | yes |
| `must-total` | MUST total score (Step 1 + Step 2 + Step 3) | integer | yes |
| `must-actions` | Management: 0 = low risk — routine care, repeat screening · 1 = medium risk — observe, doc | display |  |

Uses SDC observation-based extraction: coded items extract to Observations conforming to the ONC profiles; display/logic items carry no code and do not extract.
