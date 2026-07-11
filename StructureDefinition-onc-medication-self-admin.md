# Medication Self-Administration Observation - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Medication Self-Administration Observation**

## Resource Profile: Medication Self-Administration Observation 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/StructureDefinition/onc-medication-self-admin | *Version*:1.0.0 |
| Active as of 2026-07-11 | *Computable Name*:ONCMedicationSelfAdmin |

 
Observation of the patient performing self-administration. 

**Usages:**

* Examples for this Profile: [Observation/example-medication-self-admin](Observation-example-medication-self-admin.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/onc.ig|current/StructureDefinition/StructureDefinition-onc-medication-self-admin.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-medication-self-admin.csv), [Excel](StructureDefinition-onc-medication-self-admin.xlsx), [Schematron](StructureDefinition-onc-medication-self-admin.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-medication-self-admin",
  "url" : "https://opennursingcoreig.com/StructureDefinition/onc-medication-self-admin",
  "version" : "1.0.0",
  "name" : "ONCMedicationSelfAdmin",
  "title" : "Medication Self-Administration Observation",
  "status" : "active",
  "date" : "2026-07-11T18:02:47+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "Observation of the patient performing self-administration.",
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
          "code" : "225425006",
          "display" : "Self-administration of medication"
        }]
      }
    },
    {
      "id" : "Observation.value[x]",
      "path" : "Observation.value[x]",
      "type" : [{
        "code" : "CodeableConcept"
      }]
    }]
  }
}

```
