# Open Nursing Core FHIR Implementation Guide

The **Open Nursing Core FHIR Implementation Guide (ONC-IG)** provides a foundational set of standardised, nurse-led data models for the NHS and comparable health systems. It is built on **HL7 FHIR R4 (4.0.1)** and organised around the complete nursing process — **Assessment, Diagnosis, Planning, Implementation and Evaluation (ADPIE)** — rather than a purely pathology-driven medical model.

The IG is grounded in United Kingdom nursing and information standards, in particular the **Professional Record Standards Body (PRSB)** Nursing Care Needs standard, the **NANDA International (NANDA-I)** diagnostic taxonomy, and the person-centred practice principles of the **Foundation of Nursing Studies (FONS)**.

## Purpose and scope

This guide defines the structured data required to record nursing care in an interoperable, equitable and safety-aware manner. It is intended for use by NHS digital teams, electronic health record (EHR) suppliers, clinical safety officers, and nurse informaticians who need a shared vocabulary for the fundamentals of nursing.

The current release defines **60 profiles**, **27 value sets**, **3 code systems**, **4 extensions**, **1 logical model** (the Relational Care model) and **49 worked examples**. See the [Published Versions](history.html) page for the full release record.

## Core principles

- **Process-led** — every profile maps to a phase of the [ADPIE nursing process](adpie.html), making the *reasoning* of care computable, not only its outcomes.
- **Person-centred** — captures "[What Matters to Me](StructureDefinition-onc-what-matters.html)" and the [Patient Story](StructureDefinition-onc-patient-story.html) alongside clinical measurement, in line with FONS values-based practice.
- **Equitable by design** — leads with the [Monk Skin Tone Scale](equity.html) for skin assessment and records [Reasonable Adjustments](StructureDefinition-onc-reasonable-adjustment.html) under the Equality Act 2010. See the [Health Equity & Inclusion](equity.html) page.
- **Safety-aware** — validated instruments such as [NEWS2](StructureDefinition-onc-news2-score.html) and pressure-ulcer risk scores act as clinical [safety gates](safety.html).

## Profile library

The profile library is organised below by function. For the full navigable list of every artifact, see the [Artifacts](artifacts.html) index.

### 1. Nursing process core

Base profiles that carry the ADPIE spine.

- [ONC Nursing Assessment](StructureDefinition-onc-nursing-assessment.html) — the base observation for all assessment instruments
- [ONC Nursing Problem](StructureDefinition-onc-nursing-problem.html) — nursing diagnosis (Condition)
- [ONC Nursing Need](StructureDefinition-onc-nursing-need.html) and [ONC Nursing Strength](StructureDefinition-onc-nursing-strength.html) — PRSB needs-and-strengths framing
- [ONC Nursing Goal](StructureDefinition-onc-nursing-goal.html) — planned outcomes
- [ONC Nursing Intervention](StructureDefinition-onc-nursing-intervention.html) — delivered care
- [ONC Goal Evaluation](StructureDefinition-onc-goal-evaluation.html) and [ONC Nursing Clinical Impression](StructureDefinition-onc-nursing-clinical-impression.html) — evaluation

### 2. Clinical safety and deterioration

Validated risk instruments used as safety gates. See the [Clinical Safety](safety.html) page.

- [NEWS2](StructureDefinition-onc-news2-score.html) — National Early Warning Score 2 (deterioration)
- [Braden Scale](StructureDefinition-onc-braden-scale-assessment.html) and [Waterlow Score](StructureDefinition-onc-waterlow-score.html) — pressure-ulcer risk
- [MUST](StructureDefinition-onc-must-score.html) — malnutrition screening
- [4AT Delirium Screen](StructureDefinition-onc-4at-delirium.html), [Morse Fall Scale](StructureDefinition-onc-morse-fall-scale.html), [qSOFA](StructureDefinition-onc-qsofa.html)

### 3. Relational and inclusive care

Capturing the person behind the patient. See [Health Equity & Inclusion](equity.html).

- [What Matters To Me](StructureDefinition-onc-what-matters.html) and [Patient Story](StructureDefinition-onc-patient-story.html)
- [Monk Skin Tone Observation](StructureDefinition-onc-monk-skintone-observation.html) — 10-point equitable skin assessment (A–J)
- [Skin Tone Observation](StructureDefinition-onc-skintone-observation.html) — Fitzpatrick classification (secondary)
- [Reasonable Adjustment](StructureDefinition-onc-reasonable-adjustment.html) — Equality Act 2010
- [Mental Capacity Assessment](StructureDefinition-onc-mental-capacity.html) — Mental Capacity Act 2005

### 4. Fundamental care

The essentials of daily nursing.

- [Bristol Stool Chart](StructureDefinition-onc-bristol-stool-chart.html) — elimination
- [Fluid Balance](StructureDefinition-onc-fluid-balance.html) — hydration
- [Abbey Pain Scale](StructureDefinition-onc-abbey-pain-scale.html) — non-verbal pain
- [Oral Health](StructureDefinition-onc-oral-health.html) and [Sleep Pattern](StructureDefinition-onc-sleep-pattern.html)

### 5. Specialist and mental health

Instruments for learning disability, mental health and older-person care.

- [ABC Chart](StructureDefinition-onc-abc-chart.html) — Positive Behaviour Support
- [Seizure Record](StructureDefinition-onc-seizure-record.html) — epilepsy
- [Clinical Frailty Scale](StructureDefinition-onc-clinical-frailty-scale.html) and [Glasgow Coma Scale](StructureDefinition-onc-glasgow-coma-scale.html)
- [MMSE](StructureDefinition-onc-mmse.html), [Urinalysis](StructureDefinition-onc-urinalysis.html)

## Guidance pages

- [The ADPIE Nursing Process](adpie.html) — how the IG is structured around clinical reasoning
- [Clinical Safety](safety.html) — safety gates, escalation and the DCB0129/0160 context
- [Health Equity & Inclusion](equity.html) — Monk Skin Tone Scale and reasonable adjustments
- [Security & Privacy](security.html) — UK GDPR, DSPT and Caldicott
- [Terminology](terminology.html) — SNOMED CT, LOINC and the ONC code systems
- [Relational AI](relation-ai.html) — the FONS-aligned language model
- [Published Versions](history.html) — release history

## Getting started

1. **Browse the artifacts** — every profile, extension, value set and example is listed on the [Artifacts](artifacts.html) page.
2. **Read the process guide** — start with [ADPIE](adpie.html) to understand how the profiles fit together.
3. **Contribute** — the IG is open source under the MIT licence. Issues and pull requests are welcome on [GitHub](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig).

---

*The Open Nursing Core is maintained by the Open Nursing Community. This guide is a technical specification and does not replace professional clinical judgement; all clinical documentation must be verified by a registered nurse.*
