# How This Was Built — the Human Bootstrap

This repo was not written in one sitting by one person. It came out of a short chain of
**human inputs** (about seven sentences total) driving three different AI systems, each
leaving durable files behind for the next one to pick up. This page documents that process
so you can replicate it for your own recovery — with any capable AI assistant — and so you
can judge how much to trust each layer.

## The pipeline at a glance

```text
Human seed (1 sentence)
   └─► LRA research pipeline (autonomous agents)
          └─► 172 sourced findings: ICC rules, Indianapolis ordinances, parcel GIS, event reporting
Human seed #2 (1 sentence)
   └─► Second research collection
          └─► 107 findings: FEMA IA, SBA loans, duplication-of-benefits law
Human: "Using this research help me plan for rebuild / recovery"
   └─► Claude (Anthropic) synthesized the findings into a phased recovery plan
Human: "FEMA declared this a national disaster" + pointer to new research
   └─► Claude updated the plan for the declaration (and over-trusted one claim — see Lessons)
Human: "create agent file and anything needed for future sessions to pick this up"
   └─► Claude wrote the handoff layer: project instructions, status log, plan source
Human: "correct plan, create spec"  (in a ChatGPT/Codex session)
   └─► GPT-5 audited the plan against PRIMARY sources, fixed errors, and wrote the
       execution runbook (the spec) — plus the homeowner supplied their case facts
       (carrier, adjuster, date of loss, application status) as they became known
Human: "create a version any homeowner can use"
   └─► This public repo
```

## Every human input, verbatim or near-verbatim

1. **The research seed:** *"Research 'FEMA's Increased Cost of Compliance (ICC) coverage.
   How to maximize, utilize, strategy post 2026 flood after tear out for [address]' from
   all sources."* — one sentence containing the domain, the property, and the intent.
2. **A second seed:** the same pattern for *FEMA disaster assistance / SBA disaster loan
   assistance*.
3. **"Using this research help me plan for rebuild / recovery."**
4. **"FEMA declared this a national disaster. also here is some new research [path]."**
5. **"Create agent file and anything needed for future sessions to pick this up."**
6. **"Correct plan, create spec."** — handed to a *different* AI (ChatGPT/GPT-5) for a cold
   audit of the first AI's work.
7. **Case facts as they happened** (the only inputs that required the homeowner's personal
   knowledge): who the insurance carrier and adjuster were, the date of loss, which
   applications had been filed, policy limits and renewal dates, and a recalled base flood
   elevation — which the audit AI *corrected* against FEMA's official flood hazard layer.

Everything else — the research, drafting, verification, corrections, file structure — was
agent work between those inputs.

## Why the multi-agent handoff worked

- **Durable, self-describing files at every stage.** Findings were stored as sourced JSONL;
  the plan as HTML with a change log; open items in an append-only STATUS log; the runbook
  as a spec with a control board. Each agent could pick up cold by reading files, not by
  being re-briefed.
- **Cross-vendor audit.** The most valuable single step was handing one AI's plan to a
  different AI with the instruction "correct plan." The audit caught a real over-claim
  (hazard-mitigation grants had been marked active without a declaration record), replaced
  generic program terms with event-specific ones (exact SBA rates and deadlines), and fixed
  a mis-recalled base flood elevation by two orders of 100 ft against primary FEMA data.
- **Humans supplied only what agents cannot know:** intent, real-world events, and personal
  case facts. Agents supplied everything that is knowable from public sources — and were
  required to cite them.

## Lessons if you replicate this

1. **Seed with one dense sentence** naming the program, the event, and your address/area.
2. **Make the AI cite primary sources** (statutes, CFR, FEMA pages, city ordinances, GIS
   records) — not news summaries — and keep the findings file.
3. **Never let one model grade its own homework.** Have a second model (different vendor if
   possible) audit the plan against primary sources before you act on it.
4. **Keep an append-only status log** and make every session read it first and write to it
   last. That file *is* the continuity.
5. **Keep personal data out of anything public or Git-tracked.** Store claim numbers,
   policy documents, and photos in a secure location; reference them by sanitized pointers
   (e.g., "identifier ending 1234, stored in secure binder").
6. **Treat AI statements about active deadlines and program status as unverified until tied
   to a primary-source URL and a date.** Agencies change rules by bulletin.

## What lives where in this repo

| Path | What it is |
|---|---|
| `README.md` | The homeowner recovery guide (strategy + money + deadlines) |
| `docs/HOW_THIS_WAS_BUILT.md` | This page — the process and its lessons |
| `docs/specs/SPEC_HOMEOWNER_FLOOD_RECOVERY_EXECUTION.md` | The generalized execution runbook: control board, phases, gates, scripts |
| `templates/STATUS_TEMPLATE.md` | Append-only status log to copy into your own (private) workspace |
| `templates/FUNDING_WORKSHEET.md` | Substantial-damage ratio and combined-cap ledger |
| `templates/EVIDENCE_INDEX_TEMPLATE.md` | Tear-out / damage evidence manifest |
