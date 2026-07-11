---
type: "FHIR Profile"
title: "MUST Score (Malnutrition Universal Screening Tool)"
description: "Malnutrition Universal Screening Tool for identifying adults at risk of malnutrition. Score 0=low risk, 1=medium risk, 2+=high risk. NHS-standard nutritional screening."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-must-score"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T14:13:20Z
---

# MUST Score (Malnutrition Universal Screening Tool)

Malnutrition Universal Screening Tool for identifying adults at risk of malnutrition. Score 0=low risk, 1=medium risk, 2+=high risk. NHS-standard nutritional screening.

**Parent:** [onc-nursing-assessment](/profiles/onc-nursing-assessment.md)

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.code` |  |  |  |
| `Observation.value[x]` | 1.. | Quantity | MUST total score (0-6, higher = higher risk) |
| `Observation.value[x].value` |  |  |  |
| `Observation.value[x].unit` |  |  |  |
| `Observation.value[x].system` |  |  |  |
| `Observation.component` | 3..3 |  |  |
| `Observation.component` | 1..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | Quantity |  |
| `Observation.component.value[x].value` |  |  |  |
| `Observation.component.value[x].unit` |  |  |  |
| `Observation.component.value[x].system` |  |  |  |
| `Observation.component` | 1..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | Quantity |  |
| `Observation.component.value[x].value` |  |  |  |
| `Observation.component.value[x].unit` |  |  |  |
| `Observation.component.value[x].system` |  |  |  |
| `Observation.component` | 1..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | Quantity |  |
| `Observation.component.value[x].value` |  |  |  |
| `Observation.component.value[x].unit` |  |  |  |
| `Observation.component.value[x].system` |  |  |  |
