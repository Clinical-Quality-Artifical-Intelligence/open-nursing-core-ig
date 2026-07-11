---
type: "FHIR Profile"
title: "Glasgow Coma Scale"
description: "Glasgow Coma Scale (GCS) for assessing level of consciousness. Total score 3-15 with three required components: Eye (1-4), Verbal (1-5), Motor (1-6)."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-glasgow-coma-scale"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T13:58:05Z
---

# Glasgow Coma Scale

Glasgow Coma Scale (GCS) for assessing level of consciousness. Total score 3-15 with three required components: Eye (1-4), Verbal (1-5), Motor (1-6).

**Parent:** [onc-nursing-assessment](/profiles/onc-nursing-assessment.md)

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.code` |  |  |  |
| `Observation.value[x]` | 1.. | Quantity | GCS total score (3-15) |
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
