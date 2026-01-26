# example-medication-self-admin - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-medication-self-admin**

## Example Observation: example-medication-self-admin

Profile: [Medication Self-Administration Observation](StructureDefinition-onc-medication-self-admin.md)

**status**: Final

**category**: Survey

**code**: Medication Self-Administration

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**effective**: 2025-03-15 10:00:00+0000

**performer**: [Practitioner Nightingale ](Practitioner-practitioner-example.md)

**value**: Observed taking morning meds correctly



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-medication-self-admin",
  "meta" : {
    "profile" : [
      "https://opennursingcoreig.com/StructureDefinition/onc-medication-self-admin"
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
        "code" : "medication-self-admin"
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
    "text" : "Observed taking morning meds correctly"
  }
}

```
