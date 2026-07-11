---
type: "FHIR Profile"
title: "PBS ABC Chart"
description: "Antecedent-Behaviour-Consequence (ABC) Chart for recording behaviours of concern. Fundamental tool in Positive Behaviour Support (PBS) for Learning Disabilities."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-abc-chart"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T14:13:20Z
---

# PBS ABC Chart

Antecedent-Behaviour-Consequence (ABC) Chart for recording behaviours of concern. Fundamental tool in Positive Behaviour Support (PBS) for Learning Disabilities.

**Parent:** [onc-nursing-assessment](/profiles/onc-nursing-assessment.md)

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.value[x]` | 1.. | CodeableConcept | Hypothesized Function (SEAT) (binds [onc-pbs-function-vs](/valuesets/onc-pbs-function-vs.md)) |
| `Observation.component` | 3.. |  |  |
| `Observation.component` | 1..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` | 1.. | string | Trigger/Context (Who, What, Where, When) |
| `Observation.component` | 1..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` | 1.. | string | Exact description of what was done |
| `Observation.component` | 1..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` | 1.. | string | Staff response & Outcome |
| `Observation.component` | 0..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` | 1.. | Quantity |  |
| `Observation.component.value[x].unit` |  |  |  |
| `Observation.component.value[x].system` |  |  |  |
| `Observation.component.value[x].code` |  |  |  |
| `Observation.component` | 0..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` | 1.. | integer | 1 (Mild) to 10 (Severe) |
