---
type: "FHIR Extension"
title: "ONC Equity Marker"
description: "A technical extension applied to observations that have passed the Mandatory Equity Gate (i.e., they are skin-tone aware)."
resource: "https://opennursingcoreig.com/StructureDefinition/onc-equity-marker"
tags: [fhir, nursing, extension]
timestamp: 2026-07-11T13:58:05Z
---

# ONC Equity Marker

A technical extension applied to observations that have passed the Mandatory Equity Gate (i.e., they are skin-tone aware).

**Parent:** `http://hl7.org/fhir/StructureDefinition/Extension`

# Key elements (differential)

| Path | Card. | Type | Notes |
|------|-------|------|-------|
| `Extension.extension` | ..0 |  |  |
| `Extension.url` |  |  |  |
| `Extension.value[x]` | 1.. | boolean |  |
