# GitHub to UNICC automatic mirror

GitHub is the source of truth for Open Nursing Core. Every push to GitHub
`main` is mirrored to the UNICC GitLab project by
`.github/workflows/mirror-unicc.yml`.

Target:
`https://opensource.unicc.org/nursecitizendeveloper/open-nursing-core-ig`

## One-time credential setup

1. In the UNICC GitLab project, create a project access token, deploy token or
   personal access token that can push to the repository. Grant only the
   `write_repository` scope and use an account permitted to update `main`.
2. In the GitHub repository, open **Settings → Secrets and variables → Actions**.
3. Add these repository secrets:
   - `UNICC_GITLAB_USERNAME` — the GitLab token username/account name.
   - `UNICC_GITLAB_TOKEN` — the token value.
4. Run **Mirror main to UNICC GitLab** manually once from GitHub Actions.
5. Confirm that the UNICC `main` commit matches GitHub `main`.

Do not store the token in this repository, a workflow file, local Git config or
a deployment log. Rotate it according to the UNICC account's security policy.

## Safety behaviour

The workflow performs a one-way, fast-forward-only update. Before pushing, it
verifies that UNICC `main` is an ancestor of GitHub `main`. If someone commits
directly on UNICC, mirroring stops instead of deleting or overwriting their
work. Reconcile the UNICC commit into GitHub and rerun the workflow.

Tags, merge requests, issues, releases and GitLab settings are not mirrored.
FHIR validation and application CI continue to run on GitHub Actions.
