---
type: "FHIR Profile"
title: "Mini Mental State Examination (MMSE)"
description: "Mini Mental State Examination for cognitive function screening. Score 24-30=no impairment, 18-23=mild, 0-17=severe. Total range 0-30."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-mmse"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T09:01:38Z
---

# Mini Mental State Examination (MMSE)

Mini Mental State Examination for cognitive function screening. Score 24-30=no impairment, 18-23=mild, 0-17=severe. Total range 0-30.

**Parent:** [onc-nursing-assessment](/profiles/onc-nursing-assessment.md)

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.code` |  |  |  |
| `Observation.value[x]` | 1.. | Quantity | MMSE total score (0-30) |
| `Observation.value[x].value` |  |  |  |
| `Observation.value[x].unit` |  |  |  |
| `Observation.value[x].system` |  |  |  |
