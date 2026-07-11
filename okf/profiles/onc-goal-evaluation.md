---
type: "FHIR Profile"
title: "ONC Goal Evaluation"
description: "Explicit evaluation of whether a nursing goal was achieved, closing the ADPIE loop."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-goal-evaluation"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T09:01:38Z
---

# ONC Goal Evaluation

Explicit evaluation of whether a nursing goal was achieved, closing the ADPIE loop.

**Parent:** `http://hl7.org/fhir/StructureDefinition/Observation`

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.extension` | 0..1 | Extension |  |
| `Observation.status` |  |  |  |
| `Observation.code` |  |  |  |
| `Observation.subject` |  | Reference |  |
| `Observation.focus` | 1..1 | Reference |  |
| `Observation.value[x]` |  | CodeableConcept | (binds [goal-evaluation-valueset](/valuesets/goal-evaluation-valueset.md)) |
| `Observation.note` | ..1 |  |  |
| `Observation.derivedFrom` |  | Reference |  |
