# Contents / Personal Property Inventory

**Keep the filled-in copy in `private/`.** This is the list FEMA, a tax preparer, or an SBA
loan officer will work from. It is also the list you will wish you had made before the debris
pile went to the curb, so start it the same day you start throwing things out.

## Why contents get their own list

Flood building coverage does not pay for contents. If you have no contents coverage (most
policies on elevated homes don't, and even with it, items *stored* in the space below the
lowest elevated floor are generally excluded), everything freestanding goes to **FEMA Other
Needs Assistance** as an uninsured loss, and to the **IRS casualty-loss deduction** and the
**SBA personal-property loan** if you use them.

FEMA's own acknowledgment letter names what its personal-property category pays for:
appliances, room furnishings, items required for employment or school, and a separate line
for cleanup tools bought after the disaster (generator, dehumidifier, chainsaw). It does not
name recreational or hobby property. Expect FEMA to pay on the freezer, the vacuums, the
chairs, and the table, and not on the trolling motor, the pellet grill, or the gaming PC.
**List everything anyway.** FEMA decides, and the tax deduction takes the whole list.

## The workflow that worked

1. **Photograph data plates first, items second.** Wipe the mud off the label. Model and
   serial are what turn "a freezer" into a claim line. One wide shot per room before anything
   moves; one plate shot per item as it comes out.
2. **Export your order history.** Amazon: *Account → Your Orders → Request Your Data* (or
   *Download order reports*). Big-box retailers keep order-details pages that print as
   receipts with the serial on them (Best Buy does). Outdoor and specialty shops send order
   confirmation emails you can search for by brand. `tools/match_orders.py` in this repo
   searches an Amazon export by keyword.
3. **Match every plate to a purchase record** and put the order number, date, and price in
   the row. No record is not a dead end: a gifted or in-store item is still a loss at its
   depreciated value. Write "in-store, approx. YYYY, approx. $X" rather than leaving blanks.
4. **Kept or disposed, and tested.** If you still have an item, say so; an inspector can see
   it. If you tried to repair it and failed, write the date and result. Do not attempt a
   cleanup that would muddy the record on a big item.
5. **Walk the debris photos for what you forgot.** The pile at the curb holds items nobody
   inventoried. Add them as **CANDIDATE** rows tied to the photo, then confirm each one
   yourself. A box in the pile is not proof the unit was lost.
6. **State the use honestly.** "Required for employment" means paid work. Unpaid teaching,
   hobbies, and volunteering do not qualify, and misstating use is federal fraud under the
   same statute printed in the FEMA letter. The downside dwarfs the upside on any item.
7. **Value at loss.** FEMA and the IRS use depreciated value. Fill the column from purchase
   year and price; a defensible estimate beats a blank.

## Columns

| Item | Location | Make / brand | Model | Serial | Year bought | Purchase price | Est. value at loss | Condition before | Damage | Photo file(s) | Receipt Y/N | Disposed / kept | FEMA category | Notes (order #, source) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | |

**FEMA category** is one of: `appliance`, `furnishing`, `employment/school`, `cleanup tool`,
`other` (recreational, hobby, vehicle-related, boat gear). Sort by it before you talk to FEMA.

## Photo index

Keep a second table so every photo is described once and every row can point to a file.

| File | Date | What it shows | Type (plate / item / scene / debris) | Inventory row(s) |
|---|---|---|---|---|
| | | | | |

## Second structure on the parcel

If an outbuilding or second house was lost, keep its contents on a separate tab tagged with
that address, and keep its demolition and debris invoices separate from the main house's
cleanup costs. They have different payers.
