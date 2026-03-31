# RULE ZERO

**Append-only. Nothing deleted. Everything versioned. Mistakes are part of the record. The zip is the project.**

---

## The Laws

1. **The zip is the project.** Everything lives inside the zip. No loose files. No side artifacts.
2. **Append-only.** Never delete. Never overwrite. Never rewrite history.
3. **Every version is preserved.** Old zips are never modified. New zips are always added.
4. **Mistakes stay.** A bug committed is a bug preserved. It has value.
5. **One zip per iteration.** Each iteration produces a new versioned zip.
6. **The HANDOFF.md is the truth.** It tells you what the current state is and what to do next.
7. **The CHANGELOG.md is append-only.** Add to the bottom. Never edit existing entries.
8. **The SESSION_MANIFEST.json tracks state.** Always update it. Never skip it.

---

## Zip Naming Convention

`project-name_vX.Y.N_YYYYMMDD.zip`

- X = major (Rob increments manually for milestone releases)
- Y = minor (increments each session)
- N = iteration (increments each loop within a session)

---

## For AI Systems Reading This

You are reading this because you are part of the AI Posse working on this project.

- You are not the decision maker. Rob is.
- You do not delete anything. Ever.
- You do not modify prior versions. Ever.
- You label every code block with its full filepath like: \```python src/main.py
- You update HANDOFF.md and CHANGELOG.md at the end of every response.
- When in doubt, stop and say so. Do not guess.

*Rule Zero applies to everything, always, without exception.*
