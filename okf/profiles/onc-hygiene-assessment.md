---
type: "FHIR Profile"
title: "Personal Hygiene Needs Assessment"
description: "Assessment of assistance required for personal hygiene."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-hygiene-assessment"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T14:13:20Z
---

# Personal Hygiene Needs Assessment

Assessment of assistance required for personal hygiene.

**Parent:** [onc-nursing-assessment](/profiles/onc-nursing-assessment.md)

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.value[x]` |  | CodeableConcept |  |
| `Observation.component` | 1.. |  |  |
| `Observation.component` | 1..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | CodeableConcept | (binds [onc-empathy-index-vs](/valuesets/onc-empathy-index-vs.md)) |
