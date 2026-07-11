# Publication & distribution

Files that control how the Open Nursing Core IG is published and distributed.

| File | Purpose |
|------|---------|
| `package-list.json` | Version history consumed by the IG Publisher (copied to the site root). |
| `package-feed.xml` | **FHIR package feed** (RSS 2.0) — the input the HL7 FHIR package-registry crawler reads to publish `onc.ig` on [packages.fhir.org](https://packages.fhir.org). Copied to the site root by `docs.yml`. |

## Making `onc.ig` resolvable on packages.fhir.org

FHIR tooling and Open Health Stack builds resolve dependencies from
`packages.fhir.org`, which is populated by a crawler over registered publisher
feeds. Three things are required:

1. **A live package feed** — `package-feed.xml`, published at
   `https://opennursingcoreig.com/package-feed.xml` (this repo, via `docs.yml`). ✅
2. **Feed registered** in `package-feeds.json` in the HL7
   [`FHIR/ig-registry`](https://github.com/FHIR/ig-registry) repo.
3. **IG registered** in `fhir-ig-list.json` in the same repo.

Steps 2–3 are a one-time pull request to an external HL7 repo. The exact
entries to add are prepared in `publication/ig-registry-entries/` (see that
folder's README).

### Per-release checklist

When cutting a new IG version:

- [ ] Add a new `<item>` to `package-feed.xml` (newest first) with the version,
      `package.tgz` URL and an RFC-822 `pubDate`; update `<lastBuildDate>`.
- [ ] Add the edition to `package-list.json`.
- [ ] After the registry PR lands, no further registry action is needed — the
      crawler picks up new feed items automatically.

## Secondary distribution

`.github/workflows/publish-package.yml` also publishes the package to **GitHub
Packages** (npm) under `@clinical-quality-artifical-intelligence`. This is a
convenience mirror; the FHIR-native channel above is the one FHIR tooling uses.
