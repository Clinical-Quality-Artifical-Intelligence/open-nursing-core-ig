# example-hygiene-assessment - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-hygiene-assessment**

## Example Observation: example-hygiene-assessment

Profile: [Personal Hygiene Needs Assessment](StructureDefinition-onc-hygiene-assessment.md)

**status**: Final

**category**: Survey

**code**: Assessment of personal hygiene pattern

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**effective**: 2025-03-15 10:00:00+0000

**performer**: [Practitioner Nightingale ](Practitioner-practitioner-example.md)

**value**: Needs assistance washing lower legs and back

### Components

| | | |
| :--- | :--- | :--- |
| - | **Code** | **Value[x]** |
| * | ONC Empathy Index | High Empathy |



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-hygiene-assessment",
  "meta" : {
    "profile" : [
      "https://opennursingcoreig.com/StructureDefinition/onc-hygiene-assessment"
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
        "code" : "712552002",
        "display" : "Assessment of personal hygiene pattern"
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
    "text" : "Needs assistance washing lower legs and back"
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
            "code" : "empathy-4",
            "display" : "High Empathy"
          }
        ]
      }
    }
  ]
}

```
