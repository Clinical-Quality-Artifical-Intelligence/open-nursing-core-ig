# Relational Care Logical Model - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Relational Care Logical Model**

## Logical Model: Relational Care Logical Model 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/StructureDefinition/ONCRelationalCareModel | *Version*:1.0.0 |
| Active as of 2026-07-11 | *Computable Name*:ONCRelationalCareModel |

 
A vendor-neutral clinical model of the relational nursing assessment. Defines WHAT data must be captured, regardless of HOW it is stored in FHIR. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/onc.ig|current/StructureDefinition/StructureDefinition-ONCRelationalCareModel.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-ONCRelationalCareModel.csv), [Excel](StructureDefinition-ONCRelationalCareModel.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ONCRelationalCareModel",
  "url" : "https://opennursingcoreig.com/StructureDefinition/ONCRelationalCareModel",
  "version" : "1.0.0",
  "name" : "ONCRelationalCareModel",
  "title" : "Relational Care Logical Model",
  "status" : "active",
  "date" : "2026-07-11T14:47:20+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "A vendor-neutral clinical model of the relational nursing assessment. Defines WHAT data must be captured, regardless of HOW it is stored in FHIR.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "https://opennursingcoreig.com/StructureDefinition/ONCRelationalCareModel",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "ONCRelationalCareModel",
      "path" : "ONCRelationalCareModel",
      "short" : "Relational Care Logical Model",
      "definition" : "A vendor-neutral clinical model of the relational nursing assessment. Defines WHAT data must be captured, regardless of HOW it is stored in FHIR."
    },
    {
      "id" : "ONCRelationalCareModel.patientPreferences",
      "path" : "ONCRelationalCareModel.patientPreferences",
      "short" : "The patient's personal goals and what matters most to them today.",
      "definition" : "The patient's personal goals and what matters most to them today.",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "ONCRelationalCareModel.relationalEngagement",
      "path" : "ONCRelationalCareModel.relationalEngagement",
      "short" : "A score from 1-5 representing the depth of the therapeutic relationship.",
      "definition" : "A score from 1-5 representing the depth of the therapeutic relationship.",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "integer"
      }]
    },
    {
      "id" : "ONCRelationalCareModel.empathyIndex",
      "path" : "ONCRelationalCareModel.empathyIndex",
      "short" : "The ONC Empathy Index (1-5) measuring relational quality.",
      "definition" : "The ONC Empathy Index (1-5) measuring relational quality.",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "https://opennursingcoreig.com/ValueSet/onc-empathy-index-vs"
      }
    },
    {
      "id" : "ONCRelationalCareModel.skinToneEquity",
      "path" : "ONCRelationalCareModel.skinToneEquity",
      "short" : "The patient's skin tone classification (Monk primary, Fitzpatrick secondary/legacy) used to guide clinical assessment.",
      "definition" : "The patient's skin tone classification (Monk primary, Fitzpatrick secondary/legacy) used to guide clinical assessment.",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "extensible",
        "valueSet" : "https://opennursingcoreig.com/ValueSet/onc-skin-tone-vs"
      }
    },
    {
      "id" : "ONCRelationalCareModel.mandatoryEquityValidation",
      "path" : "ONCRelationalCareModel.mandatoryEquityValidation",
      "short" : "Technical flag ensuring the 'Fairness Gate' was passed.",
      "definition" : "Technical flag ensuring the 'Fairness Gate' was passed.",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "boolean"
      }]
    },
    {
      "id" : "ONCRelationalCareModel.adpieStatus",
      "path" : "ONCRelationalCareModel.adpieStatus",
      "short" : "The current stage of the professional nursing process (Assessment, Diagnosis, Planning, Implementation, Evaluation).",
      "definition" : "The current stage of the professional nursing process (Assessment, Diagnosis, Planning, Implementation, Evaluation).",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "https://opennursingcoreig.com/ValueSet/onc-adpie-vs"
      }
    },
    {
      "id" : "ONCRelationalCareModel.clinicalNarrative",
      "path" : "ONCRelationalCareModel.clinicalNarrative",
      "short" : "The person-centred narrative describing the patient's experience.",
      "definition" : "The person-centred narrative describing the patient's experience.",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    }]
  }
}

```
