# example-bladder-assessment - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-bladder-assessment**

## Example Observation: example-bladder-assessment

Profile: [Bladder Assessment](StructureDefinition-onc-bladder-assessment.md)

**status**: Final

**category**: Survey

**code**: Assessment of urinary bladder

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**effective**: 2025-03-15 10:00:00+0000

**performer**: [Practitioner Nightingale ](Practitioner-practitioner-example.md)

**value**: Normal voiding pattern



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-bladder-assessment",
  "meta" : {
    "profile" : ["https://opennursingcoreig.com/StructureDefinition/onc-bladder-assessment"]
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
      "code" : "268390008",
      "display" : "Assessment of urinary bladder"
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
    "text" : "Normal voiding pattern"
  }
}

```
