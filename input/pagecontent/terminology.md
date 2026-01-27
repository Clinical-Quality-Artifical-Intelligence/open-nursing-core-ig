# Terminology

This IG relies on standard terminologies to ensure interoperability.

## Code Systems
- **SNOMED CT**: The primary clinical vocabulary (Procedure, Finding, Situation).
- **LOINC**: Used for observations and scores (NEWS2, Vital Signs).
- **ICD-10**: Used for diagnosis (secondary to SNOMED).

## Value Sets
The IG defines specific ValueSets for nursing assessments where standard codes may be missing or insufficient.

| ValueSet | Description |
|----------|-------------|
| **[SkinToneVS](ValueSet-onc-skin-tone-vs.html)** | Monk and Fitzpatrick scales for equitable skin assessment. |
| **[NEWS2ScoreVS](ValueSet-onc-news2-score-vs.html)** | NEWS2 total score categories. |
| **[PainScoreVS](ValueSet-onc-pain-score-vs.html)** | Standard 0-10 or Abbey Pain Scale score |

## Mapping
To ensure semantic interoperability, internal ONC concepts are mapped to international standards using ConceptMaps.

- **[Mapping ONC to NANDA-I](ConceptMap-onc-to-nanda.html)**: Alignment of relational care findings to formal nursing diagnoses.

Implementers **MUST** map local legacy codes to the SNOMED CT and LOINC codes defined in these ValueSets to maintain decision-support integrity.
