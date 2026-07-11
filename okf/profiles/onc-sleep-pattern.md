---
type: "FHIR Profile"
title: "Sleep Pattern"
description: "Observation of sleep quality, duration, and disturbances. Sleep pattern disturbance is a key indicator for delirium and general wellbeing."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-sleep-pattern"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T13:58:05Z
---

# Sleep Pattern

Observation of sleep quality, duration, and disturbances. Sleep pattern disturbance is a key indicator for delirium and general wellbeing.

**Parent:** [onc-nursing-assessment](/profiles/onc-nursing-assessment.md)

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.value[x]` | 1.. | string | Overall summary of sleep period |
| `Observation.component` |  |  |  |
| `Observation.component` | 0..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | string | e.g., 'Restful', 'Fitful', 'Broken' |
| `Observation.component` | 0..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | Quantity |  |
| `Observation.component.value[x].unit` |  |  |  |
| `Observation.component.value[x].system` |  |  |  |
| `Observation.component.value[x].code` |  |  |  |
| `Observation.component` | 0..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | string |  |
