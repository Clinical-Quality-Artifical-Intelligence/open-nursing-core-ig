---
type: "FHIR Questionnaire (SDC)"
title: "Monk Skin Tone Scale (A–J)"
description: "SDC questionnaire capturing the patient's skin tone on the 10-point Monk Skin Tone Scale (A–J). Extracts to an Observation conforming to ONCMonkSkinToneObservation. This record is the required input to the IG's equity fairness gate for wound and pressure-area assessment."
resource: "https://opennursingcoreig.com/Questionnaire/onc-monk-skintone-questionnaire"
tags: [fhir, nursing, questionnaire]
timestamp: 2026-07-11T13:58:05Z
---

# Monk Skin Tone Scale (A–J)

SDC questionnaire capturing the patient's skin tone on the 10-point Monk Skin Tone Scale (A–J). Extracts to an Observation conforming to ONCMonkSkinToneObservation. This record is the required input to the IG's equity fairness gate for wound and pressure-area assessment.

# Items

| linkId | Text | Type | Required |
|--------|------|------|----------|
| `mst-intro` | Record the skin tone that best matches the patient, assessed with the patient's involvemen | display |  |
| `mst-score` | Monk Skin Tone Scale rating | choice | yes |

Uses SDC observation-based extraction: coded items extract to Observations conforming to the ONC profiles; display/logic items carry no code and do not extract.
