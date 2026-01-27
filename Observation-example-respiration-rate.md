# example-respiration-rate - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-respiration-rate**

## Example Observation: example-respiration-rate

Profile: [Respiration Rate](StructureDefinition-onc-respiration-rate.md)

**status**: Final

**category**: Survey

**code**: Respiratory rate

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**effective**: 2025-03-15 10:00:00+0000

**performer**: [Practitioner Nightingale ](Practitioner-practitioner-example.md)

**value**: 22 /min



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-respiration-rate",
  "meta" : {
    "profile" : [
      "https://opennursingcoreig.com/StructureDefinition/onc-respiration-rate"
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
        "code" : "9279-1",
        "display" : "Respiratory rate"
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
    "value" : 22,
    "unit" : "/min"
  }
}

```
