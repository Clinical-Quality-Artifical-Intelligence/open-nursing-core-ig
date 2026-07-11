---
type: "FHIR Profile"
title: "Bristol Stool Chart"
description: "Assessment of stool form using the Bristol Stool Chart (Types 1-7). Gold standard for bowel function assessment."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-bristol-stool-chart"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T09:01:38Z
---

# Bristol Stool Chart

Assessment of stool form using the Bristol Stool Chart (Types 1-7). Gold standard for bowel function assessment.

**Parent:** [onc-nursing-assessment](/profiles/onc-nursing-assessment.md)

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.code` |  |  |  |
| `Observation.value[x]` | 1.. | Quantity | Bristol Stool Type (1-7) |
| `Observation.value[x].value` |  |  |  |
| `Observation.value[x].unit` |  |  |  |
| `Observation.value[x].system` |  |  |  |
| `Observation.note` |  |  | Additional notes (e.g., colour, amount) |
