# example-mobility-assessment - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-mobility-assessment**

## Example Observation: example-mobility-assessment

Profile: [Mobility Assessment](StructureDefinition-onc-mobility-assessment.md)

**status**: Final

**category**: Survey

**code**: Impaired mobility

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**effective**: 2025-03-15 10:00:00+0000

**performer**: [Practitioner Nightingale ](Practitioner-practitioner-example.md)

**value**: Mobilses with Zimmer frame

### Components

| | | |
| :--- | :--- | :--- |
| - | **Code** | **Value[x]** |
| * | ONC Empathy Index | Moderate Empathy |



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-mobility-assessment",
  "meta" : {
    "profile" : [
      "https://opennursingcoreig.com/StructureDefinition/onc-mobility-assessment"
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
        "system" : "http://snomed.info/sct",
        "code" : "82971005",
        "display" : "Impaired mobility"
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
    "text" : "Mobilses with Zimmer frame"
  },
  "component" : [
    {
      "code" : {
        "coding" : [
          {
            "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
            "code" : "empathy-index"
          }
        ]
      },
      "valueCodeableConcept" : {
        "coding" : [
          {
            "system" : "https://opennursingcoreig.com/CodeSystem/onc-observation-codes",
            "code" : "empathy-3",
            "display" : "Moderate Empathy"
          }
        ]
      }
    }
  ]
}

```
