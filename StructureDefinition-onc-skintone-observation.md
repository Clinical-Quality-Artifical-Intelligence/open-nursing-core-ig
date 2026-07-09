# Skin Tone Observation (Fitzpatrick -- secondary/legacy) - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Skin Tone Observation (Fitzpatrick -- secondary/legacy)**

## Resource Profile: Skin Tone Observation (Fitzpatrick -- secondary/legacy) 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/StructureDefinition/onc-skintone-observation | *Version*:1.0.0 |
| Active as of 2026-07-09 | *Computable Name*:ONCSkinToneObservation |

 
Observation of patient skin tone using the Fitzpatrick skin type classification. Fitzpatrick was designed to describe UV photosensitivity, not clinical skin tone, and compresses the darker end of the range into few categories. This profile is RETAINED FOR BACKWARD COMPATIBILITY with systems that already record Fitzpatrick phototypes; it is secondary to, and SHOULD NOT be used in place of, the Monk Skin Tone Scale (see ONCMonkSkinToneObservation), which is this IG's primary and recommended skin-tone vocabulary. 

**Usages:**

* Refer to this Profile: [Braden Scale Assessment](StructureDefinition-onc-braden-scale-assessment.md) and [Waterlow Score](StructureDefinition-onc-waterlow-score.md)
* Examples for this Profile: [Observation/observation-skin-tone](Observation-observation-skin-tone.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/onc.ig|current/StructureDefinition/StructureDefinition-onc-skintone-observation.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-skintone-observation.csv), [Excel](StructureDefinition-onc-skintone-observation.xlsx), [Schematron](StructureDefinition-onc-skintone-observation.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-skintone-observation",
  "url" : "https://opennursingcoreig.com/StructureDefinition/onc-skintone-observation",
  "version" : "1.0.0",
  "name" : "ONCSkinToneObservation",
  "title" : "Skin Tone Observation (Fitzpatrick -- secondary/legacy)",
  "status" : "active",
  "date" : "2026-07-09T22:28:17+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "Observation of patient skin tone using the Fitzpatrick skin type classification. Fitzpatrick was designed to describe UV photosensitivity, not clinical skin tone, and compresses the darker end of the range into few categories. This profile is RETAINED FOR BACKWARD COMPATIBILITY with systems that already record Fitzpatrick phototypes; it is secondary to, and SHOULD NOT be used in place of, the Monk Skin Tone Scale (see ONCMonkSkinToneObservation), which is this IG's primary and recommended skin-tone vocabulary.",
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
          "code" : "66555-4"
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
        "strength" : "required",
        "valueSet" : "https://opennursingcoreig.com/ValueSet/onc-skin-tone-vs"
      }
    }]
  }
}

```
