# Example Nursing Strength: Motivation - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Example Nursing Strength: Motivation**

## Example Observation: Example Nursing Strength: Motivation

Profile: [ONC Nursing Strength](StructureDefinition-onc-nursing-strength.md)

**status**: Final

**code**: Nursing Strengths

**subject**: [Patient/example-patient](Patient/example-patient)

**effective**: 2026-01-15 10:00:00+0000

**performer**: [Practitioner/example-nurse](Practitioner/example-nurse)

**value**: Highly motivated to maintain independence in upper body dressing.

**note**: 

> 

Patient explicitly stated desire to continue buttoning own shirt if given enough time.




## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "ExampleNursingStrength-Motivation",
  "meta" : {
    "profile" : ["https://opennursingcoreig.com/StructureDefinition/onc-nursing-strength"]
  },
  "status" : "final",
  "code" : {
    "coding" : [{
      "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
      "code" : "nursing-strengths"
    }]
  },
  "subject" : {
    "reference" : "Patient/example-patient"
  },
  "effectiveDateTime" : "2026-01-15T10:00:00Z",
  "performer" : [{
    "reference" : "Practitioner/example-nurse"
  }],
  "valueString" : "Highly motivated to maintain independence in upper body dressing.",
  "note" : [{
    "text" : "Patient explicitly stated desire to continue buttoning own shirt if given enough time."
  }]
}

```
