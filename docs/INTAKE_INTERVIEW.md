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
| Q4b | If insured: does the policy include contents coverage (Coverage B)? | `CONTENTS` yes/no/unsure — matters for FEMA Other Needs routing and for what a supplement can include |
| Q5 | If insured: have you filed the flood claim? Do you know your adjuster's name and whether they've inspected? | `CLAIM_FILED` yes/no · `INSPECTED` yes/no |
| Q6 | Has any demolition, gutting, or tear-out already happened? | `TEAROUT_DONE` yes/no |
| Q7 | How bad is the damage, roughly: cosmetic only / significant but livable / major structural / uninhabitable? | `SEVERITY` = cosmetic · significant · major · destroyed |
| Q7b | Is your home elevated on posts, piers, or columns, and did the water stay below the lowest living floor (garage or enclosure only)? | `ELEVATED` yes/no — if yes, the 50%/elevation/ICC material largely does not apply; enclosure coverage is limited (README "already elevated" section) |
| Q8 | Have you applied to FEMA yet? To SBA? | `FEMA_FILED` yes/no · `SBA_FILED` yes/no |
| Q8b | If FEMA is filed: have you logged into the DisasterAssistance.gov portal and read every letter there? Did you ask FEMA for help with a damaged vehicle? | `FEMA_LETTERS_READ` yes/no · `VEHICLE` yes/no — letters post within minutes of filing; a Request for Information carries a 30-day deadline |
| Q9 | Is there a mortgage on the home? | `MORTGAGE` yes/no |
| Q10 | Do you know if your home is in the mapped floodplain (Zone AE) or the floodway? Most riverfront homes in this event are. | `ZONE_KNOWN` yes/no (never resolve this from a map yourself — WS5 gets it in writing) |
| Q11 | Has the city (DBNS) contacted you, inspected, or sent any letter — especially anything mentioning "substantial damage"? | `SD_LETTER` yes/no/pending |
| Q11b | Is there a second building on the property (outbuilding, second house) that was damaged or that you plan to demolish? | `SECOND_STRUCTURE` yes/no |
| Q12 | Are you working with any professionals already (public adjuster, attorney, contractor, remediation firm)? Has a remediation/drying firm finished and left? | `PROS` list · `REMEDIATION_DONE` yes/no |
| Q12b | If a dry-out firm was used: what did it bill, and how does that compare with what the adjuster's estimate allows for the same work? | `MITIGATION_INVOICE` amount/unknown · `ESTIMATE_GAP` yes/no/unknown |
| Q13 | What's your biggest worry right now, in one sentence? | `PRIORITY` free text — use it to order the program empathetically |
| Q14 | Do you have documents you can paste or attach now — adjuster estimate or Proof of Loss, FEMA portal letters, contractor invoices, insurance emails? | `DOCS` — read them **first** and confirm the answers they contain instead of asking (AGENTS.md rule 9). A closing package alone answers Q3, Q4, Q4b, Q5, and Q9 |
| Q15 | If contents were lost: do you have photos of the items or their data plates, and can you export your Amazon or retailer order history? | `CONTENTS_PHOTOS` yes/no · `ORDER_EXPORT` yes/no — routes to the contents workflow (AGENTS.md Step 4b, `templates/CONTENTS_INVENTORY_TEMPLATE.md`) |

**Ask Q14 early** — right after Q1 if the user seems organized. Documents answer more
questions than the user will remember to, and reading them prevents the assistant from
asking for facts the user has already been sent.

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
- `ELEVATED` = yes and `SD_LETTER` = no → the short program: WS1 + WS2 + WS3 (+ WS8 if any
  rebuild). Skip WS5 and WS7 and say plainly that the elevation/ICC material does not apply.
  Severity is a poor proxy here — a five-figure dry-out bill can still be a small claim.
- `FEMA_LETTERS_READ` = no and `FEMA_FILED` = yes → today's single most urgent action is
  logging into the portal; a Request for Information may already be running its 30 days.
- `VEHICLE` = yes → add the vehicle-documentation step in WS2; ask whether the auto carrier
  paid, and whether a rental car was covered (get the denial in writing).
- `ESTIMATE_GAP` = yes → open WS3's supplement step before the Proof of Loss is signed if
  possible, and in any case before the Proof of Loss deadline.
- `SECOND_STRUCTURE` = yes → open WS5's demolition step even if the main house is fine.
- `CONTENTS` = no (or `INSURED` = no) and personal property was lost → run the contents
  workflow (AGENTS.md Step 4b) inside WS1; it feeds FEMA Other Needs, the tax deduction,
  and SBA if used.
- `TEAROUT_DONE` = yes and `INSPECTED` = no → flag in WS1 and WS3: evidence preservation is
  now the claim's foundation; get the remediation firm's drying logs and final moisture
  readings before the firm becomes unreachable.
- `SD_LETTER` = yes → open WS5 immediately and check the letter against its checklist;
  tell the user to pause non-emergency repair work until WS5's gate clears.

## After routing

1. Present the personal program: numbered tracks, one line each, the user's own dates
   attached (FEMA 2026-10-25 · SBA 2026-10-25, both Sundays — safe last day Friday
   2026-10-23 · fee waiver 2026-09-13, a Sunday — submit by Friday 2026-09-11 · `POL_DEADLINE` ·
   Form 137PF 2026-12-31).
2. Name today's single most urgent action.
3. Start the first selected workstream.
4. End the session by producing their private status log (see AGENTS.md Step 5).
