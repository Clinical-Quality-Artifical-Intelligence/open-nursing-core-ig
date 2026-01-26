# example-inspired-oxygen - Open Nursing Core FHIR Implementation Guide (ONC-IG) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-inspired-oxygen**

## Example Observation: example-inspired-oxygen

Profile: [Inspired Oxygen](StructureDefinition-onc-inspired-oxygen.md)

**status**: Final

**category**: Survey

**code**: Inhaled oxygen flow rate

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**effective**: 2025-03-15 10:00:00+0000

**performer**: [Practitioner Nightingale ](Practitioner-practitioner-example.md)

**value**: Breathing room air



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-inspired-oxygen",
  "meta" : {
    "profile" : [
      "https://opennursingcoreig.com/StructureDefinition/onc-inspired-oxygen"
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
        "code" : "3151-8",
        "display" : "Inhaled oxygen flow rate"
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
    "coding" : [
      {
        "system" : "http://snomed.info/sct",
        "code" : "722742002",
        "display" : "Breathing room air"
      }
    ]
  }
}

```
