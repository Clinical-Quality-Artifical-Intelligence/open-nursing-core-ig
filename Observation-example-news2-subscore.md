# Example NEWS2 Sub-score - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Example NEWS2 Sub-score**

## Example Observation: Example NEWS2 Sub-score

Profile: [NEWS2 Sub-Score](StructureDefinition-onc-news2-subscore.md)

**status**: Final

**category**: Survey

**code**: NEWS2 Sub-score

**subject**: [Pat Example Female, DoB: 1948-05-20](Patient-example-patient.md)

**effective**: 2026-01-15 08:00:00+0000

**performer**: [Practitioner Alex Nurse ](Practitioner-example-nurse.md)

**value**: 2 {score}



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-news2-subscore",
  "meta" : {
    "profile" : ["https://opennursingcoreig.com/StructureDefinition/onc-news2-subscore"]
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
      "code" : "news2-subscore",
      "display" : "NEWS2 Sub-score"
    }]
  },
  "subject" : {
    "reference" : "Patient/example-patient"
  },
  "effectiveDateTime" : "2026-01-15T08:00:00Z",
  "performer" : [{
    "reference" : "Practitioner/example-nurse"
  }],
  "valueQuantity" : {
    "value" : 2,
    "unit" : "{score}",
    "system" : "http://unitsofmeasure.org"
  }
}

```
