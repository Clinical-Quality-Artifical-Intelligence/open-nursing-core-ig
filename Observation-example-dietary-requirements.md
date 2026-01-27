# example-dietary-requirements - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-dietary-requirements**

## Example Observation: example-dietary-requirements

Profile: [Dietary Requirements](StructureDefinition-onc-dietary-requirements.md)

**status**: Final

**category**: Survey

**code**: Eating / feeding / drinking finding

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**effective**: 2025-03-15 10:00:00+0000

**performer**: [Practitioner Nightingale ](Practitioner-practitioner-example.md)

**value**: Vegetarian diet required



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-dietary-requirements",
  "meta" : {
    "profile" : [
      "https://opennursingcoreig.com/StructureDefinition/onc-dietary-requirements"
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
        "code" : "116336009",
        "display" : "Eating / feeding / drinking finding"
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
  "valueString" : "Vegetarian diet required"
}

```
