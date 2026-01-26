# example-medication-ability - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-medication-ability**

## Example Observation: example-medication-ability

Profile: [Medication Management Ability](StructureDefinition-onc-medication-ability.md)

**status**: Final

**category**: Survey

**code**: Medication Management Ability

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**effective**: 2025-03-15 10:00:00+0000

**performer**: [Practitioner Nightingale ](Practitioner-practitioner-example.md)

**value**: Able to manage own medications with dosette box



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-medication-ability",
  "meta" : {
    "profile" : [
      "https://opennursingcoreig.com/StructureDefinition/onc-medication-ability"
    ]
  },
  "status" : "final",
  "category" : [
    {
      "coding" : [
        {
          "system" : "http://terminology.hl7.org/CodeSystem/observation-category",
          "code" : "survey"
        }
      ]
    }
  ],
  "code" : {
    "coding" : [
      {
        "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
        "code" : "medication-ability"
      }
    ]
  },
  "subject" : {
    "reference" : "Patient/patient-example-jane"
  },
  "effectiveDateTime" : "2025-03-15T10:00:00Z",
  "performer" : [
    {
      "reference" : "Practitioner/practitioner-example"
    }
  ],
  "valueCodeableConcept" : {
    "text" : "Able to manage own medications with dosette box"
  }
}

```
