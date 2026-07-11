---
type: "FHIR Profile"
title: "Wound Assessment"
description: "Comprehensive wound assessment including staging and dimensions"
resource: "https://opennursingcoreig.com/StructureDefinition/onc-wound-assessment"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T14:13:20Z
---

# Wound Assessment

Comprehensive wound assessment including staging and dimensions

**Parent:** [onc-nursing-assessment](/profiles/onc-nursing-assessment.md)

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.code` |  |  |  |
| `Observation.value[x]` | 1.. | CodeableConcept | Wound stage (binds [wound-stage-vs](/valuesets/wound-stage-vs.md)) |
| `Observation.component` |  |  |  |
| `Observation.component` | 0..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | Quantity |  |
| `Observation.component.value[x].value` |  |  |  |
| `Observation.component.value[x].unit` |  |  |  |
| `Observation.component.value[x].system` |  |  |  |
| `Observation.component.value[x].code` |  |  |  |
| `Observation.component` | 0..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | Quantity |  |
| `Observation.component.value[x].value` |  |  |  |
| `Observation.component.value[x].unit` |  |  |  |
| `Observation.component.value[x].system` |  |  |  |
| `Observation.component.value[x].code` |  |  |  |
| `Observation.component` | 0..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | Quantity |  |
| `Observation.component.value[x].value` |  |  |  |
| `Observation.component.value[x].unit` |  |  |  |
| `Observation.component.value[x].system` |  |  |  |
| `Observation.component.value[x].code` |  |  |  |
