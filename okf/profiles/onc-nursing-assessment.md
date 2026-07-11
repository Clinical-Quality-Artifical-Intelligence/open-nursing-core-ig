---
type: "FHIR Profile"
title: "Open Nursing Core Assessment"
description: "Base profile for nursing assessment observations conforming to UK Core standards. Captures structured nursing assessment data as part of the ADPIE (Assessment, Diagnosis, Planning, Implementation, Evaluation) nursing process framework. Used as parent for specialized assessments like NEWS2, Braden Scale, and clinical observations."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-nursing-assessment"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T13:58:05Z
---

# Open Nursing Core Assessment

Base profile for nursing assessment observations conforming to UK Core standards. Captures structured nursing assessment data as part of the ADPIE (Assessment, Diagnosis, Planning, Implementation, Evaluation) nursing process framework. Used as parent for specialized assessments like NEWS2, Braden Scale, and clinical observations.

**Parent:** `http://hl7.org/fhir/StructureDefinition/Observation`

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.category` | 1..1 |  |  |
| `Observation.performer` | 1..1 | Reference |  |
| `Observation.value[x]` |  | Quantity, CodeableConcept, string |  |
