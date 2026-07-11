# Example Sleep Pattern - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Example Sleep Pattern**

## Example Observation: Example Sleep Pattern

Profile: [Sleep Pattern](StructureDefinition-onc-sleep-pattern.md)

**status**: Final

**category**: Survey

**code**: Sleep Record

**subject**: [Pat Example Female, DoB: 1948-05-20](Patient-example-patient.md)

**effective**: 2026-01-16 07:30:00+0000

**performer**: [Practitioner Alex Nurse ](Practitioner-example-nurse.md)

**value**: Approximately five hours' broken sleep; woke twice (pain, then noise). Settled after analgesia at 03:00. Reports feeling unrefreshed.



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-sleep-pattern",
  "meta" : {
    "profile" : ["https://opennursingcoreig.com/StructureDefinition/onc-sleep-pattern"]
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
      "code" : "sleep-record"
    }]
  },
  "subject" : {
    "reference" : "Patient/example-patient"
  },
  "effectiveDateTime" : "2026-01-16T07:30:00Z",
  "performer" : [{
    "reference" : "Practitioner/example-nurse"
  }],
  "valueString" : "Approximately five hours' broken sleep; woke twice (pain, then noise). Settled after analgesia at 03:00. Reports feeling unrefreshed."
}

```
