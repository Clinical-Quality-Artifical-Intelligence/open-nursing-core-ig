---
type: "FHIR Profile"
title: "What Matters to Me"
description: "Captures the patient's specific, personal priorities and non-clinical goals (e.g., 'I want to walk my daughter down the aisle'). Fundamental to person-centred care."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-what-matters"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T14:13:20Z
---

# What Matters to Me

Captures the patient's specific, personal priorities and non-clinical goals (e.g., 'I want to walk my daughter down the aisle'). Fundamental to person-centred care.

**Parent:** `http://hl7.org/fhir/StructureDefinition/Observation`

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.code` |  |  |  |
| `Observation.value[x]` | 1.. | string |  |
| `Observation.note` |  |  |  |
