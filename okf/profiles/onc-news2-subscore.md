---
type: "FHIR Profile"
title: "NEWS2 Sub-Score"
description: "Individual parameter sub-score for NEWS2 (0-3 for most parameters). References the related vital sign observation."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-news2-subscore"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T14:13:20Z
---

# NEWS2 Sub-Score

Individual parameter sub-score for NEWS2 (0-3 for most parameters). References the related vital sign observation.

**Parent:** [onc-nursing-assessment](/profiles/onc-nursing-assessment.md)

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.code` |  |  |  |
| `Observation.value[x]` | 1.. | Quantity |  |
| `Observation.value[x].value` |  |  |  |
| `Observation.value[x].unit` |  |  |  |
| `Observation.value[x].system` |  |  |  |
