# Terminology - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* **Terminology**

## Terminology

# Terminology

This IG relies on standard terminologies to ensure interoperability.

## Code Systems

* **SNOMED CT**: The primary clinical vocabulary (Procedure, Finding, Situation).
* **LOINC**: Used for observations and scores (NEWS2, Vital Signs).
* **ICD-10**: Used for diagnosis (secondary to SNOMED).

## Value Sets

The IG defines specific ValueSets for nursing assessments where standard codes may be missing or insufficient.

| | |
| :--- | :--- |
| **[SkinToneVS](ValueSet-onc-skin-tone-vs.md)** | Monk and Fitzpatrick scales for equitable skin assessment. |
| **[NEWS2ScoreVS](ValueSet-onc-news2-score-vs.md)** | NEWS2 total score categories. |
| **[PainScoreVS](ValueSet-onc-pain-score-vs.md)** | Standard 0-10 or Abbey Pain Scale score |

## Mapping

To ensure semantic interoperability, internal ONC concepts are mapped to international standards using ConceptMaps.

* **[Mapping ONC to NANDA-I](ConceptMap-onc-to-nanda.md)**: Alignment of relational care findings to formal nursing diagnoses.

Implementers **MUST** map local legacy codes to the SNOMED CT and LOINC codes defined in these ValueSets to maintain decision-support integrity.

