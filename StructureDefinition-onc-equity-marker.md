# ONC Equity Marker - Open Nursing Core FHIR Implementation Guide (ONC-IG) v1.0.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **ONC Equity Marker**

## Extension: ONC Equity Marker 

| | |
| :--- | :--- |
| *Official URL*:https://opennursingcoreig.com/StructureDefinition/onc-equity-marker | *Version*:1.0.0 |
| Active as of 2026-07-09 | *Computable Name*:ONCEquityMarker |

A technical extension applied to observations that have passed the Mandatory Equity Gate (i.e., they are skin-tone aware).

**Context of Use**

**Usage info**

**Usages:**

* This Extension is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/onc.ig|current/StructureDefinition/StructureDefinition-onc-equity-marker.json)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-onc-equity-marker.csv), [Excel](StructureDefinition-onc-equity-marker.xlsx), [Schematron](StructureDefinition-onc-equity-marker.sch) 

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "onc-equity-marker",
  "url" : "https://opennursingcoreig.com/StructureDefinition/onc-equity-marker",
  "version" : "1.0.0",
  "name" : "ONCEquityMarker",
  "title" : "ONC Equity Marker",
  "status" : "active",
  "date" : "2026-07-09T22:05:12+00:00",
  "publisher" : "The Open Nursing Community",
  "description" : "A technical extension applied to observations that have passed the Mandatory Equity Gate (i.e., they are skin-tone aware).",
  "fhirVersion" : "4.0.1",
  "mapping" : [{
    "identity" : "rim",
    "uri" : "http://hl7.org/v3",
    "name" : "RIM Mapping"
  }],
  "kind" : "complex-type",
  "abstract" : false,
  "context" : [{
    "type" : "element",
    "expression" : "Element"
  }],
  "type" : "Extension",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Extension",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Extension",
      "path" : "Extension",
      "short" : "ONC Equity Marker",
      "definition" : "A technical extension applied to observations that have passed the Mandatory Equity Gate (i.e., they are skin-tone aware)."
    },
    {
      "id" : "Extension.extension",
      "path" : "Extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.url",
      "path" : "Extension.url",
      "fixedUri" : "https://opennursingcoreig.com/StructureDefinition/onc-equity-marker"
    },
    {
      "id" : "Extension.value[x]",
      "path" : "Extension.value[x]",
      "min" : 1,
      "type" : [{
        "code" : "boolean"
      }]
    }]
  }
}

```
