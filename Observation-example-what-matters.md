# example-what-matters - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-what-matters**

## Example Observation: example-what-matters

Profile: [What Matters to Me](StructureDefinition-onc-what-matters.md)

**status**: Final

**category**: Social History

**code**: What Matters to Me

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**effective**: 2026-01-15 10:00:00+0000

**performer**: [Practitioner Nightingale ](Practitioner-practitioner-example.md)

**value**: Being able to walk her dog (Buster) daily.

**note**: 

> 

This is her primary motivation for physiotherapy.




## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-what-matters",
  "meta" : {
    "profile" : ["https://opennursingcoreig.com/StructureDefinition/onc-what-matters"]
  },
  "status" : "final",
  "category" : [{
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/observation-category",
      "code" : "social-history"
    }]
  }],
  "code" : {
    "coding" : [{
      "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
      "code" : "what-matters"
    }]
  },
  "subject" : {
    "reference" : "Patient/patient-example-jane"
  },
  "effectiveDateTime" : "2026-01-15T10:00:00Z",
  "performer" : [{
    "reference" : "Practitioner/practitioner-example"
  }],
  "valueString" : "Being able to walk her dog (Buster) daily.",
  "note" : [{
    "text" : "This is her primary motivation for physiotherapy."
  }]
}

```
