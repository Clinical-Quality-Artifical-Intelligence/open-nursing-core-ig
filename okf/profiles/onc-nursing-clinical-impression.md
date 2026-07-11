---
type: "FHIR Profile"
title: "ONC Nursing Clinical Impression"
description: "Nurse's synthesis of patient progress against care plan, aggregating multiple goal evaluations."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-nursing-clinical-impression"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T14:13:20Z
---

# ONC Nursing Clinical Impression

Nurse's synthesis of patient progress against care plan, aggregating multiple goal evaluations.

**Parent:** `http://hl7.org/fhir/StructureDefinition/ClinicalImpression`

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `ClinicalImpression.code` |  |  |  |
| `ClinicalImpression.subject` |  | Reference |  |
| `ClinicalImpression.encounter` |  |  |  |
| `ClinicalImpression.effective[x]` |  |  |  |
| `ClinicalImpression.effective[x]` | 0..1 | dateTime |  |
| `ClinicalImpression.assessor` |  | Reference |  |
| `ClinicalImpression.problem` | 1.. | Reference |  |
| `ClinicalImpression.summary` |  |  |  |
| `ClinicalImpression.prognosisCodeableConcept` |  |  | (binds [onc-prognosis-vs](/valuesets/onc-prognosis-vs.md)) |
| `ClinicalImpression.supportingInfo` |  | Reference |  |
