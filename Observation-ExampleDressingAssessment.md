# Example Dressing Assessment - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Example Dressing Assessment**

## Example Observation: Example Dressing Assessment

Profile: [Dressing and Undressing Assessment](StructureDefinition-onc-dressing-assessment.md)

**status**: Final

**category**: Survey

**code**: Ability to dress

**subject**: [Pat Example Female, DoB: 1948-05-20](Patient-example-patient.md)

**effective**: 2026-01-15 10:00:00+0000

**performer**: [Practitioner Alex Nurse ](Practitioner-example-nurse.md)

**value**: Requires assistance with lower body dressing



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "ExampleDressingAssessment",
  "meta" : {
    "profile" : ["https://opennursingcoreig.com/StructureDefinition/onc-dressing-assessment"]
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
      "code" : "165235000",
      "display" : "Ability to dress"
    }]
  },
  "subject" : {
    "reference" : "Patient/example-patient"
  },
  "effectiveDateTime" : "2026-01-15T10:00:00Z",
  "performer" : [{
    "reference" : "Practitioner/example-nurse"
  }],
  "valueCodeableConcept" : {
    "text" : "Requires assistance with lower body dressing"
  }
}

```
