---
type: "FHIR Profile"
title: "Mobility Assessment"
description: "Assessment of capability to move and limitations."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-mobility-assessment"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T14:13:20Z
---

# Mobility Assessment

Assessment of capability to move and limitations.

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
