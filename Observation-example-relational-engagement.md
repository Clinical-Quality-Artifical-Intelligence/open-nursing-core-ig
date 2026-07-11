# Example Relational Engagement Score - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Example Relational Engagement Score**

## Example Observation: Example Relational Engagement Score

Profile: [Relational Engagement Score](StructureDefinition-onc-relational-observation.md)

**status**: Final

**code**: Relational Engagement Score

**subject**: [Pat Example Female, DoB: 1948-05-20](Patient-example-patient.md)

**effective**: 2026-01-16 15:00:00+0000

**value**: 4



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-relational-engagement",
  "meta" : {
    "profile" : ["https://opennursingcoreig.com/StructureDefinition/onc-relational-observation"]
  },
  "status" : "final",
  "code" : {
    "coding" : [{
      "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
      "code" : "relational-engagement"
    }]
  },
  "subject" : {
    "reference" : "Patient/example-patient"
  },
  "effectiveDateTime" : "2026-01-16T15:00:00Z",
  "valueInteger" : 4
}

```
