# Example Barthel Index - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Example Barthel Index**

## Example Observation: Example Barthel Index

Profile: [Barthel Index](StructureDefinition-onc-barthel-index.md)

**status**: Final

**category**: Survey

**code**: Barthel Index Score

**subject**: [Pat Example Female, DoB: 1948-05-20](Patient-example-patient.md)

**effective**: 2026-01-15 10:00:00+0000

**performer**: [Practitioner Alex Nurse ](Practitioner-example-nurse.md)

**value**: 65 {score}



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-barthel-index",
  "meta" : {
    "profile" : ["https://opennursingcoreig.com/StructureDefinition/onc-barthel-index"]
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
      "code" : "barthel-score",
      "display" : "Barthel Index Score"
    }]
  },
  "subject" : {
    "reference" : "Patient/example-patient"
  },
  "effectiveDateTime" : "2026-01-15T10:00:00Z",
  "performer" : [{
    "reference" : "Practitioner/example-nurse"
  }],
  "valueQuantity" : {
    "value" : 65,
    "unit" : "{score}",
    "system" : "http://unitsofmeasure.org"
  }
}

```
