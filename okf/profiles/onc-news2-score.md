---
type: "FHIR Profile"
title: "NEWS2 Score"
description: "National Early Warning Score 2 (NEWS2) for detecting clinical deterioration. Fully aligned with NHS CareConnect-NEWS2-Observation-1."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-news2-score"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T14:13:20Z
---

# NEWS2 Score

National Early Warning Score 2 (NEWS2) for detecting clinical deterioration. Fully aligned with NHS CareConnect-NEWS2-Observation-1.

**Parent:** [onc-nursing-assessment](/profiles/onc-nursing-assessment.md)

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.code` |  |  |  |
| `Observation.value[x]` | 1.. | Quantity | NEWS2 total score (0-20) |
| `Observation.value[x].value` |  |  |  |
| `Observation.value[x].unit` |  |  |  |
| `Observation.value[x].system` |  |  |  |
