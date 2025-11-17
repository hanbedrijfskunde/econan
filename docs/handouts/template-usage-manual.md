# Template Usage Manual - ECONAN Financial Statement Templates

## Doel van dit Document

Deze handleiding legt uit hoe je de 3 ECONAN financial statement templates gebruikt om data uit jaarrekeningen te structureren. De templates zorgen voor consistentie tussen alle Analisten in je team.

---

## De 3 Templates: Overzicht

| Template | Doel | Tijd (AI) | Tijd (Manual) |
|----------|------|-----------|---------------|
| **Balance Sheet** | Bezittingen & Schulden structuur | 20 min | 40 min |
| **Income Statement** | Winst & Verlies structuur | 15 min | 30 min |
| **Cash Flow Statement** | Kasstroom activiteiten structuur | 15 min | 30 min |

**Totaal per bedrijf**: ~50 min (AI) of ~100 min (Manual)

---

## Template 1: Balance Sheet Template

### Locatie

`background-docs/subjects/balance-sheet-template.md`

### Structuur Uitleg

```markdown
## Assets (Bezittingen)
### Current Assets (Vlottende Activa - < 1 jaar liquide)
* Cash and Cash Equivalents
* Other Net Receivables
* Inventory
* Other Current Assets

### Non-Current Assets (Vaste Activa - > 1 jaar)
* Property Plant and Equipment (PPE)
* Intangible Assets
* Other Non-Current Assets

## Liabilities (Schulden)
### Current Liabilities (Kortlopende Schulden - < 1 jaar betalen)
* Trade Payables
* Progress Payments/Advances from Customers
* Other Current Liabilities

### Non-Current Liabilities (Langlopende Schulden - > 1 jaar)
* Long Term Debt
* Provisions for Risks and Charges
* Other Non-Current Liabilities

## Stockholder's Equity (Eigen Vermogen)
* Share Capital
* Other Reserves
```

### Mapping: Template ↔ Jaarrekening

**Probleem**: Jaarrekeningen gebruiken verschillende termen voor hetzelfde concept!

| Template Term | Mogelijke Jaarrekening Termen |
|---------------|------------------------------|
| **Cash and Cash Equivalents** | "Cash", "Cash at bank", "Liquid assets", "Short-term investments" |
| **Other Net Receivables** | "Trade receivables", "Accounts receivable", "Trade and other receivables" |
| **Inventory** | "Inventories", "Stock", "Merchandise inventory" |
| **Property Plant and Equipment** | "PPE", "Tangible fixed assets", "Property and equipment", "Fixed assets" |
| **Intangible Assets** | "Goodwill and intangibles", "Intangible fixed assets", "Patents and trademarks" |
| **Trade Payables** | "Accounts payable", "Trade and other payables", "Suppliers" |
| **Long Term Debt** | "Non-current borrowings", "Long-term loans", "Bonds payable" |

**Richtlijn**: Match op **betekenis**, niet op exacte woorden!

### Speciale Gevallen

#### Geval 1: Goodwill Separate Gerapporteerd

**Jaarrekening**:

```text
Goodwill: €5,000
Other Intangible Assets: €2,000
```

**Template Oplossing**:

```markdown
* Intangible Assets: €7,000  # Goodwill (€5,000) + Other (€2,000)
```

#### Geval 2: Sub-Items Zijn Geaggregeerd

**Jaarrekening**:

```text
Current Assets: €10,000 (total, geen breakdown)
```

**Template Oplossing**:

```markdown
### Current Assets
* Cash and Cash Equivalents: Not separately reported
* Other Net Receivables: Not separately reported
* Inventory: Not separately reported
* Other Current Assets: Not separately reported

**Total Current Assets: €10,000**
```

#### Geval 3: Extra Items in Jaarrekening

**Jaarrekening heeft**:

```text
Deferred Tax Assets: €500
```

**Template Oplossing**:

```markdown
* Other Non-Current Assets: €3,500  # Includes Deferred Tax (€500) + Other (€3,000)
```

### Verificatie Formule

```text
CRITICAL CHECK:
Total Assets = Total Liabilities + Total Equity

Als dit NIET klopt → er is een fout in je extractie!
```

---

## Template 2: Income Statement Template

### Locatie

`background-docs/subjects/income-statement-template.md`

### Structuur Uitleg

```markdown
* Total Revenue (Totale Omzet)
* (Total Operating Expenses) (Operationele Kosten)
* Earnings Before Interest and Taxes (EBIT) (Operationele Winst)
* (Net Interest Expense) (Rentekosten min rentebaten)
* (Income Tax Expense) (Belastingen)
* Discontinued Operations (Gestopte activiteiten)
* Net Income (Netto Winst)
```

**Flow**:

```text
Revenue (€100)
  - Operating Expenses (€60)
  = EBIT (€40)
  - Interest (€5)
  = EBT (€35)
  - Tax (€10)
  = Net Income (€25)
```

### Mapping: Template ↔ Jaarrekening

| Template Term | Mogelijke Jaarrekening Termen |
|---------------|------------------------------|
| **Total Revenue** | "Sales", "Net sales", "Turnover", "Net revenue" |
| **Total Operating Expenses** | "Cost of sales + Operating expenses", "COGS + SG&A", "Total costs" |
| **EBIT** | "Operating profit", "Operating income", "Profit before interest and tax" |
| **Net Interest Expense** | "Finance costs - Finance income", "Interest expense net", "Net financial result" |
| **Income Tax Expense** | "Income tax", "Tax expense", "Provision for income taxes" |
| **Net Income** | "Profit for the year", "Net profit", "Earnings", "Bottom line" |

### Speciale Gevallen

#### Geval 1: EBIT Niet Direct Gerapporteerd

**Jaarrekening heeft**:

```text
Revenue: €100
Operating expenses: €60
Depreciation: €10
(geen expliciete "EBIT" regel)
```

**Berekening**:

```text
EBIT = Revenue - Operating Expenses - Depreciation
EBIT = €100 - €60 - €10 = €30
```

**Template**:

```markdown
* Earnings Before Interest and Taxes (EBIT): €30  # Calculated: Revenue - Op.Exp - Depr.
```

#### Geval 2: Discontinued Operations

**Als jaarrekening GEEN discontinued operations heeft**:

```markdown
* Discontinued Operations: €0  # Not applicable
```

**Als jaarrekening WEL discontinued operations heeft**:

```markdown
* Discontinued Operations: €500  # Profit from discontinued ops (see Note 12)
```

### Verificatie Formule

```text
SANITY CHECK:
Net Income = Revenue - All Expenses - Interest - Tax + Other Items

Typical Profit Margin (Net Income / Revenue):
- Retail: 2-5%
- Tech: 15-25%
- Utilities: 8-12%

Als je profit margin 50%+ is → check je cijfers!
```

---

## Template 3: Cash Flow Statement Template

### Locatie

`background-docs/subjects/cash-flow-statement-template.md`

### Structuur Uitleg

```markdown
## Cash Flow from Operating Activities (Operationele Kasstroom)
  [Sub-items zoals depreciation, working capital changes]
  **Net Cash from Operations: [WAARDE]**

## Cash Flow from Investing Activities (Investerings Kasstroom)
  [Sub-items zoals capital expenditures, acquisitions]
  **Net Cash from Investing: [WAARDE]**

## Cash Flow from Financing Activities (Financierings Kasstroom)
  [Sub-items zoals debt issuance, dividends]
  **Net Cash from Financing: [WAARDE]**

* **Change In Cash and Cash Equivalents**: [WAARDE]
```

### De 3 Categorieën

| Categorie | Wat zit erin? | Typisch + of -? |
|-----------|---------------|-----------------|
| **Operating** | Cash van core business (earnings + working capital) | Positief (gezond bedrijf) |
| **Investing** | Kopen/verkopen assets (CapEx, acquisitions) | Negatief (groeiend bedrijf) |
| **Financing** | Debt/equity transacties (leningen, dividends) | Varieert |

**Voorbeeld Mature Bedrijf (Coca-Cola)**:

```text
Operating: +€10,000 (geld verdienen met verkoop)
Investing: -€2,000 (kopen nieuwe bottling plants)
Financing: -€7,000 (dividends betalen + debt aflossen)
Change in Cash: +€1,000
```

**Voorbeeld Growth Bedrijf (Tesla)**:

```text
Operating: +€5,000
Investing: -€15,000 (nieuwe Gigafactories)
Financing: +€12,000 (nieuwe leningen + aandelen uitgifte)
Change in Cash: +€2,000
```

### Template Simplificatie

**BELANGRIJK**: Voor ECONAN Week 2/3 hoef je **alleen de totalen** te extracten:

```markdown
## Cash Flow from Operating Activities
**Net Cash from Operations: €10,000**

## Cash Flow from Investing Activities
**Net Cash from Investing: -€2,000**

## Cash Flow from Financing Activities
**Net Cash from Financing: -€7,000**

* **Change In Cash and Cash Equivalents**: €1,000
```

**Je HOEFT NIET alle sub-items (zoals "Depreciation", "CapEx") in te vullen voor Week 2!**

### Verificatie Formule

```text
CRITICAL CHECK:
Change in Cash = Operating + Investing + Financing

Voorbeeld:
€1,000 = €10,000 + (-€2,000) + (-€7,000) ✅ KLOPT
```

---

## Unit Conversions

### Probleem: Verschillende Eenheden in Jaarrekeningen

| Jaarrekening Unit | Voorbeeld Waarde | Conversie naar € millions |
|-------------------|------------------|---------------------------|
| **€ thousands** | 2,847,000 | ÷ 1,000 = 2,847 |
| **€ millions** | 2,847 | No conversion (already millions) |
| **€ billions** | 2.847 | × 1,000 = 2,847 |
| **USD thousands** | $3,000,000 | ÷ 1,000 × EUR/USD rate |

### ECONAN Standaard: € Millions

**Waarom € millions?**

- ✅ Meeste Euronext bedrijven rapporteren in millions
- ✅ Makkelijk te lezen (niet te veel nullen)
- ✅ Consistent voor benchmark vergelijking

**Voorbeeld Conversie**:

**Jaarrekening**: "Cash and cash equivalents: €2,847,000 (in thousands)"

**Template**: `* Cash and Cash Equivalents: €2,847  # Converted from thousands`

### USD/GBP Bedrijven

**Als jaarrekening in USD**:

1. Vind exchange rate op reporting date (bijv. 31 Dec 2023: 1 EUR = 1.10 USD)
2. Converteer: USD value ÷ 1.10 = EUR value
3. Noteer in header:

```markdown
# Balance Sheet - [Company] (2023)
**Source Currency**: USD
**Conversion Rate**: 1 EUR = 1.10 USD (31-Dec-2023)
**Unit**: € millions (converted from USD)
```

---

## Best Practices

### 1. Header Altijd Invullen

```markdown
# [Template Type] - [Company Name] (Year)

**Source**: Annual Report [Year], p.[XX]
**Unit**: € millions
**Extracted by**: Analyst [1/2/3]
**Date**: YYYY-MM-DD
**Method**: [AI-Augmented / Conventional]
**Peer Reviewed**: [Yes/No - by whom]
```

### 2. Comments Gebruiken voor Clarity

```markdown
* Intangible Assets: €7,000  # Goodwill (€5,000) + Other (€2,654)
* Other Current Assets: €987  # Includes prepayments (€200) + deferred charges (€787)
```

### 3. Source Traceability

**Voor major items, noteer paginanummer**:

```markdown
* Total Assets: €31,733  # Source: p.142, line "Total assets"
```

### 4. Peer Review Protocol

**Na extractie**:

1. Swap files met andere Analyst in je team
2. Check 5 random items tegen de PDF
3. Verify totals formulas (Assets = Liab + Equity)
4. Sign off:

```markdown
**Peer Review**:
- Reviewed by: Analyst 2
- Date: 2025-01-16
- Issues found: 1 (Inventory unit was thousands, corrected to millions)
- Status: ✅ Approved
```

---

## Troubleshooting

### Probleem 1: "Ik kan een line item niet vinden in de jaarrekening"

**Oplossingen**:

1. **Zoek alternatieven**: Bijv. "PPE" kan ook "Tangible assets" zijn
2. **Check notes**: Soms staat detail in notes (bijv. Note 5: Property, Plant and Equipment)
3. **Aggregate oplossing**: Als echt niet te vinden, gebruik "Other" categorie

**Voorbeeld**:

```markdown
* Other Current Assets: €2,000  # Unable to locate specific breakdown
```

### Probleem 2: "Totals kloppen niet"

**Debug Stappenplan**:

1. Check alle getallen opnieuw (typfouten?)
2. Check units (mix van thousands/millions?)
3. Check of je alle sub-items hebt (mis je een categorie?)
4. Check kolom (gebruik je 2023, niet 2022 data?)

### Probleem 3: "Jaarrekening heeft 50 line items, template heeft 10"

**Oplossing**: **Aggregate!**

**Jaarrekening**:

```text
Buildings: €5,000
Land: €2,000
Machinery: €3,000
Vehicles: €1,000
```

**Template**:

```markdown
* Property Plant and Equipment: €11,000  # Buildings + Land + Machinery + Vehicles
```

### Probleem 4: "AI geeft inconsistente output"

**Voorbeeld**: First time AI zegt "€2,847", second time "€2.847 billion"

**Oplossing**:

1. **Specifieke prompt**: "Return values in € millions format: e.g. €2,847 (not billions, not thousands)"
2. **Verification layer**: Check AI output tegen PDF manually
3. **Conventional fallback**: Als AI blijft falen, switch naar handmatige extractie

---

## Checklist: Ben ik klaar?

### Voor elk template:

- [ ] Header compleet ingevuld (source, unit, date, method)
- [ ] Alle items ingevuld (geen [EXTRACT] placeholders over)
- [ ] Units consistent (€ millions overal)
- [ ] Totals verified (formules kloppen)
- [ ] Comments toegevoegd waar nodig (voor clarity)
- [ ] Peer reviewed door teamgenoot

### Voor het team (3 Analisten):

- [ ] Alle 3 bedrijven hebben 3 templates = 9 files totaal
- [ ] Alle 3 Analisten gebruiken dezelfde unit (€ millions)
- [ ] Template structuur identical (zelfde headings, zelfde indeling)
- [ ] Data side-by-side vergelijkbaar
- [ ] **Ready for Week 3 ratio calculations!**

---

## Appendix: Template Files Locaties

| Template | Locatie | Doel |
|----------|---------|------|
| Balance Sheet | `background-docs/subjects/balance-sheet-template.md` | Bezittingen & Schulden |
| Income Statement | `background-docs/subjects/income-statement-template.md` | Winst & Verlies |
| Cash Flow Statement | `background-docs/subjects/cash-flow-statement-template.md` | Kasstroom |

**Download instructie**:

1. Navigeer naar `background-docs/subjects/`
2. Open template file
3. Copy/paste naar je working document (Word/Notepad/Markdown editor)
4. Begin met extractie!

---

**Einde Template Usage Manual**
