# Clinical Safety - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* **Clinical Safety**

## Clinical Safety

# Clinical Safety

The Open Nursing Core IG incorporates "Safety Gate" profiles designed to detect deterioration and risk.

## Early Warning Scores (NEWS2)

The **[National Early Warning Score 2 (NEWS2)](StructureDefinition-onc-news2-score.md)** is standard in the NHS for detecting deterioration.

* **Usage**: MUST be calculated for all acute admissions.
* **Escalation**: Scores of 5+ or 3 in a single parameter require urgent clinical review.

## Pressure Ulcer Risk

### Braden Scale

The **[Braden Scale](StructureDefinition-onc-braden-scale-assessment.md)** assesses risk based on sensory perception, moisture, activity, mobility, nutrition, and friction/shear.

### Waterlow Score

The **[Waterlow Score](StructureDefinition-onc-waterlow-score.md)** is an alternative risk assessment tool widely used in the UK.

## Automation & Safety

Systems implementing this IG **SHOULD** automatically trigger alerts when safety scores breach critical thresholds (e.g., NEWS2 > 5).

