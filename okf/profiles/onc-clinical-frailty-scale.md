---
type: "FHIR Profile"
title: "Clinical Frailty Scale (CFS)"
description: "Assessment of frailty using the Rockwood Clinical Frailty Scale (1-9). Essential for older adults to determine baseline functional status."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-clinical-frailty-scale"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T09:01:38Z
---

# Clinical Frailty Scale (CFS)

Assessment of frailty using the Rockwood Clinical Frailty Scale (1-9). Essential for older adults to determine baseline functional status.

**Parent:** [onc-nursing-assessment](/profiles/onc-nursing-assessment.md)

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.code` |  |  |  |
| `Observation.value[x]` | 1.. | CodeableConcept | Frailty Level (1-9) (binds [onc-cfs-vs](/valuesets/onc-cfs-vs.md)) |
