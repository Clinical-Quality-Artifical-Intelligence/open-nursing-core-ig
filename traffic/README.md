# Repository Traffic

This folder holds a rolling history of GitHub **clone** and **view** statistics
for the repository, collected automatically by
[`.github/workflows/traffic.yml`](../.github/workflows/traffic.yml).

GitHub's built-in traffic stats (Insights → Traffic) are only retained for **14
days** and are visible only to users with write access. This workflow snapshots
them every week and appends to a permanent, deduplicated history so the numbers
survive beyond the 14-day window.

## Files

| File | Contents |
|------|----------|
| `clones.csv` | `date, count, uniques` — daily clone counts |
| `views.csv` | `date, count, uniques` — daily page-view counts |
| `clones-badge.json` | [shields.io endpoint](https://shields.io/endpoint) badge data (cumulative) |
| `views-badge.json` | shields.io endpoint badge data (cumulative) |

The CSVs are the source of truth if you want to chart the data over time.

## Notes

- The workflow uses the built-in `GITHUB_TOKEN`, which can read the Traffic API
  because the job has `contents: write` on this repository. If your org
  restricts the default token, add a `repo`-scoped PAT as a secret and pass it
  to the `github-script` step instead.
- Totals shown in the README badges accumulate from the day tracking started —
  they are not retrospective before the first workflow run.
