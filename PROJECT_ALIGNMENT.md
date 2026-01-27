# Project Alignment Verification: UK Nursing Data Strategy

## Executive Summary
This document verifies the technical alignment of the **Open Nursing Core (ONC) Implementation Guide** with the key pillars of the UK Nursing Data Strategy. It demonstrates how the "Wicked Problem" of unstructured data is addressed through specific FHIR artifacts, ensuring that nursing care is visible, interoperable, and computable.

---

## 1. Addressing the "Wicked Problem" (Standardization)
**The Challenge:** Nursing documentation is historically unstructured narrative, making it invisible to "Big Data" analytics.
**The ONC Solution:** We have implemented the **Relational Care Logical Model** to strictly define *what* must be collected, separate from *how* it is stored.

*   **Artifact:** `input/fsh/onc-logical-models.fsh`
*   **Verification:** The model enforces structured capture of "soft" metrics like `empathyIndex` (Code: ONC-EMPATHY) and `patientPreferences`, making relational care computable for the first time.

---

## 2. The PRSB Nursing Care Needs Standard (Interoperability)
**The Challenge:** Fragmented care due to lack of interoperability between hospital and community systems.
**The ONC Solution:** We have fully implemented the **PRSB Nursing Care Needs Standard v1.0** as a set of FHIR Profiles. This ensures that a "Mobility Assessment" in the hospital uses the exact same structure as one in the community.

*   **Artifact:** `input/fsh/onc-alignment-prsb.fsh`
*   **Coverage:** 
    *   **Elimination**: Bladder & Bowel Assessment
    *   **Nutrition**: Oral Intake, Swallowing, Dietary Needs
    *   **Mobility**: Mobility Assessment, Device Use
    *   **Hygiene**: Personal Hygiene, Dressing Assessment
    *   **Skin**: Skin Integrity Assessment, Pressure Ulcer Risk
    *   **Medication**: Ability to Manage, Self-Administration

---

## 3. SNOMED CT Compliance (Computability)
**The Challenge:** The "Reality Gap" where 62% of trusts are non-compliant due to the complexity of SNOMED CT.
**The ONC Solution:** We have embedded **SNOMED CT** directly into the profiles ("baking it in"). The nurse selects a simple concept (e.g., "Assistance with dressing"), and the system automatically records the complex SNOMED code.

*   **Artifact:** `input/fsh/onc-alignment-prsb.fsh` & `onc-terminology.fsh`
*   **Key Mappings:**
    *   **Dressing**: `165235000` |Ability to dress (observable entity)|
    *   **Skin**: `711041003` |Assessment of skin integrity (procedure)|
    *   **Continence**: `417476007` |Bowel continence assessment (procedure)|
    *   **Medication**: `285033005` |Manage medication (finding)|

---

## 4. Visibility of "Needs and Strengths"
**The Challenge:** Moving away from a deficit model to identifying what a person *can* do.
**The ONC Solution:** We established a clear Framework for **Needs** and **Strengths**.
*   **ONCNursingNeed (Condition)**: Formalizes the care need (e.g., "Difficulty dressing").
*   **ONCNursingStrength (Observation)**: Formalizes the patient's capability (e.g., "Highly motivated").

---

## Conclusion
The Open Nursing Core IG is now **Strategy-Ready**. It does not just "support" the UK Nursing Data Strategy; it is a **technical instantiation** of it. By solving the usability gap of SNOMED CT through pre-coordination and AI enablement (NurseEmbed), ONC offers a viable path to the "Unified Vision" of nursing documentation.
