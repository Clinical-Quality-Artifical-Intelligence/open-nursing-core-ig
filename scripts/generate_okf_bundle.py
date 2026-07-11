#!/usr/bin/env python3
"""
Generate an Open Knowledge Format (OKF) bundle from the compiled ONC-IG.

OKF (https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf)
is a vendor-neutral, agent-readable knowledge format: directories of markdown
concept documents with YAML frontmatter, cross-linked into a graph. This
producer walks the SUSHI build output (fsh-generated/resources) plus the
static resources in input/resources and emits okf/ so any AI agent - not only
FHIR tooling - can consume the ONC standard natively.

Usage:
    npx fsh-sushi .                      # ensure fresh build output
    python3 scripts/generate_okf_bundle.py

The bundle is committed to the repo; re-run this script after profile changes.
Hand-authored concepts (okf/metrics/) are preserved - only generated
directories are rewritten.
"""
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GEN = ROOT / "fsh-generated" / "resources"
STATIC = ROOT / "input" / "resources"
OUT = ROOT / "okf"
CANONICAL = "https://opennursingcoreig.com"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

GENERATED_DIRS = ["profiles", "extensions", "logical-models", "valuesets",
                  "codesystems", "questionnaires", "conceptmaps", "libraries"]

MAX_TABLE_ROWS = 30


def esc(s):
    """Make a value safe for single-line YAML frontmatter."""
    s = (s or "").replace("\n", " ").replace('"', "'").strip()
    return s[:500]


def md_escape(s):
    return (s or "").replace("|", "\\|").replace("\n", " ").strip()


def frontmatter(type_, title, description, resource, tags):
    lines = ["---",
             f'type: "{esc(type_)}"',
             f'title: "{esc(title)}"',
             f'description: "{esc(description)}"',
             f'resource: "{resource}"',
             f"tags: [{', '.join(tags)}]",
             f"timestamp: {NOW}",
             "---", ""]
    return "\n".join(lines)


def local_link(url, registry):
    """Return a relative markdown link if the canonical URL is an ONC artifact."""
    return registry.get(url)


def load_resources():
    resources = []
    for d in (GEN, STATIC):
        if not d.exists():
            continue
        for f in sorted(d.glob("*.json")):
            if f.name.startswith("._"):
                continue
            try:
                r = json.loads(f.read_text())
            except (json.JSONDecodeError, UnicodeDecodeError):
                continue
            if isinstance(r, dict) and r.get("resourceType"):
                resources.append(r)
    return resources


def classify(r):
    rt = r.get("resourceType")
    if rt == "StructureDefinition":
        if r.get("kind") == "logical":
            return "logical-models", "FHIR Logical Model"
        if r.get("type") == "Extension":
            return "extensions", "FHIR Extension"
        return "profiles", "FHIR Profile"
    return {
        "ValueSet": ("valuesets", "FHIR ValueSet"),
        "CodeSystem": ("codesystems", "FHIR CodeSystem"),
        "Questionnaire": ("questionnaires", "FHIR Questionnaire (SDC)"),
        "ConceptMap": ("conceptmaps", "FHIR ConceptMap"),
        "Library": ("libraries", "FHIR Library (CQL)"),
        "PlanDefinition": ("libraries", "FHIR PlanDefinition"),
    }.get(rt, (None, None))


def build_registry(resources):
    """canonical url -> repo-relative okf path, for cross-linking."""
    reg = {}
    for r in resources:
        d, _ = classify(r)
        if d and r.get("url"):
            reg[r["url"]] = f"/{d}/{r['id']}.md"
    return reg


def sd_body(r, reg):
    out = []
    base = r.get("baseDefinition", "")
    if base:
        link = local_link(base, reg)
        parent = f"[{base.split('/')[-1]}]({link})" if link else f"`{base}`"
        out.append(f"**Parent:** {parent}\n")
    elements = (r.get("differential") or {}).get("element", [])
    rows = []
    for e in elements[1:MAX_TABLE_ROWS + 1]:
        path = e.get("path", "")
        card = f"{e.get('min', '')}..{e.get('max', '')}" if "min" in e or "max" in e else ""
        types = ", ".join(t.get("code", "") for t in e.get("type", [])[:3])
        short = md_escape(e.get("short") or e.get("definition") or "")[:110]
        binding = e.get("binding", {}).get("valueSet", "")
        if binding:
            b = binding.split("|")[0]
            link = local_link(b, reg)
            short = (short + " " if short else "") + (
                f"(binds [{b.split('/')[-1]}]({link}))" if link else f"(binds `{b}`)")
        rows.append(f"| `{path}` | {card} | {types} | {short} |")
    if rows:
        out.append("# Key elements (differential)\n")
        out.append("| Path | Card. | Type | Notes |")
        out.append("|------|-------|------|-------|")
        out.extend(rows)
        if len(elements) - 1 > MAX_TABLE_ROWS:
            out.append(f"\n*…and {len(elements) - 1 - MAX_TABLE_ROWS} more elements — "
                       f"see the [full definition]({r.get('url', '')}).*")
    return "\n".join(out)


def vs_body(r, reg):
    out = ["# Composition\n"]
    for inc in (r.get("compose") or {}).get("include", []):
        sys = inc.get("system", "")
        link = local_link(sys, reg)
        label = f"[{sys.split('/')[-1]}]({link})" if link else f"`{sys}`"
        concepts = inc.get("concept", [])
        if concepts:
            codes = ", ".join(f"`{c.get('code')}`" for c in concepts[:15])
            out.append(f"- Codes from {label}: {codes}"
                       + (" …" if len(concepts) > 15 else ""))
        else:
            out.append(f"- All codes from {label}")
    return "\n".join(out)


def cs_body(r, reg):
    concepts = r.get("concept", [])
    out = [f"# Concepts ({len(concepts)})\n",
           "| Code | Display | Definition |", "|------|---------|------------|"]
    for c in concepts[:MAX_TABLE_ROWS]:
        out.append(f"| `{c.get('code')}` | {md_escape(c.get('display', ''))} "
                   f"| {md_escape(c.get('definition', ''))[:100]} |")
    if len(concepts) > MAX_TABLE_ROWS:
        out.append(f"\n*…and {len(concepts) - MAX_TABLE_ROWS} more concepts.*")
    return "\n".join(out)


def q_body(r, reg):
    out = ["# Items\n", "| linkId | Text | Type | Required |",
           "|--------|------|------|----------|"]
    for it in r.get("item", []):
        out.append(f"| `{it.get('linkId')}` | {md_escape(it.get('text', ''))[:90]} "
                   f"| {it.get('type')} | {'yes' if it.get('required') else ''} |")
    out.append("\nUses SDC observation-based extraction: coded items extract to "
               "Observations conforming to the ONC profiles; display/logic items "
               "carry no code and do not extract.")
    return "\n".join(out)


def generic_body(r, reg):
    return ""


BODY_BUILDERS = {"StructureDefinition": sd_body, "ValueSet": vs_body,
                 "CodeSystem": cs_body, "Questionnaire": q_body}


def write_concept(r, reg):
    d, type_ = classify(r)
    if not d:
        return None
    title = r.get("title") or r.get("name") or r["id"]
    desc = r.get("description", "")
    url = r.get("url") or f"{CANONICAL}/{r['resourceType']}/{r['id']}"
    tags = ["fhir", "nursing", d.rstrip("s")]
    body = BODY_BUILDERS.get(r["resourceType"], generic_body)(r, reg)
    doc = frontmatter(type_, title, desc, url, tags) + f"\n# {title}\n\n{desc}\n"
    if body:
        doc += "\n" + body + "\n"
    path = OUT / d / f"{r['id']}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(doc)
    return d, r["id"], title


def write_indexes(written):
    labels = {"profiles": "FHIR Profiles", "extensions": "Extensions",
              "logical-models": "Logical Models", "valuesets": "ValueSets",
              "codesystems": "CodeSystems", "questionnaires": "SDC Questionnaires",
              "conceptmaps": "ConceptMaps", "libraries": "Computable Logic (CQL / PlanDefinition)"}
    for d, items in sorted(written.items()):
        lines = [frontmatter("Index", labels.get(d, d),
                             f"Index of ONC-IG {labels.get(d, d)}",
                             f"{CANONICAL}/artifacts.html", ["fhir", "nursing", "index"]),
                 f"\n# {labels.get(d, d)}\n"]
        for rid, title in sorted(items):
            lines.append(f"- [{title}]({rid}.md)")
        (OUT / d / "index.md").write_text("\n".join(lines) + "\n")

    root = [frontmatter("Knowledge Base", "Open Nursing Core IG",
                        "Agent-readable knowledge bundle for the Open Nursing Core "
                        "FHIR Implementation Guide (trial-use, pre-ballot community release)",
                        CANONICAL, ["fhir", "nursing", "okf"]),
            "\n# Open Nursing Core — agent knowledge bundle\n",
            "Generated from the compiled IG (see `scripts/generate_okf_bundle.py`). "
            "Concepts link to each other, forming a navigable graph of the nursing "
            "process (ADPIE), its safety instruments and the equity layer.\n"]
    for d in sorted(written):
        root.append(f"- [{labels.get(d, d)}]({d}/index.md) ({len(written[d])})")
    if (OUT / "metrics" / "index.md").exists():
        root.append("- [Analytics Metrics](metrics/index.md) (hand-authored)")
    (OUT / "index.md").write_text("\n".join(root) + "\n")


def main():
    resources = load_resources()
    reg = build_registry(resources)
    # clear generated dirs only (preserve hand-authored okf/metrics, okf/README.md)
    for d in GENERATED_DIRS:
        p = OUT / d
        if p.exists():
            for f in p.glob("*.md"):
                f.unlink()
    written = {}
    for r in resources:
        res = write_concept(r, reg)
        if res:
            d, rid, title = res
            written.setdefault(d, []).append((rid, title))
    write_indexes(written)
    total = sum(len(v) for v in written.values())
    print(f"wrote {total} concept documents across {len(written)} directories -> {OUT}/")


if __name__ == "__main__":
    main()
