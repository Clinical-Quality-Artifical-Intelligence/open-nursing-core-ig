---
type: "FHIR Profile"
title: "ONC Nursing Strength"
description: "A structured representation of a patient's strength or capability. Explicitly required by PRSB to move away from deficit-based models."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-nursing-strength"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T13:58:05Z
---

# ONC Nursing Strength

A structured representation of a patient's strength or capability. Explicitly required by PRSB to move away from deficit-based models.

**Parent:** `http://hl7.org/fhir/StructureDefinition/Observation`

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.code` |  |  |  |
| `Observation.subject` |  | Reference |  |
| `Observation.value[x]` |  | CodeableConcept, string |  |
| `Observation.note` |  |  |  |
