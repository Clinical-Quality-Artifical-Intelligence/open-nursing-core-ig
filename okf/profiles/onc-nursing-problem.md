---
type: "FHIR Profile"
title: "Nursing Problem"
description: "Nursing diagnosis or problem identified during assessment. Represents clinical judgments about individual, family, or community responses to actual or potential health problems. Part of the ADPIE framework's Diagnosis phase."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-nursing-problem"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T14:13:20Z
---

# Nursing Problem

Nursing diagnosis or problem identified during assessment. Represents clinical judgments about individual, family, or community responses to actual or potential health problems. Part of the ADPIE framework's Diagnosis phase.

**Parent:** `http://hl7.org/fhir/StructureDefinition/Condition`

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Condition.category` | 1..1 |  | (binds [problem-category-valueset](/valuesets/problem-category-valueset.md)) |
| `Condition.code` | 1.. |  | (binds [nursing-problem-valueset](/valuesets/nursing-problem-valueset.md)) |
