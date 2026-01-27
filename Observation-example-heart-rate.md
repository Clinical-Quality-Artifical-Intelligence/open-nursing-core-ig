# example-heart-rate - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-heart-rate**

## Example Observation: example-heart-rate

Profile: [Heart Rate](StructureDefinition-onc-heart-rate.md)

**status**: Final

**category**: Survey

**code**: Heart rate

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**effective**: 2025-03-15 10:00:00+0000

**performer**: [Practitioner Nightingale ](Practitioner-practitioner-example.md)

**value**: 95 /min



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-heart-rate",
  "meta" : {
    "profile" : [
      "https://opennursingcoreig.com/StructureDefinition/onc-heart-rate"
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
        "code" : "8867-4",
        "display" : "Heart rate"
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
    "value" : 95,
    "unit" : "/min"
  }
}

```
