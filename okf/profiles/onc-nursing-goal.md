---
type: "FHIR Profile"
title: "ONC Nursing Goal"
description: "Patient-centered goal with mandatory evaluation requirements. Serves as the 'spine' of the CarePlan, linking problems to outcomes."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-nursing-goal"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T14:13:20Z
---

# ONC Nursing Goal

Patient-centered goal with mandatory evaluation requirements. Serves as the 'spine' of the CarePlan, linking problems to outcomes.

**Parent:** `http://hl7.org/fhir/StructureDefinition/Goal`

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Goal.lifecycleStatus` |  |  |  |
| `Goal.achievementStatus` |  |  |  |
| `Goal.category` |  |  |  |
| `Goal.subject` |  | Reference |  |
| `Goal.target` | 1.. |  |  |
| `Goal.target.measure` |  |  | (binds [onc-goal-target-measure-vs](/valuesets/onc-goal-target-measure-vs.md)) |
| `Goal.target.due[x]` | 1.. |  |  |
| `Goal.target.due[x]` | 1..1 | date |  |
| `Goal.addresses` | 1.. | Reference |  |
