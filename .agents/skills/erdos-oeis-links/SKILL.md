---
name: erdos-oeis-links
description: Evaluate OEIS links for Erdős problems and prepare link-only upstream contributions from this personal fork.
---

# OEIS links for Erdős problems

Follow the current upstream [CONTRIBUTING.md](https://github.com/teorth/erdosproblems/blob/main/CONTRIBUTING.md), especially [Notes on template fields](https://github.com/teorth/erdosproblems/blob/main/CONTRIBUTING.md#notes-on-template-fields) and [Linking with the OEIS](https://github.com/teorth/erdosproblems/blob/main/CONTRIBUTING.md#linking-with-the-oeis). Check the current text when preparing a contribution; it takes precedence over this summary.

## Assess relevance

- Apply the upstream criterion: would a researcher interested in the problem plausibly find information on the OEIS page useful, or vice versa? Exclude extremely well known sequences as upstream requests.
- Compare mathematical definitions, not just initial terms or an OEIS backlink. Check offsets, allowed indices, strict versus non-strict inequalities, and empty or degenerate cases.
- A sequence need not be the exact function named in the problem. For a transformation, inverse, special case, or auxiliary quantity, explain the precise mathematical relation and why it is useful. Shared subject matter alone does not establish relevance; do not present an auxiliary sequence as the original function.
- Multiple sequences are allowed. Explain their roles and consider whether transformed sequences add useful information or merely duplicate a link; this is a judgment call, not a one-link limit.
- If an apparently unrelated sequence only matches computed terms, investigate the definitions and the upstream guidance before proposing a confirmed match.

## Prepare a link-only PR

- Read the personal `CLAUDE.md` upstream-PR rules before switching branches. Local `main` and `origin/main` are personal; start the PR branch from freshly fetched `upstream/main`.
- Edit only the relevant `oeis` entry in `data/problems.yaml`. Follow upstream meanings for `possible`, `submitted`, `in progress`, and `N/A`; preserve `possible` when further relevant sequences remain to be identified.
- Do not hand-edit the generated README or derived fields. Keep this skill and personal workflow files out of the upstream PR.
- In the PR description, state the definition correspondence, material conventions, and any indirect relation. Disclose AI assistance under the current contribution rules.
- Run the repository validator and `git diff --check`; inspect commits and the full diff against `upstream/main`, then verify the actual PR files and commits after creation.

This skill does not authorize remote changes or OEIS submissions. Follow the user's authorization and the current repository and OEIS rules.
