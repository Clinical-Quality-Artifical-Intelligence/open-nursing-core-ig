# Bug Report: Open Nursing Core

> **Status (remediation pass):** Most items below have been resolved and
> verified. Each entry is annotated with its current state. The FHIR IG now
> builds with **0 errors / 0 warnings** under SUSHI, and the application image
> installs a complete dependency set.

## High Severity

### 1. Hardcoded Credentials — ✅ RESOLVED
**File:** `app.py`, `app_phase2.py`, `core/validator.py`
**Description:** Admin/Nurse/Clinician demonstration passwords were previously hardcoded.
**Current state:** Credentials now come from environment variables via
`core/settings.py` (`ADMIN_PASSWORD`, `NURSE_PASSWORD`, `CLINICIAN_PASSWORD`)
with production configuration enforcement (`Settings.check_security`). There
are now no built-in credentials, production rejects in-memory authentication,
and database failures fail closed. Passwords are hashed with **bcrypt** and
verified in constant time (`core/validator.py`).

### 2. Insecure Docker Deployment (Phase 1 vs Phase 2) — ✅ RESOLVED
**File:** `Dockerfile`
**Current state:** The Dockerfile entrypoint is
`streamlit run app_phase2.py` (the database-backed app). The image now also
runs as a non-root user and uses Streamlit's `/_stcore/health` healthcheck.

### 3. Thread-Safety in Chat History — ✅ RESOLVED
**File:** `core/validator.py`
**Current state:** Phase 2 uses the database as the primary store. The JSON
fallback's read-modify-write is now guarded by a module-level
`threading.Lock`, preventing concurrent-write corruption.

### 4. FHIR Profile Validation Errors — ✅ RESOLVED
**File:** `input/fsh/*.fsh`
**Current state:** `sushi .` compiles all 60 profiles, 4 extensions, 27
ValueSets and 3 CodeSystems with **0 errors and 0 warnings**.

## Medium Severity

### 5. Dependency Issues — ✅ RESOLVED
**File:** `requirements.txt`
**Current state:** The root `requirements.txt` previously listed only four
packages, so the container crashed on boot (`ModuleNotFoundError`). It now
pins the full, version-bounded runtime set (web app + auth + AI + DB +
optional ML). The GPU/model-training stack remains isolated in
`hf_space/requirements.txt`.

### 6. Missing Monk Skin Tone Implementation — ✅ RESOLVED
**File:** `input/fsh/onc-equity.fsh`
**Current state:** `ONCMonkScale` CodeSystem, `ONCMonkScaleVS` ValueSet and
the `ONCMonkSkinToneObservation` profile are all present.

## Low Severity

### 7. Missing Dependencies in Sushi Config — ℹ️ NOT REQUIRED
**File:** `sushi-config.yaml`
**Current state:** SUSHI resolves `hl7.fhir.r4.core#4.0.1` automatically and
builds cleanly; an explicit `dependencies` exclusion is unnecessary.

### 8. Unused Code — ✅ RESOLVED
**File:** `ml/*.py`
**Current state:** The ML modules are integrated into `app_phase2.py` behind a
guarded optional import (`ML_AVAILABLE`), so they load when their
dependencies are installed and degrade gracefully otherwise.
