## Summary

<!-- What does this PR change? 2-3 sentences. -->

## Type of change

- [ ] 🩺 Clinical correction (fixes a clinical error or inaccuracy)
- [ ] 🧬 New FHIR profile or extension
- [ ] 📝 Documentation update
- [ ] 🐛 Bug fix (SUSHI / tooling / build)
- [ ] 🏛️ openEHR archetype alignment
- [ ] 🔧 Configuration / CI change

## Clinical review checklist

> *For any change touching FSH profiles or terminology bindings — skip if documentation-only.*

- [ ] Change is based on a validated clinical instrument or published guideline
- [ ] SNOMED CT / LOINC / UCUM codes have been verified
- [ ] The clinical disclaimer is present: *"This tool supports but does not replace clinical judgment."*
- [ ] Profile aligns with PRSB Standards of Proficiency (2018) where applicable
- [ ] Tested with `sushi .` — builds without errors

## FHIR technical checklist

- [ ] Profile compiles cleanly with SUSHI
- [ ] Examples are valid instances of the profile
- [ ] Terminology bindings use standard code systems
- [ ] No hardcoded canonical URLs (use `sushi-config.yaml` canonical)

## Linked issues

<!-- Closes #... -->

## Notes for reviewers

<!-- Anything specific you'd like clinical or technical reviewers to look at? -->
