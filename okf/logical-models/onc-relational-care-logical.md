---
type: "FHIR Logical Model"
title: "Relational Care Logical Model"
description: "A vendor-neutral clinical model of the relational nursing assessment. Defines WHAT data must be captured, regardless of HOW it is stored in FHIR."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-relational-care-logical"
tags: [fhir, nursing, logical-model]
timestamp: 2026-07-11T09:01:38Z
---

# Relational Care Logical Model

A vendor-neutral clinical model of the relational nursing assessment. Defines WHAT data must be captured, regardless of HOW it is stored in FHIR.

**Parent:** `http://hl7.org/fhir/StructureDefinition/Base`

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `onc-relational-care-logical.patientPreferences` | 1..1 | string | The patient's personal goals and what matters most to them today. |
| `onc-relational-care-logical.relationalEngagement` | 1..1 | integer | A score from 1-5 representing the depth of the therapeutic relationship. |
| `onc-relational-care-logical.empathyIndex` | 1..1 | code | The ONC Empathy Index (1-5) measuring relational quality. (binds [onc-empathy-index-vs](/valuesets/onc-empathy-index-vs.md)) |
| `onc-relational-care-logical.skinToneEquity` | 1..1 | code | The patient's skin tone classification (Monk primary, Fitzpatrick secondary/legacy) used to guide clinical ass (binds [onc-skin-tone-vs](/valuesets/onc-skin-tone-vs.md)) |
| `onc-relational-care-logical.mandatoryEquityValidation` | 1..1 | boolean | Technical flag ensuring the 'Fairness Gate' was passed. |
| `onc-relational-care-logical.adpieStatus` | 1..1 | code | The current stage of the professional nursing process (Assessment, Diagnosis, Planning, Implementation, Evalua (binds [onc-adpie-vs](/valuesets/onc-adpie-vs.md)) |
| `onc-relational-care-logical.clinicalNarrative` | 1..1 | string | The person-centred narrative describing the patient's experience. |
