---
type: "FHIR Profile"
title: "Reasonable Adjustment"
description: "Captures specific strict requirements for care adjustments under the Equality Act (e.g., 'Needs BSL Interpreter', 'Cannot use stairs', 'Requires large print')."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-reasonable-adjustment"
tags: [fhir, nursing, profile]
timestamp: 2026-07-11T13:58:05Z
---

# Reasonable Adjustment

Captures specific strict requirements for care adjustments under the Equality Act (e.g., 'Needs BSL Interpreter', 'Cannot use stairs', 'Requires large print').

**Parent:** [onc-nursing-assessment](/profiles/onc-nursing-assessment.md)

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Observation.value[x]` | 1.. | string | Description of required adjustment |
| `Observation.note` | ..1 |  |  |
