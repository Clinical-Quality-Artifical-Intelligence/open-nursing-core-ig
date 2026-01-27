# example-acvpu - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-acvpu**

## Example Observation: example-acvpu

Profile: [ACVPU Consciousness Level](StructureDefinition-onc-acvpu.md)

**status**: Final

**category**: Survey

**code**: ACVPU (Alert Confusion Voice Pain Unresponsive) scale score

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**effective**: 2025-03-15 10:00:00+0000

**performer**: [Practitioner Nightingale ](Practitioner-practitioner-example.md)

**value**: Mentally alert



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-acvpu",
  "meta" : {
    "profile" : [
      "https://opennursingcoreig.com/StructureDefinition/onc-acvpu"
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
        "code" : "1104441000000107",
        "display" : "ACVPU (Alert Confusion Voice Pain Unresponsive) scale score"
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
        "code" : "248234008",
        "display" : "Mentally alert"
      }
    ]
  }
}

```
