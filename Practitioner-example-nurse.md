# Example Nurse - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Example Nurse**

## Example Practitioner: Example Nurse

**name**: Alex Nurse 

### Qualifications

| | |
| :--- | :--- |
| - | **Code** |
| * | Registered Nurse (NMC) |



## Resource Content

```json
{
  "resourceType" : "Practitioner",
  "id" : "example-nurse",
  "name" : [{
    "family" : "Nurse",
    "given" : ["Alex"]
  }],
  "qualification" : [{
    "code" : {
      "text" : "Registered Nurse (NMC)"
    }
  }]
}

```
