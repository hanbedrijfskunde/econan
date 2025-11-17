# Verification Checklist - ECONAN Data Extraction Quality Control

## Waarom Verificatie Critical Is

> **"Garbage In = Garbage Out"**

Week 3 ratio berekeningen zijn **alleen betrouwbaar** als je Week 2 data extraction **100% correct** is.

**Impact van fouten**:

- ❌ Verkeerde Total Assets (€31,000 vs €31,733) → Foutieve ROA berekening
- ❌ Verkeerde units (thousands vs millions) → Ratio's zijn 1000x te hoog!
- ❌ Ontbrekende data → Ratio berekening onmogelijk

**✅ Deze checklist voorkomt deze fouten!**

---

## Verification Workflow

```text
┌─────────────────────┐
│  Data Extraction    │ (AI of Conventional)
│  (30-60 min)        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  SELF-CHECK         │ ◄── JE BENT HIER (10 min)
│  (deze checklist)   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  PEER REVIEW        │ (10 min)
│  (teamgenoot check) │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  TEAM ALIGNMENT     │ (5 min)
│  (3 Analysts sync)  │
└──────────┬──────────┘
           │
           ▼
        ✅ APPROVED
    Ready for Week 3!
```

---

## Checklist: Balance Sheet Template

### ✅ LEVEL 1: Completeness Check (2 min)

**Alle items ingevuld?**

- [ ] Cash and Cash Equivalents: `[waarde ingevuld, niet [EXTRACT]]`
- [ ] Other Net Receivables: `[waarde ingevuld]`
- [ ] Inventory: `[waarde ingevuld]`
- [ ] Other Current Assets: `[waarde ingevuld]`
- [ ] Property Plant and Equipment: `[waarde ingevuld]`
- [ ] Intangible Assets: `[waarde ingevuld]`
- [ ] Other Non-Current Assets: `[waarde ingevuld]`
- [ ] **Total Assets**: `[waarde ingevuld]`
- [ ] Trade Payables: `[waarde ingevuld]`
- [ ] Progress Payments/Advances: `[waarde ingevuld]`
- [ ] Other Current Liabilities: `[waarde ingevuld]`
- [ ] Long Term Debt: `[waarde ingevuld]`
- [ ] Provisions for Risks and Charges: `[waarde ingevuld]`
- [ ] Other Non-Current Liabilities: `[waarde ingevuld]`
- [ ] **Total Liabilities**: `[waarde ingevuld]`
- [ ] Share Capital: `[waarde ingevuld]`
- [ ] Other Reserves: `[waarde ingevuld]`
- [ ] **Total Equity**: `[waarde ingevuld]`

**Als iets niet ingevuld**: Ga terug naar extractie!

### ✅ LEVEL 2: Totals Verification (3 min)

**De Heilige Formule**:

```text
Total Assets = Total Liabilities + Total Equity
```

**Voorbeeld Check**:

```text
Total Assets: €31,733
Total Liabilities: €18,566
Total Equity: €13,167

Verify: €31,733 = €18,566 + €13,167
        €31,733 = €31,733 ✅ KLOPT!
```

- [ ] **Totals formule klopt (geen verschil)**

**Als formule NIET klopt**:

1. Check alle sub-totals:
   - [ ] Total Current Assets = som van current asset items?
   - [ ] Total Non-Current Assets = som van non-current asset items?
   - [ ] Total Current Liabilities = som van current liability items?
   - [ ] Total Non-Current Liabilities = som van non-current liability items?
2. Check typfouten (€31,733 vs €31,733)
3. Check of je dezelfde kolom gebruikt (2023 niet 2022)

### ✅ LEVEL 3: Units Consistency (2 min)

**Alle waardes in € millions?**

- [ ] Cash: `€2,847` (niet €2,847,000 thousands!)
- [ ] Total Assets: `€31,733` (niet €31.7 billions!)
- [ ] Consistent currency symbol: € (niet $, £, CHF)

**Test**: Zijn volgende waardes realistisch?

| Item | Typische Range (€M) | Jouw Waarde | Check |
|------|---------------------|-------------|-------|
| Cash | 100 - 10,000 | _______ | ✅/❌ |
| Total Assets | 1,000 - 100,000 | _______ | ✅/❌ |
| Total Equity | 500 - 50,000 | _______ | ✅/❌ |

**Als waardes >€1 trillion of <€1 million**: Check je units!

### ✅ LEVEL 4: Source Traceability (3 min)

**Kun je waardes terugvinden in jaarrekening?**

**Random Sample Test**: Check 5 willekeurige items:

1. [ ] Open jaarrekening PDF op Consolidated Balance Sheet pagina
2. [ ] Zoek "Cash and Cash Equivalents" → Waarde klopt met template? ✅/❌
3. [ ] Zoek "Total Assets" → Waarde klopt? ✅/❌
4. [ ] Zoek "Long Term Debt" → Waarde klopt? ✅/❌
5. [ ] Zoek "Share Capital" → Waarde klopt? ✅/❌
6. [ ] Zoek "Total Equity" → Waarde klopt? ✅/❌

**Als 1+ items NIET kloppen**: Controleer alle waardes opnieuw!

---

## Checklist: Income Statement Template

### ✅ LEVEL 1: Completeness Check (1 min)

- [ ] Total Revenue: `[waarde ingevuld]`
- [ ] Total Operating Expenses: `[waarde ingevuld]`
- [ ] EBIT: `[waarde ingevuld]`
- [ ] Net Interest Expense: `[waarde ingevuld]`
- [ ] Income Tax Expense: `[waarde ingevuld]`
- [ ] Discontinued Operations: `[waarde ingevuld of €0]`
- [ ] Net Income: `[waarde ingevuld]`

### ✅ LEVEL 2: Sanity Check (2 min)

**Logische Flow**:

```text
Revenue > EBIT > Net Income (normaal gesproken)
```

**Test**:

- [ ] Revenue > 0? (bedrijf moet omzet hebben!)
- [ ] EBIT < Revenue? (kosten kunnen niet hoger zijn dan omzet, unless loss-making)
- [ ] Net Income < EBIT? (interest + tax reduceren EBIT)

**Profit Margin Check**:

```text
Profit Margin = (Net Income / Revenue) × 100%
```

| Sector | Typische Margin | Jouw Margin | Check |
|--------|-----------------|-------------|-------|
| Retail | 2-5% | ______% | ✅/❌ |
| Tech | 15-25% | ______% | ✅/❌ |
| Utilities | 8-12% | ______% | ✅/❌ |
| Energy | 5-10% | ______% | ✅/❌ |

**Als margin >50% of <-20%**: Double-check je cijfers!

### ✅ LEVEL 3: Units Consistency (1 min)

- [ ] Alle waardes in € millions (consistent met Balance Sheet)
- [ ] Revenue realistic? (bijv. Ahold Delhaize ~€80,000M, Shell ~€350,000M)

### ✅ LEVEL 4: Source Traceability (2 min)

**Random Sample Test**: Check 3 items:

1. [ ] Open PDF op Consolidated Income Statement pagina
2. [ ] Total Revenue → Klopt? ✅/❌
3. [ ] EBIT (or "Operating Profit") → Klopt? ✅/❌
4. [ ] Net Income (or "Profit for the year") → Klopt? ✅/❌

---

## Checklist: Cash Flow Statement Template

### ✅ LEVEL 1: Completeness Check (1 min)

- [ ] Net Cash from Operating Activities: `[waarde ingevuld]`
- [ ] Net Cash from Investing Activities: `[waarde ingevuld]`
- [ ] Net Cash from Financing Activities: `[waarde ingevuld]`
- [ ] Change in Cash and Cash Equivalents: `[waarde ingevuld]`

### ✅ LEVEL 2: Totals Verification (2 min)

**De Formule**:

```text
Change in Cash = Operating + Investing + Financing
```

**Voorbeeld**:

```text
Operating: €10,000
Investing: -€2,000
Financing: -€7,000

Change in Cash: €10,000 + (-€2,000) + (-€7,000) = €1,000 ✅
```

- [ ] **Formule klopt**

**Als formule NIET klopt**: Re-check alle 3 cash flow categories in PDF!

### ✅ LEVEL 3: Sanity Check (2 min)

**Typical Patterns**:

| Bedrijf Type | Operating | Investing | Financing |
|--------------|-----------|-----------|-----------|
| **Mature** (Coca-Cola) | ➕ Positief | ➖ Negatief (klein) | ➖ Negatief (dividends) |
| **Growth** (Tesla) | ➕ Positief | ➖➖ Zeer Negatief (CapEx) | ➕ Positief (funding) |
| **Distressed** | ➖ Negatief | ➕ Positief (sell assets) | ➕ Positief (emergency funding) |

- [ ] Past jouw bedrijf in een van deze patterns?
- [ ] Zo niet, kun je uitleggen waarom? (bijv. special dividend, grote acquisition)

### ✅ LEVEL 4: Cross-Check met Balance Sheet (2 min)

**Cash Continuity Check**:

```text
Balance Sheet (2022): Cash = €2,500
Cash Flow (2023): Change in Cash = +€347
Balance Sheet (2023): Cash = €2,847 ✅ KLOPT (€2,500 + €347)
```

- [ ] **Cash continuity klopt tussen jaren**

**Als NIET klopt**: Check of je de juiste jaren gebruikt (2023 vs 2022)

---

## Peer Review Protocol

### Stap 1: Swap Files (1 min)

**Binnen je team**:

- Analyst 1 reviewed door → Analyst 2
- Analyst 2 reviewed door → Analyst 3
- Analyst 3 reviewed door → Analyst 1

**Deel**:

- Je 3 template files (balance-sheet, income-statement, cash-flow)
- Jaarrekening PDF

### Stap 2: Peer Check (5 min per file set)

**Peer reviewt**:

1. [ ] **Completeness**: Alle items ingevuld?
2. [ ] **Totals**: Formules kloppen (Assets = Liab + Equity, Cash flow formula)?
3. [ ] **Units**: Consistent € millions?
4. [ ] **Traceability**: Sample 3 random items → Check tegen PDF → Kloppen ze?

**Feedback format**:

```markdown
**Peer Review by: Analyst 2**
**Date**: 2025-01-16
**Files reviewed**: Balance Sheet, Income Statement, Cash Flow

**Issues found**:
1. Balance Sheet: Inventory was €3,456,000 (thousands) → should be €3,456 (millions) ❌
2. Income Statement: All OK ✅
3. Cash Flow: Change in Cash formula had typo (€1,100 vs €1,000) ❌

**Corrections made**: Yes (by original Analyst)
**Re-verified**: Yes ✅
**Status**: ✅ APPROVED
```

### Stap 3: Address Feedback (2 min)

**Original Analyst**:

1. Read peer feedback
2. Correct issues
3. Re-verify totals formulas
4. Confirm with peer: "Fixed! Please re-check"

### Stap 4: Final Sign-Off (1 min)

**Add to template file header**:

```markdown
**Peer Reviewed**: ✅ Yes
**Reviewed by**: Analyst 2
**Review date**: 2025-01-16
**Status**: Approved for Week 3
```

---

## Team Alignment Check (3 Analisten samen)

### Meeting Agenda (15 min total)

**Check 1: Template Structure Aligned** (3 min)

- [ ] Alle 3 Analisten gebruiken exact dezelfde template versie?
- [ ] Headings identical? (bijv. "Cash and Cash Equivalents" niet "Cash")
- [ ] Structuur identical? (zelfde order van items)

**Check 2: Units Aligned** (2 min)

- [ ] Alle 3 Analisten gebruiken € millions?
- [ ] Geen mix van thousands/millions/billions?

**Check 3: Side-by-Side Comparability Test** (5 min)

**Maak een quick comparison table**:

| Metric | Analyst 1 (AH) | Analyst 2 (Carrefour) | Analyst 3 (Casino) |
|--------|----------------|----------------------|-------------------|
| **Total Assets** | €31,733 | €XX,XXX | €XX,XXX |
| **Total Equity** | €13,167 | €XX,XXX | €XX,XXX |
| **Revenue** | €87,534 | €XX,XXX | €XX,XXX |
| **Net Income** | €2,456 | €XX,XXX | €XX,XXX |

**Vragen**:

- [ ] Kunnen we deze cijfers direct vergelijken? ✅/❌
- [ ] Zijn relatieve groottes logisch? (AH > Casino in assets?) ✅/❌
- [ ] Zien we geen rare outliers (bijv. 1000x verschil)? ✅/❌

**Check 4: Data Quality Agreement** (3 min)

**Team akkoord**:

- [ ] Alle 9 files (3 Analysts × 3 templates) zijn compleet
- [ ] Alle files zijn peer reviewed
- [ ] Totals formulas kloppen voor alle files
- [ ] Units consistent (€ millions)
- [ ] **TEAM IS READY FOR WEEK 3 RATIO CALCULATIONS** ✅

**Sign-Off**:

```markdown
**Team Alignment Check - [Team Name]**
**Date**: 2025-01-17
**Participants**: Analyst 1 ([naam]), Analyst 2 ([naam]), Analyst 3 ([naam])

**Files verified**: 9/9 ✅
- Balance Sheets: 3/3 ✅
- Income Statements: 3/3 ✅
- Cash Flow Statements: 3/3 ✅

**Issues found**: [aantal]
**Issues resolved**: [aantal] ✅

**Decision**: APPROVED for Week 3
**Signed**: [Analyst 1], [Analyst 2], [Analyst 3]
```

### Check 5: Week 3 Readiness (2 min)

**Final Checklist**:

- [ ] Alle 3 Analisten hebben extracted data klaar
- [ ] Data is verified (self + peer)
- [ ] Team alignment compleet
- [ ] Files geüpload naar shared folder (Teams/Drive)
- [ ] **READY TO CALCULATE RATIOS IN WEEK 3!** 🎯

---

## Red Flags: Wanneer STOP & RE-CHECK

### 🚩 Red Flag 1: Totals Formule Klopt Niet

```text
Total Assets: €31,733
Total Liabilities + Equity: €31,500

Verschil: €233 ❌ STOP!
```

**Actie**: Re-check ALLE asset/liability/equity items tegen PDF

### 🚩 Red Flag 2: Profit Margin > 50%

```text
Revenue: €1,000
Net Income: €600
Margin: 60% ❌ ONREALISTISCH!
```

**Actie**: Check of je Revenue correct is (niet missing items?) + check Net Income

### 🚩 Red Flag 3: Cash Flow ≠ Change in Cash

```text
Operating: €10,000
Investing: -€2,000
Financing: -€7,000
Totaal: €1,000

Change in Cash gerapporteerd: €500 ❌ KLOPT NIET!
```

**Actie**: Re-check alle 3 cash flow categories tegen PDF

### 🚩 Red Flag 4: Total Assets < Total Equity

```text
Total Assets: €10,000
Total Equity: €15,000 ❌ ONMOGELIJK!
```

**Rationale**: Equity kan nooit groter zijn dan Assets (tenzij negatieve liabilities, zeer zeldzaam)

**Actie**: Check units (is één in thousands, ander in millions?)

### 🚩 Red Flag 5: Peer Reviewer Vindt 3+ Fouten

**Actie**: Start opnieuw met data extraction (AI prompt verbeteren of handmatige extractie)

---

## Success Criteria: Ben je Week 3 Ready?

### Individual Analyst Checklist

- [ ] **3 templates compleet**: Balance Sheet ✅, Income Statement ✅, Cash Flow ✅
- [ ] **Self-check passed**: Alle Level 1-4 checks gedaan
- [ ] **Totals verified**: Formules kloppen (Balance Sheet + Cash Flow)
- [ ] **Units consistent**: € millions overal
- [ ] **Peer reviewed**: Door teamgenoot gecontroleerd + approved
- [ ] **Header compleet**: Source, unit, date, method ingevuld

### Team Checklist (3 Analisten)

- [ ] **9 files compleet**: 3 bedrijven × 3 templates
- [ ] **All peer reviewed**: Elke Analyst heeft review ontvangen
- [ ] **Team alignment done**: Side-by-side comparability check passed
- [ ] **Units aligned**: Alle 3 Analisten gebruiken € millions
- [ ] **Data quality approved**: Team sign-off compleet
- [ ] **Files shared**: Geüpload naar team folder

### Week 3 Readiness Indicator

```text
✅ GREEN (GO): All checks passed → START RATIO CALCULATIONS WEEK 3!
🟡 YELLOW (CAUTION): 1-2 minor issues → Fix before Week 3
🔴 RED (STOP): 3+ issues or major red flag → Re-do extraction
```

**Target**: 🟢 **GREEN** voor alle teams!

---

## Troubleshooting: Veelvoorkomende Verificatie Problemen

### Probleem 1: "Peer reviewer en ik komen tot andere cijfers"

**Diagnose**:

- Check: Gebruiken jullie dezelfde PDF versie? (2023 report, niet 2022)
- Check: Kijken jullie naar dezelfde pagina? (Consolidated vs Parent Company)
- Check: Zelfde kolom? (31-Dec-2023 vs 31-Dec-2022 in PDF)

### Probleem 2: "Balance Sheet klopt, maar Cash Flow niet"

**Diagnose**:

- Cash Flow is complexer (heeft sub-items)
- Check: Heb je "Net Cash from Operations" (totaal) of alleen "Cash from sales" (sub-item)?
- Oplossing: Zoek de **totals** voor Operating/Investing/Financing, niet sub-items

### Probleem 3: "AI geeft elke keer andere cijfers"

**Diagnose**:

- AI is niet deterministic (randomness in output)
- Oplossing 1: Run AI 3x, check welke cijfers consistent zijn
- Oplossing 2: Switch naar Conventional (handmatige extractie)
- Oplossing 3: Use AI voor draft, manual verification voor final

### Probleem 4: "Team heeft geen tijd voor peer review"

**Reality check**: **Peer review is MANDATORY!**

- Zonder peer review: 30% kans op fouten in data
- Met peer review: <5% kans op fouten
- Week 3 ratio calculations met foute data = **garbage output**

**Oplossing**: Schedule 30 min peer review session (15 min each way)

---

## Appendix: Verification Formula Reference

### Balance Sheet

```text
Total Assets = Total Liabilities + Total Equity
Total Assets = Current Assets + Non-Current Assets
Total Liabilities = Current Liabilities + Non-Current Liabilities
```

### Income Statement

```text
EBIT = Revenue - Operating Expenses
EBT = EBIT - Net Interest Expense
Net Income = EBT - Income Tax + Discontinued Operations
```

### Cash Flow Statement

```text
Change in Cash = Operating CF + Investing CF + Financing CF
```

### Cross-Statement Verification

```text
Balance Sheet Cash (2023) = Balance Sheet Cash (2022) + Change in Cash (2023)
```

---

**Einde Verification Checklist**

**Final Reminder**: **Verification is niet optioneel - het is essentieel voor Week 3 succes!** 🎯
