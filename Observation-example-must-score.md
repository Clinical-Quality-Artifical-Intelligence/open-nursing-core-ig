# example-must-score - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-must-score**

## Example Observation: example-must-score

Profile: [MUST Score (Malnutrition Universal Screening Tool)](StructureDefinition-onc-must-score.md)

**status**: Final

**category**: Survey

**code**: MUST Score

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**effective**: 2025-03-15 10:00:00+0000

**performer**: [Practitioner Nightingale ](Practitioner-practitioner-example.md)

**value**: 1 {score}

> **component****code**: MUST BMI Score**value**: 0

> **component****code**: MUST Weight Loss Score**value**: 1

> **component****code**: MUST Acute Disease Score**value**: 0



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-must-score",
  "meta" : {
    "profile" : [
      "https://opennursingcoreig.com/StructureDefinition/onc-must-score"
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
        "code" : "must-score",
        "display" : "MUST Score"
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
  "valueQuantity" : {
    "value" : 1,
    "unit" : "{score}"
  },
  "component" : [
    {
      "code" : {
        "coding" : [
          {
            "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
            "code" : "must-bmi-score",
            "display" : "MUST BMI Score"
          }
        ]
      },
      "valueQuantity" : {
        "value" : 0
      }
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
            "code" : "must-weight-loss-score",
            "display" : "MUST Weight Loss Score"
          }
        ]
      },
      "valueQuantity" : {
        "value" : 1
      }
    },
    {
      "code" : {
        "coding" : [
          {
            "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
            "code" : "must-acute-disease-score",
            "display" : "MUST Acute Disease Score"
          }
        ]
      },
      "valueQuantity" : {
        "value" : 0
      }
    }
  ]
}

```
