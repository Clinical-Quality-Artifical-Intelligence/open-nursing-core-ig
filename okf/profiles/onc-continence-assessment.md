---
type: "FHIR Profile"
title: "Continence Assessment"
description: "Assessment of bladder and bowel control status."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-continence-assessment"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T13:58:05Z
---

# Continence Assessment

Assessment of bladder and bowel control status.

**Parent:** [onc-nursing-assessment](/profiles/onc-nursing-assessment.md)

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.value[x]` |  | CodeableConcept | (binds `http://hl7.org/fhir/ValueSet/consistency-type`) |
