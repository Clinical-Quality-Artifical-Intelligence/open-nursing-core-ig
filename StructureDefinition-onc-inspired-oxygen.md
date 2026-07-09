# Inspired Oxygen - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Inspired Oxygen**

## Resource Profile: Inspired Oxygen 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/StructureDefinition/onc-inspired-oxygen | *Version*:1.0.0 |
| Active as of 2026-07-09 | *Computable Name*:ONCInspiredOxygen |

 
Inspired oxygen observation for NEWS2 (air vs supplemental oxygen) 

**Usages:**

* Examples for this Profile: [Observation/example-inspired-oxygen](Observation-example-inspired-oxygen.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/onc.ig|current/StructureDefinition/StructureDefinition-onc-inspired-oxygen.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-inspired-oxygen.csv), [Excel](StructureDefinition-onc-inspired-oxygen.xlsx), [Schematron](StructureDefinition-onc-inspired-oxygen.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-inspired-oxygen",
  "url" : "https://opennursingcoreig.com/StructureDefinition/onc-inspired-oxygen",
  "version" : "1.0.0",
  "name" : "ONCInspiredOxygen",
  "title" : "Inspired Oxygen",
  "status" : "active",
  "date" : "2026-07-09T22:05:12+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "Inspired oxygen observation for NEWS2 (air vs supplemental oxygen)",
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
          "system" : "http://loinc.org",
          "code" : "3151-8",
          "display" : "Inhaled oxygen flow rate"
        }]
      }
    },
    {
      "id" : "Observation.value[x]",
      "path" : "Observation.value[x]",
      "slicing" : {
        "discriminator" : [{
          "type" : "type",
          "path" : "$this"
        }],
        "ordered" : false,
        "rules" : "open"
      },
      "type" : [{
        "code" : "Quantity"
      },
      {
        "code" : "CodeableConcept"
      }]
    },
    {
      "id" : "Observation.value[x]:valueQuantity",
      "path" : "Observation.value[x]",
      "sliceName" : "valueQuantity",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "Quantity"
      }]
    },
    {
      "id" : "Observation.value[x]:valueQuantity.unit",
      "path" : "Observation.value[x].unit",
      "patternString" : "L/min"
    },
    {
      "id" : "Observation.value[x]:valueQuantity.system",
      "path" : "Observation.value[x].system",
      "patternUri" : "http://unitsofmeasure.org"
    },
    {
      "id" : "Observation.value[x]:valueCodeableConcept",
      "path" : "Observation.value[x]",
      "sliceName" : "valueCodeableConcept",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "CodeableConcept"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "https://opennursingcoreig.com/ValueSet/inspired-oxygen-vs"
      }
    }]
  }
}

```
