# Skin Integrity Assessment - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Skin Integrity Assessment**

## Resource Profile: Skin Integrity Assessment 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/StructureDefinition/onc-skin-assessment | *Version*:0.1.0 |
| Draft as of 2026-01-26 | *Computable Name*:ONCSkinAssessment |

 
Detailed assessment of skin condition (e.g., intact, dry, broken), separate from pressure ulcer risk. 

**Usages:**

* Examples for this Profile: [Observation/ExampleSkinAssessment](Observation-ExampleSkinAssessment.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/onc.ig|current/StructureDefinition/onc-skin-assessment)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-skin-assessment.csv), [Excel](StructureDefinition-onc-skin-assessment.xlsx), [Schematron](StructureDefinition-onc-skin-assessment.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-skin-assessment",
  "url" : "https://opennursingcoreig.com/StructureDefinition/onc-skin-assessment",
  "version" : "0.1.0",
  "name" : "ONCSkinAssessment",
  "title" : "Skin Integrity Assessment",
  "status" : "draft",
  "date" : "2026-01-26T23:55:12+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "Detailed assessment of skin condition (e.g., intact, dry, broken), separate from pressure ulcer risk.",
  "fhirVersion" : "4.0.1",
  "mapping" : [
    {
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
    }
  ],
  "kind" : "resource",
  "abstract" : false,
  "type" : "Observation",
  "baseDefinition" : "https://opennursingcoreig.com/StructureDefinition/onc-nursing-assessment",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "Observation",
        "path" : "Observation"
      },
      {
        "id" : "Observation.code",
        "path" : "Observation.code",
        "patternCodeableConcept" : {
          "coding" : [
            {
              "system" : "http://snomed.info/sct",
              "code" : "711041003",
              "display" : "Assessment of skin integrity"
            }
          ]
        }
      },
      {
        "id" : "Observation.value[x]",
        "path" : "Observation.value[x]",
        "type" : [
          {
            "code" : "CodeableConcept"
          }
        ]
      },
      {
        "id" : "Observation.bodySite",
        "path" : "Observation.bodySite",
        "mustSupport" : true
      }
    ]
  }
}

```
