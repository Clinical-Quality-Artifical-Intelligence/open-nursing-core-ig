# example-bowel-assessment - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-bowel-assessment**

## Example Observation: example-bowel-assessment

Profile: [Bowel Assessment](StructureDefinition-onc-bowel-assessment.md)

**status**: Final

**category**: Survey

**code**: Bowel assessment

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**effective**: 2025-03-15 10:00:00+0000

**performer**: [Practitioner Nightingale ](Practitioner-practitioner-example.md)

**value**: Daily empty, no strain



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-bowel-assessment",
  "meta" : {
    "profile" : ["https://opennursingcoreig.com/StructureDefinition/onc-bowel-assessment"]
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
      "code" : "268389004",
      "display" : "Bowel assessment"
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
    "text" : "Daily empty, no strain"
  }
}

```
