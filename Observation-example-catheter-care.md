# example-catheter-care - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-catheter-care**

## Example Observation: example-catheter-care

Profile: [Catheter Care](StructureDefinition-onc-catheter-care.md)

**status**: Final

**category**: Survey

**code**: Care of central line

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**effective**: 2025-03-15 10:00:00+0000

**performer**: [Practitioner Nightingale ](Practitioner-practitioner-example.md)

**value**: Catheter changed, patent, clear urine draining.



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-catheter-care",
  "meta" : {
    "profile" : [
      "https://opennursingcoreig.com/StructureDefinition/onc-catheter-care"
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
        "code" : "226005007",
        "display" : "Care of central line"
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
  "valueString" : "Catheter changed, patent, clear urine draining."
}

```
