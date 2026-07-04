# Clinical Safety - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* **Clinical Safety**

## Clinical Safety

# Clinical Safety

The Open Nursing Core IG treats a defined set of validated assessment instruments as **safety gates** — structured checks whose purpose is to detect deterioration and risk early and to trigger a proportionate clinical response. This page describes those instruments, the computable logic behind them, and the clinical-safety governance context in which the IG should be implemented.

## Clinical risk management context

Digital clinical systems used in the NHS are governed by two clinical-safety standards published by NHS England:

* **DCB0129** — clinical risk management for the **manufacturer** of a health IT system.
* **DCB0160** — clinical risk management for the **organisation deploying** it.

The ONC-IG is a specification, not a deployed product; it does not by itself discharge either duty. Organisations implementing these profiles **SHOULD** do so within their own DCB0160 clinical risk management process, with a nominated Clinical Safety Officer, a hazard log, and a clinical safety case. The safety-gate design of the IG is intended to **support** that process by making risk instruments explicit and computable.

## Early warning: NEWS2

The **[National Early Warning Score 2 (NEWS2)](StructureDefinition-onc-news2-score.md)** is the NHS standard for detecting and responding to acute deterioration in adults. The IG models the full score and each of its component parameters:

* [Respiration Rate](StructureDefinition-onc-respiration-rate.md), [Oxygen Saturation](StructureDefinition-onc-oxygen-saturation.md), [Inspired Oxygen](StructureDefinition-onc-inspired-oxygen.md)
* [Body Temperature](StructureDefinition-onc-body-temperature.md), [Blood Pressure](StructureDefinition-onc-blood-pressure.md), [Heart Rate](StructureDefinition-onc-heart-rate.md)
* [ACVPU level of consciousness](StructureDefinition-onc-acvpu.md)
* [NEWS2 sub-score](StructureDefinition-onc-news2-subscore.md) for each parameter, aggregated into the [total NEWS2 score](StructureDefinition-onc-news2-score.md)

### Computable logic

Scoring is not left to manual calculation. The IG ships an executable **[Clinical Quality Language (CQL) library](Library-onc-news2-cql.md)** (`ONC_NEWS2_Logic`) that computes the score from the underlying FHIR observations, including the **SpO2 Scale 2** logic used for patients with hypercapnic respiratory failure. This is paired with a **[NEWS2 Escalation PlanDefinition](PlanDefinition-news2-escalation.md)** that encodes the response protocol.

### Escalation thresholds

NEWS2 escalation follows the nationally defined bands:

| | | |
| :--- | :--- | :--- |
| 0–4 | Low | Routine monitoring; ward-based review as needed |
| 3 in any single parameter | Low–medium | Registered nurse review to decide if escalation is required |
| 5–6 | Medium | Urgent review by a clinician competent to assess acutely ill patients |
| 7 or more | High | Emergency response by a critical-care-capable team |

Systems implementing this IG **SHOULD** automatically flag when a NEWS2 result crosses these thresholds, in line with the escalation PlanDefinition.

## Pressure ulcer risk

Two complementary risk instruments are provided:

* **[Braden Scale](StructureDefinition-onc-braden-scale-assessment.md)** — assesses sensory perception, moisture, activity, mobility, nutrition, and friction/shear.
* **[Waterlow Score](StructureDefinition-onc-waterlow-score.md)** — a UK-developed tool widely used across the NHS.

Pressure-area assessment must be read together with the [Health Equity & Inclusion](equity.md) guidance: early tissue damage presents differently across skin tones, so a valid pressure-risk assessment depends on skin tone being recorded on the [Monk Skin Tone Scale](equity.md). This is the IG's **fairness gate** — a wound or pressure-area assessment is incomplete until skin tone has been captured.

## Other safety instruments

* **[MUST](StructureDefinition-onc-must-score.md)** — Malnutrition Universal Screening Tool, for nutritional risk.
* **[4AT Delirium Screen](StructureDefinition-onc-4at-delirium.md)** — rapid screening for delirium in older or acutely unwell patients.
* **[Morse Fall Scale](StructureDefinition-onc-morse-fall-scale.md)** — falls risk.
* **[qSOFA](StructureDefinition-onc-qsofa.md)** — rapid identification of possible sepsis.

## Conformance language

Throughout the IG, the key words **MUST**, **SHOULD** and **MAY** are used in the sense of RFC 2119. "MUST" denotes a requirement for conformance; "SHOULD" a strong recommendation that may be departed from with justification; "MAY" an option.

-------

**The instruments described here support clinical judgement; they do not replace it. Every score and escalation decision must be reviewed and actioned by a registered nurse or other competent clinician. Implementers are responsible for their own clinical safety case under DCB0160.**

