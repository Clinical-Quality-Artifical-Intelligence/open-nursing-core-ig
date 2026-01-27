# Example Skin Assessment - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Example Skin Assessment**

## Example Observation: Example Skin Assessment

Profile: [Skin Integrity Assessment](StructureDefinition-onc-skin-assessment.md)

**status**: Final

**category**: Survey

**code**: Assessment of skin integrity

**subject**: [Patient/example-patient](Patient/example-patient)

**performer**: [Practitioner/example-nurse](Practitioner/example-nurse)

**value**: Dry, papery skin with no breaks

**bodySite**: Left lower leg



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "ExampleSkinAssessment",
  "meta" : {
    "profile" : [
      "https://opennursingcoreig.com/StructureDefinition/onc-skin-assessment"
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
        "code" : "711041003",
        "display" : "Assessment of skin integrity"
      }
    ]
  },
  "subject" : {
    "reference" : "Patient/example-patient"
  },
  "performer" : [
    {
      "reference" : "Practitioner/example-nurse"
    }
  ],
  "valueCodeableConcept" : {
    "text" : "Dry, papery skin with no breaks"
  },
  "bodySite" : {
    "text" : "Left lower leg"
  }
}

```
