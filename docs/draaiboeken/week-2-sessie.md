# Week 2 Draaiboek: Financial Statement Analysis Introductie

## Sessie Overzicht
**Doel**: Introductie tot Financial Statement Analysis als fundament voor data-gedreven business besluitvorming
**Duur**: 1 sessie van 2 uur (120 minuten)
**Connectie**: BEDROM (conceptueel) → ECONAN (kwantitatief met data)

---

## Pre-Check: Hebben Teams de 3 Grote Beslissingen Genomen?

**Vóór de sessie begint**: Snelle poll (5 min)

Teams hebben al gedaan:
- ✅ Sector gekozen (uit BEDROM)
- ✅ Euronext bedrijf jaarrekening gedownload

**Te checken**: Hebben alle teams de **Decision Framework** afgerond?

### 3 Grote Beslissingen:

1. **Strategische Vraag**: Welke ECONAN vraag beantwoorden we?
   - Geformuleerd door Management rol
   - Rendement/risico/groei gerelateerd

2. **Rol Verdeling**:
   - Wie is **Management** (1 persoon)?
   - Wie zijn **Analisten** (3-4 personen)?

3. **Methodologie Keuze** (per Analist):
   - **AI-Augmented Path** of **Conventional Tools Path**?

**Actie**:
- ✅ Compleet → Sessie kan starten
- ❌ Niet compleet → 10 min team-time om af te ronden

---

## Sessie Structuur (120 minuten totaal)

### **Blok 1: BEDROM → ECONAN Bridge** (25 min)

**Activiteit**: Van conceptuele BEDROM analyse naar kwantitatieve ECONAN analyse

**1A. Recap & Reframe** (10 min)
- **Docent**: "In Week 1 kozen jullie je BEDROM sector. Nu gaan we van **kwalitatief** naar **kwantitatief**"
- **Plenaire vraag**: "Geef een voorbeeld van een BEDROM conclusie over je sector"
  - 3-4 studenten delen (1 min per student):
    - "Retail heeft hoge concurrentie"
    - "Energy sector heeft veel schulden"
    - "Healthcare heeft ESG risico's"
    - "Tech sector heeft hoge groei"
- **Docent**: "Vandaag leren we deze uitspraken om te zetten in **data met getallen**"

**1B. Docent Demonstratie** (12 min): "Van conceptueel naar data-gedreven"

**Voorbeeld 1: Winstgevendheid Retail Sector**
- **BEDROM**: "Retail sector heeft hoge concurrentie dus lage marges" (kwalitatief)
- **ECONAN**: Operating margin analyse met 3-bedrijven benchmark
  - **Analyst 1** (eigen bedrijf): Ahold Delhaize operating margin = 4.2%
  - **Analyst 2** (concurrent): Carrefour operating margin = 3.8%
  - **Analyst 3** (concurrent): Casino Group operating margin = 3.5%
  - **Externe benchmark**: Sector gemiddelde (CBS data) = 3.7%
  - **Data-gedreven conclusie**: "AH presteert +0.5pp boven concurrent gemiddelde (3.7%) → schaalvoordeel zichtbaar in data"

**Voorbeeld 2: Financiële Gezondheid Energy Sector**
- **BEDROM**: "Shell heeft veel schulden door olie-investeringen" (kwalitatief)
- **ECONAN**: Debt/Equity ratio berekenen met 3-bedrijven benchmark
  - **Analyst 1** (eigen bedrijf): Shell D/E = 0.50 (€75B debt / €150B equity)
  - **Analyst 2** (concurrent): BP D/E = 0.65
  - **Analyst 3** (concurrent): TotalEnergies D/E = 0.45
  - **Concurrent gemiddelde**: 0.55
  - **Data-gedreven conclusie**: "Shell D/E (0.50) onder concurrent gemiddelde → conservatiever gefinancierd dan peers"

**Voorbeeld 3: ESG Impact op Cost of Capital**
- **BEDROM**: "Duurzaamheid wordt belangrijker voor consumenten" (kwalitatief)
- **ECONAN**: ESG score correlatie met WACC (Refinitiv ESG data + jaarrekening)
  - Bedrijven ESG A-rating: gemiddelde WACC 6.2%
  - Bedrijven ESG C-rating: gemiddelde WACC 7.1%
  - **Data-gedreven conclusie**: "ESG verbetering kan 0.9pp WACC besparing opleveren → NPV impact calculeren"

**1C. Individuele Reflectie** (3 min)
- "Welke BEDROM inzichten kan ik kwantificeren met data?"
- Noteer 1-2 ideeën in je notities

**Doel**: LR-BEDROM-1 explicit bridge maken

---

### **Blok 2: Financial Statements & Data Extraction** (35 min)

#### **2A: De Drie Financiële Overzichten - Conceptueel** (15 min)

**Visualisatie**: Toon [accounting-balance-sheet.html](../background-docs/subjects/accounting-balance-sheet.html)

**Snelle Recap van de 3 Statements**:

**1. Balance Sheet (Balans)**:

```
Assets = Liabilities + Shareholders' Equity
```

- **Assets**: Current (cash, inventory, receivables) + Non-Current (PPE, intangibles)
- **Liabilities**: Current (payables, short-term debt) + Non-Current (long-term debt)
- **Equity**: Share capital + reserves
- **Kernbeperking**: Historical cost (backward-looking)

**2. Income Statement (Resultatenrekening)**:

```
Revenues (Opbrengsten)
- Costs (Kosten)
= Earnings (Winst)
```

**3. Cash Flow Statement (Kasstroomoverzicht)**:

```
Cash In (Geld binnen)
- Cash Out (Geld buiten)
= Net Cash Flow
```

**Kritisch Verschil**: Damodaran quote: **"You can't spend earnings, only cash"**

**Doel**: Basiskennis financiële overzichten opfrissen voor data extractie

---

#### **2B: Template-Based Data Extraction Workshop** (20 min)

**Doel**: Leer data uit jaarrekeningen te structureren met standaard templates

**Waarom templates gebruiken?**

- ✅ **Consistentie**: Alle 3 Analisten gebruiken dezelfde structuur
- ✅ **Vergelijkbaarheid**: Benchmark data tussen bedrijven is direct te vergelijken
- ✅ **Kwaliteit**: Gestructureerde data voorkomt fouten in Week 3 ratio berekeningen
- ✅ **Efficiency**: AI kan beter werken met gestandaardiseerde output formaten

**De 3 Templates**:

1. **[balance-sheet-template.md](../background-docs/subjects/balance-sheet-template.md)** - Balans structuur
2. **[income-statement-template.md](../background-docs/subjects/income-statement-template.md)** - Resultatenrekening structuur
3. **[cash-flow-statement-template.md](../background-docs/subjects/cash-flow-statement-template.md)** - Kasstroom structuur

---

**Docent Demonstratie** (10 min): "Data Extraction in actie"

**Voorbeeld: Ahold Delhaize Annual Report 2023 → Balance Sheet Template**

**Stap 1: Open jaarrekening** (PDF pagina 142: Consolidated Balance Sheet)

**Stap 2A: AI-Augmented Path**

*Prompt voorbeeld*:

```
Extract the following data from the Ahold Delhaize 2023 Annual Report
Consolidated Balance Sheet (page 142) and format it according to this template:

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

[... rest of template ...]

Return ONLY the filled template with actual € millions values.
Verify totals: Total Assets must equal Total Liabilities + Equity.
```

**Stap 2B: Conventional Path**

*Handmatig*:
- Open template in Word/Notepad
- Zoek "Cash and Cash Equivalents" in PDF
- Kopieer waarde: €2,847 million
- Plak in template regel
- Herhaal voor alle items

---

**Stap 3: Verificatie** (CRITICAL voor beide paths!)

**Verificatie Checklist**:

- [ ] **Totals Check**: Total Assets = Total Liabilities + Equity? (moet kloppen!)
- [ ] **Units Check**: Alle waardes in dezelfde eenheid? (€ millions of € thousands?)
- [ ] **Completeness**: Alle template items ingevuld? (geen [EXTRACT] placeholders over)
- [ ] **Source Trace**: Kun je elke waarde terugvinden in jaarrekening pagina?

**Live Demo Resultaat**:

```markdown
## Assets
### Current Assets
* Cash and Cash Equivalents: €2,847
* Other Net Receivables: €1,234
* Inventory: €3,456
[...]

**Total Assets: €45,678**

## Liabilities
[...]

**Total Liabilities + Equity: €45,678** ✅ KLOPT!
```

---

**Teamopdracht** (10 min): "Jullie beurt - test de workflow"

**Opdracht**:

- **AI Path Studenten**: Bouw een prompt om 1 template sectie te vullen (bijv. Current Assets)
- **Conventional Path Studenten**: Vul handmatig 1 template sectie in
- **Alle Studenten**: Verifieer met checklist

**Debrief** (laatste 2 min):

- Vraag 1-2 studenten: "Wat was lastig?"
- Typische antwoorden:
  - AI: "Goodwill stond in jaarrekening als 'Goodwill and Intangibles combined'"
  - Conventional: "Units waren soms € millions, soms € thousands"
- **Docent**: "Exact daarom doen we verificatie - Week 3 ratio's zijn alleen betrouwbaar als data klopt!"

**Doel**: Hands-on ervaring met template-based data extraction + verificatie workflow

---

### **Blok 3: Van Accounting naar Finance Perspectief** (30 min)

#### **3A: Finance Balance Sheet** (20 min)

**Vergelijk**:
- [accounting-balance-sheet.html](../background-docs/subjects/accounting-balance-sheet.html) **vs.**
- [financing-balance-sheet.html](../background-docs/subjects/financing-balance-sheet.html)

**Het Fundamentele Verschil**:

| Perspectief | Accounting | Finance |
|------------|------------|---------|
| **Focus** | Wat je **betaalde** | Wat het **waard is** |
| **Tijdshorizon** | Verleden (historical) | Toekomst (forward-looking) |
| **Waardering** | Historical cost | Market value |
| **Doelgroep** | Auditors, belastingdienst | Investeerders, management |

**Assets Kant Verschil**:

**Accounting Balance Sheet**:
- Tangible assets (book value)
- Intangible assets (goodwill)
- Current assets

**Finance Balance Sheet**:
- **Assets in Place**: Waarde van investeringen al gedaan
  - Past investments die cash flows genereren
  - Bestaande producten, fabrieken, klantenbestand

- **Growth Assets**: Waarde van toekomstige verwachtingen
  - Future expectations die nog niet gerealiseerd zijn
  - R&D projecten, nieuwe markten, productpipeline

**Damodaran NVIDIA Voorbeeld**:

**Vrijdag 24 januari 2025**:
- **Marktwaarde**: €4.3 trillion totaal
- **Assets in Place**: ~€0.5T
  - Chips al verkocht
  - Fabrieken gebouwd
  - Bestaande klanten (Microsoft, Google, etc.)
- **Growth Assets**: ~€3.8T
  - Verwachtingen AI toekomst
  - Nieuwe generatie chips (Blackwell, etc.)
  - Toekomstige vraag naar AI computing

**Maandag 27 januari 2025 (na DeepSeek nieuws)**:
- DeepSeek toont dat AI mogelijk is met minder krachtige chips
- **Impact**: Growth Assets worden hergewaardeerd ↓
- Assets in Place blijven grotendeels intact
- **Koersdaling**: Vooral growth expectations die aangetast worden

**Liabilities Kant**:
- Zelfde structuur: Debt + Equity
- Maar: **marktwaarde** ipv boekwaarde
- **Equity market value** = Aandelenkoers × Aantal aandelen
  - Dagelijks waarneembaar
  - Reflecteert verwachtingen investeerders

**3B: Interactieve Discussie** (10 min)

**Vraag aan studenten**:

1. **"Welke bedrijven hebben vooral Assets in Place?"**
   - **Antwoord**: Mature bedrijven
   - Voorbeelden: Coca-Cola, Unilever, Heineken, Shell
   - Waarom? Gevestigde producten, stabiele markten, weinig groei

2. **"Welke bedrijven hebben vooral Growth Assets?"**
   - **Antwoord**: Growth/tech bedrijven
   - Voorbeelden: Palantir, ASML, Tesla, OpenAI
   - Waarom? Potentieel in nieuwe markten, disruptieve technologie

3. **"Waar zou jouw BEDROM sector bedrijf zitten?"**
   - Studenten reflecteren op eigen gekozen bedrijf
   - Is het mature (Assets in Place) of growth (Growth Assets)?

**Doel**: Strategic view van firm value begrijpen

---

### **Blok 4: Corporate Finance First Principles** (20 min)

**Visualisatie**: Toon [corporate-finance-decisions.html](../background-docs/subjects/corporate-finance-decisions.html)

**Damodaran Quote**:
> "Corporate Finance covers **any decision** made by a business that involves the use of money"

**De Corporate Finance Tree**:

```
                    GOAL: Maximize Firm Value
                              |
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
   INVESTMENT            FINANCING             DIVIDEND
    DECISION              DECISION             DECISION
```

---

#### **1️⃣ Investment Decision** (Blauwe Kolom)

**Principe**: Investeer alleen als **expected return > hurdle rate**

**Sub-vragen**:
- Welke projecten nemen we aan?
- Hoeveel investeren we in nieuwe activa?

**Voorbeeld Shell Windpark**:
- Verwacht rendement: 12%
- Hurdle rate: 9%
- **Beslissing**: ✅ GO (12% > 9%)

**Hurdle rate hangt af van**:
- **Risico**: Risicovoller project → hogere hurdle rate
- **Debt/Equity mix**: Hoe financier je het?

---

#### **2️⃣ Financing Decision** (Groene Kolom)

**Principe**: Vind optimale **debt/equity mix** (minimaliseer hurdle rate)

**Sub-vragen**:
- Hoeveel lenen (debt) vs. eigen vermogen (equity)?
- Welk type debt (kortlopend/langlopend, welke valuta)?

**Match Debt aan Assets** (Damodaran voorbeeld):

**Voorbeeld: Portugese Toll Road**
- **Assets**: Tolweg genereert cash flows in Euro's voor 30 jaar
- **Juiste debt**: 30-jaar Euro debt
- **Fout**: Kortlopende USD debt (mismatch!)
  - Kortlopend = moet snel herfinancieren (refinancing risk)
  - USD = valutarisico (als Euro daalt, schuld stijgt in Euro's)

**Steady Safe Case** (Indonesië 1990s):
- Assets: Taxi's in Indonesië (genereren Rupiah)
- Fout: 10-jaar USD debt (op advies investment bank: "goedkoper!")
- 1997: Rupiah devalueert 65%
  - Assets in USD: ↓ 65%
  - Debt in USD: blijft 100%
  - **Resultaat**: Faillissement

**Les**: "Goedkoper" betekent niet beter - match debt aan assets!

---

#### **3️⃣ Dividend Decision** (Paarse Kolom)

**Principe**: Als geen goede investeringen → **geef cash terug** aan aandeelhouders

**Sub-vragen**:
- Hoeveel cash teruggeven?
- Dividends of buybacks?

**Wanneer cash teruggeven?**
- Hurdle rate: 9%
- Best investment opportunity: 7.5%
- **Beslissing**: Stop met investeren, geef cash terug
  - Aandeelhouders kunnen zelf investeren tegen >7.5%

**Dividends vs. Buybacks**:

| Bedrijf | Shareholders Profiel | Voorkeur |
|---------|---------------------|----------|
| **Google** | Groei-investeerders, jonger publiek | **Buybacks** (geen belasting tot verkoop) |
| **ConEd** (utility) | Pensionfondsen, 65+ | **Dividends** (willen cash income) |

**Doel**: Big picture van corporate finance overzien - alles draait om value maximization

---

### **Blok 5: Team Check-in & Data Extraction Planning** (10 min)

**Instructie**: Team huddle (10 min binnen team)

**Check 1: Decision Framework Status**
- ✅ Strategische vraag geformuleerd? (Management)
- ✅ Rol verdeling duidelijk? (1 Management, 3-4 Analisten)
- ✅ Methodologie keuze gemaakt? (elke Analist: AI of Conventional)

**Check 2: Analyst Rolverdeling & Data**
- Hebben de 3 Analisten hun specifieke rol bepaald?
  - **Analyst 1**: Financial statement analysis **eigen bedrijf**
  - **Analyst 2**: Financial statement analysis **concurrent 1** (Euronext)
  - **Analyst 3**: Financial statement analysis **concurrent 2** (Euronext)
- Externe data voor benchmark:
  - ESG databases (Refinitiv, MSCI)
  - Sector rapporten (CBS, brancheverenigingen)
  - Andere relevante bronnen
- Is strategische vraag beantwoordbaar met deze 3-bedrijven benchmark?

**Check 3: Data Extraction Readiness** ⭐ NIEUW

**CRITICAL voor Week 3**: Alle 3 Analisten moeten dezelfde template structuur gebruiken!

**Verificatie Afspraken**:
- [ ] **Template Agreement**: Welke 3 templates gebruiken jullie? (balance-sheet, income-statement, cash-flow)
- [ ] **Units Agreement**: Welke eenheid? (€ millions aanbevolen voor consistency)
- [ ] **Verification Protocol**: Wie controleert data extraction quality? (peer review binnen team)
- [ ] **Deadline Agreement**: Wanneer hebben alle 3 Analisten data extraction klaar? (voor Week 3 sessie!)

**Waarom dit belangrijk is**:
- Week 3: Ratio berekeningen zijn alleen betrouwbaar als data extraction correct is
- Benchmark vergelijking werkt alleen als alle 3 bedrijven dezelfde structuur hebben
- Garbage in = Garbage out!

**Check 4: Week 3 Voorbereiding**
- **Volgende week**: Business Understanding deep dive
  - Management presenteert strategische vraag (5 min per team)
  - Analisten presenteren data aanpak + **tonen extracted data templates** (5 min per team)

**Actie**:
- Zorg dat Decision Framework compleet is voor volgende week
- **Analisten starten met template-based data extraction** (HUISWERK - zie hieronder)

---

## Afsluiting & Huiswerk (5 min uitdelen instructies)

### **Huiswerk voor Week 3**:

**1. Team Project Charter Finaliseren** (indien nog niet compleet)

- **Strategische Vraag** (Management-led):
  - Voorbeeld AH: "Moet AH investeren in €50M sustainable packaging plant?"
  - Voorbeeld ASML: "Moet ASML EUV capaciteit uitbreiden naar China?"

- **3-Analyst Structuur** (Analyst-led):
  - **Analyst 1**: Analyseer **eigen bedrijf** (bijv. Ahold Delhaize)
  - **Analyst 2**: Analyseer **concurrent 1** (bijv. Carrefour)
  - **Analyst 3**: Analyseer **concurrent 2** (bijv. Casino Group)
  - **Gezamenlijk**: Benchmark opbouwen met 3 bedrijven + externe sector data

- **Methodologie Keuze per Analyst**:
  - AI-Augmented Path of Conventional Tools Path
  - Rationale: Waarom past deze aanpak bij jouw leerdoel?

- **Databronnen**:
  - Euronext jaarrekeningen (3 bedrijven)
  - Externe benchmark data (ESG databases, sector rapporten)
  - Feasibility check: "Is strategische vraag beantwoordbaar?"

**2. 🎯 PRIORITY: Template-Based Data Extraction** (Analisten - CRITICAL voor Week 3!)

**Opdracht**: Elk van de 3 Analisten extraheert financiële data van hun toegewezen bedrijf

**Deliverable**: 3 ingevulde templates per Analyst:

1. **[balance-sheet-template.md](../background-docs/subjects/balance-sheet-template.md)** → `balance-sheet-[bedrijfsnaam]-[jaar].md`
2. **[income-statement-template.md](../background-docs/subjects/income-statement-template.md)** → `income-statement-[bedrijfsnaam]-[jaar].md`
3. **[cash-flow-statement-template.md](../background-docs/subjects/cash-flow-statement-template.md)** → `cash-flow-[bedrijfsnaam]-[jaar].md`

**Workflow AI-Augmented Path**:

```
Stap 1: Download jaarrekening PDF (Euronext company annual report 2023)
Stap 2: Upload PDF naar AI tool (Claude, ChatGPT, etc.)
Stap 3: Gebruik deze prompt structure:

"Extract data from [Company Name] 2023 Annual Report and fill this template:

[PLAK TEMPLATE HIER]

Rules:
- Use € millions as unit
- Verify: Total Assets = Total Liabilities + Equity
- Return ONLY the filled template"

Stap 4: Verificatie (zie checklist hieronder)
Stap 5: Sla op als markdown file
```

**Workflow Conventional Path**:

```
Stap 1: Download jaarrekening PDF
Stap 2: Open template in Word/Notepad
Stap 3: Handmatig zoeken in PDF:
  - Zoek "Consolidated Balance Sheet" pagina
  - Zoek "Cash and Cash Equivalents" → kopieer waarde
  - Vul in template regel
  - Herhaal voor alle items
Stap 4: Verificatie (zie checklist hieronder)
Stap 5: Sla op als markdown file
```

**Verificatie Checklist** (BEIDE paths - MANDATORY!)

- [ ] **Totals Check**: Total Assets = Total Liabilities + Equity?
- [ ] **Units Consistent**: Alle waardes in € millions (of zelfde eenheid)?
- [ ] **Completeness**: Alle template items ingevuld? (geen gaps)
- [ ] **Source Traceable**: Kun je elke waarde terugvinden in jaarrekening + pagina nummer?
- [ ] **Peer Review**: Heeft een andere Analyst je data gecontroleerd?

**Deadline**: **Voor Week 3 sessie** - Week 3 ratio berekeningen zijn alleen mogelijk als data extraction klaar is!

**Team Alignment Check**:

- Hebben alle 3 Analisten dezelfde templates gebruikt? ✅
- Zijn units consistent (bijv. alle 3 in € millions)? ✅
- Kunnen jullie data side-by-side vergelijken? ✅

**3. Pulse Check** (individueel, vrijdag, 2 minuten)

- **Purpose**: Ik voel verbinding met opdracht (1-5)
- **Autonomy**: Ik heb controle over HOE (1-5)
- **Mastery**: Te makkelijk / Precies goed / Te moeilijk

**4. Methodologie Voorbereiding** (Analisten - optioneel)

- **AI-Augmented Path**: Experimenteer met verschillende prompt formaten
- **Conventional Tools Path**: Check Excel/Python setup voor ratio calculations
- **Definitieve keuze deadline**: Week 3

---

## PAM Framework Alignment

### **Purpose** (target: 5/5)
- ✅ **Activatie**: BEDROM sector kennis heeft directe waarde
- ✅ **Authenticiteit**: Eigen sector + échte beursgenoteerde bedrijven
- ✅ **Impact**: Van conceptueel beschrijven → kwantitatief onderbouwen met NPV/ROI

**Hoe meten**:
- Pulse check vraag 1: "Ik voel verbinding met opdracht" (target ≥4/5)

### **Autonomy** (target: 5/5)
- ✅ **Keuze 1**: Welk Euronext bedrijf binnen BEDROM sector? (al gedaan)
- ✅ **Keuze 2**: Welke rol (Management strategisch vs. Analyst technisch)?
- ✅ **Keuze 3**: Welke methodologie (AI vs. Conventional)?
- ✅ **Guided**: Voorbeelden gegeven + rationale vereist in charter

**Hoe meten**:
- Pulse check vraag 2: "Ik heb controle over HOE" (target ≥4/5)

### **Mastery** (target: 5/5)
- ✅ **Goldilocks**: Bekend domein (BEDROM sector) + nieuwe skill (kwantitatief)
- ✅ **Groei zichtbaar**: Van conceptueel → data-gedreven
- ✅ **Pulse check**: Vrijdag (early warning voor calibratie)

**Hoe meten**:
- Pulse check vraag 3: "Te makkelijk / Precies goed / Te moeilijk"
- Target: <30% zegt "te makkelijk" of "te moeilijk"

---

## Materialen Benodigd

### **HTML Visualisaties** (`background-docs/subjects/`):

- [accounting-balance-sheet.html](../background-docs/subjects/accounting-balance-sheet.html)
- [financing-balance-sheet.html](../background-docs/subjects/financing-balance-sheet.html)
- [corporate-finance-decisions.html](../background-docs/subjects/corporate-finance-decisions.html)

### **Damodaran Quotes** (transcript lines 635-1050):
- "Accounting balance sheet: what you paid. Finance balance sheet: what it's worth"
- "NVIDIA: €0.5T assets in place, €3.8T growth assets"
- "You can't spend earnings, only cash"
- "Corporate finance = any business decision involving money"
- "Goodwill is a plug variable to make balance sheets balance"

### **Textbook Referenties**:
- Fundamentals of Corporate Finance Ch3 (Financial Statements)
- Damodaran Corporate Finance transcript Session 1

---

## LRD Requirements Checklist

✅ **LR-CS2**: Week 2-3 Discovery & Preparation
✅ **LR-BEDROM-1**: Explicit 25-min BEDROM → ECONAN bridge
✅ **LR-R2**: Management (Seniors) formuleren strategische vraag
✅ **LR-R3**: Analysts data feasibility check
✅ **LR-H3**: Methodology choice guidance (AI vs. Conventional)
✅ **LR-M5**: Pulse check Week 2 (Goldilocks calibration)
✅ **LR-P1**: Authentieke opdracht (Euronext bedrijven)

---

## Timing Breakdown (120 min totaal)

| Blok | Activiteit | Minuten |
|------|-----------|---------|
| Pre-check | Decision Framework poll | 5 |
| 1 | BEDROM → ECONAN Bridge | 25 |
| 2 | Drie Financiële Overzichten | 35 |
| 3 | Accounting vs. Finance Perspectief | 30 |
| 4 | Corporate Finance First Principles | 20 |
| 5 | Team Check-in & Planning | 10 |
| Afsluiting | Huiswerk instructies | 5 |
| **Totaal** | | **130** |

*(10 min buffer voor vragen/discussie)*

---

## Docent Notities

### **Verwachte Vragen**:

**Q: "Waarom is accounting balance sheet nog relevant als het zo beperkt is?"**
- A: Wettelijk vereist, basis voor belastingen, investors gebruiken het als startpunt (maar niet eindpunt)

**Q: "Hoe bereken je de waarde van Growth Assets?"**
- A: Komt later in de cursus (DCF, scenario analysis) - vandaag alleen conceptueel begrip

**Q: "Moet ik AI of Conventional kiezen?"**
- A: Hangt af van leerdoel. AI = leren prompt engineering + kritisch evalueren. Conventional = technische skills. Beide even zwaar in assessment.

**Q: "Kan ik later switchen tussen AI en Conventional?"**
- A: Tot Week 3 is switchen toegestaan. Na Week 4 commitment aan gekozen pad (LR-H5).

### **Rode Vlaggen**:

⚠️ **Team zonder duidelijke rolverdeling**:
- Interventie: "Wie neemt welke rol? Management moet strategische vraag leiden."

⚠️ **Vage strategische vraag**:
- Voorbeeld fout: "We kijken naar duurzaamheid"
- Voorbeeld goed: "Moet AH investeren in €50M sustainable packaging plant? (NPV >0?)"

⚠️ **Analysts zonder databronnen**:
- Interventie: "Jullie moeten data feasibility checken - welke 3 bronnen gebruiken jullie?"

---

**Einde Draaiboek Week 2**
