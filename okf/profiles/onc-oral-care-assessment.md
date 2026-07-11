---
type: "FHIR Profile"
title: "Oral Care Needs Assessment"
description: "Assessment of mouth care needs and oral health."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-oral-care-assessment"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T14:13:20Z
---

# Oral Care Needs Assessment

Assessment of mouth care needs and oral health.

**Parent:** [onc-nursing-assessment](/profiles/onc-nursing-assessment.md)

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.code` |  |  |  |
| `Observation.value[x]` |  | CodeableConcept |  |
| `Observation.component` | 1.. |  |  |
| `Observation.component` | 1..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | CodeableConcept | (binds [onc-empathy-index-vs](/valuesets/onc-empathy-index-vs.md)) |
