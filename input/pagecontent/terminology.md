# Terminology

The Open Nursing Core IG relies on established international terminologies wherever suitable codes exist, and defines its own code systems only to fill gaps specific to nursing assessment. This layered approach preserves interoperability while giving nursing concepts a precise, computable representation.

## External terminologies

- **SNOMED CT** — the primary clinical vocabulary, used for findings, procedures and situations. It is the preferred coding system for nursing problems and interventions.
- **LOINC** — used for observations and scores, including the NEWS2 component vital signs.
- **ICD-10** — used for medical diagnosis where required, secondary to SNOMED CT.

## ONC code systems

The IG defines three code systems for concepts that are not adequately covered by the external terminologies:

| Code system | Purpose |
|-------------|---------|
| **[Monk Skin Tone Scale](CodeSystem-onc-monk-scale.html)** (`onc-monk-scale`) | The 10-point (A–J) skin-tone scale used for equitable skin assessment. |
| **[ONC Observation Codes](CodeSystem-onc-observation-codes.html)** (`onc-observation-codes`) | Local codes for nursing assessment scores and items where no LOINC/SNOMED code exists (e.g. Waterlow, MUST, Braden components, empathy index, ADPIE phases). |
| **[Problem Type](CodeSystem-onc-problem-type.html)** (`onc-problem-type`) | Categorises nursing diagnoses as actual, risk, or health-promotion diagnoses. |

## Value sets

The IG defines value sets for nursing assessments where standard codes are missing or insufficient. Selected examples:

| Value set | Description |
|-----------|-------------|
| **[Monk Skin Tone Scale ValueSet](ValueSet-onc-monk-scale-vs.html)** | The Monk A–J scale — the primary vocabulary for skin-tone assessment. |
| **[Skin Tone Value Set](ValueSet-onc-skin-tone-vs.html)** | Combined set including Monk and Fitzpatrick codes, for backward compatibility. |
| **[NEWS2 Score Categories](ValueSet-onc-news2-score-vs.html)** | NEWS2 total-score risk bands (low, medium, high). |
| **[ADPIE Nursing Process Phases](ValueSet-onc-adpie-vs.html)** | The five phases of the nursing process, used to tag resources. |
| **[Empathy & Relational Engagement Index](ValueSet-onc-empathy-index-vs.html)** | The 1–5 relational engagement scale. |
| **[Pain Score Value Set](ValueSet-onc-pain-score-vs.html)** | Standard 0–10 or Abbey Pain Scale scoring. |

The full list of 27 value sets is available on the [Artifacts](artifacts.html) page.

## Concept maps

To support semantic interoperability, ONC concepts are mapped to international standards:

- **[ONC → NANDA-I](ConceptMap-onc-to-nanda.html)** — aligns ONC relational and clinical findings with formal NANDA-I nursing diagnoses (for example, mapping a Patient Story narrative indicating isolation to the NANDA-I *Social Isolation* diagnosis).

> **⚠️ Note for implementers — not production-ready.** NANDA-I is a proprietary, licensed terminology. The concept map currently targets an explicit **local placeholder canonical** (`nanda-i-PLACEHOLDER`), not an official NANDA-I or HL7 THO system — the example codes it maps to (e.g. `#00053`, `#00054`) illustrate the intended mapping shape only and have not been verified against a current, licensed NANDA-I release. Organisations using NANDA-I **MUST** hold the appropriate licence and **MUST** substitute the official system URI before relying on this map clinically. Progress is tracked in [issue #123](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/issues/123).

## Implementer requirements

Implementers **MUST** map local legacy codes to the SNOMED CT and LOINC codes defined in these value sets to maintain decision-support integrity. Where an ONC local code is used, it **SHOULD** be accompanied by an equivalent SNOMED CT or LOINC code wherever one exists, so that data remains interpretable outside the ONC context.
