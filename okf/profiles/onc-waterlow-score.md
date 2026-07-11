---
type: "FHIR Profile"
title: "Waterlow Score"
description: "Waterlow Pressure Ulcer Risk Assessment - NHS standard tool. Score ≥10 indicates at risk, ≥15 high risk, ≥20 very high risk."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-waterlow-score"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T13:58:05Z
---

# Waterlow Score

Waterlow Pressure Ulcer Risk Assessment - NHS standard tool. Score ≥10 indicates at risk, ≥15 high risk, ≥20 very high risk.

**Parent:** [onc-nursing-assessment](/profiles/onc-nursing-assessment.md)

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.status` |  |  |  |
| `Observation.code` |  |  |  |
| `Observation.value[x]` | 1.. | Quantity | Waterlow total score (0-64+, higher = higher risk) |
| `Observation.value[x].value` |  |  |  |
| `Observation.value[x].unit` |  |  |  |
| `Observation.value[x].system` |  |  |  |
| `Observation.hasMember` | 1.. |  |  |
| `Observation.hasMember` | 1..1 | Reference | Mandatory Skin Tone Context (Equity Gate) |
| `Observation.component` |  |  | Risk factor components (build, skin type, age, continence, mobility, appetite, special risks) |
