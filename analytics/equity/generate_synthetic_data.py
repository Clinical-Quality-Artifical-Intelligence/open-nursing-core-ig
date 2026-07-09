#!/usr/bin/env python3
"""
Synthetic FHIR data generator for the ONC equity analytics example.

Produces NDJSON files of Patient, Monk Skin Tone Observation and pressure-ulcer
Observation resources shaped like the ONC-IG profiles, with a DELIBERATELY
INJECTED detection-delay bias against darker Monk skin-tone bands, so the
analysis pipeline has a visible inequity to surface.

*** ALL DATA PRODUCED BY THIS SCRIPT IS SYNTHETIC. It contains no real
patients and must never be presented as clinical evidence. The injected bias
models a pattern reported in the literature (delayed pressure-damage detection
on darker skin when assessment relies on redness/blanching) purely so the
dashboard has something to demonstrate. ***

Usage:
    python3 generate_synthetic_data.py [--patients 600] [--bias 1.0] [--seed 42]
    --bias 0.0 generates the null (no-inequity) scenario.
"""
import argparse
import json
import random
from datetime import datetime, timedelta
from pathlib import Path

CANONICAL = "https://opennursingcoreig.com"
ONC_CODES = f"{CANONICAL}/CodeSystem/onc-observation-codes"
MONK_CS = f"{CANONICAL}/CodeSystem/onc-monk-scale"
SCT = "http://snomed.info/sct"

MONK_BANDS = list("ABCDEFGHIJ")

# ONC pressure-ulcer stage codes (onc-observation-codes) in detection order.
# Detection at stage 3+, unstageable or deep-tissue = "late detection".
STAGES = ["stage-1", "stage-2", "stage-3", "stage-4", "unstageable", "deep-tissue"]
LATE_STAGES = {"stage-3", "stage-4", "unstageable", "deep-tissue"}


def make_patient(pid: str, band: str) -> dict:
    return {
        "resourceType": "Patient",
        "id": pid,
        "meta": {"profile": [f"{CANONICAL}/StructureDefinition/onc-nhs-patient"]},
        "gender": random.choice(["male", "female"]),
        "birthDate": f"{random.randint(1935, 1985)}-01-01",
        # Band retained only for generator bookkeeping; analysis reads the
        # Monk Observation, exactly as it would against a real FHIR store.
        "extension": [{"url": f"{CANONICAL}/StructureDefinition/synthetic-monk-band",
                       "valueCode": band}],
    }


def make_monk_obs(oid: str, pid: str, band: str, when: datetime) -> dict:
    return {
        "resourceType": "Observation",
        "id": oid,
        "meta": {"profile": [f"{CANONICAL}/StructureDefinition/onc-monk-skintone-observation"]},
        "status": "final",
        "category": [{"coding": [{"system": "http://terminology.hl7.org/CodeSystem/observation-category",
                                  "code": "survey"}]}],
        "code": {"coding": [{"system": ONC_CODES, "code": "mst-score",
                             "display": "Monk Skin Tone Score"}]},
        "subject": {"reference": f"Patient/{pid}"},
        "performer": [{"reference": "Practitioner/synthetic-nurse"}],
        "effectiveDateTime": when.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "valueCodeableConcept": {"coding": [{"system": MONK_CS, "code": band}]},
    }


def make_ulcer_obs(oid: str, pid: str, monk_oid: str, stage: str,
                   detected: datetime) -> dict:
    return {
        "resourceType": "Observation",
        "id": oid,
        "meta": {"profile": [f"{CANONICAL}/StructureDefinition/onc-wound-assessment"]},
        "status": "final",
        "category": [{"coding": [{"system": "http://terminology.hl7.org/CodeSystem/observation-category",
                                  "code": "survey"}]}],
        "code": {"coding": [{"system": SCT, "code": "399912005", "display": "Pressure ulcer"}]},
        "subject": {"reference": f"Patient/{pid}"},
        "performer": [{"reference": "Practitioner/synthetic-nurse"}],
        "effectiveDateTime": detected.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "valueCodeableConcept": {"coding": [{"system": ONC_CODES, "code": stage}]},
        "hasMember": [{"reference": f"Observation/{monk_oid}"}],
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--patients", type=int, default=600)
    ap.add_argument("--bias", type=float, default=1.0,
                    help="Strength of the injected detection-delay bias (0 = none)")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--out", default="data")
    args = ap.parse_args()

    random.seed(args.seed)
    out = Path(__file__).parent / args.out
    out.mkdir(parents=True, exist_ok=True)

    base = datetime(2026, 1, 1, 8, 0, 0)
    patients, monks, ulcers = [], [], []

    for i in range(args.patients):
        pid = f"synth-{i:04d}"
        band = random.choice(MONK_BANDS)
        admitted = base + timedelta(days=random.randint(0, 120), hours=random.randint(0, 12))

        patients.append(make_patient(pid, band))
        monk_oid = f"mst-{i:04d}"
        monks.append(make_monk_obs(monk_oid, pid, band, admitted))

        # ~45% of synthetic patients develop pressure damage.
        if random.random() < 0.45:
            # Injected inequity: darker bands are detected later. band_idx/9 in
            # [0,1]; bias scales both the delay and odds of late-stage detection.
            band_idx = MONK_BANDS.index(band)
            darkness = band_idx / (len(MONK_BANDS) - 1)
            # Days from skin-tone assessment (baseline) to first documentation.
            delay = random.lognormvariate(1.1 + args.bias * 0.75 * darkness, 0.45)
            # Probability the first documentation is already a late stage.
            p_late = min(0.9, 0.12 + args.bias * 0.42 * darkness)
            if random.random() < p_late:
                stage = random.choice(sorted(LATE_STAGES))
            else:
                stage = random.choice(["stage-1", "stage-1", "stage-2"])
            detected = admitted + timedelta(days=delay)
            ulcers.append(make_ulcer_obs(f"pu-{i:04d}", pid, monk_oid, stage, detected))

    for name, rows in (("Patient.ndjson", patients),
                       ("Observation_monk.ndjson", monks),
                       ("Observation_ulcer.ndjson", ulcers)):
        with open(out / name, "w") as f:
            for r in rows:
                f.write(json.dumps(r) + "\n")
        print(f"wrote {len(rows):4d} resources -> {out / name}")

    print(f"\nSynthetic cohort: {args.patients} patients, {len(ulcers)} pressure ulcers, "
          f"bias={args.bias} (0 = null scenario). SYNTHETIC DATA ONLY.")


if __name__ == "__main__":
    main()
