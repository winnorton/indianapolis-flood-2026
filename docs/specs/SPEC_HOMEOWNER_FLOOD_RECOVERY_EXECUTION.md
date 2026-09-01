# SPEC_HOMEOWNER_FLOOD_RECOVERY_EXECUTION

**Event:** August 2026 White River flood — FEMA **DR-4933-IN** (declared 2026-08-25) · SBA **IN-20022**
**Executor:** You (the homeowner), with family and professional advisers as you designate
**Reference guide:** `../../README.md`
**Change log:** your private copy of `templates/STATUS_TEMPLATE.md`

> This is a human recovery runbook. "Current state / Required state" replaces code diffs;
> a test result becomes **completion evidence**; rollback becomes a **stop/escalate
> condition**. This is planning research, not legal, insurance, engineering, tax, or
> financial advice. Generalized from a working single-property runbook; fill in the blanks
> with your own case facts and keep that filled-in copy **private**.

## Start Here

If today is chaotic, do only the first unblocked `NOW` row in the Control Board. Never mark
a task done from memory: save the confirmation, letter, or dated call note first.

1. Call DBNS at **317-327-7800** or email **PermitQuestions@indy.gov** about your property's
   permit path, fee-waiver eligibility (window ends **2026-09-13** — a Sunday; submit by
   **Friday 2026-09-11**), and a written
   site-specific BFE/floodway determination (Appendix B script).
2. Ask your flood-insurance adjuster to confirm your **date of loss** and **Proof of Loss
   deadline** (60 days after the date of loss) in writing (Appendix A script).
3. Apply to FEMA under **DR-4933-IN** and to SBA under **IN-20022** by **2026-10-25** —
   both dates fall on a Sunday, so file by **Friday 2026-10-23** — if you haven't.
4. Freeze and index your tear-out/damage evidence; keep sensitive records out of any public
   or shared repository.
5. Check your FEMA portal weekly and respond to every notice by its stated date.

## Privacy and Safety Hard Contract

- **Do not put sensitive recovery records anywhere public** (including a Git repo): Social
  Security numbers, banking details, policy declarations, IDs, full claim numbers, interior
  photos, signatures, tax or medical documents.
- In any shared/tracked file, record only sanitized references such as
  `secure binder: FEMA submission <date>` or the last four characters of an identifier.
- Life safety, mold prevention, utilities, structural stabilization, and emergency drying
  outrank paperwork. Photograph first when safe, keep receipts, and don't create unsafe delay.
- The paperwork hold applies to **permanent repair and demolition** — not to emergency
  protective work or to filing FEMA/SBA/NFIP applications.

**Secure evidence root — fill in before Step 1.4:** `____________________________`
(a non-public folder, encrypted drive, or physical binder you can actually access)

## Control Board

Statuses: `NOW`, `NEXT`, `WAITING`, `WATCH`, `DONE`. This board is the sole live tracker;
your status log is the append-only history.

| Status | Action | Hard date / trigger | Waiting on | Done when | Evidence ref |
|---|---|---|---|---|---|
| NOW | DBNS: fee-waiver eligibility, permit intake, SD-evaluation intake, written BFE/floodway determination request | Waiver ends 2026-09-13 (Sunday — submit by Fri 2026-09-11) | DBNS / IDNR | Written response with intake number | |
| NOW | Carrier: confirm date of loss + Proof of Loss deadline in writing | Today | Adjuster | Both dates in writing | |
| NOW | FEMA application (DR-4933-IN) | 2026-10-25 (Sunday — file by Fri 2026-10-23) | — | Submission identifier issued | |
| NOW | SBA application (IN-20022) | 2026-10-25 (Sunday — file by Fri 2026-10-23) | — | Application accepted | |
| NOW | Name secure evidence root; freeze and index evidence | Today | You | Index complete; originals preserved | |
| NEXT | Independent pre-flood market-value appraisal | Before SD decision | Appraiser | Signed appraisal | |
| NEXT | Itemized repair estimate + three comparable mitigation bids | Before mitigation decision | Contractors | Comparable written bids | |
| WAITING | DBNS substantial-damage determination | After intake | DBNS | Complete signed letter | |
| WAITING | ICC packet | SD letter + permit + contract | Carrier/DBNS/contractor | ICC Proof of Loss accepted | |
| WATCH | Hazard Mitigation (HMGP) amendment to DR-4933-IN and any city project | No current award | FEMA/State/City | Written funded-project offer naming your property | |
| WATCH | NFIP Proof of Loss extension bulletin for this event | Until POL accepted | FEMA/WYO bulletins | Written bulletin or carrier acceptance | |
| WATCH | Form 137PF property-tax filing | 2026-12-31 | Marion Co. Assessor | Filing accepted | |

## Dependency Path

```text
W0 exact dates + written contacts
 ├── W0A DBNS fee-waiver / permit-intake lane (start now; 2026-09-13 cutoff — a Sunday, effectively Fri 2026-09-11)
 ├── W1 FEMA / SBA / NFIP applications
 └── W2 evidence + neutral appraisal + estimates
          └── W3 DBNS substantial-damage letter + complete permits
W1 + W3 ── W4 mitigation choice + funding decision
W3 + W4 ── W5 ICC packet + construction + closeout
```

Applications, emergency protective work, evidence collection, and the DBNS permit lane run
**in parallel**. Permanent construction waits for the W3/W4 gates.

## Pre-flight — Halting Gate

Does **not** delay emergency safety work, applications, or evidence preservation. If any row
fails, stop before accepting a final settlement, signing a permanent construction/demolition
contract, assigning ICC, or starting permanent work.

| Check | Expected | If it fails |
|---|---|---|
| Disaster identity | DR-4933-IN, declared 2026-08-25, Marion County designated for Individual Assistance, FEMA deadline 2026-10-25 | Resolve via FEMA helpline against the official record |
| SBA identity | IN-20022, physical-damage deadline 2026-10-25 per the SBA event record (a Sunday — file by Fri 2026-10-23), event rates 3%/6% | Call SBA; don't rely on generic "60-day" language |
| NFIP clock | Carrier confirms YOUR recorded date of loss and exact POL deadline in writing | Escalate to a claims supervisor; manage to the earliest plausible deadline meanwhile |
| Policy status | Carrier confirms coverage limits and renewal date from the declarations page | Request corrections or cure options immediately |
| Local process | Written site-specific BFE (NAVD88), floodway/fringe status, required design elevation, and permit sequence — GIS overlays are not a survey | Request a FARA via the Indiana Floodplain Information Portal; do not finalize design from a digital map |
| Evidence custody | Originals preserved and indexed in a secure, non-public location | Stop destructive non-emergency work until captured |

## Phase 1 — Preserve Applications, Claim, and Evidence

- **1.1 FEMA record** — application submitted; every inspection notice, request for
  information, and decision tracked to a dated disposition. *Blocked?* Call the helpline,
  record representative + incident number. Registration does not guarantee any payment.
- **1.2 SBA record** — application accepted (applying ≠ accepting the loan). Get the rate
  determination, collateral requirement, maturity, deferment, mitigation-increase ceiling,
  and any mortgage-refinance eligibility **in writing** before acceptance (Appendix C).
- **1.3 NFIP claim** — carrier confirms date of loss, claim number, inspection status, POL
  deadline, and any written event extension. Submit the sworn Proof of Loss by the
  confirmed deadline.
- **1.4 Evidence index** — every damaged area/material has dated visual evidence,
  description, quantity, related invoice/receipt, and file location (use
  `templates/EVIDENCE_INDEX_TEMPLATE.md`). If tear-out preceded inspection, also collect
  the remediation firm's **daily drying logs and final moisture readings**. Never recreate
  or alter evidence; document gaps with affidavits where needed.
- **1.5 DBNS intake** — written answer on property eligibility for the fee waiver, the
  complete-submission checklist, and whether an IDNR floodway step must precede the city
  permit. Start this immediately; do not wait for the appraisal or SD letter.

**Checkpoint:** FEMA, SBA, and NFIP each have a dated record; the evidence index exists;
DBNS is answered or in `WAITING` with dated delivery evidence and a follow-up date.

## Phase 2 — Local Determination and Permit Path

- **2.1 Independent appraisal** — neutral licensed appraisal of **pre-flood market value**
  (assessed value is not automatically the DBNS basis). Never direct the appraiser toward a
  desired number.
- **2.2 SD evaluation request** — DBNS acknowledges the request, lists inputs, names the
  reviewer, and states the decision/appeal process.
- **2.3 The determination letter** — must state: the determination, the percentage/basis,
  that qualifying damage was **caused by flood** (required for ICC), and the market-value
  basis. Review it the day it arrives; request written correction immediately if an element
  is missing. If adverse, calendar every appeal deadline before deciding anything.
- **2.4 Complete permit submission** — submit only what DBNS defines as complete. Treat
  *written BFE + 2 ft* as your design elevation only once the written determination
  confirms both inputs. Floodway parcels need the IDNR step first.

**Checkpoint:** appraisal + determination (or documented pending status) + written permit
path. Permanent repair/demolition stays on hold.

## Phase 3 — Choose the Mitigation and Funding Path

- **3.1 Three comparable bids** — one written scope to all bidders; separately priced
  elevation, foundation, utilities, access, basement/slab work, engineering, permits,
  contingency, closeout. Never compare lump sums.
- **3.2 Funding worksheet** — complete `templates/FUNDING_WORKSHEET.md` with a source
  document for every number. Use "unknown," never a guess presented as fact.
- **3.3 Signed decision memo** — elevate / demolish-rebuild / express acquisition interest.
  Treat HMGP/buyout as **contingent** until a government sponsor makes a written funded
  offer naming your property. Do not sign a construction contract against hoped-for grants.

**Checkpoint:** worksheet balances; chosen path has a written compliance basis; confirmed
funding plus an explicitly accepted self-funded gap covers the contract amount.

## Phase 4 — File and Control the ICC Claim

- **4.1 Packet** — written determination + permit specifying required mitigation + signed
  contractor contract + signed ICC Proof of Loss. Submit indexed; get a deficiency list in
  writing if rejected.
- **4.2 Advance** — ask your carrier whether an advance is available, its amount,
  conditions, eligible uses, and return obligation, in writing. Ledger every expenditure.
- **4.3 Duplication-of-benefits ledger** — every invoice line has one category, one primary
  payer, any required offset, and a source document. Hold disputed funds unspent.
- **4.4 Conditional ICC assignment** — only if a hazard-mitigation declaration and a funded
  local project exist, your property is named, and reversion terms are written. Otherwise
  keep ICC under your own claim.

**Checkpoint:** carrier accepts the packet; the combined building+ICC cap worksheet is
current; every received dollar has a documented category.

## Phase 5 — Contract, Build, Close Out

- **5.1 Contract + notice to proceed** — scope matches permit and ICC submission; explicit
  pricing, change-order control, schedule, insurance, lien waivers, milestones. Proceed
  only after permits and funding gates pass.
- **5.2 Change ledger** — no change proceeds without written scope/price/schedule/permit
  effect and payer category.
- **5.3 Compliance closeout** — DBNS final inspection, certificate of occupancy or
  compliance letter (releases final ICC payment), final Elevation Certificate where
  applicable, paid invoices, lien waivers, final photos, carrier closeout, and a written
  premium quote using the new elevation data.
- **5.4 Form 137PF** — filed with the Marion County Assessor by **2026-12-31** with proof
  of delivery.

**Checkpoint / Post-flight:** FEMA + SBA dispositions dated; NFIP building and ICC claims
reconciled; appeal rights preserved or knowingly waived; permits and occupancy records
complete; funding ledger balances with zero unexplained difference; sensitive records still
private; status log has a closeout entry.

## Executor Handoff

**Most likely mistake:** waiting for every document before applying to FEMA/SBA — or the
opposite: starting permanent construction before the carrier and DBNS gates. Apply and
preserve evidence now; hold permanent work until the written requirements are satisfied.

**When an agency answer conflicts with this runbook:** record the person, date, question,
and exact answer; request the rule in writing; follow the current controlling written
authority; update your status log before relying on the change.

## Appendix A — Carrier Call Script

> "Please confirm in writing: the date of loss you have recorded, my claim number,
> inspection status, my exact sworn Proof of Loss deadline, and whether FEMA has issued any
> written extension for this Indiana event. Also confirm my policy renewal date and
> building-coverage limit, and tell me what evidence you need where tear-out occurred
> before the adjuster could observe the materials."

## Appendix B — DBNS Call/Email Script

> "This concerns flood damage at [address]. Please confirm the Substantial Damage
> Evaluation intake steps, required documents, reviewer, market-value method, and appeal
> path. Please identify every required permit and the required flood-protection grade for
> my parcel, whether a FARA or other IDNR review must precede city issuance, whether this
> property is eligible for the Aug 14 – Sept 13 fee waiver, and exactly what DBNS considers
> a complete, timely submission. Please respond in writing."

**FARA fallback:** [Indiana Floodplain Information Portal](https://www.in.gov/dnr/water/surface-water/indiana-floodplain-mapping/indiana-floodplain-information-portal/)
— request a "building-footprint floodway determination and regulatory flood elevation" for
your parcel number. If unavailable: water_inquiry@dnr.IN.gov · 317-232-4160 ·
877-928-3755 opt 1.

## Appendix C — SBA Questions

> "My application is under Indiana disaster IN-20022 / FEMA DR-4933. Please state in
> writing my approved rate, whether SBA found credit available elsewhere, collateral
> requirement, maturity, first-payment/interest deferral, the mitigation-increase ceiling
> and request deadline, any mortgage-refinance eligibility, and how insurance, FEMA, and
> ICC proceeds affect my approved amount."
