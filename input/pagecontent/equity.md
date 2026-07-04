# Health Equity & Inclusion

Health equity is a design requirement of the Open Nursing Core IG, not an optional module. Nursing assessment tools that were validated on predominantly light-skinned populations, or that assume a single cultural norm, can systematically under-serve the people most at risk of harm. This IG builds explicit countermeasures into its data models so that inequity becomes visible — and therefore addressable — in the record itself.

## Skin tone assessment: leading with the Monk Scale

Accurate skin tone assessment is a patient-safety issue. Several conditions central to nursing — **pressure ulcers, cyanosis, jaundice, pallor and erythema** — present differently across skin tones. Early pressure-damage signs described as "redness" or "blanching" are unreliable on brown and black skin, and reliance on those descriptors is a recognised cause of delayed detection and worse outcomes for people with darker skin.

### The Monk Skin Tone Scale (primary)

The IG's primary skin-tone vocabulary is the **[Monk Skin Tone Scale](CodeSystem-onc-monk-scale.html)** — a 10-point scale (A–J) developed to represent the full range of human skin tone with far greater granularity at the darker end of the range than older classifications provide.

| Code | Description |
|------|-------------|
| A | Light skin |
| B | Light-medium skin |
| C | Medium skin |
| D | Medium-dark skin |
| E | Dark skin |
| F | Deep dark skin |
| G | Very dark skin |
| H | Deepest dark skin |
| I | Ultra dark skin |
| J | Black skin |

This scale is bound by the **[Monk Skin Tone Observation](StructureDefinition-onc-monk-skintone-observation.html)** profile and the **[Monk Skin Tone Scale ValueSet](ValueSet-onc-monk-scale-vs.html)**. It is the recommended default for any skin, wound or tissue-viability assessment.

### Fitzpatrick classification (secondary)

The **[Skin Tone Observation](StructureDefinition-onc-skintone-observation.html)** profile records the older **Fitzpatrick** phototypes (I–VI). Fitzpatrick was designed to describe *sun sensitivity*, not clinical skin tone, and it collapses the darker end of the range into only two categories. It is retained in the IG for backward compatibility and interoperability with systems that already use it, but it **should not** be used as the sole basis for skin-tone-aware clinical decisions.

> **Implementation guidance.** Where a system can support only one scale, implementers **SHOULD** adopt the Monk Scale. Where both are recorded, the Monk observation is the authoritative one for equity-sensitive decision support.

### The fairness gate

The IG treats skin tone as a mandatory input to wound and pressure-area assessment rather than an optional demographic field. This "fairness gate" approach means a tissue-viability assessment is considered incomplete until the person's skin tone has been recorded on an appropriate scale, ensuring that no patient's risk is assessed against a threshold that was never calibrated for their skin.

## Reasonable adjustments under the Equality Act 2010

The **Equality Act 2010** places a legal duty on health services to make *reasonable adjustments* for disabled people so that they are not disadvantaged in accessing care. Recording those adjustments in structured, retrievable form — rather than in free-text notes that are easily missed — is essential to meeting that duty in practice.

The **[Reasonable Adjustment](StructureDefinition-onc-reasonable-adjustment.html)** profile captures a specific, actionable adjustment requirement, for example:

- "Requires a British Sign Language interpreter"
- "Cannot use stairs — ground-floor appointments only"
- "Requires large-print correspondence"
- "Needs a longer appointment slot and a quiet waiting area"

Each adjustment is stored as a discrete, machine-readable requirement so that it can be surfaced at every subsequent encounter. This aligns with the NHS commitment to a digital flag for reasonable adjustments and supports continuity of accessible care across services.

## Ethnicity and cultural context

Equitable care also depends on recording the person's ethnicity accurately and consistently. The **[ONC NHS Patient](StructureDefinition-onc-nhs-patient.html)** profile carries the **[UK Core Ethnic Category](StructureDefinition-UKCore-Extension-EthnicCategory.html)** extension, enabling ethnicity to be recorded using nationally agreed categories. Ethnicity data supports population-level monitoring of health inequalities and should always be collected with the person's involvement, never inferred.

## Why this matters

Documenting skin tone, reasonable adjustments and ethnicity in structured fields turns equity from an aspiration into something that can be measured, audited and acted upon. It allows a service to answer questions it otherwise could not — for example, whether pressure-ulcer detection rates differ across skin tones, or whether recorded reasonable adjustments are actually honoured at the next appointment. Making inequity visible in the data is the first step to closing it.

---

*Equity features in this IG support, but do not replace, professional and organisational duties under the Equality Act 2010 and NHS accessible-information and health-inequalities policy. Clinical decisions remain the responsibility of the registered nurse and the wider care team.*
