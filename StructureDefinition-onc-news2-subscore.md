# NEWS2 Sub-Score - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **NEWS2 Sub-Score**

## Resource Profile: NEWS2 Sub-Score 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/StructureDefinition/onc-news2-subscore | *Version*:1.0.0 |
| Active as of 2026-06-29 | *Computable Name*:ONCNEWS2Subscore |

 
Individual parameter sub-score for NEWS2 (0-3 for most parameters). References the related vital sign observation. 

**Usages:**

* This Profile is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/onc.ig|current/StructureDefinition/StructureDefinition-onc-news2-subscore.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-news2-subscore.csv), [Excel](StructureDefinition-onc-news2-subscore.xlsx), [Schematron](StructureDefinition-onc-news2-subscore.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-news2-subscore",
  "url" : "https://opennursingcoreig.com/StructureDefinition/onc-news2-subscore",
  "version" : "1.0.0",
  "name" : "ONCNEWS2Subscore",
  "title" : "NEWS2 Sub-Score",
  "status" : "active",
  "date" : "2026-06-29T21:13:26+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "Individual parameter sub-score for NEWS2 (0-3 for most parameters). References the related vital sign observation.",
  "fhirVersion" : "4.0.1",
  "mapping" : [{
    "identity" : "workflow",
    "uri" : "http://hl7.org/fhir/workflow",
    "name" : "Workflow Pattern"
  },
  {
    "identity" : "sct-concept",
    "uri" : "http://snomed.info/conceptdomain",
    "name" : "SNOMED CT Concept Domain Binding"
  },
  {
    "identity" : "v2",
    "uri" : "http://hl7.org/v2",
    "name" : "HL7 v2 Mapping"
  },
  {
    "identity" : "rim",
    "uri" : "http://hl7.org/v3",
    "name" : "RIM Mapping"
  },
  {
    "identity" : "w5",
    "uri" : "http://hl7.org/fhir/fivews",
    "name" : "FiveWs Pattern Mapping"
  },
  {
    "identity" : "sct-attr",
    "uri" : "http://snomed.org/attributebinding",
    "name" : "SNOMED CT Attribute Binding"
  }],
  "kind" : "resource",
  "abstract" : false,
  "type" : "Observation",
  "baseDefinition" : "https://opennursingcoreig.com/StructureDefinition/onc-nursing-assessment",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Observation",
      "path" : "Observation"
    },
    {
      "id" : "Observation.status",
      "path" : "Observation.status",
      "patternCode" : "final",
      "mustSupport" : true
    },
    {
      "id" : "Observation.code",
      "path" : "Observation.code",
      "patternCodeableConcept" : {
        "coding" : [{
          "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
          "code" : "news2-subscore",
          "display" : "NEWS2 Sub-score"
        }]
      },
      "mustSupport" : true
    },
    {
      "id" : "Observation.value[x]",
      "path" : "Observation.value[x]",
      "min" : 1,
      "type" : [{
        "code" : "Quantity"
      }]
    },
    {
      "id" : "Observation.value[x].value",
      "path" : "Observation.value[x].value",
      "constraint" : [{
        "key" : "subscore-range",
        "severity" : "error",
        "human" : "NEWS2 sub-score must be between 0 and 3",
        "expression" : "$this >= 0 and $this <= 3",
        "source" : "https://opennursingcoreig.com/StructureDefinition/onc-news2-subscore"
      }]
    },
    {
      "id" : "Observation.value[x].unit",
      "path" : "Observation.value[x].unit",
      "patternString" : "{score}"
    },
    {
      "id" : "Observation.value[x].system",
      "path" : "Observation.value[x].system",
      "patternUri" : "http://unitsofmeasure.org"
    }]
  }
}

```
