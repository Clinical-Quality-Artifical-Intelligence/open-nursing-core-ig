---
type: "FHIR Profile"
title: "Urinalysis"
description: "Point-of-care urine dipstick test results. Used to screen for urinary tract infection (UTI), diabetes (glucose/ketones), and kidney health."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-urinalysis"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T14:13:20Z
---

# Urinalysis

Point-of-care urine dipstick test results. Used to screen for urinary tract infection (UTI), diabetes (glucose/ketones), and kidney health.

**Parent:** [onc-nursing-assessment](/profiles/onc-nursing-assessment.md)

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.value[x]` | 1.. | string | Overall Interpretation (e.g. 'suggestive of UTI') |
| `Observation.component` |  |  |  |
| `Observation.component` | 0..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | string | e.g., 'Trace', '+', '++' |
| `Observation.component` | 0..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | string | Positive/Negative |
| `Observation.component` | 0..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | string | e.g., 'Non-hemolyzed', 'Large' |
| `Observation.component` | 0..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | string |  |
| `Observation.component` | 0..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | string |  |
| `Observation.component` | 0..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | string |  |
| `Observation.component` | 0..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | Quantity |  |
| `Observation.component` | 0..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | Quantity |  |
