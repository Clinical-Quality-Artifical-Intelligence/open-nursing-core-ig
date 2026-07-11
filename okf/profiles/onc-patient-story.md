---
type: "FHIR Profile"
title: "Patient Story"
description: "A narrative summary of the patient's background, biography, preferences, and personhood. Goes beyond clinical history to capture 'who the person is'."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-patient-story"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T14:13:20Z
---

# Patient Story

A narrative summary of the patient's background, biography, preferences, and personhood. Goes beyond clinical history to capture 'who the person is'.

**Parent:** `http://hl7.org/fhir/StructureDefinition/Observation`

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.code` |  |  |  |
| `Observation.value[x]` | 1.. | string | Narrative story of the patient |
