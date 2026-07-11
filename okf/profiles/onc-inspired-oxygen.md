---
type: "FHIR Profile"
title: "Inspired Oxygen"
description: "Inspired oxygen observation for NEWS2 (air vs supplemental oxygen)"
resource: "https://opennursingcoreig.com/StructureDefinition/onc-inspired-oxygen"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T14:13:20Z
---

# Inspired Oxygen

Inspired oxygen observation for NEWS2 (air vs supplemental oxygen)

**Parent:** [onc-nursing-assessment](/profiles/onc-nursing-assessment.md)

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.value[x]` |  | Quantity, CodeableConcept |  |
| `Observation.value[x]` | 0..1 | Quantity |  |
| `Observation.value[x].unit` |  |  |  |
| `Observation.value[x].system` |  |  |  |
| `Observation.value[x]` | 0..1 | CodeableConcept | (binds [inspired-oxygen-vs](/valuesets/inspired-oxygen-vs.md)) |
