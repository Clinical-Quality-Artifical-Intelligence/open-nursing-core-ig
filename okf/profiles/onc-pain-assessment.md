---
type: "FHIR Profile"
title: "Pain Assessment (NRS 0-10)"
description: "Pain severity assessment using the Numeric Rating Scale (0-10)"
resource: "https://opennursingcoreig.com/StructureDefinition/onc-pain-assessment"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T13:58:05Z
---

# Pain Assessment (NRS 0-10)

Pain severity assessment using the Numeric Rating Scale (0-10)

**Parent:** [onc-nursing-assessment](/profiles/onc-nursing-assessment.md)

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.code` |  |  | (binds [pain-assessment-code-vs](/valuesets/pain-assessment-code-vs.md)) |
| `Observation.effective[x]` | 1.. |  |  |
| `Observation.effective[x]` | 1..1 | dateTime |  |
| `Observation.value[x]` | 1.. | Quantity | Pain severity score (0-10) |
| `Observation.value[x].value` |  |  |  |
| `Observation.value[x].unit` |  |  |  |
| `Observation.value[x].system` |  |  |  |
| `Observation.bodySite` |  |  | Location of pain |
