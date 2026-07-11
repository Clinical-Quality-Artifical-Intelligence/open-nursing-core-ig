# ONC Agent Knowledge Bundle (Open Knowledge Format)

This directory is an **[Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf)**
(OKF v0.1) bundle: markdown concept documents with YAML frontmatter,
cross-linked into a graph, so **any AI agent — not only FHIR tooling — can
consume the Open Nursing Core standard natively**. OKF is vendor-neutral
(plain markdown + files), so this bundle works with Google Cloud's Knowledge
Catalog, LLM agent frameworks, or a plain filesystem mount.

Start at [`index.md`](index.md).

## What's here

| Directory | Contents | Source |
|---|---|---|
| `profiles/`, `extensions/`, `logical-models/` | One concept per StructureDefinition, with parent links, key differential elements and value-set bindings | generated |
| `valuesets/`, `codesystems/` | Terminology with composition/concept tables | generated |
| `questionnaires/` | The SDC capture forms, item by item | generated |
| `conceptmaps/`, `libraries/` | NANDA-I mapping (placeholder-flagged), NEWS2 CQL + escalation PlanDefinition | generated |
| `metrics/` | **Hand-authored** analytics metric definitions (e.g. the equity late-detection rate) | curated |

## Regenerating

```bash
npx fsh-sushi .                          # fresh IG build output
python3 scripts/generate_okf_bundle.py   # rewrites generated dirs only
```

Hand-authored content (`metrics/`, this README) is preserved. Re-run after
any profile/terminology change and commit the diff.

## Status

Experimental: OKF is a v0.1 specification (July 2026). The bundle costs one
generator script over artifacts the IG already produces and stands alone as
readable documentation even if the format does not gain adoption. It is not
part of the IG's formal standards track (see `STANDARDS_ROADMAP.md`).
