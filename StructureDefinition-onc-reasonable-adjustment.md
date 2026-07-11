# Reasonable Adjustment - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Reasonable Adjustment**

## Resource Profile: Reasonable Adjustment 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/StructureDefinition/onc-reasonable-adjustment | *Version*:1.0.0 |
| Active as of 2026-07-11 | *Computable Name*:ONCReasonableAdjustment |

 
Captures specific strict requirements for care adjustments under the Equality Act (e.g., 'Needs BSL Interpreter', 'Cannot use stairs', 'Requires large print'). 

**Usages:**

* Examples for this Profile: [Observation/example-reasonable-adjustment](Observation-example-reasonable-adjustment.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/onc.ig|current/StructureDefinition/StructureDefinition-onc-reasonable-adjustment.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-reasonable-adjustment.csv), [Excel](StructureDefinition-onc-reasonable-adjustment.xlsx), [Schematron](StructureDefinition-onc-reasonable-adjustment.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-reasonable-adjustment",
  "url" : "https://opennursingcoreig.com/StructureDefinition/onc-reasonable-adjustment",
  "version" : "1.0.0",
  "name" : "ONCReasonableAdjustment",
  "title" : "Reasonable Adjustment",
  "status" : "active",
  "date" : "2026-07-11T09:35:24+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "Captures specific strict requirements for care adjustments under the Equality Act (e.g., 'Needs BSL Interpreter', 'Cannot use stairs', 'Requires large print').",
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
          "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
          "code" : "reasonable-adjustment"
        }]
      }
    },
    {
      "id" : "Observation.value[x]",
      "path" : "Observation.value[x]",
      "short" : "Description of required adjustment",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Observation.note",
      "path" : "Observation.note",
      "max" : "1",
      "mustSupport" : true
    }]
  }
}

```
