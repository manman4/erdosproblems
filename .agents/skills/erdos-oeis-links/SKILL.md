---
name: erdos-oeis-links
description: Evaluate OEIS links for Erdős problems and prepare link-only upstream contributions from this personal fork.
---

# OEIS links for Erdős problems

Follow the current upstream [CONTRIBUTING.md](https://github.com/teorth/erdosproblems/blob/main/CONTRIBUTING.md), especially [Notes on template fields](https://github.com/teorth/erdosproblems/blob/main/CONTRIBUTING.md#notes-on-template-fields) and [Linking with the OEIS](https://github.com/teorth/erdosproblems/blob/main/CONTRIBUTING.md#linking-with-the-oeis). Check the current text when preparing a contribution; it takes precedence over this summary.

## Assess relevance

Locate the user's OEIS checkout (normally `../OEIS` relative to this repository root). Read `数学ネタ/Erdos/OEIS_CANDIDATE_DECISIONS.md` for the current judgment criteria and `数学ネタ/Erdos/reviews/README.md` for record placement and verification scope. These are the authoritative personal instructions; do not maintain a second copy of their criteria in this skill.

Use `数学ネタ/Erdos/reviews/README.md` as the problem index, then read/update `reviews/NNxx/NNNN.md`. If a problem has no note, create one following the index instructions. Keep `OEIS_CANDIDATE_DECISIONS.md` for common criteria; do not add problem-specific entries there. Apply the current upstream relevance and contribution rules alongside those personal instructions.

## Prepare a link-only PR

- Read the personal `CLAUDE.md` upstream-PR rules before switching branches. Local `main` and `origin/main` are personal; start the PR branch from freshly fetched `upstream/main`.
- Edit only the relevant `oeis` entry in `data/problems.yaml`. Follow upstream meanings for `possible`, `submitted`, `in progress`, and `N/A`; preserve `possible` when further relevant sequences remain to be identified.
- Do not hand-edit the generated README or derived fields. Keep this skill and personal workflow files out of the upstream PR.
- In the PR description, state the definition correspondence, material conventions, and any indirect relation. Disclose AI assistance under the current contribution rules.
- Run the repository validator and `git diff --check`; inspect commits and the full diff against `upstream/main`, then verify the actual PR files and commits after creation.

## Update personal records after creating the PR

Update both the problem note and `数学ネタ/Erdos/README.md` in the OEIS checkout. Follow `reviews/README.md` for the separate OEIS registration status, upstream link status, dates, and index updates.

Add the problem/A-number mapping to the personal README correspondence table in problem-number order using its existing relative Japanese-translation links and note format. Check the problem record, applicable review index, and correspondence table before reporting completion.

Follow the OEIS checkout's `CLAUDE.md` and Markdown checks. Keep personal records outside the upstream PR. Commit or push them only when explicitly requested for those records, respecting a commit-only request.

This skill does not authorize remote changes or OEIS submissions. Follow the user's authorization and the current repository and OEIS rules.
