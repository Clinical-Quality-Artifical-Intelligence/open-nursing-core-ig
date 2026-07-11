---
type: "FHIR Profile"
title: "ACVPU Consciousness Level"
description: "ACVPU consciousness level assessment for NEWS2 (Alert, Confusion, Voice, Pain, Unresponsive)"
resource: "https://opennursingcoreig.com/StructureDefinition/onc-acvpu"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T14:13:20Z
---

# ACVPU Consciousness Level

ACVPU consciousness level assessment for NEWS2 (Alert, Confusion, Voice, Pain, Unresponsive)

**Parent:** [onc-nursing-assessment](/profiles/onc-nursing-assessment.md)

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.value[x]` |  | CodeableConcept | (binds [acvpu-vs](/valuesets/acvpu-vs.md)) |
