# Home - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* **Home**

## Home

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/ImplementationGuide/onc.ig | *Version*:1.0.0 |
| Active as of 2026-07-09 | *Computable Name*:OpenNursingCoreIG |

# Open Nursing Core FHIR Implementation Guide

> **⚠️ Standards status: Trial Use — Pre-Ballot Community Release.** This IG has **not** undergone formal HL7 standards balloting or independent clinical/peer review. Its `active`/`release` labels reflect development maturity within this project, not endorsement by HL7 International, PRSB, or any other standards body. It is a specification, not a deployed product, and does not by itself discharge an implementing organisation's clinical-safety (DCB0129/DCB0160) or information-governance obligations. See the [Standards & Governance Roadmap](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/blob/main/STANDARDS_ROADMAP.md) for the path toward formal review and balloting.

The **Open Nursing Core FHIR Implementation Guide (ONC-IG)** provides a foundational set of standardised, nurse-led data models for the NHS and comparable health systems. It is built on **HL7 FHIR R4 (4.0.1)** and organised around the complete nursing process — **Assessment, Diagnosis, Planning, Implementation and Evaluation (ADPIE)** — rather than a purely pathology-driven medical model.

The IG is grounded in United Kingdom nursing and information standards, in particular the **Professional Record Standards Body (PRSB)** Nursing Care Needs standard, the **NANDA International (NANDA-I)** diagnostic taxonomy, and the person-centred practice principles of the **Foundation of Nursing Studies (FONS)**.

## Purpose and scope

This guide defines the structured data required to record nursing care in an interoperable, equitable and safety-aware manner. It is intended for use by NHS digital teams, electronic health record (EHR) suppliers, clinical safety officers, and nurse informaticians who need a shared vocabulary for the fundamentals of nursing.

The current release defines **60 profiles**, **27 value sets**, **3 code systems**, **4 extensions**, **1 logical model** (the Relational Care model) and **49 worked examples**. See the [Published Versions](history.md) page for the full release record.

## Core principles

* **Process-led** — every profile maps to a phase of the [ADPIE nursing process](adpie.md), making the **reasoning** of care computable, not only its outcomes.
* **Person-centred** — captures "[What Matters to Me](StructureDefinition-onc-what-matters.md)" and the [Patient Story](StructureDefinition-onc-patient-story.md) alongside clinical measurement, in line with FONS values-based practice.
* **Equitable by design** — leads with the [Monk Skin Tone Scale](equity.md) for skin assessment and records [Reasonable Adjustments](StructureDefinition-onc-reasonable-adjustment.md) under the Equality Act 2010. See the [Health Equity & Inclusion](equity.md) page.
* **Safety-aware** — validated instruments such as [NEWS2](StructureDefinition-onc-news2-score.md) and pressure-ulcer risk scores act as clinical [safety gates](safety.md).

## Profile library

The profile library is organised below by function. For the full navigable list of every artifact, see the [Artifacts](artifacts.md) index.

### 1. Nursing process core

Base profiles that carry the ADPIE spine.

* [ONC Nursing Assessment](StructureDefinition-onc-nursing-assessment.md) — the base observation for all assessment instruments
* [ONC Nursing Problem](StructureDefinition-onc-nursing-problem.md) — nursing diagnosis (Condition)
* [ONC Nursing Need](StructureDefinition-onc-nursing-need.md) and [ONC Nursing Strength](StructureDefinition-onc-nursing-strength.md) — PRSB needs-and-strengths framing
* [ONC Nursing Goal](StructureDefinition-onc-nursing-goal.md) — planned outcomes
* [ONC Nursing Intervention](StructureDefinition-onc-nursing-intervention.md) — delivered care
* [ONC Goal Evaluation](StructureDefinition-onc-goal-evaluation.md) and [ONC Nursing Clinical Impression](StructureDefinition-onc-nursing-clinical-impression.md) — evaluation

### 2. Clinical safety and deterioration

Validated risk instruments used as safety gates. See the [Clinical Safety](safety.md) page.

* [NEWS2](StructureDefinition-onc-news2-score.md) — National Early Warning Score 2 (deterioration)
* [Braden Scale](StructureDefinition-onc-braden-scale-assessment.md) and [Waterlow Score](StructureDefinition-onc-waterlow-score.md) — pressure-ulcer risk
* [MUST](StructureDefinition-onc-must-score.md) — malnutrition screening
* [4AT Delirium Screen](StructureDefinition-onc-4at-delirium.md), [Morse Fall Scale](StructureDefinition-onc-morse-fall-scale.md), [qSOFA](StructureDefinition-onc-qsofa.md)

### 3. Relational and inclusive care

Capturing the person behind the patient. See [Health Equity & Inclusion](equity.md).

* [What Matters To Me](StructureDefinition-onc-what-matters.md) and [Patient Story](StructureDefinition-onc-patient-story.md)
* [Monk Skin Tone Observation](StructureDefinition-onc-monk-skintone-observation.md) — 10-point equitable skin assessment (A–J)
* [Skin Tone Observation](StructureDefinition-onc-skintone-observation.md) — Fitzpatrick classification (secondary)
* [Reasonable Adjustment](StructureDefinition-onc-reasonable-adjustment.md) — Equality Act 2010
* [Mental Capacity Assessment](StructureDefinition-onc-mental-capacity.md) — Mental Capacity Act 2005

### 4. Fundamental care

The essentials of daily nursing.

* [Bristol Stool Chart](StructureDefinition-onc-bristol-stool-chart.md) — elimination
* [Fluid Balance](StructureDefinition-onc-fluid-balance.md) — hydration
* [Abbey Pain Scale](StructureDefinition-onc-abbey-pain-scale.md) — non-verbal pain
* [Oral Health](StructureDefinition-onc-oral-health.md) and [Sleep Pattern](StructureDefinition-onc-sleep-pattern.md)

### 5. Specialist and mental health

Instruments for learning disability, mental health and older-person care.

* [ABC Chart](StructureDefinition-onc-abc-chart.md) — Positive Behaviour Support
* [Seizure Record](StructureDefinition-onc-seizure-record.md) — epilepsy
* [Clinical Frailty Scale](StructureDefinition-onc-clinical-frailty-scale.md) and [Glasgow Coma Scale](StructureDefinition-onc-glasgow-coma-scale.md)
* [MMSE](StructureDefinition-onc-mmse.md), [Urinalysis](StructureDefinition-onc-urinalysis.md)

## Guidance pages

* [The ADPIE Nursing Process](adpie.md) — how the IG is structured around clinical reasoning
* [Clinical Safety](safety.md) — safety gates, escalation and the DCB0129/0160 context
* [Health Equity & Inclusion](equity.md) — Monk Skin Tone Scale and reasonable adjustments
* [Security & Privacy](security.md) — UK GDPR, DSPT and Caldicott
* [Terminology](terminology.md) — SNOMED CT, LOINC and the ONC code systems
* [Structured Data Capture](questionnaires.md) — SDC Questionnaires for offline-first capture (Open Health Stack compatible)
* [Relational AI](relation-ai.md) — the FONS-aligned language model
* [Published Versions](history.md) — release history

## Getting started

1. **Browse the artifacts**— every profile, extension, value set and example is listed on the[Artifacts](artifacts.md)page.
1. **Read the process guide**— start with[ADPIE](adpie.md)to understand how the profiles fit together.
1. **Contribute**— the IG is open source under the MIT licence. Issues and pull requests are welcome on[GitHub](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig).

-------

**The Open Nursing Core is maintained by the Open Nursing Community. This guide is a technical specification and does not replace professional clinical judgement; all clinical documentation must be verified by a registered nurse.**



## Resource Content

```json
{
  "resourceType" : "ImplementationGuide",
  "id" : "onc.ig",
  "url" : "https://opennursingcoreig.com/ImplementationGuide/onc.ig",
  "version" : "1.0.0",
  "name" : "OpenNursingCoreIG",
  "title" : "Open Nursing Core FHIR Implementation Guide (ONC-IG)",
  "status" : "active",
  "date" : "2026-07-09T22:02:23+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "Foundational FHIR profiles for the nursing process (ADPIE), including Safety and Equity modules. RELEASE 1.0.0 — Trial Use, Pre-Ballot Community Release. Not yet submitted to formal HL7 standards balloting; see STANDARDS_ROADMAP.md.",
  "packageId" : "onc.ig",
  "license" : "MIT",
  "fhirVersion" : ["4.0.1"],
  "dependsOn" : [{
    "id" : "hl7tx",
    "extension" : [{
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-dependency-comment",
      "valueMarkdown" : "Automatically added as a dependency - all IGs depend on HL7 Terminology"
    }],
    "uri" : "http://terminology.hl7.org/ImplementationGuide/hl7.terminology",
    "packageId" : "hl7.terminology.r4",
    "version" : "7.2.0"
  },
  {
    "id" : "hl7ext",
    "extension" : [{
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-dependency-comment",
      "valueMarkdown" : "Automatically added as a dependency - all IGs depend on the HL7 Extension Pack"
    }],
    "uri" : "http://hl7.org/fhir/extensions/ImplementationGuide/hl7.fhir.uv.extensions",
    "packageId" : "hl7.fhir.uv.extensions.r4",
    "version" : "5.3.0"
  }],
  "definition" : {
    "extension" : [{
      "extension" : [{
        "url" : "code",
        "valueString" : "copyrightyear"
      },
      {
        "url" : "value",
        "valueString" : "2025+"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "releaselabel"
      },
      {
        "url" : "value",
        "valueString" : "release"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "autoload-resources"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "path-liquid"
      },
      {
        "url" : "value",
        "valueString" : "template/liquid"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "path-liquid"
      },
      {
        "url" : "value",
        "valueString" : "input/liquid"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "path-qa"
      },
      {
        "url" : "value",
        "valueString" : "temp/qa"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "path-temp"
      },
      {
        "url" : "value",
        "valueString" : "temp/pages"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "path-output"
      },
      {
        "url" : "value",
        "valueString" : "output"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "path-suppressed-warnings"
      },
      {
        "url" : "value",
        "valueString" : "input/ignoreWarnings.txt"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "path-history"
      },
      {
        "url" : "value",
        "valueString" : "https://opennursingcoreig.com/history.html"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "template-html"
      },
      {
        "url" : "value",
        "valueString" : "template-page.html"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "template-md"
      },
      {
        "url" : "value",
        "valueString" : "template-page-md.html"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "apply-contact"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "apply-context"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "apply-copyright"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "apply-jurisdiction"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "apply-license"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "apply-publisher"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "apply-version"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "apply-wg"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "active-tables"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "fmm-definition"
      },
      {
        "url" : "value",
        "valueString" : "http://hl7.org/fhir/versions.html#maturity"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "propagate-status"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "excludelogbinaryformat"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "tabbed-snapshots"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-internal-dependency",
      "valueCode" : "hl7.fhir.uv.tools.r4#1.1.2"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "copyrightyear"
      },
      {
        "url" : "value",
        "valueString" : "2025+"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "releaselabel"
      },
      {
        "url" : "value",
        "valueString" : "release"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "autoload-resources"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "path-liquid"
      },
      {
        "url" : "value",
        "valueString" : "template/liquid"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "path-liquid"
      },
      {
        "url" : "value",
        "valueString" : "input/liquid"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "path-qa"
      },
      {
        "url" : "value",
        "valueString" : "temp/qa"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "path-temp"
      },
      {
        "url" : "value",
        "valueString" : "temp/pages"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "path-output"
      },
      {
        "url" : "value",
        "valueString" : "output"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "path-suppressed-warnings"
      },
      {
        "url" : "value",
        "valueString" : "input/ignoreWarnings.txt"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "path-history"
      },
      {
        "url" : "value",
        "valueString" : "https://opennursingcoreig.com/history.html"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "template-html"
      },
      {
        "url" : "value",
        "valueString" : "template-page.html"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "template-md"
      },
      {
        "url" : "value",
        "valueString" : "template-page-md.html"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "apply-contact"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "apply-context"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "apply-copyright"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "apply-jurisdiction"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "apply-license"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "apply-publisher"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "apply-version"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "apply-wg"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "active-tables"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "fmm-definition"
      },
      {
        "url" : "value",
        "valueString" : "http://hl7.org/fhir/versions.html#maturity"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "propagate-status"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "excludelogbinaryformat"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "tabbed-snapshots"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    }],
    "resource" : [{
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/onc-4at-acute-change-vs"
      },
      "name" : "4AT Acute Change Value Set",
      "description" : "Scoring for Acute Change or Fluctuating Course",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/onc-4at-alertness-vs"
      },
      "name" : "4AT Alertness Value Set",
      "description" : "Scoring options for 4AT Alertness",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/onc-4at-amt4-vs"
      },
      "name" : "4AT AMT4 Value Set",
      "description" : "Scoring options for AMT4 (Age, DOB, Place, Year)",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/onc-4at-attention-vs"
      },
      "name" : "4AT Attention Value Set",
      "description" : "Scoring for Months Backwards test",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-4at-delirium"
      },
      "name" : "4AT Delirium Assessment",
      "description" : "Rapid clinical test for delirium (4AT) comprising Alertness, AMT4, Attention, and Acute Change/Fluctuating Course. A total score of 4 or more suggests possible delirium.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-abbey-pain-scale"
      },
      "name" : "Abbey Pain Scale",
      "description" : "Pain assessment for people with dementia or who cannot verbalise. Assesses 6 parameters: Vocalization, Facial Expression, Body Language, Behavioral Change, Physiological Change, Physical Changes. Total score determines pain severity (0-2 No pain, 3-7 Mild, 8-13 Moderate, 14+ Severe).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-acvpu"
      },
      "name" : "ACVPU Consciousness Level",
      "description" : "ACVPU consciousness level assessment for NEWS2 (Alert, Confusion, Voice, Pain, Unresponsive)",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/acvpu-vs"
      },
      "name" : "ACVPU Value Set",
      "description" : "ACVPU consciousness level codes",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/onc-adpie-vs"
      },
      "name" : "ADPIE Nursing Process Phases",
      "description" : "The five phases of the professional nursing process.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-barthel-index"
      },
      "name" : "Barthel Index",
      "description" : "Barthel Index for measuring independence in activities of daily living (ADL). Score 0-20=total dependency, 91-99=slight dependency, 100=independent. Total range 0-100.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-bladder-assessment"
      },
      "name" : "Bladder Assessment",
      "description" : "Detailed assessment of bladder function, including voiding patterns.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-blood-pressure"
      },
      "name" : "Blood Pressure",
      "description" : "Blood pressure observation for NEWS2 (systolic BP used for scoring)",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-body-temperature"
      },
      "name" : "Body Temperature",
      "description" : "Body temperature observation for NEWS2",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-bowel-assessment"
      },
      "name" : "Bowel Assessment",
      "description" : "Detailed assessment of bowel function and regularity.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-braden-scale-assessment"
      },
      "name" : "Braden Scale Assessment",
      "description" : "A profile for the Braden Scale pressure ulcer risk assessment",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Questionnaire"
      }],
      "reference" : {
        "reference" : "Questionnaire/onc-braden-questionnaire"
      },
      "name" : "Braden Scale Capture Form",
      "description" : "SDC questionnaire for the Braden pressure-ulcer risk assessment: six subscales, total score, and a mandatory Monk Skin Tone item (the equity fairness gate is embedded at the capture layer). Coded items extract to Observations using the ONC Braden component codes; assembling them into the single component-based ONCBradenScaleAssessment Observation (including hasMember[skinTone]) is the capturing app's responsibility.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-bristol-stool-chart"
      },
      "name" : "Bristol Stool Chart",
      "description" : "Assessment of stool form using the Bristol Stool Chart (Types 1-7). Gold standard for bowel function assessment.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-catheter-care"
      },
      "name" : "Catheter Care",
      "description" : "Documentation of catheter site care and status.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-clinical-frailty-scale"
      },
      "name" : "Clinical Frailty Scale (CFS)",
      "description" : "Assessment of frailty using the Rockwood Clinical Frailty Scale (1-9). Essential for older adults to determine baseline functional status.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/onc-cfs-vs"
      },
      "name" : "Clinical Frailty Scale Value Set",
      "description" : "Codes for Rockwood Clinical Frailty Scale (1-9)",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-continence-assessment"
      },
      "name" : "Continence Assessment",
      "description" : "Assessment of bladder and bowel control status.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-device-use-statement"
      },
      "name" : "Device Use Statement",
      "description" : "Documentation of mobility aids or other devices used by the patient.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-dietary-requirements"
      },
      "name" : "Dietary Requirements",
      "description" : "Documentation of specific dietary needs (e.g. textural modification, cultural).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-dressing-assessment"
      },
      "name" : "Dressing and Undressing Assessment",
      "description" : "Assessment of assistance required for dressing and undressing, as per PRSB Personal Hygiene section.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/ExampleDressingAssessment"
      },
      "name" : "Example Dressing Assessment",
      "description" : "Demonstration of the ONCDressingAssessment profile.",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-dressing-assessment"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Condition"
      }],
      "reference" : {
        "reference" : "Condition/ExampleNursingNeed-Dressing"
      },
      "name" : "Example Nursing Need: Dressing Difficulty",
      "description" : "Demonstration of the ONCNursingNeed profile.",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-nursing-need"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/ExampleNursingStrength-Motivation"
      },
      "name" : "Example Nursing Strength: Motivation",
      "description" : "Demonstration of the ONCNursingStrength profile.",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-nursing-strength"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/ExampleSkinAssessment"
      },
      "name" : "Example Skin Assessment",
      "description" : "Demonstration of the ONCSkinAssessment profile for general skin integrity.",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-skin-assessment"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-4at-delirium"
      },
      "name" : "example-4at-delirium",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-4at-delirium"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-abbey-pain"
      },
      "name" : "example-abbey-pain",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-abbey-pain-scale"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-abc-chart"
      },
      "name" : "example-abc-chart",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-abc-chart"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-acvpu"
      },
      "name" : "example-acvpu",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-acvpu"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-bladder-assessment"
      },
      "name" : "example-bladder-assessment",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-bladder-assessment"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-blood-pressure"
      },
      "name" : "example-blood-pressure",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-blood-pressure"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-bowel-assessment"
      },
      "name" : "example-bowel-assessment",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-bowel-assessment"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-bristol-stool"
      },
      "name" : "example-bristol-stool",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-bristol-stool-chart"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-catheter-care"
      },
      "name" : "example-catheter-care",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-catheter-care"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-clinical-frailty"
      },
      "name" : "example-clinical-frailty",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-clinical-frailty-scale"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-continence-assessment"
      },
      "name" : "example-continence-assessment",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-continence-assessment"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-dietary-requirements"
      },
      "name" : "example-dietary-requirements",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-dietary-requirements"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-fluid-balance"
      },
      "name" : "example-fluid-balance",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-fluid-balance"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-goal-evaluation"
      },
      "name" : "example-goal-evaluation",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-goal-evaluation"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-heart-rate"
      },
      "name" : "example-heart-rate",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-heart-rate"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-hygiene-assessment"
      },
      "name" : "example-hygiene-assessment",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-hygiene-assessment"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-inspired-oxygen"
      },
      "name" : "example-inspired-oxygen",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-inspired-oxygen"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-medication-ability"
      },
      "name" : "example-medication-ability",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-medication-ability"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-medication-self-admin"
      },
      "name" : "example-medication-self-admin",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-medication-self-admin"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-mental-capacity"
      },
      "name" : "example-mental-capacity",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-mental-capacity"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-mobility-assessment"
      },
      "name" : "example-mobility-assessment",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-mobility-assessment"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-monk-skin-tone"
      },
      "name" : "example-monk-skin-tone",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-monk-skintone-observation"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-must-score"
      },
      "name" : "example-must-score",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-must-score"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-news2-score"
      },
      "name" : "example-news2-score",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-news2-score"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Procedure"
      }],
      "reference" : {
        "reference" : "Procedure/example-nursing-intervention"
      },
      "name" : "example-nursing-intervention",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-nursing-intervention"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Condition"
      }],
      "reference" : {
        "reference" : "Condition/example-nursing-problem"
      },
      "name" : "example-nursing-problem",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-nursing-problem"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-oral-care-assessment"
      },
      "name" : "example-oral-care-assessment",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-oral-care-assessment"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-oral-health"
      },
      "name" : "example-oral-health",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-oral-health"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-oral-intake"
      },
      "name" : "example-oral-intake",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-oral-intake-assessment"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-oxygen-saturation"
      },
      "name" : "example-oxygen-saturation",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-oxygen-saturation"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Goal"
      }],
      "reference" : {
        "reference" : "Goal/example-patient-goal"
      },
      "name" : "example-patient-goal",
      "description" : "Patient will remain free from falls.",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-nursing-goal"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-patient-story"
      },
      "name" : "example-patient-story",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-patient-story"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-reasonable-adjustment"
      },
      "name" : "example-reasonable-adjustment",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-reasonable-adjustment"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-respiration-rate"
      },
      "name" : "example-respiration-rate",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-respiration-rate"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-seizure-record"
      },
      "name" : "example-seizure-record",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-seizure-record"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-swallowing-assessment"
      },
      "name" : "example-swallowing-assessment",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-swallowing-assessment"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-temperature"
      },
      "name" : "example-temperature",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-body-temperature"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-urinalysis"
      },
      "name" : "example-urinalysis",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-urinalysis"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-waterlow-score"
      },
      "name" : "example-waterlow-score",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-waterlow-score"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/example-what-matters"
      },
      "name" : "example-what-matters",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-what-matters"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-fluid-balance"
      },
      "name" : "Fluid Balance",
      "description" : "Assessment of fluid intake, output, and balance. Critical for renal function, hydration status, and heart failure monitoring.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-glasgow-coma-scale"
      },
      "name" : "Glasgow Coma Scale",
      "description" : "Glasgow Coma Scale (GCS) for assessing level of consciousness. Total score 3-15 with three required components: Eye (1-4), Verbal (1-5), Motor (1-6).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/goal-evaluation-valueset"
      },
      "name" : "Goal Evaluation Value Set",
      "description" : "Value set for evaluating patient goal outcomes",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/onc-goal-target-measure-vs"
      },
      "name" : "Goal Target Measure ValueSet",
      "description" : "Codes used for goal target measures",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-heart-rate"
      },
      "name" : "Heart Rate",
      "description" : "Heart rate (pulse) observation for NEWS2",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/housing-status-vs"
      },
      "name" : "Housing Status Value Set",
      "description" : "Value set for patient housing status",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-inspired-oxygen"
      },
      "name" : "Inspired Oxygen",
      "description" : "Inspired oxygen observation for NEWS2 (air vs supplemental oxygen)",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/inspired-oxygen-vs"
      },
      "name" : "Inspired Oxygen Value Set",
      "description" : "Codes for inspired oxygen status",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      }],
      "reference" : {
        "reference" : "StructureDefinition/intervention-goal-reference"
      },
      "name" : "Intervention Goal Reference",
      "description" : "Extension to link nursing interventions to the patient goals they are intended to achieve.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ConceptMap"
      }],
      "reference" : {
        "reference" : "ConceptMap/onc-to-nanda"
      },
      "name" : "Mapping ONC Relational Concepts to NANDA-I",
      "description" : "Maps Open Nursing Core clinical findings to NANDA-I Nursing Diagnoses. NOT PRODUCTION-READY: see the placeholder-canonical note below.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-medication-ability"
      },
      "name" : "Medication Management Ability",
      "description" : "Assessment of the patient's ability to manage their own medication.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-medication-self-admin"
      },
      "name" : "Medication Self-Administration Observation",
      "description" : "Observation of the patient performing self-administration.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-mental-capacity"
      },
      "name" : "Mental Capacity Assessment",
      "description" : "Records the outcome of a Mental Capacity Assessment for a specific decision. Fundamental legal safeguard in UK nursing practice.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/onc-mca-vs"
      },
      "name" : "Mental Capacity Finding Value Set",
      "description" : "Codes indicating presence or absence of capacity",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-mmse"
      },
      "name" : "Mini Mental State Examination (MMSE)",
      "description" : "Mini Mental State Examination for cognitive function screening. Score 24-30=no impairment, 18-23=mild, 0-17=severe. Total range 0-30.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-mobility-assessment"
      },
      "name" : "Mobility Assessment",
      "description" : "Assessment of capability to move and limitations.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Questionnaire"
      }],
      "reference" : {
        "reference" : "Questionnaire/onc-monk-skintone-questionnaire"
      },
      "name" : "Monk Skin Tone Capture Form",
      "description" : "SDC questionnaire capturing the patient's skin tone on the 10-point Monk Skin Tone Scale (A–J). Extracts to an Observation conforming to ONCMonkSkinToneObservation. This record is the required input to the IG's equity fairness gate for wound and pressure-area assessment.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-monk-skintone-observation"
      },
      "name" : "Monk Skin Tone Observation",
      "description" : "Observation of patient skin tone using the Monk Skin Tone Scale (10-point scale A-J). Provides more granular skin tone assessment than Fitzpatrick scale, particularly for darker skin tones. Supports equitable care and accurate clinical assessment across diverse populations.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      }],
      "reference" : {
        "reference" : "CodeSystem/onc-monk-scale"
      },
      "name" : "Monk Skin Tone Scale CodeSystem",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/onc-monk-scale-vs"
      },
      "name" : "Monk Skin Tone Scale ValueSet",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-morse-fall-scale"
      },
      "name" : "Morse Fall Scale",
      "description" : "Morse Fall Scale for assessing fall risk. Score 0-24=no risk, 25-50=low risk, ≥51=high risk. Total range 0-125.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Questionnaire"
      }],
      "reference" : {
        "reference" : "Questionnaire/onc-must-questionnaire"
      },
      "name" : "MUST Capture Form",
      "description" : "SDC questionnaire for the Malnutrition Universal Screening Tool: three step scores and the total. Coded items extract to Observations using the ONC MUST component codes; assembling them into the single component-based ONCMUSTScore Observation is the capturing app's responsibility.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-must-score"
      },
      "name" : "MUST Score (Malnutrition Universal Screening Tool)",
      "description" : "Malnutrition Universal Screening Tool for identifying adults at risk of malnutrition. Score 0=low risk, 1=medium risk, 2+=high risk. NHS-standard nutritional screening.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Questionnaire"
      }],
      "reference" : {
        "reference" : "Questionnaire/onc-news2-questionnaire"
      },
      "name" : "NEWS2 Capture Form",
      "description" : "SDC questionnaire for capturing the NEWS2 physiological parameter set and total score. Coded items extract to Observations conforming to the ONC NEWS2 and vital-sign profiles. Scoring and escalation logic is computable via the ONC_NEWS2_Logic CQL library and the news2-escalation PlanDefinition.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/news2-code-vs"
      },
      "name" : "NEWS2 Code Value Set",
      "description" : "LOINC and SNOMED codes for NEWS2",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "PlanDefinition"
      }],
      "reference" : {
        "reference" : "PlanDefinition/news2-escalation-plan"
      },
      "name" : "NEWS2 Escalation Protocol",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-news2-score"
      },
      "name" : "NEWS2 Score",
      "description" : "National Early Warning Score 2 (NEWS2) for detecting clinical deterioration. Fully aligned with NHS CareConnect-NEWS2-Observation-1.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/onc-news2-score-vs"
      },
      "name" : "NEWS2 Score Categories Value Set",
      "description" : "NEWS2 total score categories.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-news2-subscore"
      },
      "name" : "NEWS2 Sub-Score",
      "description" : "Individual parameter sub-score for NEWS2 (0-3 for most parameters). References the related vital sign observation.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/news2-subscore-code-vs"
      },
      "name" : "NEWS2 Sub-Score Codes",
      "description" : "SNOMED codes for NEWS2 sub-scores",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/nursing-intervention-valueset"
      },
      "name" : "Nursing Intervention Value Set",
      "description" : "Value set for nursing interventions",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-nursing-problem"
      },
      "name" : "Nursing Problem",
      "description" : "Nursing diagnosis or problem identified during assessment. Represents clinical judgments about individual, family, or community responses to actual or potential health problems. Part of the ADPIE framework's Diagnosis phase.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/nursing-problem-valueset"
      },
      "name" : "Nursing Problem Value Set",
      "description" : "Value set for nursing problems and diagnoses",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/onc-prognosis-vs"
      },
      "name" : "Nursing Prognosis ValueSet",
      "description" : "Prognosis codes for clinical impression",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      }],
      "reference" : {
        "reference" : "StructureDefinition/observation-goal-reference"
      },
      "name" : "Observation Goal Reference",
      "description" : "Extension to link goal evaluation observations to the patient goals being evaluated.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/observation-braden-scale"
      },
      "name" : "observation-braden-scale",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-braden-scale-assessment"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Observation"
      }],
      "reference" : {
        "reference" : "Observation/observation-skin-tone"
      },
      "name" : "observation-skin-tone",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-skintone-observation"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/onc-empathy-index-vs"
      },
      "name" : "ONC Empathy & Relational Engagement Index",
      "description" : "A clinical scale measuring the depth of therapeutic empathy in nurse-patient interactions. Traditional EHRs ignore this; the Super-Gold Standard makes it a primary outcome.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-equity-marker"
      },
      "name" : "ONC Equity Marker",
      "description" : "A technical extension applied to observations that have passed the Mandatory Equity Gate (i.e., they are skin-tone aware).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-goal-evaluation"
      },
      "name" : "ONC Goal Evaluation",
      "description" : "Explicit evaluation of whether a nursing goal was achieved, closing the ADPIE loop.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Library"
      }],
      "reference" : {
        "reference" : "Library/onc-news2-cql"
      },
      "name" : "ONC NEWS2 Auto-Calculation Logic",
      "description" : "Logic library for calculating National Early Warning Score 2 (NEWS2) from FHIR Observations.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-nhs-patient"
      },
      "name" : "ONC NHS Patient",
      "description" : "A patient profile for use in NHS nursing contexts with ethnic category extension.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-nursing-clinical-impression"
      },
      "name" : "ONC Nursing Clinical Impression",
      "description" : "Nurse's synthesis of patient progress against care plan, aggregating multiple goal evaluations.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-nursing-goal"
      },
      "name" : "ONC Nursing Goal",
      "description" : "Patient-centered goal with mandatory evaluation requirements. Serves as the 'spine' of the CarePlan, linking problems to outcomes.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-nursing-intervention"
      },
      "name" : "ONC Nursing Intervention",
      "description" : "Nursing intervention performed to achieve patient goals. Part of ADPIE Implementation phase.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-nursing-need"
      },
      "name" : "ONC Nursing Need",
      "description" : "A structured representation of a nursing care need as defined by the PRSB standard. Maps to the 'Needs' section of the information model.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-nursing-strength"
      },
      "name" : "ONC Nursing Strength",
      "description" : "A structured representation of a patient's strength or capability. Explicitly required by PRSB to move away from deficit-based models.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      }],
      "reference" : {
        "reference" : "CodeSystem/onc-observation-codes"
      },
      "name" : "ONC Observation Codes",
      "description" : "Custom observation codes for Open Nursing Core",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/onc-relational-outcomes-vs"
      },
      "name" : "ONC Relational Care Outcomes",
      "description" : "Captures the measurable outcomes of relational and empathic nursing care.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-nursing-assessment"
      },
      "name" : "Open Nursing Core Assessment",
      "description" : "Base profile for nursing assessment observations conforming to UK Core standards. Captures structured nursing assessment data as part of the ADPIE (Assessment, Diagnosis, Planning, Implementation, Evaluation) nursing process framework. Used as parent for specialized assessments like NEWS2, Braden Scale, and clinical observations.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-oral-care-assessment"
      },
      "name" : "Oral Care Needs Assessment",
      "description" : "Assessment of mouth care needs and oral health.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-oral-health"
      },
      "name" : "Oral Health Assessment",
      "description" : "Assessment of oral cavity health. Critical for prevention of pneumonia in frail elderly and maintaining nutrition/hydration.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-oral-intake-assessment"
      },
      "name" : "Oral Intake Assessment",
      "description" : "Assessment of ability to take food and fluids orally.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-oxygen-saturation"
      },
      "name" : "Oxygen Saturation",
      "description" : "Oxygen saturation (SpO2) observation for NEWS2",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-pain-assessment"
      },
      "name" : "Pain Assessment (NRS 0-10)",
      "description" : "Pain severity assessment using the Numeric Rating Scale (0-10)",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/pain-assessment-code-vs"
      },
      "name" : "Pain Assessment Code Value Set",
      "description" : "LOINC codes for pain severity assessment",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/onc-pain-score-vs"
      },
      "name" : "Pain Score Value Set",
      "description" : "Standard 0-10 or Abbey Pain Scale score",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-patient-story"
      },
      "name" : "Patient Story",
      "description" : "A narrative summary of the patient's background, biography, preferences, and personhood. Goes beyond clinical history to capture 'who the person is'.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Patient"
      }],
      "reference" : {
        "reference" : "Patient/patient-example-jane"
      },
      "name" : "patient-example-jane",
      "exampleCanonical" : "https://opennursingcoreig.com/StructureDefinition/onc-nhs-patient"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-abc-chart"
      },
      "name" : "PBS ABC Chart",
      "description" : "Antecedent-Behaviour-Consequence (ABC) Chart for recording behaviours of concern. Fundamental tool in Positive Behaviour Support (PBS) for Learning Disabilities.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/onc-pbs-function-vs"
      },
      "name" : "PBS Behaviour Function ValueSet",
      "description" : "Common functions of behaviour (SEAT)",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Questionnaire"
      }],
      "reference" : {
        "reference" : "Questionnaire/onc-person-centred-questionnaire"
      },
      "name" : "Person-Centred Care Capture Form",
      "description" : "SDC questionnaire capturing 'What Matters to Me' and reasonable adjustments (Equality Act 2010) as structured, retrievable records. Items extract to Observations conforming to ONCWhatMattersToMe and ONCReasonableAdjustment.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-hygiene-assessment"
      },
      "name" : "Personal Hygiene Needs Assessment",
      "description" : "Assessment of assistance required for personal hygiene.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Practitioner"
      }],
      "reference" : {
        "reference" : "Practitioner/practitioner-example"
      },
      "name" : "practitioner-example",
      "exampleBoolean" : true
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/problem-category-valueset"
      },
      "name" : "Problem Category Value Set",
      "description" : "Value set for categorizing nursing problems",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      }],
      "reference" : {
        "reference" : "CodeSystem/onc-problem-type"
      },
      "name" : "Problem Type CodeSystem",
      "description" : "Code system for categorizing types of nursing problems",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-qsofa"
      },
      "name" : "qSOFA (Quick SOFA)",
      "description" : "Quick Sequential Organ Failure Assessment for sepsis screening. Score ≥2 indicates high risk. Total range 0-3.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-reasonable-adjustment"
      },
      "name" : "Reasonable Adjustment",
      "description" : "Captures specific strict requirements for care adjustments under the Equality Act (e.g., 'Needs BSL Interpreter', 'Cannot use stairs', 'Requires large print').",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-relational-care-logical"
      },
      "name" : "Relational Care Logical Model",
      "description" : "A vendor-neutral clinical model of the relational nursing assessment. Defines WHAT data must be captured, regardless of HOW it is stored in FHIR.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-relational-observation"
      },
      "name" : "Relational Engagement Score",
      "description" : "Assessment of the quality and depth of the nurse-patient relationship or engagement level. Supports the relational aspect of care.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-respiration-rate"
      },
      "name" : "Respiration Rate",
      "description" : "Respiration rate observation for NEWS2",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-seizure-record"
      },
      "name" : "Seizure Record",
      "description" : "Record of a specific seizure event, including type, duration, triggers, and recovery phases. Essential for epilepsy management and identifying patterns.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-skin-assessment"
      },
      "name" : "Skin Integrity Assessment",
      "description" : "Detailed assessment of skin condition (e.g., intact, dry, broken), separate from pressure ulcer risk.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-skintone-observation"
      },
      "name" : "Skin Tone Observation (Fitzpatrick -- secondary/legacy)",
      "description" : "Observation of patient skin tone using the Fitzpatrick skin type classification. Fitzpatrick was designed to describe UV photosensitivity, not clinical skin tone, and compresses the darker end of the range into few categories. This profile is RETAINED FOR BACKWARD COMPATIBILITY with systems that already record Fitzpatrick phototypes; it is secondary to, and SHOULD NOT be used in place of, the Monk Skin Tone Scale (see ONCMonkSkinToneObservation), which is this IG's primary and recommended skin-tone vocabulary.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/onc-skin-tone-vs"
      },
      "name" : "Skin Tone Value Set",
      "description" : "Skin tone scales for equitable skin assessment. Monk (A-J) is the primary, recommended scale; Fitzpatrick (I-VI) is retained only for backward compatibility with legacy systems.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-sleep-pattern"
      },
      "name" : "Sleep Pattern",
      "description" : "Observation of sleep quality, duration, and disturbances. Sleep pattern disturbance is a key indicator for delirium and general wellbeing.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-swallowing-assessment"
      },
      "name" : "Swallowing Assessment",
      "description" : "Screening for dysphagia and swallowing difficulties.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      }],
      "reference" : {
        "reference" : "StructureDefinition/UKCore-Extension-EthnicCategory"
      },
      "name" : "UK Core Ethnic Category",
      "description" : "An extension to record the ethnic category of a patient, as per UK Core standards.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-urinalysis"
      },
      "name" : "Urinalysis",
      "description" : "Point-of-care urine dipstick test results. Used to screen for urinary tract infection (UTI), diabetes (glucose/ketones), and kidney health.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-waterlow-score"
      },
      "name" : "Waterlow Score",
      "description" : "Waterlow Pressure Ulcer Risk Assessment - NHS standard tool. Score ≥10 indicates at risk, ≥15 high risk, ≥20 very high risk.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Questionnaire"
      }],
      "reference" : {
        "reference" : "Questionnaire/onc-waterlow-questionnaire"
      },
      "name" : "Waterlow Score Capture Form",
      "description" : "SDC questionnaire for the Waterlow pressure-ulcer risk assessment total score, with a mandatory Monk Skin Tone item (equity fairness gate embedded at the capture layer). The total extracts to an Observation using the ONC Waterlow code; linking the skin-tone Observation via hasMember[skinTone] is the capturing app's responsibility.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-what-matters"
      },
      "name" : "What Matters to Me",
      "description" : "Captures the patient's specific, personal priorities and non-clinical goals (e.g., 'I want to walk my daughter down the aisle'). Fundamental to person-centred care.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/onc-wound-assessment"
      },
      "name" : "Wound Assessment",
      "description" : "Comprehensive wound assessment including staging and dimensions",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/wound-stage-vs"
      },
      "name" : "Wound Stage Value Set",
      "exampleBoolean" : false
    }],
    "page" : {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
        "valueUrl" : "toc.html"
      }],
      "nameUrl" : "toc.html",
      "title" : "Table of Contents",
      "generation" : "html",
      "page" : [{
        "extension" : [{
          "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
          "valueUrl" : "index.html"
        }],
        "nameUrl" : "index.html",
        "title" : "Home",
        "generation" : "markdown"
      },
      {
        "extension" : [{
          "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
          "valueUrl" : "adpie.html"
        }],
        "nameUrl" : "adpie.html",
        "title" : "The ADPIE Nursing Process",
        "generation" : "markdown"
      },
      {
        "extension" : [{
          "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
          "valueUrl" : "safety.html"
        }],
        "nameUrl" : "safety.html",
        "title" : "Clinical Safety",
        "generation" : "markdown"
      },
      {
        "extension" : [{
          "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
          "valueUrl" : "equity.html"
        }],
        "nameUrl" : "equity.html",
        "title" : "Health Equity & Inclusion",
        "generation" : "markdown"
      },
      {
        "extension" : [{
          "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
          "valueUrl" : "security.html"
        }],
        "nameUrl" : "security.html",
        "title" : "Security & Privacy",
        "generation" : "markdown"
      },
      {
        "extension" : [{
          "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
          "valueUrl" : "terminology.html"
        }],
        "nameUrl" : "terminology.html",
        "title" : "Terminology",
        "generation" : "markdown"
      },
      {
        "extension" : [{
          "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
          "valueUrl" : "questionnaires.html"
        }],
        "nameUrl" : "questionnaires.html",
        "title" : "Structured Data Capture",
        "generation" : "markdown"
      },
      {
        "extension" : [{
          "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
          "valueUrl" : "relation-ai.html"
        }],
        "nameUrl" : "relation-ai.html",
        "title" : "Relational Ai (AI Model)",
        "generation" : "markdown"
      },
      {
        "extension" : [{
          "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
          "valueUrl" : "history.html"
        }],
        "nameUrl" : "history.html",
        "title" : "Published Versions",
        "generation" : "markdown"
      }]
    },
    "parameter" : [{
      "code" : "path-resource",
      "value" : "input/capabilities"
    },
    {
      "code" : "path-resource",
      "value" : "input/examples"
    },
    {
      "code" : "path-resource",
      "value" : "input/extensions"
    },
    {
      "code" : "path-resource",
      "value" : "input/models"
    },
    {
      "code" : "path-resource",
      "value" : "input/operations"
    },
    {
      "code" : "path-resource",
      "value" : "input/profiles"
    },
    {
      "code" : "path-resource",
      "value" : "input/resources"
    },
    {
      "code" : "path-resource",
      "value" : "input/vocabulary"
    },
    {
      "code" : "path-resource",
      "value" : "input/maps"
    },
    {
      "code" : "path-resource",
      "value" : "input/testing"
    },
    {
      "code" : "path-resource",
      "value" : "input/history"
    },
    {
      "code" : "path-resource",
      "value" : "fsh-generated/resources"
    },
    {
      "code" : "path-pages",
      "value" : "template/config"
    },
    {
      "code" : "path-pages",
      "value" : "input/images"
    },
    {
      "code" : "path-tx-cache",
      "value" : "input-cache/txcache"
    }]
  }
}

```
