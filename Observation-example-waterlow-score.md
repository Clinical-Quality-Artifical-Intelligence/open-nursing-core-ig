# example-waterlow-score - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-waterlow-score**

## Example Observation: example-waterlow-score

Profile: [Waterlow Score](StructureDefinition-onc-waterlow-score.md)

**status**: Final

**category**: Survey

**code**: Waterlow Score

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**effective**: 2025-03-15 10:00:00+0000

**performer**: [Practitioner Nightingale ](Practitioner-practitioner-example.md)

**value**: 12 {score}

**hasMember**: [Observation Skin type [Fitzpatrick Classification Scale]](Observation-observation-skin-tone.md)



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-waterlow-score",
  "meta" : {
    "profile" : [
      "https://opennursingcoreig.com/StructureDefinition/onc-waterlow-score"
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
        "code" : "waterlow-score",
        "display" : "Waterlow Score"
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
    "value" : 12,
    "unit" : "{score}"
  },
  "hasMember" : [
    {
      "reference" : "Observation/observation-skin-tone"
    }
  ]
}

```
