---
type: "FHIR Questionnaire (SDC)"
title: "NEWS2 (National Early Warning Score 2)"
description: "SDC questionnaire for capturing the NEWS2 physiological parameter set and total score. Coded items extract to Observations conforming to the ONC NEWS2 and vital-sign profiles. Scoring and escalation logic is computable via the ONC_NEWS2_Logic CQL library and the news2-escalation PlanDefinition."
resource: "https://opennursingcoreig.com/Questionnaire/onc-news2-questionnaire"
tags: [fhir, nursing, questionnaire]
timestamp: 2026-07-11T13:58:05Z
---

# NEWS2 (National Early Warning Score 2)

SDC questionnaire for capturing the NEWS2 physiological parameter set and total score. Coded items extract to Observations conforming to the ONC NEWS2 and vital-sign profiles. Scoring and escalation logic is computable via the ONC_NEWS2_Logic CQL library and the news2-escalation PlanDefinition.

# Items

| linkId | Text | Type | Required |
|--------|------|------|----------|
| `resp-rate` | Respiration rate (breaths per minute) | integer | yes |
| `spo2` | Oxygen saturation, SpO2 (%) | integer | yes |
| `spo2-scale2` | Use SpO2 Scale 2? (Prescribed target saturation 88–92%, e.g. hypercapnic respiratory failu | boolean | yes |
| `o2-status` | Air or supplemental oxygen? | choice | yes |
| `systolic-bp` | Systolic blood pressure (mmHg) | integer | yes |
| `diastolic-bp` | Diastolic blood pressure (mmHg) — recorded, not scored | integer |  |
| `heart-rate` | Pulse / heart rate (beats per minute) | integer | yes |
| `temperature` | Body temperature (°C) | decimal | yes |
| `acvpu` | Level of consciousness (ACVPU) | choice | yes |
| `news2-total` | NEWS2 total score (0–20) | integer | yes |
| `escalation-guidance` | Escalation (RCP NEWS2): 0–4 low risk — routine monitoring · 3 in any single parameter — re | display |  |

Uses SDC observation-based extraction: coded items extract to Observations conforming to the ONC profiles; display/logic items carry no code and do not extract.
