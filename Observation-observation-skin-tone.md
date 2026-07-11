# observation-skin-tone - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **observation-skin-tone**

## Example Observation: observation-skin-tone

Profile: [Skin Tone Observation (Fitzpatrick -- secondary/legacy)](StructureDefinition-onc-skintone-observation.md)

**status**: Final

**category**: Survey

**code**: Skin type [Fitzpatrick Classification Scale]

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**effective**: 2026-01-15 10:00:00+0000

**performer**: [Practitioner Nightingale ](Practitioner-practitioner-example.md)

**value**: Type II



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "observation-skin-tone",
  "meta" : {
    "profile" : ["https://opennursingcoreig.com/StructureDefinition/onc-skintone-observation"]
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
      "system" : "http://loinc.org",
      "code" : "66555-4"
    }]
  },
  "subject" : {
    "reference" : "Patient/patient-example-jane"
  },
  "effectiveDateTime" : "2026-01-15T10:00:00Z",
  "performer" : [{
    "reference" : "Practitioner/practitioner-example"
  }],
  "valueCodeableConcept" : {
    "coding" : [{
      "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
      "code" : "fitzpatrick-2",
      "display" : "Type II"
    }]
  }
}

```
