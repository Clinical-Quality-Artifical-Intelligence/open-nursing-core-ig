# example-mental-capacity - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-mental-capacity**

## Example Observation: example-mental-capacity

Profile: [Mental Capacity Assessment](StructureDefinition-onc-mental-capacity.md)

**status**: Final

**category**: Survey

**code**: Mental Capacity Assessment

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**effective**: 2026-01-15 10:00:00+0000

**performer**: [Practitioner Nightingale ](Practitioner-practitioner-example.md)

**value**: Capacity Present

**note**: 

> 

Assessment for decision to return home.




## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-mental-capacity",
  "meta" : {
    "profile" : ["https://opennursingcoreig.com/StructureDefinition/onc-mental-capacity"]
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
      "code" : "mca-assessment"
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
      "code" : "mca-present",
      "display" : "Capacity Present"
    }]
  },
  "note" : [{
    "text" : "Assessment for decision to return home."
  }]
}

```
