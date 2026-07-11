---
type: "FHIR Profile"
title: "Seizure Record"
description: "Record of a specific seizure event, including type, duration, triggers, and recovery phases. Essential for epilepsy management and identifying patterns."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-seizure-record"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T13:58:05Z
---

# Seizure Record

Record of a specific seizure event, including type, duration, triggers, and recovery phases. Essential for epilepsy management and identifying patterns.

**Parent:** [onc-nursing-assessment](/profiles/onc-nursing-assessment.md)

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.value[x]` | 1.. | string | Description of the event |
| `Observation.component` |  |  |  |
| `Observation.component` | 0..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | string |  |
| `Observation.component` | 0..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | Quantity |  |
| `Observation.component.value[x].unit` |  |  |  |
| `Observation.component.value[x].system` |  |  |  |
| `Observation.component.value[x].code` |  |  |  |
| `Observation.component` | 0..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | string |  |
| `Observation.component` | 0..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | string |  |
