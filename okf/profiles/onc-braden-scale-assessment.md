---
type: "FHIR Profile"
title: "Braden Scale Assessment"
description: "A profile for the Braden Scale pressure ulcer risk assessment"
resource: "https://opennursingcoreig.com/StructureDefinition/onc-braden-scale-assessment"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T09:01:38Z
---

# Braden Scale Assessment

A profile for the Braden Scale pressure ulcer risk assessment

**Parent:** [onc-nursing-assessment](/profiles/onc-nursing-assessment.md)

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.status` |  |  |  |
| `Observation.code` |  |  |  |
| `Observation.value[x]` | 1.. | Quantity |  |
| `Observation.value[x].unit` |  |  |  |
| `Observation.value[x].system` |  |  |  |
| `Observation.value[x].code` |  |  |  |
| `Observation.hasMember` | 1.. |  |  |
| `Observation.hasMember` | 1..1 | Reference | Mandatory Skin Tone Context (Equity Gate) |
| `Observation.component` | 6..6 |  |  |
| `Observation.component` | 1..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | Quantity |  |
| `Observation.component` | 1..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | Quantity |  |
| `Observation.component` | 1..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | Quantity |  |
| `Observation.component` | 1..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | Quantity |  |
| `Observation.component` | 1..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | Quantity |  |
| `Observation.component` | 1..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | Quantity |  |
