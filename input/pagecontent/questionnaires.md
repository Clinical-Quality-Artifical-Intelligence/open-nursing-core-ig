# Structured Data Capture

This IG ships **SDC (Structured Data Capture) Questionnaires** for its core nursing assessments, so ONC content can be rendered and captured directly by SDC-conformant form renderers — in particular the **Open Health Stack** data-capture libraries ([android-fhir](https://github.com/ohs-foundation/android-fhir) and [kotlin-fhir-data-capture](https://github.com/ohs-foundation/kotlin-fhir-data-capture)) used in offline-first deployments by Ministries of Health, NGOs and community services.

## Available questionnaires

| Questionnaire | Captures | Extracts toward |
|---|---|---|
| [NEWS2](Questionnaire-onc-news2-questionnaire.html) | All seven physiological parameters + total score | [NEWS2 Score](StructureDefinition-onc-news2-score.html) and the vital-sign profiles |
| [Monk Skin Tone](Questionnaire-onc-monk-skintone-questionnaire.html) | Skin tone on the 10-point Monk Scale (A–J) | [Monk Skin Tone Observation](StructureDefinition-onc-monk-skintone-observation.html) |
| [Braden Scale](Questionnaire-onc-braden-questionnaire.html) | Six subscales + total + **mandatory Monk skin tone** | [Braden Scale Assessment](StructureDefinition-onc-braden-scale-assessment.html) |
| [Waterlow Score](Questionnaire-onc-waterlow-questionnaire.html) | Total score + risk factors + **mandatory Monk skin tone** | [Waterlow Score](StructureDefinition-onc-waterlow-score.html) |
| [MUST](Questionnaire-onc-must-questionnaire.html) | Three step scores + total | [MUST Score](StructureDefinition-onc-must-score.html) |
| [Person-Centred Care](Questionnaire-onc-person-centred-questionnaire.html) | "What Matters to Me" + reasonable adjustments (repeating) | [What Matters to Me](StructureDefinition-onc-what-matters.html), [Reasonable Adjustment](StructureDefinition-onc-reasonable-adjustment.html) |

## How extraction works

The questionnaires use **[observation-based extraction](https://hl7.org/fhir/uv/sdc/extraction.html#observation-based-extraction)** (`sdc-questionnaire-observationExtract = true` at the questionnaire root):

- Every item that carries an `item.code` extracts to an `Observation` with that code. Display/guidance items and pure logic flags (e.g. the SpO2 Scale 2 toggle) carry no code and do not extract.
- Integer and decimal items carry the core `questionnaire-unit` extension, so extracted values become `valueQuantity` with the UCUM unit the ONC profiles require (e.g. `{score}` for assessment totals, `/min`, `%`, `Cel`, `mm[Hg]` for vital signs).
- Choice items (ACVPU, oxygen status, Monk skin tone) extract to `valueCodeableConcept`, with options drawn from the same value sets the profiles bind.

### Implementer responsibilities

Observation-based extraction produces **one Observation per coded item**. Three things remain the capturing application's responsibility:

1. **Category and performer.** Set `Observation.category` to `observation-category#survey` and populate `performer`, as required by the [ONC Nursing Assessment](StructureDefinition-onc-nursing-assessment.html) base profile.
2. **Composite assembly.** [Braden](StructureDefinition-onc-braden-scale-assessment.html) and [MUST](StructureDefinition-onc-must-score.html) define their subscales as `Observation.component` on a single resource. The questionnaires capture every component code, so assembling the composite Observation (or transforming via StructureMap) is mechanical.
3. **The equity gate.** Braden and Waterlow require a `hasMember` reference to a skin-tone Observation. Both questionnaires embed a **mandatory Monk Skin Tone item**, so the data is always captured in the same form response — the app links the extracted skin-tone Observation via `hasMember[skinTone]`.

## Equity by design, at the capture layer

The IG's [fairness gate](equity.html) — no pressure-area assessment without a skin-tone record — is enforced here **in the form itself**: the Braden and Waterlow questionnaires will not complete without a Monk Skin Tone Scale rating. This means the equity constraint holds even in offline settings before any server-side validation runs.

## Status

These questionnaires are published at **draft** status: they build and validate as part of this IG, and their extraction design has been verified against the target profiles, but they have not yet been demonstrated end-to-end in the Android FHIR SDK demo app. That verification step is tracked in [issue #125](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/issues/125) — implementers who render one of these forms are warmly invited to report results there.

---

*Forms support clinical judgement; they do not replace it. Score interpretation and escalation decisions remain the responsibility of a registered nurse or other competent clinician.*
