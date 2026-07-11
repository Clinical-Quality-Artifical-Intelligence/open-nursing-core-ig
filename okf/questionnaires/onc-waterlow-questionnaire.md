---
type: "FHIR Questionnaire (SDC)"
title: "Waterlow Score (Pressure Ulcer Risk)"
description: "SDC questionnaire for the Waterlow pressure-ulcer risk assessment total score, with a mandatory Monk Skin Tone item (equity fairness gate embedded at the capture layer). The total extracts to an Observation using the ONC Waterlow code; linking the skin-tone Observation via hasMember[skinTone] is the capturing app's responsibility."
resource: "https://opennursingcoreig.com/Questionnaire/onc-waterlow-questionnaire"
tags: [fhir, nursing, questionnaire]
timestamp: 2026-07-11T14:13:20Z
---

# Waterlow Score (Pressure Ulcer Risk)

SDC questionnaire for the Waterlow pressure-ulcer risk assessment total score, with a mandatory Monk Skin Tone item (equity fairness gate embedded at the capture layer). The total extracts to an Observation using the ONC Waterlow code; linking the skin-tone Observation via hasMember[skinTone] is the capturing app's responsibility.

# Items

| linkId | Text | Type | Required |
|--------|------|------|----------|
| `waterlow-total` | Waterlow total score (sum of all risk-factor items on the Waterlow chart) | integer | yes |
| `waterlow-factors` | Contributing risk factors (build/weight, skin type, continence, mobility, appetite, specia | text |  |
| `waterlow-skintone` | Monk Skin Tone Scale rating (required — equity fairness gate: pressure-area assessment is  | choice | yes |
| `waterlow-banding` | Risk banding: ≥10 at risk · ≥15 high risk · ≥20 very high risk. On darker skin tones do no | display |  |

Uses SDC observation-based extraction: coded items extract to Observations conforming to the ONC profiles; display/logic items carry no code and do not extract.
