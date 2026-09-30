# Executive Lead List – Plan & Instructions

## Goal
For each of the 427 companies in `data/companies.csv`, find the **CEO and CFO**.
If a role can't be found, use any other C-suite executive (COO, CMO, CSO, CTO, CBO, CCO, President…).

## Output format
One file per batch: `output/batch_XX.csv`, with these columns in this order:

```
first_name,last_name,title,company_name,ticker,source_url,confidence
```

- Write **one row per person**. A company normally gets 2 rows (CEO + CFO).
- `title`: the exact title, e.g. `Chief Executive Officer`, `Chief Financial Officer`,
  `Interim CFO`, `President & CEO`.
- `source_url`: where the name was confirmed. Prefer the company's IR/leadership page,
  then SEC filings, press releases, and finally LinkedIn or news.
- `confidence`: `high` means confirmed on an official source from 2025–2026. `medium` means a
  news source or older page. `low` means unclear or possibly outdated.
- If nothing is found, write one row with empty name fields and `confidence=not_found`.
- Leave out suffixes and credentials (M.D., Ph.D., Jr.) in the name fields. Middle initials can
  be dropped.

## Steps for each batch
1. Read `data/batches/batch_XX.csv` (25 companies).
2. For each company, web-search `"<company name>" CEO CFO leadership` and prefer the
   company's own "Leadership / Management team" page.
3. Watch for recent changes: interim roles, acquisitions, bankruptcies (for example SGMOQ),
   and recent IPOs or de-SPACs whose names differ from the ticker.
4. Write `output/batch_XX.csv`, then commit and push.
5. Run 3–4 batches in parallel with subagents.

## Merge
Once every batch is done, run `python3 scripts/merge.py` to build `output/executives_all.csv`
and print a summary of the not_found and low-confidence rows.

## Progress
Check which batches are done with `ls output/`.
