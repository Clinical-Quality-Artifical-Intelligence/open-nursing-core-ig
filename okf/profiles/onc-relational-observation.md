---
type: "FHIR Profile"
title: "Relational Engagement Score"
description: "Assessment of the quality and depth of the nurse-patient relationship or engagement level. Supports the relational aspect of care."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-relational-observation"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T09:01:38Z
---

# Relational Engagement Score

Assessment of the quality and depth of the nurse-patient relationship or engagement level. Supports the relational aspect of care.

**Parent:** `http://hl7.org/fhir/StructureDefinition/Observation`

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.code` |  |  |  |
| `Observation.value[x]` | 1.. | integer | Engagement Level (1-5) |
