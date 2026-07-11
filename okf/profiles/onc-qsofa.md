---
type: "FHIR Profile"
title: "qSOFA (Quick SOFA)"
description: "Quick Sequential Organ Failure Assessment for sepsis screening. Score ≥2 indicates high risk. Total range 0-3."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-qsofa"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T13:58:05Z
---

# qSOFA (Quick SOFA)

Quick Sequential Organ Failure Assessment for sepsis screening. Score ≥2 indicates high risk. Total range 0-3.

**Parent:** [onc-nursing-assessment](/profiles/onc-nursing-assessment.md)

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.code` |  |  |  |
| `Observation.value[x]` | 1.. | Quantity | qSOFA total score (0-3, ≥2 = high risk) |
| `Observation.value[x].value` |  |  |  |
| `Observation.value[x].unit` |  |  |  |
| `Observation.value[x].system` |  |  |  |
