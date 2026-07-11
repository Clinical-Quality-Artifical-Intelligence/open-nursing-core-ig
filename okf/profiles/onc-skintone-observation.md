---
type: "FHIR Profile"
title: "Skin Tone Observation (Fitzpatrick -- secondary/legacy)"
description: "Observation of patient skin tone using the Fitzpatrick skin type classification. Fitzpatrick was designed to describe UV photosensitivity, not clinical skin tone, and compresses the darker end of the range into few categories. This profile is RETAINED FOR BACKWARD COMPATIBILITY with systems that already record Fitzpatrick phototypes; it is secondary to, and SHOULD NOT be used in place of, the Monk Skin Tone Scale (see ONCMonkSkinToneObservation), which is this IG's primary and recommended skin-t"
resource: "https://opennursingcoreig.com/StructureDefinition/onc-skintone-observation"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T09:01:38Z
---

# Skin Tone Observation (Fitzpatrick -- secondary/legacy)

Observation of patient skin tone using the Fitzpatrick skin type classification. Fitzpatrick was designed to describe UV photosensitivity, not clinical skin tone, and compresses the darker end of the range into few categories. This profile is RETAINED FOR BACKWARD COMPATIBILITY with systems that already record Fitzpatrick phototypes; it is secondary to, and SHOULD NOT be used in place of, the Monk Skin Tone Scale (see ONCMonkSkinToneObservation), which is this IG's primary and recommended skin-tone vocabulary.

**Parent:** [onc-nursing-assessment](/profiles/onc-nursing-assessment.md)

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.value[x]` |  | CodeableConcept | (binds [onc-skin-tone-vs](/valuesets/onc-skin-tone-vs.md)) |
