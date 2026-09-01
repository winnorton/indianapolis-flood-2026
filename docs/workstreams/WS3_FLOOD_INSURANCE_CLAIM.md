# WS3 — Flood Insurance Claim (insured users)

**Goal:** the NFIP/flood claim is filed, documented, and sworn on time, and the user
understands the numbers before accepting anything final.

**The one unforgiving date:** the sworn **Proof of Loss** is due **60 days from the date of
loss** (the carrier's recorded date controls). Compute it with the user and treat it as
immovable unless a written FEMA bulletin extends it for this event.

**Elevated homes (`ELEVATED` = yes):** the policy covers only a short list of items in the
enclosure below the lowest elevated floor — clean-up, utility connections, foundation
elements. Finishes and stored contents are generally excluded even with contents coverage.
Tell the user to expect a small, clean-up-only estimate so the number is not a shock, and
have them confirm the covered list with the adjuster in writing.

## Steps

1. **Confirm the claim is filed** and get in writing from the adjuster: recorded date of
   loss, claim number, inspection status, and the exact Proof of Loss deadline (script in
   the spec's Appendix A).
   *Done when:* a dated email/letter from the carrier says all four.
2. **Support the inspection** with the WS1 evidence — especially if tear-out preceded it.
   Ask the adjuster what additional evidence they need, in writing.
3. **Review the estimate line by line.** If it's short (missed rooms, code items,
   quantities), submit a supplement with contractor estimates. Users can represent
   themselves; a public adjuster (typically ~10% contingency) or attorney is an option for
   large disputes.
3b. **Dry-out invoice vs. the estimate.** The adjuster prices clean-up, antimicrobial, and
   drying from a regional price list. A fast professional firm often bills well above it.
   That gap is the most common supplement for a small claim. Packet: itemized invoice with
   equipment counts and days, daily drying logs (temperature, humidity, dehumidifier
   readings), initial and final material moisture readings, moisture map, signed work
   authorization, photos, disposal receipts, antimicrobial record. Ask the firm to send it
   to the adjuster directly (README script) and to copy the user. Frame it honestly: a
   request the carrier may hold to list pricing, not an entitlement. Whatever stays unpaid
   routes to FEMA (WS2 step 1c), then SBA, then the IRS casualty-loss deduction.
3c. **When the adjuster sends a Proof of Loss to sign** (usually an e-signature envelope
   containing the FEMA Proof of Loss form and the estimate, marked *adjuster-prepared* and
   *initial*): check the recorded date of loss, coverage limits, deductible, mortgagee
   line, contents line, and the scope before signing. The form says it is *not a release*
   and that the user may still request payment for other damage — so signing locks in the
   undisputed amount and keeps supplement rights. "Viewed" in the e-signature system is not
   "signed"; the claim goes to the carrier for payment only after the signed copy returns.
   Small cosmetic errors on the form (a mis-ticked box with no dollar effect) are not worth
   holding up the signature.
4. **Submit the sworn Proof of Loss by the deadline** — even if amounts are still in
   dispute; it can state the undisputed amount with supplements to follow. Keep proof of
   delivery.
5. **Track the cap math** (use `templates/FUNDING_WORKSHEET.md`): building payments and any
   later ICC payment together cannot exceed the building coverage limit. If the building
   claim will run near the limit and substantial damage is likely (WS5/WS7), model the
   trade-off BEFORE accepting a final settlement.

## Stop / escalate

- Denial or disputed settlement → 60-day FEMA appeal clock from the written denial;
  appraisal-clause and lawsuit (1-year) paths exist but close other doors — licensed
  advice first.
- Any request to sign a full release while supplements are pending → advice first.
- No adjuster contact within a reasonable time → escalate in writing to a claims
  supervisor; document every call (name, date, content).
