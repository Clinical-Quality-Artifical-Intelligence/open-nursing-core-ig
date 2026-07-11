---
type: "FHIR Profile"
title: "Monk Skin Tone Observation"
description: "Observation of patient skin tone using the Monk Skin Tone Scale (10-point scale A-J). Provides more granular skin tone assessment than Fitzpatrick scale, particularly for darker skin tones. Supports equitable care and accurate clinical assessment across diverse populations."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-monk-skintone-observation"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T14:13:20Z
---

# Monk Skin Tone Observation

Observation of patient skin tone using the Monk Skin Tone Scale (10-point scale A-J). Provides more granular skin tone assessment than Fitzpatrick scale, particularly for darker skin tones. Supports equitable care and accurate clinical assessment across diverse populations.

**Parent:** [onc-nursing-assessment](/profiles/onc-nursing-assessment.md)

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.value[x]` |  | CodeableConcept | (binds [onc-monk-scale-vs](/valuesets/onc-monk-scale-vs.md)) |
