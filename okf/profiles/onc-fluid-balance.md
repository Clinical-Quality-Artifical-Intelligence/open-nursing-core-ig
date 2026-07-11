---
type: "FHIR Profile"
title: "Fluid Balance"
description: "Assessment of fluid intake, output, and balance. Critical for renal function, hydration status, and heart failure monitoring."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-fluid-balance"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T14:13:20Z
---

# Fluid Balance

Assessment of fluid intake, output, and balance. Critical for renal function, hydration status, and heart failure monitoring.

**Parent:** [onc-nursing-assessment](/profiles/onc-nursing-assessment.md)

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.value[x]` | 1.. | Quantity | Net Fluid Balance (Input - Output) |
| `Observation.value[x].unit` |  |  |  |
| `Observation.value[x].system` |  |  |  |
| `Observation.value[x].code` |  |  |  |
| `Observation.component` |  |  |  |
| `Observation.component` | 0..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` | 1.. | Quantity |  |
| `Observation.component.value[x].unit` |  |  |  |
| `Observation.component.value[x].system` |  |  |  |
| `Observation.component.value[x].code` |  |  |  |
| `Observation.component` | 0..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` | 1.. | Quantity |  |
| `Observation.component.value[x].unit` |  |  |  |
| `Observation.component.value[x].system` |  |  |  |
| `Observation.component.value[x].code` |  |  |  |
| `Observation.component` | 0..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` | 1.. | Quantity |  |
| `Observation.component.value[x].unit` |  |  |  |
| `Observation.component.value[x].system` |  |  |  |
| `Observation.component.value[x].code` |  |  |  |
