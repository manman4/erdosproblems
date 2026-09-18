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
