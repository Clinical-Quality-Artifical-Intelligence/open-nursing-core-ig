---
type: "FHIR Questionnaire (SDC)"
title: "Person-Centred Care (What Matters to Me & Reasonable Adjustments)"
description: "SDC questionnaire capturing 'What Matters to Me' and reasonable adjustments (Equality Act 2010) as structured, retrievable records. Items extract to Observations conforming to ONCWhatMattersToMe and ONCReasonableAdjustment."
resource: "https://opennursingcoreig.com/Questionnaire/onc-person-centred-questionnaire"
tags: [fhir, nursing, questionnaire]
timestamp: 2026-07-11T13:58:05Z
---

# Person-Centred Care (What Matters to Me & Reasonable Adjustments)

SDC questionnaire capturing 'What Matters to Me' and reasonable adjustments (Equality Act 2010) as structured, retrievable records. Items extract to Observations conforming to ONCWhatMattersToMe and ONCReasonableAdjustment.

# Items

| linkId | Text | Type | Required |
|--------|------|------|----------|
| `what-matters` | What matters to you? (The person's own priorities and goals, in their own words — e.g. 'I  | text | yes |
| `reasonable-adjustment` | Reasonable adjustment required (one per entry — e.g. 'Requires a British Sign Language int | text |  |
| `adjustments-note` | Recording adjustments as discrete, structured entries (not free-text notes) is what makes  | display |  |

Uses SDC observation-based extraction: coded items extract to Observations conforming to the ONC profiles; display/logic items carry no code and do not extract.
