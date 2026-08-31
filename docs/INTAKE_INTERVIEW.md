# Intake Interview and Routing Table

For the AI assistant: ask these **in order, one at a time**, in your own words. Skip any
already answered. Each answer sets flags; the routing table at the bottom converts flags
into the user's personal program of workstreams. Do not diagnose or conclude eligibility —
flags only route which playbooks to open.

## Questions

| # | Ask (in your own words) | Record |
|---|---|---|
| Q1 | Are you and your household safe, and do you have a place to stay tonight? | `SAFE` yes/no · `DISPLACED` yes/no |
| Q2 | Is this your primary residence, and do you own it? | `OWNER_PRIMARY` yes/no (if renter or second home: parts of this playbook won't fit — FEMA/SBA still may; say so honestly) |
| Q3 | What date did the flood damage your home? (their best knowledge; the insurer's recorded date controls later) | `DATE_OF_LOSS` → compute `POL_DEADLINE` = date + 60 days |
| Q4 | Do you have flood insurance (an NFIP policy or private flood policy)? | `INSURED` yes/no/unsure — if unsure, help them check their mortgage escrow or call their home insurer |
| Q5 | If insured: have you filed the flood claim? Do you know your adjuster's name and whether they've inspected? | `CLAIM_FILED` yes/no · `INSPECTED` yes/no |
| Q6 | Has any demolition, gutting, or tear-out already happened? | `TEAROUT_DONE` yes/no |
| Q7 | How bad is the damage, roughly: cosmetic only / significant but livable / major structural / uninhabitable? | `SEVERITY` = cosmetic · significant · major · destroyed |
| Q8 | Have you applied to FEMA yet? To SBA? | `FEMA_FILED` yes/no · `SBA_FILED` yes/no |
| Q9 | Is there a mortgage on the home? | `MORTGAGE` yes/no |
| Q10 | Do you know if your home is in the mapped floodplain (Zone AE) or the floodway? Most riverfront homes in this event are. | `ZONE_KNOWN` yes/no (never resolve this from a map yourself — WS5 gets it in writing) |
| Q11 | Has the city (DBNS) contacted you, inspected, or sent any letter — especially anything mentioning "substantial damage"? | `SD_LETTER` yes/no/pending |
| Q12 | Are you working with any professionals already (public adjuster, attorney, contractor, remediation firm)? Has a remediation/drying firm finished and left? | `PROS` list · `REMEDIATION_DONE` yes/no |
| Q13 | What's your biggest worry right now, in one sentence? | `PRIORITY` free text — use it to order the program empathetically |

## Routing table

Select every workstream whose condition is true. Present them in this order.

| Workstream | Select when |
|---|---|
| **WS6 Temporary housing** | `DISPLACED` = yes (do this FIRST, same conversation) |
| **WS1 Evidence & records** | always |
| **WS2 Applications & deadlines** (FEMA, SBA, tax relief) | always |
| **WS3 Flood insurance claim** | `INSURED` = yes |
| **WS4 Uninsured funding path** | `INSURED` = no |
| **WS5 Permits & substantial damage** | `SEVERITY` ≥ significant, or `SD_LETTER` ≠ no, or `TEAROUT_DONE` = yes |
| **WS7 Mitigation decision & ICC** | `SEVERITY` ≥ major (ICC sections only if `INSURED` = yes) |
| **WS8 Rebuild & closeout** | whenever repair/rebuild work lies ahead (nearly everyone; open it last) |

Immediate overrides, regardless of routing:
- `SAFE` = no → address safety/shelter before any interview question.
- `SEVERITY` = cosmetic and `INSURED` = yes → the program may be as small as WS1 + WS2 + WS3;
  don't burden the user with the rest.
- `TEAROUT_DONE` = yes and `INSPECTED` = no → flag in WS1 and WS3: evidence preservation is
  now the claim's foundation; get the remediation firm's drying logs and final moisture
  readings before the firm becomes unreachable.
- `SD_LETTER` = yes → open WS5 immediately and check the letter against its checklist;
  tell the user to pause non-emergency repair work until WS5's gate clears.

## After routing

1. Present the personal program: numbered tracks, one line each, the user's own dates
   attached (FEMA 2026-10-25 · SBA 2026-10-26 · fee waiver 2026-09-13 · `POL_DEADLINE` ·
   Form 137PF 2026-12-31).
2. Name today's single most urgent action.
3. Start the first selected workstream.
4. End the session by producing their private status log (see AGENTS.md Step 5).
