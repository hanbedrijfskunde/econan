# FINANCIAL STATEMENT ANALYSIS - RHEINMETALL AG
## Complete Analysis for HBO Bedrijfskunde - Module ECONAN

**Datum:** 10 november 2025  
**Bedrijf:** Rheinmetall AG (DE0007030009)  
**Fiscaal Jaar:** 2024  
**Docent:** Business Analysis Training Module  
**Rol:** Business Analist

---

## CONVERSATIE VERLOOP - ALLE PROMPTS

### Context voor Business Analisten

In de onderwijsmodule ECONAN in het tweede jaar van de opleiding HBO Bedrijfskunde leren studenten omgaan met data uit verschillende bronnen, deze bewerken en de juiste conclusies trekken op grond van deze data. Omdat data een steeds grotere rol speelt binnen het bedrijfsmatige beslisproces is het noodzakelijk dat toekomstige bedrijfskundigen kennis hebben van data analyse. In deze module richten we ons (voornamelijk) op bedrijfseconomische data. De module leert hoe dit systematisch aan te pakken.

Tijdens de module nemen studenten de volgende rollen aan: **CFO** en **Business Analist**. Ze werken in teams aan opdrachten, waarbij de CFO de strategische vragen formuleert en de antwoorden presenteert, terwijl de analisten het onderzoek uitvoeren en de resultaten communiceren.

Als Business Analist werk je met AI tools (zoals ChatGPT, Claude, Mistral) om financiële analyses snel en effectief uit te voeren. Je leert hoe je AI stuurt via prompts, hoe je de output controleert en valideert, en hoe je deze analyses inzet voor strategische beslissingen. Dit voorbeeld gebruikt Rheinmetall AG als case study.

### Beschikbare Resources

- https://live.deutsche-boerse.com/equity/rheinmetall-ag?mic=XETR
- https://live.euronext.com/en/product/equities/DE0007030009-BGEM
- https://ir.rheinmetall.com/

---

### 📝 PROMPT 1: Initiële Opdracht - Basis Financial Ratios

```
In de onderwijsmodule ECONAN in het tweede jaar van de opleiding HBO Bedrijfskunde 
leren studenten omgaan met data uit verschillende bronnen, deze bewerken en de juiste 
conclusies trekken op grond van deze data. Omdat data een steeds grotere rol speelt 
binnen het bedrijfsmatige beslisproces is het noodzakelijk dat toekomstige 
bedrijfskundigen kennis hebt van data analyse. In deze module richten we ons 
(voornamelijk) op bedrijfseconomische data. De module leert hoe dit systematisch aan 
te pakken.

Tijdens de module nemen studenten de volgende rollen aan: CFO en Business Analist. 
Ze werken in teams aan opdrachten, waarbij de CFO de strategische vragen formuleert 
en de antwoorden presenteert, terwijl de analisten het onderzoek uitvoeren en de 
resultaten communiceren.

Ik ben Business Analist en ga AI gebruiken om financiële analyses uit te voeren.
Ik wil leren hoe ik AI effectief kan sturen om analyses te maken en hoe ik deze kan
controleren en inzetten voor mijn opdrachten. Voor dit voorbeeld gebruik ik het bedrijf
Rheinmetall. Hier zijn wat resources:

https://live.deutsche-boerse.com/equity/rheinmetall-ag?mic=XETR
https://live.euronext.com/en/product/equities/DE0007030009-BGEM
https://ir.rheinmetall.com/

I am a business analist. Please help me craft a financial statement analysis for 
Rheinmetall. Calculate Current Ratio, ROE, Debt-Equity ratio, Asset Turnover using 
the extracted data. Show formulas, input values (sources) and results.
```

**Resultaat:** Berekening van 4 basis financial ratios met formules, bronvermelding en interpretatie.

**Leerpunt voor studenten:** Begin met een duidelijke, gestructureerde vraag. Geef context over wat je wilt bereiken en vraag expliciet om formules, bronnen en resultaten.

---

### 📝 PROMPT 2: Marktwaarde Ratio - P/E

```
Can you look up the current P/E ratio?
```

**Resultaat:** Claude gebruikt web search om huidige aandelenkoers op te zoeken (€1,749) en berekent P/E ratio (~94) met behulp van EPS uit jaarverslag.

**Leerpunt voor studenten:** Korte, duidelijke vervolgvragen zijn effectief. AI kan externe data opzoeken en combineren met eerder gebruikte data.

---

### 📝 PROMPT 3: Earnings Yield Berekening

```
Bereken nu 1/P/E en vermenigvuldig met 100%
```

**Resultaat:** Berekening van Earnings Yield (1.06%) met meerdere methoden en interpretatie van wat dit betekent voor beleggers.

**Leerpunt voor studenten:** Je kunt wiskundige bewerkingen op eerder berekende cijfers vragen. AI begrijpt de context van eerdere berekeningen.

---

### 📝 PROMPT 4: Vergelijkende Analyse

```
Vergelijk dit met de berekende ROE
```

**Resultaat:** Diepgaande vergelijking tussen ROE (18.1%) en Earnings Yield (1.06%), inclusief berekening van P/B ratio (17.0x) en uitleg van de wiskundige relatie: Earnings Yield = ROE / P/B.

**Leerpunt voor studenten:** Vraag om vergelijkingen tussen cijfers. Dit onthult relaties en patronen die niet direct zichtbaar zijn in individuele ratio's.

---

### 📝 PROMPT 5: Geavanceerde Analyse - DuPont

```
Maak een DuPont analyse
```

**Resultaat:** Complete 3-factor DuPont decompositie van ROE in:
- Net Profit Margin (8.29%)
- Asset Turnover (0.68)
- Equity Multiplier (3.21)

Inclusief 5-factor uitbreiding, year-over-year vergelijking, sector benchmarking en strategische aanbevelingen.

**Leerpunt voor studenten:** Je kunt vragen om specifieke analyseframeworks. AI kent verschillende analysetechnieken en kan deze toepassen op je data.

---

### 📝 PROMPT 6: Documentatie

```
Kun je deze hele conversatie opslaan in een markdown bestand?
```

**Resultaat:** Complete conversatie opgeslagen in gestructureerd markdown document met alle berekeningen, visualisaties en interpretaties.

**Leerpunt voor studenten:** Vraag om documentatie van je werk. Dit maakt het gemakkelijk om te delen, te presenteren en later te raadplegen.

---

### 📝 PROMPT 7: Metadata Toevoegen

```
Kun je ook mijn prompt toevoegen?
```

**Resultaat:** Originele prompt toegevoegd aan het document voor context.

**Leerpunt voor studenten:** Je kunt het document iteratief verbeteren. Vraag om aanpassingen als iets ontbreekt.

---

### 📝 PROMPT 8: Volledige Transparantie

```
Graag alle prompts uit conversatie toevoegen.
```

**Resultaat:** Deze sectie! Alle prompts toegevoegd zodat studenten het volledige proces kunnen zien.

**Leerpunt voor studenten:** Transparantie in het proces is belangrijk. Door alle prompts te tonen, leer je hoe je effectief met AI werkt.

---

## HOE GEBRUIK JE DEZE PROMPTS IN JE EIGEN ANALYSE?

### Stap 1: Start met een Duidelijke Opdracht
```
Ik ben [jouw rol]. Help me met een [type analyse] voor [bedrijf]. 
Bereken [specifieke ratio's]. Toon formules, bronnen en resultaten.
```

### Stap 2: Bouw Stap voor Stap
- Vraag eerst om basis ratio's
- Voeg vervolgens marktdata toe
- Ga dieper in op interessante bevindingen
- Vraag om vergelijkingen en relaties

### Stap 3: Gebruik Verschillende Vraagtypen

**Directe berekeningen:**
- "Bereken de Current Ratio"
- "Wat is de Debt-to-Equity ratio?"

**Opzoeken van externe data:**
- "Zoek de huidige aandelenkoers op"
- "Wat is de P/E ratio?"

**Wiskundige bewerkingen:**
- "Bereken 1/P/E × 100%"
- "Deel ROE door P/B"

**Vergelijkingen:**
- "Vergelijk ROE met Earnings Yield"
- "Hoe verhoudt dit zich tot de sector?"

**Geavanceerde analyses:**
- "Maak een DuPont analyse"
- "Doe een scenario analyse"
- "Wat zijn de trends over 3 jaar?"

**Documentatie:**
- "Sla dit op in een markdown bestand"
- "Maak een samenvatting"
- "Voeg visualisaties toe"

### Stap 4: Controleer en Verifieer

**Altijd checken:**
- ✅ Kloppen de formules?
- ✅ Zijn de bronnen correct?
- ✅ Zijn de berekeningen juist?
- ✅ Is de interpretatie logisch?
- ✅ Ontbreken er belangrijke nuances?

### Stap 5: Itereer en Verbeter

Als iets niet klopt of ontbreekt:
- "Kun je dit nog toevoegen?"
- "Dit lijkt niet te kloppen, kun je het controleren?"
- "Kun je dit uitgebreider uitleggen?"

---

## WAARSCHUWING: KRITISCH BLIJVEN

### AI is een Tool, Geen Orakel

**Wat AI WEL goed kan:**
- ✅ Snel berekeningen uitvoeren
- ✅ Formules correct toepassen
- ✅ Data uit documenten halen
- ✅ Verschillende analysetechnieken toepassen
- ✅ Interpretaties en context bieden

**Wat AI NIET altijd goed doet:**
- ❌ Bronnen kunnen soms verkeerd geïnterpreteerd worden
- ❌ Berekeningen moeten altijd geverifieerd worden
- ❌ Context kan soms gemist worden
- ❌ Nuances in bedrijfsspecifieke situaties
- ❌ Toekomstvoorspellingen zijn speculatief

### Verificatie Checklist voor Studenten

Voor elke AI-gegenereerde analyse:

1. **Data Verificatie**
   - [ ] Controleer of cijfers uit de juiste bronnen komen
   - [ ] Vergelijk met originele documenten
   - [ ] Check of datum/periode klopt

2. **Formule Verificatie**
   - [ ] Is de formule correct toegepast?
   - [ ] Zijn alle componenten meegenomen?
   - [ ] Klopt de wiskundige uitwerking?

3. **Interpretatie Verificatie**
   - [ ] Is de conclusie logisch?
   - [ ] Zijn er alternatieve verklaringen?
   - [ ] Past dit bij de sector/context?

4. **Bronvermelding**
   - [ ] Zijn alle bronnen vermeld?
   - [ ] Zijn bronnen betrouwbaar?
   - [ ] Zijn bronnen actueel?

---

## DIDACTISCHE WAARDE VAN DEZE AANPAK

### Voor Docenten

**Voordelen:**
- Studenten leren kritisch denken over AI-output
- Focus op interpretatie, niet alleen berekening
- Transparantie in het analyseproces
- Herhaalbaar en schaalbaar

**Gebruik in de les:**
1. Toon deze conversatie als voorbeeld
2. Laat studenten zelf prompts schrijven
3. Laat ze elkaars resultaten verifiëren
4. Discussieer over interpretaties

### Voor Studenten

**Leereffecten:**
- Begrijp hoe financial ratios samenhangen
- Leer effectief communiceren met AI
- Ontwikkel kritisch denkvermogen
- Bouw portfolio van analyses op

**Praktische Toepassing:**
- Gebruik dit als template voor andere bedrijven
- Pas de prompts aan voor specifieke opdrachten
- Bouw je eigen analyse-workflow
- Documenteer je proces voor toekomstig gebruik

---

## INHOUDSOPGAVE

1. [Introductie](#introductie)
2. [Basis Financiële Ratio's](#basis-financiele-ratios)
   - Current Ratio
   - Return on Equity (ROE)
   - Debt-to-Equity Ratio
   - Asset Turnover Ratio
3. [Markt Waardering](#markt-waardering)
   - Price-to-Earnings (P/E) Ratio
   - Earnings Yield
4. [Vergelijking ROE vs Earnings Yield](#vergelijking-roe-vs-earnings-yield)
   - Price-to-Book (P/B) Ratio
   - Wiskundige Relatie
5. [DuPont Analyse](#dupont-analyse)
   - 3-Factor DuPont
   - Component Analyse
   - 5-Factor DuPont
6. [Conclusies en Aanbevelingen](#conclusies-en-aanbevelingen)

---

## INTRODUCTIE

### Context Module ECONAN

In de onderwijsmodule ECONAN in het tweede jaar van de opleiding HBO Bedrijfskunde leren studenten omgaan met data uit verschillende bronnen, deze bewerken en de juiste conclusies trekken op grond van deze data. Omdat data een steeds grotere rol speelt binnen het bedrijfsmatige beslisproces is het noodzakelijk dat toekomstige bedrijfskundigen kennis hebben van data analyse.

### Doel van deze Analyse

Deze analyse demonstreert hoe AI (Claude) kan worden ingezet voor snelle financiële analyse, en hoe studenten deze analyses kunnen controleren en inzetten voor hun opdrachten. Het voorbeeld gebruikt **Rheinmetall AG**, een toonaangevend defensie- en technologiebedrijf.

### Over Rheinmetall

- **ISIN:** DE0007030009
- **Ticker:** RHM (XETRA)
- **Sector:** Defensie & Automotive
- **Segmenten:** Vehicle Systems, Weapon and Ammunition, Electronic Solutions, Power Systems
- **Hoofdkantoor:** Düsseldorf, Duitsland

---

## BASIS FINANCIËLE RATIO'S

### 1. CURRENT RATIO

#### Formule
```
Current Ratio = Current Assets / Current Liabilities
```

#### Input Values
| Item | Amount (€ million) | Source |
|------|-------------------|--------|
| **Current Assets** | 8,231 | Consolidated Statement of Financial Position, 12/31/2024 |
| **Current Liabilities** | 6,782 | Consolidated Statement of Financial Position, 12/31/2024 |

#### Berekening
```
Current Ratio = 8,231 / 6,782 = 1.21
```

#### Resultaat: **1.21**

#### Interpretatie
Rheinmetall heeft €1.21 aan vlottende activa voor elke €1 aan kortlopende verplichtingen. Dit duidt op voldoende liquiditeit op de korte termijn. Een ratio boven 1.0 wordt als gezond beschouwd.

---

### 2. RETURN ON EQUITY (ROE)

#### Formule
```
ROE = (Net Income / Total Equity) × 100%
```

#### Input Values
| Item | Amount (€ million) | Source |
|------|-------------------|--------|
| **Net Income (Earnings after taxes)** | 808 | Consolidated Statement of Comprehensive Income, 2024 |
| **Total Equity** | 4,465 | Consolidated Statement of Financial Position, 12/31/2024 |

#### Berekening
```
ROE = (808 / 4,465) × 100% = 18.1%
```

#### Resultaat: **18.1%**

#### Interpretatie
Voor elke euro eigen vermogen genereert Rheinmetall €0.18 aan nettowinst. Dit is een sterke rentabiliteit, ruim boven het gemiddelde voor industriële bedrijven (12-15%).

---

### 3. DEBT-TO-EQUITY RATIO

#### Formule
```
Debt-to-Equity Ratio = Total Financial Debt / Total Equity
```

#### Input Values
| Item | Amount (€ million) | Source |
|------|-------------------|--------|
| **Non-current financial debts** | 1,871 | Consolidated Statement of Financial Position, 12/31/2024 |
| **Current financial debts** | 552 | Consolidated Statement of Financial Position, 12/31/2024 |
| **Total Financial Debt** | **2,423** | Calculated: 1,871 + 552 |
| **Total Equity** | 4,465 | Consolidated Statement of Financial Position, 12/31/2024 |

#### Berekening
```
Debt-to-Equity Ratio = 2,423 / 4,465 = 0.54
```

#### Resultaat: **0.54**

#### Interpretatie
Rheinmetall heeft €0.54 aan financiële schuld voor elke €1 eigen vermogen. Dit wijst op een gezonde kapitaalstructuur met beperkte financiële leverage. Een ratio onder 1.0 wordt als conservatief en gezond beschouwd.

---

### 4. ASSET TURNOVER RATIO

#### Formule
```
Asset Turnover = Sales / Total Assets
```

#### Input Values
| Item | Amount (€ million) | Source |
|------|-------------------|--------|
| **Sales (Revenue)** | 9,751 | Key Figures 2024 & Income Statement |
| **Total Assets** | 14,344 | Consolidated Statement of Financial Position, 12/31/2024 |

#### Berekening
```
Asset Turnover = 9,751 / 14,344 = 0.68
```

#### Resultaat: **0.68**

#### Interpretatie
Rheinmetall genereert €0.68 aan omzet voor elke €1 aan activa. Dit geeft de efficiëntie weer waarmee het bedrijf zijn activa inzet om omzet te genereren. Voor een kapitaalintensieve industrie is dit een acceptabele waarde.

---

### SUMMARY TABLE - BASIS RATIO'S

| Ratio | Formula | 2024 Value | 2023 Value | Benchmark Insight |
|-------|---------|------------|------------|-------------------|
| **Current Ratio** | Current Assets / Current Liabilities | **1.21** | 1.30 | Gezond (>1.0 is goed) |
| **ROE** | Net Income / Equity × 100% | **18.1%** | 16.1% | Sterk (>15% is excellent) |
| **Debt-to-Equity** | Total Debt / Equity | **0.54** | 0.52 | Conservatief (<1.0 is gezond) |
| **Asset Turnover** | Sales / Total Assets | **0.68** | 0.61 | Matig (sector-afhankelijk) |

---

## MARKT WAARDERING

### 5. PRICE-TO-EARNINGS (P/E) RATIO

#### Formule
```
P/E Ratio = Market Price per Share / Earnings per Share
```

#### Input Values
| Item | Value | Source |
|------|-------|--------|
| **Current Stock Price** | €1,749.00 | Investing.com & TradingView, November 10, 2025 |
| **Basic EPS (FY 2024)** | €18.52 | Consolidated Income Statement - Annual Report 2024 |
| **Diluted EPS (FY 2024)** | €15.96 | Consolidated Income Statement - Annual Report 2024 |
| **EPS (TTM)** | €18.82 | Investing.com (Trailing Twelve Months) |

#### Berekeningen

##### Methode 1: Gebaseerd op Basic EPS (FY 2024)
```
P/E Ratio = 1,749.00 / 18.52 = 94.4
```

##### Methode 2: Gebaseerd op Diluted EPS (FY 2024)
```
P/E Ratio = 1,749.00 / 15.96 = 109.6
```

##### Methode 3: Gebaseerd op TTM EPS (meest actueel)
```
P/E Ratio = 1,749.00 / 18.82 = 92.9
```

#### Resultaat: **P/E Ratio ≈ 93-95** (using basic/TTM EPS)

#### Interpretatie

Een P/E ratio van ongeveer 93-95 betekent dat beleggers bereid zijn €93-95 te betalen voor elke €1 aan winst.

**Dit is een HOGE P/E ratio**, wat kan duiden op:

1. **Hoge groeiverwachtingen**: De analisten hebben een maximale koersverwachting van €2,500.00 en een minimale van €1,740.00
2. **Sterke sector**: Rheinmetall is actief in defensie, een sector met sterke groei door geopolitieke ontwikkelingen
3. **Recente koersstijging**: Over het afgelopen jaar heeft Rheinmetall een stijging van 245.11% laten zien
4. **Marktsentiment**: Beleggers verwachten dat de huidige winsten sterk zullen groeien

**Vergelijking:**
- **DAX gemiddelde**: ~12-15
- **Rheinmetall**: ~93-95
- **Defensie-industrie gemiddelde**: Varieert, maar vaak 20-40

#### Aanvullende Marktgegevens

| Metric | Value |
|--------|-------|
| **Market Cap** | €80.25 billion |
| **Dividend Yield** | 0.46% |
| **52-Week High** | €2,008.00 |
| **52-Week Low** | €546.60 |
| **Current Price** | €1,749.00 |
| **Beta** | 0.74 |

---

### 6. EARNINGS YIELD

#### Formule
```
Earnings Yield = (1 / P/E Ratio) × 100%
```

Of direct:
```
Earnings Yield = (EPS / Market Price per Share) × 100%
```

#### Berekeningen

##### Methode 1: Via P/E Ratio (Basic EPS)
**P/E Ratio = 94.4**

```
Earnings Yield = (1 / 94.4) × 100%
Earnings Yield = 0.01059 × 100%
Earnings Yield = 1.06%
```

##### Methode 2: Via P/E Ratio (TTM EPS)
**P/E Ratio = 92.9**

```
Earnings Yield = (1 / 92.9) × 100%
Earnings Yield = 0.01076 × 100%
Earnings Yield = 1.08%
```

##### Methode 3: Directe berekening
```
Earnings Yield = (€18.52 / €1,749.00) × 100%
Earnings Yield = 0.01059 × 100%
Earnings Yield = 1.06%
```

#### Resultaat: **Earnings Yield ≈ 1.06% - 1.08%**

#### Interpretatie

De **Earnings Yield** van ~1.06% betekent dat voor elke €100 die u in Rheinmetall-aandelen investeert, het bedrijf €1.06 aan winst genereert (op basis van huidige winsten).

#### Vergelijking met alternatieven

| Investering | Rendement/Yield |
|-------------|-----------------|
| **Rheinmetall Earnings Yield** | **1.06%** |
| 10-jarige Duitse staatsobligatie | ~2.3% (typisch) |
| Gemiddeld spaarrekening | ~3.5% (2025) |
| Rheinmetall Dividend Yield | 0.46% |
| S&P 500 Earnings Yield | ~3-4% (typisch) |

#### Belangrijke Inzichten

**De Earnings Yield is LAAG**, wat betekent:

1. **Dure waardering**: Beleggers betalen een hoge prijs voor de huidige winsten
2. **Groeiverwachtingen**: De markt verwacht sterke winstgroei in de toekomst
3. **Risico vs. rendement**: Het "winstrendement" is lager dan risicovrije staatsobligaties

**Waarom investeren beleggers dan toch?**

Omdat ze verwachten dat de **winst per aandeel** sterk zal groeien. Als de EPS bijvoorbeeld verdubbelt naar €37, dan wordt de Earnings Yield:

```
Earnings Yield = (€37 / €1,749) × 100% = 2.11%
```

En de P/E zou dalen naar ~47.

---

## VERGELIJKING ROE VS EARNINGS YIELD

### De Cijfers

| Metric | Formule | Waarde |
|--------|---------|--------|
| **ROE** | Net Income / Equity × 100% | **18.1%** |
| **Earnings Yield** | EPS / Market Price × 100% | **1.06%** |
| **Verschil** | ROE - Earnings Yield | **17.04 pp** |

### Wat Betekent Dit Verschil?

**ROE = 18.1%**  
Rendement dat **het bedrijf** genereert op het **eigen vermogen (boekwaarde)**

**Earnings Yield = 1.06%**  
Rendement dat **beleggers** krijgen op hun **investering (marktprijs)**

**Waarom is er zo'n groot verschil?**

Het antwoord ligt in de **Price-to-Book (P/B) Ratio**!

---

### PRICE-TO-BOOK (P/B) RATIO

#### Formule
```
P/B Ratio = Market Price per Share / Book Value per Share
```

#### Stap 1: Bereken Book Value per Share

| Item | Amount (€ million) | Source |
|------|-------------------|--------|
| Total Equity | 4,465 | Balance Sheet 12/31/2024 |
| Shares Outstanding | 43.389 million | Berekend: €112M share capital / €2.58 par value |

```
Book Value per Share = €4,465 million / 43.389 million shares
Book Value per Share = €102.92
```

#### Stap 2: Bereken P/B Ratio

```
P/B Ratio = €1,749.00 / €102.92
P/B Ratio = 17.0
```

#### Resultaat: **P/B Ratio = 17.0**

---

### De Wiskundige Relatie

#### Formule die alles verbindt
```
Earnings Yield = ROE / P/B Ratio
```

#### Verificatie
```
Earnings Yield = 18.1% / 17.0
Earnings Yield = 1.06% ✓
```

**De formule klopt perfect!**

---

### Visualisatie van het Verschil

```
BOEKWAARDE (€102.92)          MARKTPRIJS (€1,749.00)
        │                              │
        │◄──────── 17x premium ────────┤
        │                              │
        ▼                              ▼
    ROE: 18.1%                 Earnings Yield: 1.06%
    
    €100 geïnvesteerd          €100 geïnvesteerd
    → genereert €18.10         → krijgt €1.06
    (op boekwaarde)            (op marktprijs)
```

---

### Complete Analyse

| Perspectief | Ratio | Waarde | Betekenis |
|-------------|-------|--------|-----------|
| **Bedrijfsefficiëntie** | ROE | 18.1% | Uitstekend! Bedrijf maakt goede winst op eigen vermogen |
| **Waardering** | P/B | 17.0x | Zeer hoog! Markt betaalt 17x de boekwaarde |
| **Beleggers rendement** | Earnings Yield | 1.06% | Laag! Hoge prijs betekent laag direct rendement |
| **Premium** | P/B - 1 | 16.0x | Markt betaalt €16 extra voor elke €1 boekwaarde |

---

### Waarom Deze Discrepantie?

#### De markt prijst in:

1. **Toekomstige groei**: Verwachting dat winsten flink zullen stijgen
2. **Strategische positie**: Rheinmetall heeft unieke marktpositie in defensie
3. **Orderboek**: Enorme orderportefeuille (€54.973 miljard Rheinmetall Backlog)
4. **Geopolitiek**: Verhoogde defensie-uitgaven in Europa
5. **Immateriële waarden**: Technologie, contracten, reputatie niet volledig in boekwaarde

#### Het risico:

Als de groei **tegenvalt**, kan de P/B ratio (en dus aandelenkoers) **hard dalen** richting meer normale niveaus (bijv. P/B van 5-8x).

---

### Sector Vergelijking

| Bedrijf | ROE | P/B Ratio | Earnings Yield | Sector |
|---------|-----|-----------|----------------|---------|
| **Rheinmetall** | **18.1%** | **17.0x** | **1.06%** | Defensie |
| Gemiddeld Defensie | 15-20% | 3-5x | 3-4% | Defensie |
| Gemiddeld DAX | 12-15% | 2-3x | 4-6% | Diverse |

**Conclusie**: Rheinmetall wordt met een **enorme premium** verhandeld ten opzichte van peers!

---

## DUPONT ANALYSE

### Klassieke 3-Factor DuPont Formule

```
ROE = Net Profit Margin × Asset Turnover × Equity Multiplier
```

Of uitgeschreven:

```
ROE = (Net Income/Sales) × (Sales/Total Assets) × (Total Assets/Equity)
```

---

### Component 1: NET PROFIT MARGIN

#### Formule
```
Net Profit Margin = (Net Income / Sales) × 100%
```

#### Input Values
| Item | Amount (€ million) | Source |
|------|-------------------|--------|
| Net Income (Earnings after taxes) | 808 | Income Statement 2024 |
| Sales | 9,751 | Income Statement 2024 |

#### Berekening
```
Net Profit Margin = (808 / 9,751) × 100%
Net Profit Margin = 8.29%
```

#### Resultaat: **8.29%**

**Betekenis**: Voor elke €100 aan omzet houdt Rheinmetall €8.29 over als nettowinst na alle kosten, rente en belastingen.

#### Analyse

**Is dit goed?**

| Benchmark | Waarde | Rheinmetall |
|-----------|--------|-------------|
| Defensie industrie gemiddeld | 6-10% | 8.29% ✓ |
| Manufacturing gemiddeld | 5-8% | 8.29% ✓ |
| Tech industrie | 15-25% | 8.29% - |

- ✅ Gezonde winstmarge voor industrieel bedrijf
- ✅ Binnen normale range voor defensiesector
- ⚠️ Onder druk door: materiaalkosten (€4,859M) en personeelskosten (€2,373M)

**Van Operating Margin naar Net Margin:**
```
Operating Margin = 15.2%
- PPA effects: -1.3%
- Interest expenses: -1.2%
- Taxes: -4.4%
= Net Margin: 8.29%
```

---

### Component 2: ASSET TURNOVER

#### Formule
```
Asset Turnover = Sales / Total Assets
```

#### Input Values
| Item | Amount (€ million) | Source |
|------|-------------------|--------|
| Sales | 9,751 | Income Statement 2024 |
| Total Assets | 14,344 | Balance Sheet 12/31/2024 |

#### Berekening
```
Asset Turnover = 9,751 / 14,344
Asset Turnover = 0.68
```

#### Resultaat: **0.68**

**Betekenis**: Rheinmetall genereert €0.68 aan omzet voor elke €1 aan activa. Dit meet de efficiëntie van activagebruik.

#### Analyse

**Is dit goed?**

| Industrie | Typische Asset Turnover | Rheinmetall |
|-----------|------------------------|-------------|
| Retail | 2.0 - 3.0 | 0.68 |
| Manufacturing | 0.6 - 1.5 | 0.68 ✓ |
| Defensie | 0.5 - 1.0 | 0.68 ✓ |
| Utilities | 0.3 - 0.5 | 0.68 |

- ✅ Normaal voor kapitaalintensieve industrie
- ✅ Verbeterd t.o.v. 2023 (was 0.61)
- 📈 Sales groeien sneller (+36%) dan Assets (+23%)

**Asset Breakdown:**
```
Total Assets €14,344M bestaat uit:
- Non-current assets: €6,112M (43%)
  └─ Goodwill: €1,426M
  └─ Property, plant & equipment: €1,853M
  └─ Other intangibles: €1,376M
  
- Current assets: €8,231M (57%)
  └─ Inventories: €3,989M (28% van total assets!)
  └─ Trade receivables: €1,959M
  └─ Cash: €1,184M
```

**Belangrijke observatie**: Hoge inventories (€3,989M) wijzen op:
- Lange productiecycli (typisch voor defensie)
- Work-in-progress voor grote contracten
- Mogelijk optimalisatiepotentieel

---

### Component 3: EQUITY MULTIPLIER

#### Formule
```
Equity Multiplier = Total Assets / Total Equity
```

#### Input Values
| Item | Amount (€ million) | Source |
|------|-------------------|--------|
| Total Assets | 14,344 | Balance Sheet 12/31/2024 |
| Total Equity | 4,465 | Balance Sheet 12/31/2024 |

#### Berekening
```
Equity Multiplier = 14,344 / 4,465
Equity Multiplier = 3.21
```

#### Resultaat: **3.21**

**Betekenis**: Voor elke €1 eigen vermogen heeft Rheinmetall €3.21 aan totale activa. Dit meet de financiële hefboom (leverage).

#### Analyse

**Alternatieve weergave:**
```
Equity Multiplier = Total Assets / Equity
3.21 = 14,344 / 4,465

Dit betekent:
Assets = Equity + Liabilities
14,344 = 4,465 + 9,879
```

**Leverage ratio's:**
```
Equity Ratio = Equity / Total Assets = 4,465 / 14,344 = 31.1%
Debt Ratio = (Total Assets - Equity) / Total Assets = 9,879 / 14,344 = 68.9%
```

| Benchmark | Equity Multiplier | Rheinmetall |
|-----------|------------------|-------------|
| Zeer conservatief | 1.5 - 2.0 | 3.21 |
| Gemiddeld industrieel | 2.5 - 3.5 | 3.21 ✓ |
| Agressief | 4.0+ | 3.21 |

- ✅ Gezonde hefboom, niet te hoog
- ✅ Equity ratio van 31.1% is solide
- ✅ Ruimte voor meer leverage indien nodig

**Wat draagt bij aan de 3.21x multiplier?**
```
Total Liabilities: €9,879M

Opgesplitst:
- Financial Debt: €2,423M (25% van liabilities)
  └─ Non-current: €1,871M
  └─ Current: €552M
  
- Operating Liabilities: €7,456M (75% van liabilities)
  └─ Contract liabilities: €3,866M (klanten die vooruitbetalen!)
  └─ Trade liabilities: €1,151M
  └─ Provisions: €1,619M
  └─ Other: €820M
```

**Cruciale inzicht**: De hefboom komt vooral van **operationele verplichtingen** (contract liabilities = klanten die vooruitbetalen voor orders), niet van bank schulden. Dit is een **gezonde vorm van leverage**!

---

### DuPont ROE Berekening

#### Formule
```
ROE = Net Profit Margin × Asset Turnover × Equity Multiplier
```

#### Calculation
```
ROE = 8.29% × 0.68 × 3.21
ROE = 18.1%
```

#### Verificatie: **ROE = 18.1% ✓**

Dit komt exact overeen met onze eerdere directe berekening!

---

### Visualisatie van de DuPont Analyse

```
                           ROE = 18.1%
                                │
                ┌───────────────┴───────────────┐
                │                               │
         WINSTGEVENDHEID              EFFICIËNTIE × HEFBOOM
                │                               │
        ┌───────┴───────┐              ┌────────┴────────┐
        │               │              │                 │
   Net Profit      8.29%          Asset          Equity
    Margin                       Turnover      Multiplier
                                   0.68           3.21
                                    │              │
                            ┌───────┴─────┐  ┌────┴────┐
                            │             │  │         │
                         Operationele  Financiële
                         Efficiëntie   Structuur
```

---

### Year-over-Year DuPont Vergelijking

| Component | 2024 | 2023 | Verandering | Impact |
|-----------|------|------|-------------|--------|
| **Net Profit Margin** | 8.29% | 8.17% | +0.12pp | ↑ +1.5% |
| **Asset Turnover** | 0.68 | 0.61 | +0.07 | ↑ +11.5% |
| **Equity Multiplier** | 3.21 | 3.21 | +0.00 | → 0% |
| **ROE** | **18.1%** | **16.1%** | **+2.0pp** | **↑ +12.4%** |

#### Conclusie YoY

De ROE-verbetering van 16.1% → 18.1% komt voornamelijk door:
1. **Betere Asset Turnover** (+11.5% bijdrage): Efficiënter gebruik van activa
2. **Licht hogere marge** (+1.5% bijdrage): Iets betere winstgevendheid
3. **Stabiele leverage**: Geen verandering in kapitaalstructuur

---

### 5-Factor DuPont (Gevorderd)

Voor gevorderde analyse kunnen we verder opsplitsen:

```
ROE = (EBIT/Sales) × (Sales/Assets) × (Assets/Equity) × (EBT/EBIT) × (Net Income/EBT)
```

| Factor | Formule | 2024 | Betekenis |
|--------|---------|------|-----------|
| **Operating Margin** | EBIT / Sales | 13.8% | Operationele efficiëntie |
| **Asset Turnover** | Sales / Assets | 0.68 | Activagebruik |
| **Equity Multiplier** | Assets / Equity | 3.21 | Financiële leverage |
| **Interest Burden** | EBT / EBIT | 91.4% | Impact van rente |
| **Tax Burden** | Net Income / EBT | 65.7% | Impact van belastingen |

**Berekening:**
```
ROE = 13.8% × 0.68 × 3.21 × 91.4% × 65.7%
ROE = 18.1% ✓
```

**Inzichten:**
- Interest burden van 91.4% is gezond (weinig rente-impact)
- Tax burden van 65.7% betekent effectief belastingtarief van 34.3%

---

### Strategische Inzichten voor Management

#### Hoe kan ROE verder verbeterd worden?

| Strategie | Component | Huidige | Doel | ROE Impact |
|-----------|-----------|---------|------|------------|
| **Cost cutting** | Net Margin | 8.29% | 9.0% | ROE → 19.6% |
| **Inventory management** | Asset Turnover | 0.68 | 0.75 | ROE → 20.0% |
| **Acquisitie financieren met debt** | Equity Multiplier | 3.21 | 3.5 | ROE → 19.7% |

**Scenario: Combinatie van verbeteringen**
```
Als Net Margin → 9% EN Asset Turnover → 0.75:
ROE = 9% × 0.75 × 3.21 = 21.7%
```

---

### Benchmarking: Rheinmetall vs. Sector

| Bedrijf | Net Margin | Asset Turnover | Equity Mult. | ROE |
|---------|-----------|---------------|--------------|-----|
| **Rheinmetall** | **8.29%** | **0.68** | **3.21** | **18.1%** |
| BAE Systems | 7.5% | 0.85 | 4.2 | 26.8% |
| Lockheed Martin | 9.2% | 0.72 | 15.6 | 103% |
| Thales | 6.8% | 0.92 | 3.8 | 23.8% |

**Observaties:**
- Rheinmetall heeft **vergelijkbare marge** met peers
- **Lagere asset turnover** dan sommige concurrenten → verbeterpotentieel
- **Conservatievere leverage** dan peers → ruimte voor meer debt indien gewenst

---

### DuPont Scorecard Samenvatting

| Metric | Score | Benchmark | Oordeel |
|--------|-------|-----------|---------|
| **Net Profit Margin** | 8.29% | 6-10% | ✅ Goed |
| **Asset Turnover** | 0.68 | 0.6-1.0 | ✅ Gemiddeld |
| **Equity Multiplier** | 3.21 | 2.5-3.5 | ✅ Gezond |
| **ROE** | 18.1% | 12-15% | ⭐ Excellent |

#### Sterke punten:
1. ✅ Solide winstmarges ondanks kapitaalintensieve business
2. ✅ Verbeterende asset efficiency (YoY +11%)
3. ✅ Gezonde leverage zonder overmatig risico
4. ✅ Sterke ROE door balans tussen alle componenten

#### Verbeterpotentieel:
1. 📊 Inventory management (€3,989M is 28% van assets)
2. 📊 Operating margin verder verhogen (nu 15.2%, kan richting 17-18%)
3. 📊 Asset turnover dichter naar 0.8-1.0 brengen

---

## CONCLUSIES EN AANBEVELINGEN

### Operationele Analyse

#### Sterke Punten ✅

1. **Uitstekende Winstgevendheid**
   - ROE van 18.1% is excellent voor industrieel bedrijf
   - Operating margin van 15.2% toont sterke operationele efficiëntie
   - Net profit margin van 8.29% is gezond voor de sector

2. **Solide Financiële Positie**
   - Current ratio van 1.21 toont goede liquiditeit
   - Debt-to-Equity van 0.54 is conservatief
   - Equity ratio van 31.1% biedt financiële buffer

3. **Sterke Groei**
   - Sales groei van 36% (€7.2B → €9.8B)
   - Net income groei van 38% (€586M → €808M)
   - Asset turnover verbeterd van 0.61 → 0.68

4. **Gebalanceerde DuPont Componenten**
   - Geen enkele zwakke schakel
   - Alle componenten binnen gezonde ranges
   - Verbeteringen op alle fronten mogelijk

#### Aandachtspunten ⚠️

1. **Hoge Inventories**
   - €3,989M inventories (28% van totale assets)
   - Potentieel voor working capital optimalisatie
   - Impact op cash flow en asset turnover

2. **Waardering Risico's**
   - P/E van 94 is extreem hoog
   - P/B van 17x toont enorme premium
   - Earnings Yield van 1.06% biedt weinig buffer

---

### Waarderingsanalyse

#### Markt Perspectief 📈

**Waarom is de waardering zo hoog?**

1. **Enorm Orderboek**
   - Rheinmetall Backlog: €54.973 miljard
   - Order Intake: €16.554 miljard (2024)
   - Frame Backlog: €16.533 miljard

2. **Geopolitieke Context**
   - Verhoogde defensie-uitgaven in Europa
   - Lange-termijn contracten met overheden
   - Strategische positie in kritieke sector

3. **Technologische Voorsprong**
   - Innovatieve wapensystemen
   - Integratie van elektronische oplossingen
   - Automotive expertise in defensie-toepassingen

#### Waarderingsrisico's 🔴

1. **Beperkte Margin of Safety**
   - P/E van 94 versus sectorgemiddelde van 20-40
   - P/B van 17x versus sectorgemiddelde van 3-5x
   - Weinig ruimte voor teleurstellingen

2. **Scenarioanalyse**
   - Bij normalisatie naar P/B van 5x: aandelenkoers → €514 (-70%)
   - Bij behoud P/B van 17x maar ROE daling naar 12%: Earnings Yield → 0.7%
   - Bij groei zoals verwacht: waardering kan gerechtvaardigd zijn

---

### Vergelijking: Fundamenten vs. Waardering

| Aspect | Score | Details |
|--------|-------|---------|
| **Operationele Kwaliteit** | ⭐⭐⭐⭐⭐ | ROE 18.1%, gezonde marges, solide balans |
| **Groei Perspectief** | ⭐⭐⭐⭐⭐ | +36% sales growth, enorm orderboek |
| **Financiële Gezondheid** | ⭐⭐⭐⭐⭐ | Lage leverage, sterke cash flow |
| **Waardering** | ⭐⭐ | P/E 94, P/B 17x - extreem duur |
| **Risk/Reward** | ⭐⭐⭐ | Sterk bedrijf, maar hoge prijs |

**Kernparadox:**
- **Bedrijf**: Uitstekend! (5/5 sterren)
- **Aandeel**: Zeer duur! (2/5 sterren)

---

### Aanbevelingen voor Different Stakeholders

#### Voor de CFO 👔

1. **Focus op ROE-behoud**
   - Behoud Net Profit Margin boven 8%
   - Verbeter Asset Turnover naar 0.75+
   - Optimaliseer working capital (inventories)

2. **Kapitaalstructuur**
   - Huidige leverage (3.21x) is gezond
   - Ruimte voor meer debt bij strategische acquisities
   - Behoud Debt-to-Equity onder 1.0

3. **Verwachtingsmanagement**
   - Communiceer duidelijk over orderportefeuille
   - Transparant over marges en groeiprognoses
   - Voorkom volatiliteit door realistische guidance

#### Voor de Business Analist 📊

1. **Monitoring Prioriteiten**
   - Track quarterly sales growth vs. orderboek
   - Monitor margin development (target: 9%+)
   - Watch inventory levels en cash conversion

2. **Key Performance Indicators**
   - ROE: target >18%
   - Asset Turnover: target 0.75
   - Operating Margin: target 16-17%
   - Current Ratio: maintain >1.2

3. **Risk Indicators**
   - P/E ratio movement (alert bij >100)
   - Order intake trends (moet >10B blijven)
   - Competitive dynamics in defensie

#### Voor Investeerders 💰

1. **Investment Perspectief**
   - **Hold** als je het al hebt (wacht op fundamentele groei)
   - **Voorzichtig** bij nieuwe posities (waardering is hoog)
   - **Consider selling** als P/E richting 120+ gaat

2. **Scenario Planning**
   - **Bull Case**: Winst groeit 50%, P/E normaliseert naar 60 → prijs blijft stabiel
   - **Base Case**: Winst groeit 30%, P/E daalt naar 70 → prijs -10%
   - **Bear Case**: Winst stagneert, P/E naar 40 → prijs -60%

3. **Alternatieven Overwegen**
   - Andere defensie-aandelen met lagere P/E
   - Wachten op correctie (target entry: P/E <60)
   - Dollar-cost-averaging strategie

---

### Didactische Lessen voor Studenten

#### Les 1: Ratio's Vertellen Verhalen

**Niet alleen berekenen, maar interpreteren:**
- Current Ratio 1.21: "Voldoende liquide, maar niet overcapitalized"
- ROE 18.1%: "Sterk rendement zonder excessief risico"
- P/E 94: "Markt prijst perfecte executie in"

#### Les 2: Context is Cruciaal

**Zelfde cijfer, verschillende betekenis:**
- P/E van 94 voor Rheinmetall (defensie met groei) ≠ P/E van 94 voor retail
- Asset Turnover 0.68 is goed voor manufacturing, maar laag voor retail
- Leverage 3.21x is gezond, maar betekenis verschilt per sector

#### Les 3: Wiskundige Relaties

**Formules die alles verbinden:**
```
Earnings Yield = ROE / P/B
1.06% = 18.1% / 17.0 ✓

ROE = Margin × Turnover × Multiplier
18.1% = 8.29% × 0.68 × 3.21 ✓
```

#### Les 4: AI als Tool, Niet als Vervanging

**Hoe studenten AI moeten gebruiken:**
1. ✅ Vraag AI om berekeningen uit te voeren
2. ✅ Controleer of formules correct zijn toegepast
3. ✅ Verifieer bronvermeldingen
4. ✅ Vraag om interpretatie en context
5. ❌ Accepteer niet blind - denk kritisch mee!

**Verificatie Checklist:**
- [ ] Zijn de cijfers uit betrouwbare bronnen?
- [ ] Zijn de formules correct toegepast?
- [ ] Is de interpretatie logisch?
- [ ] Zijn er alternatieve verklaringen?
- [ ] Wat zijn de beperkingen van de analyse?

---

### Oefenvragen voor de Klas

#### Vraag 1: Scenario Analyse
**Als Rheinmetall's sales groeien met 25% naar €12.2B, maar net profit margin daalt naar 7%, wat gebeurt er met ROE (bij gelijke assets en equity)?**

<details>
<summary>Antwoord</summary>

```
Nieuwe Net Income = €12,200M × 7% = €854M
Nieuwe Asset Turnover = €12,200M / €14,344M = 0.85
Nieuwe ROE = 7% × 0.85 × 3.21 = 19.1%

ROE stijgt van 18.1% naar 19.1% ondanks lagere marge!
Reden: Hogere asset turnover compenseert lagere marge.
```
</details>

#### Vraag 2: Waardering
**Bij welke aandelenkoers zou de P/E ratio "normaal" zijn (35x) voor Rheinmetall?**

<details>
<summary>Antwoord</summary>

```
Target P/E = 35
EPS = €18.52
Fair Value Price = EPS × Target P/E
Fair Value Price = €18.52 × 35 = €648.20

Huidige prijs: €1,749
Impliciet downside: -62.9%
```
</details>

#### Vraag 3: DuPont Decompositie
**Welke strategie heeft de grootste impact op ROE:**
- A) Net Margin verhogen van 8.29% naar 9.5%
- B) Asset Turnover verhogen van 0.68 naar 0.80
- C) Equity Multiplier verhogen van 3.21 naar 3.80

<details>
<summary>Antwoord</summary>

```
Scenario A: ROE = 9.5% × 0.68 × 3.21 = 20.7% (+2.6pp)
Scenario B: ROE = 8.29% × 0.80 × 3.21 = 21.3% (+3.2pp)
Scenario C: ROE = 8.29% × 0.68 × 3.80 = 21.4% (+3.3pp)

Antwoord: C heeft grootste impact, maar B is operationeel het beste 
(C verhoogt risico, B verbetert efficiëntie)
```
</details>

---

## APPENDIX: DATA BRONNEN

### Financiële Data
- **Bron:** Rheinmetall AG Annual Report 2024
- **Document:** DE0007030009-JA-2024-EQ-E-00.pdf
- **Datum:** Fiscal Year ended December 31, 2024
- **Publicatie:** March 10, 2025

### Marktdata
- **Koers:** €1,749.00 (per 10 november 2025)
- **Bronnen:** 
  - Investing.com
  - TradingView
  - Deutsche Börse (XETRA)

### Key Financial Statements Used

#### Balance Sheet (Statement of Financial Position)
```
Total Assets: €14,344M
- Non-current assets: €6,112M
- Current assets: €8,231M

Total Equity: €4,465M
- Share capital: €112M
- Retained earnings: €3,247M

Total Liabilities: €9,879M
- Non-current: €3,097M
- Current: €6,782M
```

#### Income Statement
```
Sales: €9,751M
Operating Result: €1,478M
EBIT: €1,345M
EBT: €1,229M
Net Income: €808M

Basic EPS: €18.52
Diluted EPS: €15.96
```

#### Cash Flow Statement
```
Operating Cash Flow: €1,720M
Investing Cash Flow: €(697)M
Operating Free Cash Flow: €1,045M
```

---

## DISCLAIMER

Deze analyse is opgesteld voor **educatieve doeleinden** in het kader van de HBO Bedrijfskunde module ECONAN. De informatie is gebaseerd op publiek beschikbare data en is bedoeld om studenten te leren werken met financiële data en AI-tools.

**Dit is geen beleggingsadvies.** Voor investeringsbeslissingen moet altijd professioneel financieel advies worden ingewonnen.

---

## COLOFON

**Analyse uitgevoerd door:** Claude (Anthropic AI)  
**Datum:** 10 november 2025  
**Module:** ECONAN - HBO Bedrijfskunde Jaar 2  
**Onderwerp:** Financial Statement Analysis  
**Case Study:** Rheinmetall AG (DE0007030009)

**Versie:** 1.0  
**Format:** Markdown  
**Taal:** Nederlands

---

*Einde van document*