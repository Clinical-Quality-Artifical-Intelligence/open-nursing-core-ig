---
type: "FHIR Profile"
title: "Morse Fall Scale"
description: "Morse Fall Scale for assessing fall risk. Score 0-24=no risk, 25-50=low risk, ≥51=high risk. Total range 0-125."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-morse-fall-scale"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T09:01:38Z
---

# Morse Fall Scale

Morse Fall Scale for assessing fall risk. Score 0-24=no risk, 25-50=low risk, ≥51=high risk. Total range 0-125.

**Parent:** [onc-nursing-assessment](/profiles/onc-nursing-assessment.md)

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.code` |  |  |  |
| `Observation.value[x]` | 1.. | Quantity | Morse Fall Scale total (0-125) |
| `Observation.value[x].value` |  |  |  |
| `Observation.value[x].unit` |  |  |  |
| `Observation.value[x].system` |  |  |  |
