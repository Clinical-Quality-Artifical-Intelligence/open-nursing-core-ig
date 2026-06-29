# example-monk-skin-tone - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-monk-skin-tone**

## Example Observation: example-monk-skin-tone

Profile: [Monk Skin Tone Observation](StructureDefinition-onc-monk-skintone-observation.md)

**status**: Final

**category**: Survey

**code**: Monk Skin Tone Score

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**effective**: 2025-03-15 10:00:00+0000

**performer**: [Practitioner Nightingale ](Practitioner-practitioner-example.md)

**value**: Medium Skin



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-monk-skin-tone",
  "meta" : {
    "profile" : ["https://opennursingcoreig.com/StructureDefinition/onc-monk-skintone-observation"]
  },
  "status" : "final",
  "category" : [{
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/observation-category",
      "code" : "survey"
    }]
  }],
  "code" : {
    "coding" : [{
      "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
      "code" : "mst-score",
      "display" : "Monk Skin Tone Score"
    }]
  },
  "subject" : {
    "reference" : "Patient/patient-example-jane"
  },
  "effectiveDateTime" : "2025-03-15T10:00:00Z",
  "performer" : [{
    "reference" : "Practitioner/practitioner-example"
  }],
  "valueCodeableConcept" : {
    "coding" : [{
      "system" : "https://opennursingcoreig.com/CodeSystem/onc-monk-scale",
      "code" : "C",
      "display" : "Medium Skin"
    }]
  }
}

```
