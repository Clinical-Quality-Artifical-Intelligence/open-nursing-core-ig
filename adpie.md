# The ADPIE Nursing Process - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* **The ADPIE Nursing Process**

## The ADPIE Nursing Process

# The ADPIE Nursing Process

The Open Nursing Core IG is organised around the **nursing process** — the systematic, cyclical method of clinical reasoning that underpins registered nursing practice in the United Kingdom and internationally. The process is expressed as the **ADPIE** loop: **A**ssessment, **D**iagnosis, **P**lanning, **I**mplementation and **E**valuation.

Most clinical information models are built around a medical, diagnosis-and-treatment pathway. Nursing reasoning is different: it is continuous, holistic and centred on the person's response to their health condition rather than the pathology alone. By making ADPIE the organising spine of the IG, every profile carries an explicit place in that reasoning cycle, and the **why** of care becomes as computable as the **what**.

Each phase is tagged using the **[ADPIE Nursing Process Phases](ValueSet-onc-adpie-vs.md)** value set, so any resource can be located within the process it belongs to.

## The five phases

### A — Assessment

Structured, holistic data collection about the person's physical, psychological, social and spiritual needs. Assessment is the foundation of the process and the largest part of the IG.

* **Base profile:** [ONC Nursing Assessment](StructureDefinition-onc-nursing-assessment.md) — the parent observation from which every assessment instrument derives.
* **Validated instruments:** [NEWS2](StructureDefinition-onc-news2-score.md), [Braden Scale](StructureDefinition-onc-braden-scale-assessment.md), [Waterlow Score](StructureDefinition-onc-waterlow-score.md), [MUST](StructureDefinition-onc-must-score.md), [4AT Delirium Screen](StructureDefinition-onc-4at-delirium.md), [Abbey Pain Scale](StructureDefinition-onc-abbey-pain-scale.md), [Clinical Frailty Scale](StructureDefinition-onc-clinical-frailty-scale.md) and others.
* **Person-centred assessment:** [What Matters To Me](StructureDefinition-onc-what-matters.md), [Patient Story](StructureDefinition-onc-patient-story.md), [Monk Skin Tone Observation](StructureDefinition-onc-monk-skintone-observation.md) and [Reasonable Adjustment](StructureDefinition-onc-reasonable-adjustment.md).

The PRSB Nursing Care Needs standard requires that assessment records both **needs** and **strengths**. The IG supports this deliberately deficit-balancing approach through the [ONC Nursing Strength](StructureDefinition-onc-nursing-strength.md) profile.

### D — Diagnosis

The nurse's clinical judgement about the person's response to a health condition. Nursing diagnosis is distinct from medical diagnosis and is expressed using the **NANDA-I** taxonomy.

* **Primary profile:** [ONC Nursing Problem](StructureDefinition-onc-nursing-problem.md) (a Condition constrained for nursing use).
* **PRSB needs framing:** [ONC Nursing Need](StructureDefinition-onc-nursing-need.md).
* **Classification:** the [Problem Type](CodeSystem-onc-problem-type.md) code system distinguishes actual nursing diagnoses, risk diagnoses and health-promotion diagnoses.
* **Semantic mapping:** the [ONC → NANDA-I](ConceptMap-onc-to-nanda.md) concept map aligns ONC relational findings with formal NANDA-I diagnoses.

### P — Planning

Setting person-centred, measurable goals and the interventions intended to reach them.

* **Goals:** [ONC Nursing Goal](StructureDefinition-onc-nursing-goal.md), with target outcomes drawn from the [Goal Target Measure](ValueSet-onc-goal-target-measure-vs.md) value set.
* Goals are expressed in the person's own terms wherever possible, connecting back to the "What Matters to Me" record captured at assessment.

### I — Implementation

The delivery of planned nursing care.

* **Primary profile:** [ONC Nursing Intervention](StructureDefinition-onc-nursing-intervention.md) (a Procedure constrained for nursing use), drawn from the [Nursing Intervention](ValueSet-nursing-intervention-valueset.md) value set.
* Interventions link back to the goals they serve, so the plan and its delivery remain traceable.

### E — Evaluation

Judging whether goals have been met and feeding the result back into the next assessment cycle — the step that makes the process a loop rather than a line.

* **Outcome measurement:** [ONC Goal Evaluation](StructureDefinition-onc-goal-evaluation.md), using the [Goal Evaluation](ValueSet-goal-evaluation-valueset.md) value set (objective achieved, partially achieved, not achieved, sustained improvement, worsening).
* **Holistic review:** [ONC Nursing Clinical Impression](StructureDefinition-onc-nursing-clinical-impression.md) captures the nurse's synthesised judgement at the close of a cycle.

## The loop in practice

| | | |
| :--- | :--- | :--- |
| Assessment | What is happening for this person? | [ONC Nursing Assessment](StructureDefinition-onc-nursing-assessment.md) |
| Diagnosis | What is my clinical judgement about their response? | [ONC Nursing Problem](StructureDefinition-onc-nursing-problem.md) |
| Planning | What outcome are we working towards? | [ONC Nursing Goal](StructureDefinition-onc-nursing-goal.md) |
| Implementation | What care will we deliver? | [ONC Nursing Intervention](StructureDefinition-onc-nursing-intervention.md) |
| Evaluation | Did it work, and what next? | [ONC Goal Evaluation](StructureDefinition-onc-goal-evaluation.md) |

Evaluation is never an end point. Its findings re-enter assessment, and the cycle repeats for as long as the person is in the nurse's care. Modelling this explicitly allows systems built on the ONC-IG to reason about the **continuity** of care, not just discrete events.

-------

**This page describes the conceptual model of the IG. For the governing standards, see the [PRSB Nursing Care Needs standard](https://theprsb.org/standards/nursingcarestandard/) and the NANDA-I taxonomy. All care planning must be carried out by, or under the supervision of, a registered nurse.**

