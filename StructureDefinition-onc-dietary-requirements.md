# Dietary Requirements - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Dietary Requirements**

## Resource Profile: Dietary Requirements 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/StructureDefinition/onc-dietary-requirements | *Version*:1.0.0 |
| Active as of 2026-07-11 | *Computable Name*:ONCDietaryRequirements |

 
Documentation of specific dietary needs (e.g. textural modification, cultural). 

**Usages:**

* Examples for this Profile: [Observation/example-dietary-requirements](Observation-example-dietary-requirements.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/onc.ig|current/StructureDefinition/StructureDefinition-onc-dietary-requirements.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-dietary-requirements.csv), [Excel](StructureDefinition-onc-dietary-requirements.xlsx), [Schematron](StructureDefinition-onc-dietary-requirements.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-dietary-requirements",
  "url" : "https://opennursingcoreig.com/StructureDefinition/onc-dietary-requirements",
  "version" : "1.0.0",
  "name" : "ONCDietaryRequirements",
  "title" : "Dietary Requirements",
  "status" : "active",
  "date" : "2026-07-11T14:17:07+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "Documentation of specific dietary needs (e.g. textural modification, cultural).",
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
          "code" : "116336009",
          "display" : "Eating / feeding / drinking finding"
        }]
      }
    },
    {
      "id" : "Observation.value[x]",
      "path" : "Observation.value[x]",
      "type" : [{
        "code" : "CodeableConcept"
      },
      {
        "code" : "string"
      }]
    }]
  }
}

```
