---
type: "FHIR Questionnaire (SDC)"
title: "Braden Scale (Pressure Ulcer Risk)"
description: "SDC questionnaire for the Braden pressure-ulcer risk assessment: six subscales, total score, and a mandatory Monk Skin Tone item (the equity fairness gate is embedded at the capture layer). Coded items extract to Observations using the ONC Braden component codes; assembling them into the single component-based ONCBradenScaleAssessment Observation (including hasMember[skinTone]) is the capturing app's responsibility."
resource: "https://opennursingcoreig.com/Questionnaire/onc-braden-questionnaire"
tags: [fhir, nursing, questionnaire]
timestamp: 2026-07-11T13:58:05Z
---

# Braden Scale (Pressure Ulcer Risk)

SDC questionnaire for the Braden pressure-ulcer risk assessment: six subscales, total score, and a mandatory Monk Skin Tone item (the equity fairness gate is embedded at the capture layer). Coded items extract to Observations using the ONC Braden component codes; assembling them into the single component-based ONCBradenScaleAssessment Observation (including hasMember[skinTone]) is the capturing app's responsibility.

# Items

| linkId | Text | Type | Required |
|--------|------|------|----------|
| `braden-sensory` | Sensory perception (1 = Completely limited · 2 = Very limited · 3 = Slightly limited · 4 = | integer | yes |
| `braden-moisture` | Moisture (1 = Constantly moist · 2 = Very moist · 3 = Occasionally moist · 4 = Rarely mois | integer | yes |
| `braden-activity` | Activity (1 = Bedfast · 2 = Chairfast · 3 = Walks occasionally · 4 = Walks frequently) | integer | yes |
| `braden-mobility` | Mobility (1 = Completely immobile · 2 = Very limited · 3 = Slightly limited · 4 = No limit | integer | yes |
| `braden-nutrition` | Nutrition (1 = Very poor · 2 = Probably inadequate · 3 = Adequate · 4 = Excellent) | integer | yes |
| `braden-friction` | Friction and shear (1 = Problem · 2 = Potential problem · 3 = No apparent problem) | integer | yes |
| `braden-total` | Braden total score (6–23; lower = higher risk) | integer | yes |
| `braden-skintone` | Monk Skin Tone Scale rating (required — equity fairness gate: pressure-area assessment is  | choice | yes |
| `braden-banding` | Risk banding: 15–18 mild · 13–14 moderate · 10–12 high · ≤9 severe. On darker skin tones d | display |  |

Uses SDC observation-based extraction: coded items extract to Observations conforming to the ONC profiles; display/logic items carry no code and do not extract.
