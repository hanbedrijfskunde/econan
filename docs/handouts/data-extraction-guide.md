# Data Extraction Guide - ECONAN Week 2

## Overzicht

Deze handleiding legt uit hoe je financiële data uit jaarrekeningen extraheert en structureert met behulp van de ECONAN templates. Dit is een **kritieke stap** voor Week 3 ratio analyse.

---

## Waarom Template-Based Data Extraction?

### Het Probleem

Jaarrekeningen van verschillende bedrijven gebruiken verschillende formats:

- **Ahold Delhaize**: "Property, plant and equipment, net"
- **Carrefour**: "Tangible fixed assets"
- **Casino Group**: "PPE (net book value)"

➡️ **Probleem**: Directe vergelijking is lastig!

### De Oplossing: Gestandaardiseerde Templates

✅ **Consistentie**: Alle 3 Analisten gebruiken exact dezelfde structuur
✅ **Vergelijkbaarheid**: Benchmark analyse wordt mogelijk
✅ **Kwaliteit**: Week 3 ratio berekeningen worden betrouwbaar
✅ **Efficiency**: AI tools werken beter met gestandaardiseerde formats

---

## De 3 Templates

### 1. Balance Sheet Template

**Bestand**: `background-docs/subjects/balance-sheet-template.md`

**Structuur**:

```markdown
## Assets
### Current Assets
* Cash and Cash Equivalents: [WAARDE]
* Other Net Receivables: [WAARDE]
* Inventory: [WAARDE]
* Other Current Assets: [WAARDE]

### Non-Current Assets
* Property Plant and Equipment: [WAARDE]
* Intangible Assets: [WAARDE]
* Other Non-Current Assets: [WAARDE]

**Total Assets: [WAARDE]**

## Liabilities
### Current Liabilities
* Trade Payables: [WAARDE]
* Progress Payments/Advances from Customers: [WAARDE]
* Other Current Liabilities: [WAARDE]

### Non-Current Liabilities
* Long Term Debt: [WAARDE]
* Provisions for Risks and Charges: [WAARDE]
* Other Non-Current Liabilities: [WAARDE]

**Total Liabilities: [WAARDE]**

## Stockholder's Equity
* Share Capital: [WAARDE]
* Other Reserves: [WAARDE]

**Total Equity: [WAARDE]**

**VERIFICATION: Total Assets = Total Liabilities + Total Equity**
```

### 2. Income Statement Template

**Bestand**: `background-docs/subjects/income-statement-template.md`

**Structuur**:

```markdown
* **Total Revenue**: [WAARDE]
* (Total Operating Expenses): [WAARDE]
* **Earnings Before Interest and Taxes (EBIT)**: [WAARDE]
* (Net Interest Expense): [WAARDE]
* (Income Tax Expense): [WAARDE]
* Discontinued Operations: [WAARDE]
* **Net Income**: [WAARDE]
```

### 3. Cash Flow Statement Template

**Bestand**: `background-docs/subjects/cash-flow-statement-template.md`

**Structuur**:

```markdown
## Cash Flow from Operating Activities
[SUB-ITEMS]
**Net Cash from Operations: [WAARDE]**

## Cash Flow from Investing Activities
[SUB-ITEMS]
**Net Cash from Investing: [WAARDE]**

## Cash Flow from Financing Activities
[SUB-ITEMS]
**Net Cash from Financing: [WAARDE]**

* **Change In Cash and Cash Equivalents**: [WAARDE]
```

---

## Workflow: AI-Augmented Path

### Stap 1: Voorbereiding

**Benodigd**:

- Jaarrekening PDF (bijv. Ahold Delhaize Annual Report 2023)
- AI tool met PDF upload (Claude, ChatGPT, Gemini)
- Template files (balance-sheet, income-statement, cash-flow)

### Stap 2: PDF Upload

```text
Upload jaarrekening PDF naar je AI tool van keuze
```

### Stap 3: Prompt Engineering

**Template Prompt voor Balance Sheet**:

```text
Extract data from the [COMPANY NAME] [YEAR] Annual Report and fill this template:

## Assets
### Current Assets
* Cash and Cash Equivalents: [EXTRACT]
* Other Net Receivables: [EXTRACT]
* Inventory: [EXTRACT]
* Other Current Assets: [EXTRACT]

### Non-Current Assets
* Property Plant and Equipment: [EXTRACT]
* Intangible Assets: [EXTRACT]
* Other Non-Current Assets: [EXTRACT]

**Total Assets: [EXTRACT]**

## Liabilities
### Current Liabilities
* Trade Payables: [EXTRACT]
* Progress Payments/Advances from Customers: [EXTRACT]
* Other Current Liabilities: [EXTRACT]

### Non-Current Liabilities
* Long Term Debt: [EXTRACT]
* Provisions for Risks and Charges: [EXTRACT]
* Other Non-Current Liabilities: [EXTRACT]

**Total Liabilities: [EXTRACT]**

## Stockholder's Equity
* Share Capital: [EXTRACT]
* Other Reserves: [EXTRACT]

**Total Equity: [EXTRACT]**

INSTRUCTIONS:
1. Use € millions as the unit (convert if necessary)
2. Find the Consolidated Balance Sheet in the annual report
3. Replace [EXTRACT] with actual numeric values
4. Verify: Total Assets must equal Total Liabilities + Total Equity
5. If a line item is not present in the annual report, use: "Not reported"
6. Return ONLY the filled template with numbers
```

### Stap 4: Output Verificatie

**Check de AI output op**:

- [ ] Zijn alle [EXTRACT] placeholders vervangen door getallen?
- [ ] Zijn units consistent (€ millions)?
- [ ] Klopt de balans: Total Assets = Total Liabilities + Equity?
- [ ] Staan er geen rare waardes (bijv. negatieve cash)?

### Stap 5: Handmatige Controle

**CRITICAL**: AI maakt fouten! Controleer altijd:

1. Open de PDF op de Consolidated Balance Sheet pagina
2. Check 5 random line items:
   - Klopt "Cash and Cash Equivalents: €2,847"? → Check PDF
   - Klopt "Total Assets: €45,678"? → Check PDF
3. Bij afwijkingen: Corrigeer handmatig

### Stap 6: Opslaan

```text
Sla op als: balance-sheet-[bedrijfsnaam]-[jaar].md
```

**Voorbeeld**: `balance-sheet-ahold-delhaize-2024.md`

---

## Workflow: Conventional Path

### Stap 1: Voorbereiding

**Benodigd**:

- Jaarrekening PDF (bijv. Ahold Delhaize Annual Report 2023)
- Template files gekopieerd naar Word/Notepad
- Calculator (voor verificatie)

### Stap 2: Open Jaarrekening

```text
1. Open PDF
2. Zoek "Consolidated Balance Sheet" (vaak in "Financial Statements" sectie)
3. Noteer paginanummer: bijv. p.142
```

### Stap 3: Handmatige Data Extractie

**Voor elk template item**:

1. Zoek line item in PDF:
   - Template: "Cash and Cash Equivalents"
   - PDF: Zoek naar "Cash" of "Cash and cash equivalents"
2. Noteer waarde: €2,847 million
3. Check unit: million of thousand?
4. Vul in template: `* Cash and Cash Equivalents: €2,847`

**Herhaal voor alle ~20 balance sheet items**

### Stap 4: Totalen Berekenen

```text
1. Bereken Total Assets (som van alle asset items)
2. Bereken Total Liabilities (som van alle liability items)
3. Bereken Total Equity (som van equity items)
4. VERIFY: Total Assets = Total Liabilities + Total Equity
```

### Stap 5: Opslaan

```text
Sla op als: balance-sheet-[bedrijfsnaam]-[jaar].md
```

---

## Common Pitfalls & Oplossingen

### Probleem 1: Units Inconsistentie

**Symptoom**: Jaarrekening gebruikt € thousands, template verwacht € millions

**Oplossing**:

```text
PDF: "Cash: 2,847,000 (in thousands)"
Template: €2,847 (converted to millions)

Formule: thousands / 1000 = millions
         2,847,000 / 1000 = 2,847
```

### Probleem 2: Line Item Niet Gevonden

**Symptoom**: Template vraagt "Other Net Receivables", maar PDF heeft "Trade and other receivables"

**Oplossing**:

1. **Match semantisch**: "Trade and other receivables" ≈ "Other Net Receivables"
2. **Noteer bron**: `* Other Net Receivables: €1,234  # Source: "Trade and other receivables" p.142`
3. **Bij twijfel**: Ask docent of team

### Probleem 3: Balans Klopt Niet

**Symptoom**: Total Assets ≠ Total Liabilities + Equity

**Mogelijke oorzaken**:

1. **Typfout**: Controleer alle getallen opnieuw
2. **Missende item**: Heb je alle line items?
3. **Unit mismatch**: Zijn alle units € millions?
4. **Verkeerde kolom**: Heb je 2023 data (niet 2022)?

**Oplossing**: Check stappenplan opnieuw vanaf stap 1

### Probleem 4: Goodwill vs Intangible Assets

**Symptoom**: PDF heeft "Goodwill: €5,000" en "Other Intangibles: €2,000" apart

**Oplossing**:

```text
Template: Intangible Assets: €7,000  # Goodwill (€5,000) + Other (€2,000)
```

**Rationale**: Template combineert voor simpliciteit

---

## Verificatie Checklist (MANDATORY voor beide paths!)

### ✅ Totals Check

- [ ] **Balance Sheet**: Total Assets = Total Liabilities + Equity?
- [ ] **Income Statement**: Revenue - Expenses = Net Income (logisch)?
- [ ] **Cash Flow**: Operating + Investing + Financing = Change in Cash?

### ✅ Units Check

- [ ] Alle waardes in **€ millions** (of consistent andere unit)?
- [ ] Geen mix van thousands/millions/billions?

### ✅ Completeness Check

- [ ] Alle template items ingevuld (geen [EXTRACT] of [WAARDE] over)?
- [ ] Geen placeholder tekst zoals "TODO" of "TBD"?

### ✅ Source Traceability

- [ ] Kun je elke waarde terugvinden in jaarrekening?
- [ ] Heb je paginanummers genoteerd voor major items?

### ✅ Peer Review

- [ ] Heeft een andere Analyst (uit je team) je data gecontroleerd?
- [ ] Hebben jullie discrepancies besproken?

### ✅ Team Alignment

- [ ] Gebruiken alle 3 Analisten dezelfde template versie?
- [ ] Zijn units consistent across het team (alle € millions)?
- [ ] Kunnen jullie data side-by-side vergelijken?

---

## Output Format Voorbeeld

**Bestandsnaam**: `balance-sheet-ahold-delhaize-2024.md`

**Inhoud**:

```markdown
# Balance Sheet - Ahold Delhaize (2024)

**Source**: Annual Report 2024, p.142 (Consolidated Balance Sheet)
**Unit**: € millions
**Extracted by**: Analyst 1
**Date**: 2025-01-15
**Method**: AI-Augmented (Claude)

---

## Assets

### Current Assets
* Cash and Cash Equivalents: €2,847
* Other Net Receivables: €1,234
* Inventory: €3,456
* Other Current Assets: €987

**Total Current Assets: €8,524**

### Non-Current Assets
* Property Plant and Equipment: €12,345
* Intangible Assets: €7,654  # Goodwill (€5,000) + Other (€2,654)
* Other Non-Current Assets: €3,210

**Total Non-Current Assets: €23,209**

**Total Assets: €31,733**

---

## Liabilities

### Current Liabilities
* Trade Payables: €4,567
* Progress Payments/Advances from Customers: €234
* Other Current Liabilities: €2,890

**Total Current Liabilities: €7,691**

### Non-Current Liabilities
* Long Term Debt: €8,765
* Provisions for Risks and Charges: €1,234
* Other Non-Current Liabilities: €876

**Total Non-Current Liabilities: €10,875**

**Total Liabilities: €18,566**

---

## Stockholder's Equity

* Share Capital: €543
* Other Reserves: €12,624

**Total Equity: €13,167**

---

**VERIFICATION CHECK**:
Total Assets (€31,733) = Total Liabilities (€18,566) + Total Equity (€13,167) ✅ **KLOPT!**

---

**Notes**:
- "Other Net Receivables" matched to "Trade and other receivables" in annual report
- All values converted from € thousands to € millions for consistency
- Peer reviewed by: Analyst 2 (2025-01-16)
```

---

## Timing & Planning

### Week 2 Sessie (tijdens les)

- **10 min**: Live demo door docent (Ahold Delhaize voorbeeld)
- **10 min**: Team practice (1 template sectie proberen)

### Week 2 Huiswerk (thuis)

**Tijdsschatting**:

- **AI Path**: ~45-60 min per bedrijf (3 templates)
- **Conventional Path**: ~90-120 min per bedrijf (3 templates)

**Per Analyst**:

- Extractie: 3 templates × 1 bedrijf = 3 files
- Verificatie: 30 min (peer review + self-check)
- **Totaal**: 75-150 min

**Per Team**:

- 3 Analisten × 3 templates = 9 files totaal
- Alignment meeting: 15 min (check units, completeness)
- **Totaal team effort**: ~5-8 uur

### Week 3 Sessie (volgende week)

**CRITICAL**: Alle 3 Analisten moeten extracted data templates meebrengen!

- Management presenteert strategische vraag (5 min)
- Analisten tonen extracted data + verification (5 min)
- Week 3 ratio calculations kunnen direct starten ✅

---

## Hulp Nodig?

### Tijdens Sessie

- **Docent**: Stel vragen tijdens demo of practice time
- **Peer**: Werk samen met andere Analyst in je team

### Thuis (Huiswerk)

- **Team**: Post in team chat (Discord/Slack/Teams)
- **Docent**: Email voor technische vragen
- **AI Tool Issues**: Check AI tool documentatie (Claude, ChatGPT support)

### Veelgestelde Vragen

**Q: Welke AI tool moet ik gebruiken?**
A: Claude, ChatGPT, of Gemini werken allemaal. Kies degene waar je toegang tot hebt.

**Q: Mag ik switchen tussen AI en Conventional tijdens extractie?**
A: Ja! Je kunt AI gebruiken voor eerste draft, dan handmatig verifiëren/corrigeren.

**Q: Wat als mijn bedrijf een andere currency gebruikt (USD, GBP)?**
A: Converteer naar € met exchange rate van reporting date. Noteer dit in je file header.

**Q: Moet ik alle sub-items in Cash Flow Statement invullen?**
A: Nee, alleen de 3 totalen: Operating, Investing, Financing + Change in Cash.

---

## Success Criteria

Je data extraction is succesvol als:

✅ Alle 3 templates compleet ingevuld
✅ Totals checks kloppen (balans, etc.)
✅ Units consistent (€ millions)
✅ Peer reviewed door teamgenoot
✅ Traceable naar jaarrekening (paginanummers)
✅ Aligned met andere 2 Analisten in je team
✅ **Klaar voor Week 3 ratio calculations!**

---

**Einde Data Extraction Guide**
