---
type: "FHIR Profile"
title: "Blood Pressure"
description: "Blood pressure observation for NEWS2 (systolic BP used for scoring)"
resource: "https://opennursingcoreig.com/StructureDefinition/onc-blood-pressure"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T13:58:05Z
---

# Blood Pressure

Blood pressure observation for NEWS2 (systolic BP used for scoring)

**Parent:** [onc-nursing-assessment](/profiles/onc-nursing-assessment.md)

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.component` | 2..2 |  |  |
| `Observation.component` | 1..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | Quantity |  |
| `Observation.component.value[x].unit` |  |  |  |
| `Observation.component.value[x].system` |  |  |  |
| `Observation.component` | 1..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | Quantity |  |
| `Observation.component.value[x].unit` |  |  |  |
| `Observation.component.value[x].system` |  |  |  |
