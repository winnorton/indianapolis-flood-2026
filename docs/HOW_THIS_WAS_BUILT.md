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

## First dogfood — what a real case taught the guide (September 2026)

The guide was written from research, then run cold against the author's own claim file:
an adjuster-prepared Proof of Loss, a dry-out invoice, the FEMA portal letters, and the
inbox. The mismatches became the September 2026 revisions. Generalized, so they apply to
anyone:

1. **The guide assumed the hard case.** An already-elevated home with water only in the
   enclosure underneath gets a small clean-up-only claim, and most of the 50% / elevation /
   ICC material is noise for that user. Added the "already elevated" section, the
   `ELEVATED` intake flag, and a short-program routing override.
2. **The first FEMA deadline is set on day one.** Letters post to the portal within minutes
   of applying, and one was a Request for Information with a 30-day clock. The guide had
   said "check weekly." Now it says "log in the same day."
3. **The adjuster-prepared Proof of Loss is a moment the guide had skipped.** Users get an
   e-signature envelope with a net-claim number and need a checklist for it: what to
   verify, that it is not a release, that "viewed" is not "signed."
4. **Emergency dry-out cost is the real gap for small claims.** A premium-speed firm billed
   well above the NFIP price list. The routing for that shortfall (supplement → FEMA →
   SBA → casualty-loss deduction) was missing, and the casualty-loss deduction was absent
   from the money map entirely.
5. **Documents answer intake faster than questions.** The closing package alone answered
   five intake questions; the inbox answered the FEMA ID, SBA status, contractor names,
   and dates. Added the "documents before questions" rule and a document intake question.
6. **Vehicles and rental cars have their own path.** The auto carrier pays first; rental
   cars are often not covered; FEMA's vehicle RFI wants the denial in writing. None of
   that was in the guide.
7. **A second structure on the parcel was invisible.** Demolition of an outbuilding needs
   a wrecking permit, pre-demo photos, and a written answer from the adjuster. Added to WS5.
8. **The repo's own privacy rule needed a mechanism.** The public `docs/` folder and a
   homeowner's private "docs" folder collide in name. Added a git-ignored `private/`
   convention and a `.gitignore` that refuses PDFs and photos.

Two dogfood findings did not need a change: the call scripts were right (the Proof of Loss
package did not state the deadline or any extension, exactly what Appendix A asks for), and
the deadline math held.

### Round two, the same day: contents

The afternoon went to personal property, which the guide had barely mentioned. What it added:

1. **Contents have no home in a building-only claim**, and the guide had no workflow for
   them. Added a contents template with the sequence that worked: plates, order-history
   export, debris photos, candidate confirmation, use statement, depreciated value.
2. **Order exports turn plates into receipts.** An Amazon export matched most of a garage
   in minutes; a big-box order-details page printed as a receipt with the serial on it; a
   specialty retailer's 2018 confirmation email priced a camp chair. Added a small
   standard-library script and a retailer script.
3. **Photos surfaced items nobody had listed** — a second pressure washer, an air
   compressor, a dozen chairs — and also a box that proved nothing. Added the candidate-row
   rule and the "a box is not proof" rule to AGENTS.md.
4. **FEMA's categories are narrow and the honest use statement matters more than the
   value.** Added the category table to the README and the never-reword-use rule.
5. **Declining SBA is a legitimate choice.** The guide had leaned on it as the workhorse;
   now it says FEMA does not require it and lets the user decide.

## What lives where in this repo

| Path | What it is |
|---|---|
| `README.md` | The homeowner recovery guide (strategy + money + deadlines) |
| `docs/HOW_THIS_WAS_BUILT.md` | This page — the process and its lessons |
| `docs/specs/SPEC_HOMEOWNER_FLOOD_RECOVERY_EXECUTION.md` | The generalized execution runbook: control board, phases, gates, scripts |
| `templates/STATUS_TEMPLATE.md` | Append-only status log to copy into your own (private) workspace |
| `templates/FUNDING_WORKSHEET.md` | Substantial-damage ratio and combined-cap ledger |
| `templates/EVIDENCE_INDEX_TEMPLATE.md` | Tear-out / damage evidence manifest |
