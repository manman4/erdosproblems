# Repository instructions

Follow [`CONTRIBUTING.md`](CONTRIBUTING.md) for all repository-specific
contribution and AI-use rules.

## Public repository safeguards

- Treat every tracked file, commit, branch, issue, and pull request as public.
  Never add secrets, credentials, private keys, personal data, machine-specific
  absolute paths, or unredacted sensitive logs. Review staged changes before
  every commit.
- Do not push, publish, open or edit issues or pull requests, post comments, or
  otherwise change remote state unless the user explicitly requests it. Do not
  commit to `main` unless explicitly instructed; use the current feature branch.
- Preserve unrelated work. Do not use destructive Git or filesystem commands,
  overwrite existing research results, or delete files without explicit
  authorization and a verified target.
- Follow the documented generation and validation workflows. Do not hand-edit
  derived fields or generated files. Run relevant targeted checks and
  `git diff --check` before committing.
- Treat computational mathematical results as requiring reproducible evidence:
  retain exact commands, tool versions, checksums, and witnesses, and cross-check
  new values by an independent method. Disclose AI assistance and follow the
  repository and OEIS rules; never submit AI-generated material to the OEIS.
- Do not add dependencies, execute downloaded code, or access credentials or
  private files without a task-specific need and explicit user authorization.

## Pull requests to upstream

- Local `main` and `origin/main` are personal branches and may contain changes
  that do not belong in the upstream repository. Keep personal workflow rules
  and experiment history on the personal branches.
- Before preparing an upstream PR, verify the remotes and fetch `upstream/main`.
  Create the PR branch from the freshly fetched `upstream/main`, never from
  local `main` or `origin/main`.
- If the intended change already exists on a personal branch, transfer only
  the relevant commits onto the upstream-based PR branch. Preserve unrelated
  work and history. Do not include this personal `CLAUDE.md` or other personal
  workflow files unless the user explicitly requests an upstream contribution
  of those files.
- Before pushing or creating the PR, inspect both
  `git log --oneline upstream/main..HEAD` and
  `git diff upstream/main...HEAD`; confirm that every commit and changed file
  belongs to the requested contribution. Comparing only with `origin/main`
  does not establish the scope of an upstream PR.
- After creating or updating the PR, verify its commits and files on GitHub
  against the upstream base branch before reporting its scope to the user.
