# Continence Assessment - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Continence Assessment**

## Resource Profile: Continence Assessment 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/StructureDefinition/onc-continence-assessment | *Version*:1.0.0 |
| Active as of 2026-07-11 | *Computable Name*:ONCContinenceAssessment |

 
Assessment of bladder and bowel control status. 

**Usages:**

* Examples for this Profile: [Observation/example-continence-assessment](Observation-example-continence-assessment.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/onc.ig|current/StructureDefinition/StructureDefinition-onc-continence-assessment.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-continence-assessment.csv), [Excel](StructureDefinition-onc-continence-assessment.xlsx), [Schematron](StructureDefinition-onc-continence-assessment.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-continence-assessment",
  "url" : "https://opennursingcoreig.com/StructureDefinition/onc-continence-assessment",
  "version" : "1.0.0",
  "name" : "ONCContinenceAssessment",
  "title" : "Continence Assessment",
  "status" : "active",
  "date" : "2026-07-11T09:46:48+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "Assessment of bladder and bowel control status.",
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
      "id" : "Observation.code",
      "path" : "Observation.code",
      "patternCodeableConcept" : {
        "coding" : [{
          "system" : "http://snomed.info/sct",
          "code" : "417476007",
          "display" : "Bowel continence assessment"
        }]
      }
    },
    {
      "id" : "Observation.value[x]",
      "path" : "Observation.value[x]",
      "type" : [{
        "code" : "CodeableConcept"
      }],
      "binding" : {
        "strength" : "example",
        "valueSet" : "http://hl7.org/fhir/ValueSet/consistency-type"
      }
    }]
  }
}

```
