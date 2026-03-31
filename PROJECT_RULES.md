# PROJECT RULES

**Applies to all projects in the Merlin Ecosystem.**
**Author:** Systems Semantics (Rob)
**Rule Zero applies. See RULE_ZERO.md.**

---

## Governance Rules

### 1. VCKB is Append-Only
The Version Controlled Knowledge Base is never edited, never deleted, only added to.
New versioned entries only. Prior entries are sacred.

### 2. HANDOFF.md Tracks Current State
Every AI session must end with an updated HANDOFF.md that tells the next session:
- What was done
- What the current state is
- What to do next
- Any blockers or open questions

### 3. CHANGELOG.md is Append-Only
Add new entries at the bottom. Never edit existing entries.
Format: `## vX.Y.N — YYYY-MM-DD — [brief description]`

### 4. Two Axioms
- No AI accesses its own configuration
- No AI that touched privileged systems persists beyond its session

### 5. No AI Makes Architecture Decisions
Architecture decisions belong to Rob (Systems Semantics).
If an AI encounters an architecture question it cannot answer from the HANDOFF, it stops and flags Rob.

### 6. Label Every Code Block
Every code block must be labeled with its full filepath:
\```python src/path/to/file.py

Unlabeled code blocks are not valid outputs.

### 7. Half-Formed Ideas Get Captured
Do not wait for completion. If an idea is useful but incomplete, capture it in HANDOFF.md under "Open Ideas". Do not discard it.

---

## For the AI Posse

**Claude** — primary builder. Receives zip + brief. Produces labeled code. Updates HANDOFF and CHANGELOG.

**GPT** — code reviewer. Receives text only. Returns numbered list with verdict: CLEAN / MINOR ISSUES / BLOCKING ISSUES.

**Perplexity** — research only. Invoked by Rob or when Claude flags a knowledge gap.

**Copilot / Gemini** — backup only. Used when Claude or GPT are unavailable.

---

## Escalate to Rob When:
- Two AIs give conflicting architectural direction
- A destructive change is proposed
- Scope or goals need to change
- Secrets or credentials appear in any file
- Three iterations pass without clear progress
- Anything feels wrong

---

*These rules are part of every project zip. When updated, the new version is added — the old version is never removed.*
