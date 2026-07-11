---
type: "FHIR Profile"
title: "4AT Delirium Assessment"
description: "Rapid clinical test for delirium (4AT) comprising Alertness, AMT4, Attention, and Acute Change/Fluctuating Course. A total score of 4 or more suggests possible delirium."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-4at-delirium"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T09:01:38Z
---

# 4AT Delirium Assessment

Rapid clinical test for delirium (4AT) comprising Alertness, AMT4, Attention, and Acute Change/Fluctuating Course. A total score of 4 or more suggests possible delirium.

**Parent:** [onc-nursing-assessment](/profiles/onc-nursing-assessment.md)

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.code` |  |  |  |
| `Observation.value[x]` | 1.. | Quantity | Total 4AT Score (0-12) |
| `Observation.value[x].value` |  |  |  |
| `Observation.value[x].unit` |  |  |  |
| `Observation.value[x].system` |  |  |  |
| `Observation.value[x].code` |  |  |  |
| `Observation.component` | 4.. |  |  |
| `Observation.component` | 1..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | CodeableConcept | (binds [onc-4at-alertness-vs](/valuesets/onc-4at-alertness-vs.md)) |
| `Observation.component` | 1..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | CodeableConcept | (binds [onc-4at-amt4-vs](/valuesets/onc-4at-amt4-vs.md)) |
| `Observation.component` | 1..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | CodeableConcept | (binds [onc-4at-attention-vs](/valuesets/onc-4at-attention-vs.md)) |
| `Observation.component` | 1..1 |  |  |
| `Observation.component.code` |  |  |  |
| `Observation.component.value[x]` |  | CodeableConcept | (binds [onc-4at-acute-change-vs](/valuesets/onc-4at-acute-change-vs.md)) |
