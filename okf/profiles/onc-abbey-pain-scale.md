---
type: "FHIR Profile"
title: "Abbey Pain Scale"
description: "Pain assessment for people with dementia or who cannot verbalise. Assesses 6 parameters: Vocalization, Facial Expression, Body Language, Behavioral Change, Physiological Change, Physical Changes. Total score determines pain severity (0-2 No pain, 3-7 Mild, 8-13 Moderate, 14+ Severe)."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-abbey-pain-scale"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T14:13:20Z
---

# Abbey Pain Scale

Pain assessment for people with dementia or who cannot verbalise. Assesses 6 parameters: Vocalization, Facial Expression, Body Language, Behavioral Change, Physiological Change, Physical Changes. Total score determines pain severity (0-2 No pain, 3-7 Mild, 8-13 Moderate, 14+ Severe).

**Parent:** [onc-nursing-assessment](/profiles/onc-nursing-assessment.md)

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.value[x]` | 1.. | Quantity | Abbey Pain Total Score |
| `Observation.value[x].unit` |  |  |  |
| `Observation.value[x].system` |  |  |  |
| `Observation.component` |  |  |  |
| `Observation.component` | 0..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` | 1.. | integer | Score (0=Absent, 1=Mild, 2=Moderate, 3=Severe) |
| `Observation.component` | 0..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` | 1.. | integer |  |
| `Observation.component` | 0..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` | 1.. | integer |  |
| `Observation.component` | 0..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` | 1.. | integer |  |
| `Observation.component` | 0..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` | 1.. | integer |  |
| `Observation.component` | 0..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` | 1.. | integer |  |
