# Mobility Assessment - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Mobility Assessment**

## Resource Profile: Mobility Assessment 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/StructureDefinition/onc-mobility-assessment | *Version*:1.0.0 |
| Active as of 2026-07-11 | *Computable Name*:ONCMobilityAssessment |

 
Assessment of capability to move and limitations. 

**Usages:**

* Examples for this Profile: [Observation/example-mobility-assessment](Observation-example-mobility-assessment.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/onc.ig|current/StructureDefinition/StructureDefinition-onc-mobility-assessment.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-mobility-assessment.csv), [Excel](StructureDefinition-onc-mobility-assessment.xlsx), [Schematron](StructureDefinition-onc-mobility-assessment.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-mobility-assessment",
  "url" : "https://opennursingcoreig.com/StructureDefinition/onc-mobility-assessment",
  "version" : "1.0.0",
  "name" : "ONCMobilityAssessment",
  "title" : "Mobility Assessment",
  "status" : "active",
  "date" : "2026-07-11T14:17:07+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "Assessment of capability to move and limitations.",
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
      "path" : "Observation",
      "constraint" : [{
        "key" : "onc-mobility-gate",
        "severity" : "error",
        "human" : "Safety Rule: If patient is Bedbound, a Pressure Ulcer Risk Assessment reference is mandatory.",
        "expression" : "value.coding.where(code = 'bedbound').exists() implies hasMember.exists()",
        "source" : "https://opennursingcoreig.com/StructureDefinition/onc-mobility-assessment"
      }]
    },
    {
      "id" : "Observation.code",
      "path" : "Observation.code",
      "patternCodeableConcept" : {
        "coding" : [{
          "system" : "http://snomed.info/sct",
          "code" : "82971005",
          "display" : "Impaired mobility"
        }]
      }
    },
    {
      "id" : "Observation.value[x]",
      "path" : "Observation.value[x]",
      "type" : [{
        "code" : "CodeableConcept"
      }]
    },
    {
      "id" : "Observation.component",
      "path" : "Observation.component",
      "slicing" : {
        "discriminator" : [{
          "type" : "pattern",
          "path" : "code"
        }],
        "ordered" : false,
        "rules" : "open"
      },
      "min" : 1,
      "mustSupport" : true
    },
    {
      "id" : "Observation.component:empathyIndex",
      "path" : "Observation.component",
      "sliceName" : "empathyIndex",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Observation.component:empathyIndex.code",
      "path" : "Observation.component.code",
      "patternCodeableConcept" : {
        "coding" : [{
          "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
          "code" : "empathy-index"
        }]
      }
    },
    {
      "id" : "Observation.component:empathyIndex.value[x]",
      "path" : "Observation.component.value[x]",
      "type" : [{
        "code" : "CodeableConcept"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "https://opennursingcoreig.com/ValueSet/onc-empathy-index-vs"
      }
    }]
  }
}

```
