---
type: "FHIR Profile"
title: "Oral Health Assessment"
description: "Assessment of oral cavity health. Critical for prevention of pneumonia in frail elderly and maintaining nutrition/hydration."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-oral-health"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T13:58:05Z
---

# Oral Health Assessment

Assessment of oral cavity health. Critical for prevention of pneumonia in frail elderly and maintaining nutrition/hydration.

**Parent:** [onc-nursing-assessment](/profiles/onc-nursing-assessment.md)

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.value[x]` | 1.. | Quantity, string |  |
| `Observation.value[x]` | 1..1 | Quantity | Total Score (if using a scored tool like OHAT) |
| `Observation.value[x].unit` |  |  |  |
| `Observation.value[x].system` |  |  |  |
| `Observation.value[x].code` |  |  |  |
| `Observation.component` |  |  |  |
| `Observation.component` | 0..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | string |  |
| `Observation.component` | 0..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | string |  |
| `Observation.component` | 0..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | string |  |
| `Observation.component` | 0..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | string |  |
| `Observation.component` | 0..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | string |  |
