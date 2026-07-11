---
type: "Metric"
title: "Pressure-ulcer late-detection rate (by Monk skin-tone band)"
description: "Percentage of pressure ulcers first documented at stage 3+, unstageable, or deep-tissue injury, stratified by Monk Skin Tone band (A-J). The ONC-IG's headline equity metric."
resource: "https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/tree/main/analytics/equity"
tags: [metric, equity, nursing, pressure-ulcer]
timestamp: 2026-07-10T00:00:00Z
---

# Pressure-ulcer late-detection rate

**Definition:** for each Monk Skin Tone band *b* (A–J):

```
late_detection_rate(b) =
    count(pressure ulcers of patients in band b whose FIRST documentation
          is stage-3, stage-4, unstageable, or deep-tissue)
  / count(all pressure ulcers of patients in band b)
  × 100
```

**Why it exists:** early pressure-damage signs described as "redness" or
"blanching" are unreliable on darker skin, so detection can happen later —
at a worse stage. If a service cannot stratify detection by skin tone, that
inequity stays invisible. Because the ONC-IG records skin tone as structured
data ([Monk Skin Tone Observation](../profiles/onc-monk-skintone-observation.md))
and its fairness gate requires it on every pressure-area assessment
([Braden](../profiles/onc-braden-scale-assessment.md),
[Waterlow](../profiles/onc-waterlow-score.md)), the metric is a single join.

**Inputs:**

- Skin tone: Observations with code `mst-score`
  ([ONC Observation Codes](../codesystems/onc-observation-codes.md)),
  value from the [Monk Scale](../codesystems/onc-monk-scale.md) (A–J)
- Pressure ulcers: Observations with SNOMED `399912005`, stage in
  `valueCodeableConcept` (`stage-1` … `deep-tissue`)
- Join key: `Observation.subject` (patient)

**Companion measure:** median days from skin-tone assessment (baseline) to
first pressure-ulcer documentation, per band.

**Reference implementation:** `analytics/equity/run_analysis.py`
(FHIR NDJSON → Parquet → stratified metrics). In production the same Parquet
views come from [OHS fhir-data-pipes](https://github.com/ohs-foundation/fhir-data-pipes).

**Caution:** demo outputs in the repository use *synthetic data with a
deliberately injected bias* and must never be quoted as clinical findings.
Interpretation of any real disparity belongs with clinical and equity
leadership.
