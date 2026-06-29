# example-oral-intake - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-oral-intake**

## Example Observation: example-oral-intake

Profile: [Oral Intake Assessment](StructureDefinition-onc-oral-intake-assessment.md)

**status**: Final

**category**: Survey

**code**: Ability to drink

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**effective**: 2025-03-15 10:00:00+0000

**performer**: [Practitioner Nightingale ](Practitioner-practitioner-example.md)

**value**: Independent with cut-up food



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-oral-intake",
  "meta" : {
    "profile" : ["https://opennursingcoreig.com/StructureDefinition/onc-oral-intake-assessment"]
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
      "code" : "288852001",
      "display" : "Ability to drink"
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
    "text" : "Independent with cut-up food"
  }
}

```
