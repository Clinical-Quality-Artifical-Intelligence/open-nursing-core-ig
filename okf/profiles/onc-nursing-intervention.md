---
type: "FHIR Profile"
title: "ONC Nursing Intervention"
description: "Nursing intervention performed to achieve patient goals. Part of ADPIE Implementation phase."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-nursing-intervention"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T14:13:20Z
---

# ONC Nursing Intervention

Nursing intervention performed to achieve patient goals. Part of ADPIE Implementation phase.

**Parent:** `http://hl7.org/fhir/StructureDefinition/Procedure`

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Procedure.extension` | 0..* | Extension |  |
| `Procedure.status` |  |  |  |
| `Procedure.code` | 1.. |  | (binds [nursing-intervention-valueset](/valuesets/nursing-intervention-valueset.md)) |
