# example-news2-score - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-news2-score**

## Example Observation: example-news2-score

Profile: [NEWS2 Score](StructureDefinition-onc-news2-score.md)

**status**: Final

**category**: Survey

**code**: NEWS2 Score

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**effective**: 2025-03-15 10:00:00+0000

**performer**: [Practitioner Nightingale ](Practitioner-practitioner-example.md)

**value**: 5 {score}

**hasMember**: 

* [Observation Respiratory rate](Observation-example-respiration-rate.md)
* [Observation Oxygen saturation in Arterial blood by Pulse oximetry](Observation-example-oxygen-saturation.md)
* [Observation Inhaled oxygen flow rate](Observation-example-inspired-oxygen.md)
* [Observation Blood pressure panel with all children optional](Observation-example-blood-pressure.md)
* [Observation Heart rate](Observation-example-heart-rate.md)
* [Observation ACVPU (Alert Confusion Voice Pain Unresponsive) scale score](Observation-example-acvpu.md)
* [Observation Body temperature](Observation-example-temperature.md)



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-news2-score",
  "meta" : {
    "profile" : ["https://opennursingcoreig.com/StructureDefinition/onc-news2-score"]
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
      "code" : "news2-score",
      "display" : "NEWS2 Score"
    }]
  },
  "subject" : {
    "reference" : "Patient/patient-example-jane"
  },
  "effectiveDateTime" : "2025-03-15T10:00:00Z",
  "performer" : [{
    "reference" : "Practitioner/practitioner-example"
  }],
  "valueQuantity" : {
    "value" : 5,
    "unit" : "{score}"
  },
  "hasMember" : [{
    "reference" : "Observation/example-respiration-rate"
  },
  {
    "reference" : "Observation/example-oxygen-saturation"
  },
  {
    "reference" : "Observation/example-inspired-oxygen"
  },
  {
    "reference" : "Observation/example-blood-pressure"
  },
  {
    "reference" : "Observation/example-heart-rate"
  },
  {
    "reference" : "Observation/example-acvpu"
  },
  {
    "reference" : "Observation/example-temperature"
  }]
}

```
