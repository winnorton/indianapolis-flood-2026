#!/usr/bin/env python3
"""Search an Amazon order-history export for items by keyword.

Usage:
    python tools/match_orders.py Order_History.csv freezer "shop vac" dewalt
    python tools/match_orders.py Order_History.csv --since 2018 monitor tv

Amazon: Account -> Your Orders -> Request Your Data (or Download order reports). The CSV has a
"Product Name" column and an "Order Date" column; this script needs nothing else and has no
dependencies beyond the Python standard library. Output: date, order id, total, product name.
Copy the order id and price into the Notes column of your contents inventory.
"""
import csv, sys

def main(argv):
    if len(argv) < 2 or argv[0] in ("-h", "--help"):
        print(__doc__); return 1
    path, args = argv[0], argv[1:]
    since = None
    if "--since" in args:
        i = args.index("--since"); since = args[i + 1]; del args[i:i + 2]
    keys = [a.lower() for a in args]
    with open(path, encoding="utf-8-sig", errors="replace", newline="") as f:
        rows = list(csv.DictReader(f))
    name_col = next((c for c in rows[0] if "product name" in c.lower()), None) if rows else None
    date_col = next((c for c in rows[0] if "order date" in c.lower()), None) if rows else None
    id_col = next((c for c in rows[0] if c.lower().strip() == "order id"), None) if rows else None
    tot_col = next((c for c in rows[0] if "total amount" in c.lower()), None) if rows else None
    if not (name_col and date_col):
        print("Could not find Product Name / Order Date columns in", path); return 1
    hits = [r for r in rows if any(k in (r[name_col] or "").lower() for k in keys)]
    if since:
        hits = [r for r in hits if (r[date_col] or "")[:4] >= since]
    hits.sort(key=lambda r: r[date_col] or "")
    for r in hits:
        print((r[date_col] or "")[:10], (r.get(id_col) or "").ljust(21), (r.get(tot_col) or "").rjust(9),
              (r[name_col] or "")[:100])
    print(f"-- {len(hits)} match(es) for {keys}")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
