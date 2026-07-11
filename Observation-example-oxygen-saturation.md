# example-oxygen-saturation - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **example-oxygen-saturation**

## Example Observation: example-oxygen-saturation

Profile: [Oxygen Saturation](StructureDefinition-onc-oxygen-saturation.md)

**status**: Final

**category**: Survey

**code**: Oxygen saturation in Arterial blood by Pulse oximetry

**subject**: [Jane Doe Female, DoB Unknown](Patient-patient-example-jane.md)

**effective**: 2025-03-15 10:00:00+0000

**performer**: [Practitioner Nightingale ](Practitioner-practitioner-example.md)

**value**: 94 % (Details: UCUM code% = '%')



## Resource Content

```json
{
  "resourceType" : "Observation",
  "id" : "example-oxygen-saturation",
  "meta" : {
    "profile" : ["https://opennursingcoreig.com/StructureDefinition/onc-oxygen-saturation"]
  },
  "status" : "final",
  "category" : [{
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/observation-category",
      "code" : "survey"
    }]
  }],
  "code" : {
    "coding" : [{
      "system" : "http://loinc.org",
      "code" : "59408-5",
      "display" : "Oxygen saturation in Arterial blood by Pulse oximetry"
    }]
  },
  "subject" : {
    "reference" : "Patient/patient-example-jane"
  },
  "effectiveDateTime" : "2025-03-15T10:00:00Z",
  "performer" : [{
    "reference" : "Practitioner/practitioner-example"
  }],
  "valueQuantity" : {
    "value" : 94,
    "unit" : "%",
    "system" : "http://unitsofmeasure.org",
    "code" : "%"
  }
}

```
