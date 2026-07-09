# Repository Traffic

This folder holds a rolling history of GitHub **clone** and **view** statistics
for the repository, collected automatically by
[`.github/workflows/traffic.yml`](../.github/workflows/traffic.yml).

GitHub's built-in traffic stats (Insights → Traffic) are only retained for **14
days** and are visible only to users with write access. The workflow snapshots
them every Monday and appends to a permanent, deduplicated history so the
numbers survive beyond the 14-day window.

## Where the data lives

Because `main` is a protected branch (all changes require a pull request), the
workflow commits its updates to the dedicated **`traffic-data`** branch, not
here. The seed files in this folder on `main` exist only so the layout is
discoverable; the live data is at
[`traffic/` on `traffic-data`](https://github.com/Clinical-Quality-Artifical-Intelligence/open-nursing-core-ig/tree/traffic-data/traffic),
and the README badges point at that branch's raw URLs.

## Files

| File | Contents |
|------|----------|
| `clones.csv` | `date, count, uniques` — daily clone counts |
| `views.csv` | `date, count, uniques` — daily page-view counts |
| `clones-badge.json` | [shields.io endpoint](https://shields.io/endpoint) badge data (cumulative) |
| `views-badge.json` | shields.io endpoint badge data (cumulative) |

The CSVs are the source of truth if you want to chart the data over time.

## Required setup: `TRAFFIC_PAT` secret

The Traffic API is **not accessible to the default Actions `GITHUB_TOKEN`**
("Resource not accessible by integration"). A repository admin must create an
Actions secret named **`TRAFFIC_PAT`** containing either:

- a **fine-grained personal access token** scoped to this repository with
  **"Administration: read-only"** permission, or
- a classic PAT with the `repo` scope.

(Settings → Secrets and variables → Actions → New repository secret.)

Until the secret exists, the workflow fails with a clear message and writes
nothing, so history is never corrupted. Totals accumulate from the first
successful run — they are not retrospective.
