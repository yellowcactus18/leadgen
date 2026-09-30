import csv, glob
rows = []
for f in sorted(glob.glob("output/batch_*.csv")):
    rows += list(csv.DictReader(open(f)))
cols = ["first_name","last_name","title","company_name","ticker","source_url","confidence"]
with open("output/executives_all.csv","w",newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=cols); w.writeheader(); w.writerows(rows)
tickers = {r["ticker"] for r in csv.DictReader(open("data/companies.csv"))}
done = {r["ticker"] for r in rows}
print(f"{len(rows)} rows, {len(done)}/{len(tickers)} companies covered")
print("missing:", sorted(tickers - done))
print("not_found/low:", sorted({r["ticker"] for r in rows if r["confidence"] in ("not_found","low")}))
