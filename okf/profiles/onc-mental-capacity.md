---
type: "FHIR Profile"
title: "Mental Capacity Assessment"
description: "Records the outcome of a Mental Capacity Assessment for a specific decision. Fundamental legal safeguard in UK nursing practice."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-mental-capacity"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T13:58:05Z
---

# Mental Capacity Assessment

Records the outcome of a Mental Capacity Assessment for a specific decision. Fundamental legal safeguard in UK nursing practice.

**Parent:** [onc-nursing-assessment](/profiles/onc-nursing-assessment.md)

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.value[x]` | 1.. | CodeableConcept | Outcome (Capacity Present/Absent) (binds [onc-mca-vs](/valuesets/onc-mca-vs.md)) |
| `Observation.note` | 1.. |  | The specific decision being assessed (CRITICAL) |
