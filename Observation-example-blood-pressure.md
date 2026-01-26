# example-blood-pressure - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-blood-pressure**

## Example Observation: example-blood-pressure

Profile: [Blood Pressure](StructureDefinition-onc-blood-pressure.md)

**status**: Final

**category**: Survey

**code**: Blood pressure panel with all children optional

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**effective**: 2025-03-15 10:00:00+0000

**performer**: [Practitioner Nightingale ](Practitioner-practitioner-example.md)

> **component****code**: Systolic blood pressure**value**: 110 mm[Hg]

> **component****code**: Diastolic blood pressure**value**: 70 mm[Hg]



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-blood-pressure",
  "meta" : {
    "profile" : [
      "https://opennursingcoreig.com/StructureDefinition/onc-blood-pressure"
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
        "system" : "http://loinc.org",
        "code" : "85354-9",
        "display" : "Blood pressure panel with all children optional"
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
  "component" : [
    {
      "code" : {
        "coding" : [
          {
            "system" : "http://loinc.org",
            "code" : "8480-6",
            "display" : "Systolic blood pressure"
          }
        ]
      },
      "valueQuantity" : {
        "value" : 110,
        "unit" : "mm[Hg]"
      }
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "http://loinc.org",
            "code" : "8462-4",
            "display" : "Diastolic blood pressure"
          }
        ]
      },
      "valueQuantity" : {
        "value" : 70,
        "unit" : "mm[Hg]"
      }
    }
  ]
}

```
