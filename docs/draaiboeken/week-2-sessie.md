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

### **Blok 2: De Drie Financiële Overzichten** (35 min)

#### **2A: Accounting Balance Sheet** (20 min)

**Visualisatie**: Toon [accounting-balance-sheet.html](../background-docs/accounting-balance-sheet.html)

**Uitleg**:

**Basisprincipe**:
```
Assets = Liabilities + Shareholders' Equity
```

**Assets (Bezittingen)**:
- **Current Assets** (vlottende activa): binnen jaar liquide
  - Voorraad (inventory)
  - Debiteuren (accounts receivable)
  - Liquide middelen (cash)

- **Non-Current Assets** (vaste activa):
  - **Tangible**: gebouwen, machines, grond (wat je kunt zien/aanraken)
  - **Intangible**: goodwill, patenten, merken (wat je niet kunt zien)

**Liabilities (Schulden)**:
- **Current Liabilities** (kortlopende schulden): binnen jaar te betalen
  - Crediteuren (accounts payable)
  - Kortlopende leningen

- **Non-Current Liabilities** (langlopende schulden): na >1 jaar te betalen
  - Obligaties (bonds)
  - Langlopende leningen

**Shareholders' Equity** (Eigen Vermogen):
- Book value (boekwaarde)
- Historisch opgebouwde waarde

**Kernbeperking**: **Backward-looking** (historical cost accounting)
- "Je ziet wat Coca-Cola **betaalde** voor activa, niet wat het nu **waard is**"
- Voorbeeld: Gebouw gekocht in 1965 voor €100K staat nog steeds voor €100K (minus afschrijving)
- Damodaran over goodwill: **"plug variable to make balance sheets balance"**
  - Goodwill ontstaat alleen bij acquisities
  - Apple heeft bijna geen goodwill (geen grote acquisities)
  - Yahoo had €1B goodwill voor Alibaba terwijl het €40B waard was

#### **2B: Income Statement & Cash Flow Statement** (15 min)

**Income Statement** (Resultatenrekening):
```
Revenues (Opbrengsten)
- Costs (Kosten)
= Earnings (Winst)
```

**Cash Flow Statement** (Kasstroomoverzicht):
```
Cash In (Geld binnen)
- Cash Out (Geld buiten)
= Net Cash Flow
```

**Kritisch Verschil**:

Damodaran quote: **"You can't spend earnings, only cash"**

**Waarom earnings ≠ cash flow?**

| Item | Income Statement | Cash Flow |
|------|------------------|-----------|
| Verkoop op krediet | Telt als revenue | Nog geen cash in |
| Afschrijvingen | Telt als cost | Geen cash uit (al betaald bij aankoop) |
| Aankoop machine (€1M) | Alleen afschrijving (€100K/jaar) | Hele €1M cash uit bij aankoop |

**Voorbeeld**:
- Bedrijf verkoopt €100K producten op krediet → Income Statement: +€100K revenue
- Klant betaalt pas over 3 maanden → Cash Flow Statement: €0 nu
- **Je kunt die €100K nog niet uitgeven!**

**Doel**: Basiskennis financiële overzichten opfrissen + verschil earnings/cash begrijpen

---

### **Blok 3: Van Accounting naar Finance Perspectief** (30 min)

#### **3A: Finance Balance Sheet** (20 min)

**Vergelijk**:
- [accounting-balance-sheet.html](../background-docs/accounting-balance-sheet.html) **vs.**
- [financing-balance-sheet-v2.html](../background-docs/financing-balance-sheet-v2.html)

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

**Visualisatie**: Toon [corporate-finance-decisions.html](../background-docs/corporate-finance-decisions.html)

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

### **Blok 5: Team Check-in & Planning** (10 min)

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

**Check 3: Week 3 Voorbereiding**
- **Volgende week**: Business Understanding deep dive
  - Management presenteert strategische vraag (5 min per team)
  - Analisten presenteren data aanpak (5 min per team)

**Actie**:
- Zorg dat Decision Framework compleet is voor volgende week
- Analisten starten met data exploratie

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

**2. Pulse Check** (individueel, vrijdag, 2 minuten)
- **Purpose**: Ik voel verbinding met opdracht (1-5)
- **Autonomy**: Ik heb controle over HOE (1-5)
- **Mastery**: Te makkelijk / Precies goed / Te moeilijk

**3. Methodologie Voorbereiding** (Analisten)
- **AI-Augmented Path**: Lees prompt template library
- **Conventional Tools Path**: Check Power BI/Python setup
- **Definitieve keuze deadline**: Week 3

**4. Data Exploratie Start** (Analisten)
- Download datasets
- Eerste EDA (Exploratory Data Analysis)
- Noteer data quality issues

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

### **HTML Visualisaties** (`background-docs/`):
- [accounting-balance-sheet.html](../background-docs/accounting-balance-sheet.html)
- [financing-balance-sheet-v2.html](../background-docs/financing-balance-sheet-v2.html)
- [corporate-finance-decisions.html](../background-docs/corporate-finance-decisions.html)

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
