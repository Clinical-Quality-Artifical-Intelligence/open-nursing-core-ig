# example-oral-care-assessment - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-oral-care-assessment**

## Example Observation: example-oral-care-assessment

Profile: [Oral Care Needs Assessment](StructureDefinition-onc-oral-care-assessment.md)

**status**: Final

**category**: Survey

**code**: Initial oral examination

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**effective**: 2025-03-15 10:00:00+0000

**performer**: [Practitioner Nightingale ](Practitioner-practitioner-example.md)

**value**: Requires assistance with denture cleaning

### Components

| | | |
| :--- | :--- | :--- |
| - | **Code** | **Value[x]** |
| * | ONC Empathy Index | Moderate Empathy |



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-oral-care-assessment",
  "meta" : {
    "profile" : ["https://opennursingcoreig.com/StructureDefinition/onc-oral-care-assessment"]
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
      "system" : "http://snomed.info/sct",
      "code" : "30175009",
      "display" : "Initial oral examination"
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
    "text" : "Requires assistance with denture cleaning"
  },
  "component" : [{
    "code" : {
      "coding" : [{
        "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
        "code" : "empathy-index"
      }]
    },
    "valueCodeableConcept" : {
      "coding" : [{
        "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
        "code" : "empathy-3",
        "display" : "Moderate Empathy"
      }]
    }
  }]
}

```
