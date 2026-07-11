# Example Device Use Statement - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Example Device Use Statement**

## Example DeviceUseStatement: Example Device Use Statement

Profile: [Device Use Statement](StructureDefinition-onc-device-use-statement.md)

**status**: Active

**subject**: [Pat Example Female, DoB: 1948-05-20](Patient-example-patient.md)

**timing**: 2026-01-15

**device**: [Device](Device-example-device.md)

**note**: 

> 

Uses frame for all transfers and walking beyond a few steps; reviewed by physiotherapy.




## Resource Content

```json
{
  "resourceType" : "DeviceUseStatement",
  "id" : "example-device-use",
  "meta" : {
    "profile" : ["https://opennursingcoreig.com/StructureDefinition/onc-device-use-statement"]
  },
  "status" : "active",
  "subject" : {
    "reference" : "Patient/example-patient"
  },
  "timingDateTime" : "2026-01-15",
  "device" : {
    "reference" : "Device/example-device"
  },
  "note" : [{
    "text" : "Uses frame for all transfers and walking beyond a few steps; reviewed by physiotherapy."
  }]
}

```
