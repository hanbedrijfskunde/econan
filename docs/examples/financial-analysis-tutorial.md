# AI-AUGMENTED FINANCIAL ANALYSIS TUTORIAL
## Van Strategische Vraag naar Data-Gedreven Antwoord

**Module:** ECONAN - Economic Analysis
**Doelgroep:** Business Analisten (Week 1-2)
**Werkwijze:** AI-Augmented Path
**Tijdsinvestering:** 2-3 uur voor eerste analyse
**Tools:** ChatGPT, Claude, Gemini, of Mistral AI

---

## 🎯 WAT GA JE LEREN?

Na deze tutorial kun je:

✅ **Effectief prompts schrijven** voor financiële analyses
✅ **AI gebruiken als analysepartner** voor data-extractie en berekeningen
✅ **Financiële ratio's berekenen** met formules, bronnen en interpretaties
✅ **AI-output verifiëren en valideren** kritisch en systematisch
✅ **Complete analyses documenteren** reproduceerbaar en transparant
✅ **Zelfstandig werken** aan je Week 2 Opdracht 1 (Kengetallen analyse)

---

## 🌉 VAN BEDROM NAAR ECONAN

### Wat je al kent uit BEDROM

In BEDROM heb je **conceptuele analyses** gemaakt van je sector:
- Stakeholder mapping
- SWOT analyses
- Strategische uitdagingen (kwalitatief)
- Trends en ontwikkelingen

**Voorbeeld uit BEDROM (Fashion Retail):**
> "Duurzaamheid wordt steeds belangrijker voor consumenten. Merken die investeren in circulaire mode kunnen hun merk versterken en premium prijzen vragen."

### Wat je NU gaat doen in ECONAN

In ECONAN voeg je **kwantitatieve data** toe aan je conceptuele kennis:
- Hard cijfermatig onderbouwen
- KPI's berekenen en benchmarken
- NPV, ROI, marges analyseren
- Data-gedreven aanbevelingen doen

**Voorbeeld uit ECONAN (Fashion Retail):**
> "H&M's Conscious Collection heeft 30% hogere prijzen maar 12% lagere volumes. De netto marge stijgt van 9.8% naar 13.2% (+3.4pp). Bij schaling naar 25% van totale collectie: NPV = €2.3M positief over 3 jaar."

**De brug:** Van "dit is belangrijk" → "dit kost €X en levert €Y op"

---

## 🛠️ JOUW AI-AUGMENTED WORKFLOW

### De 5 Stappen van AI-Analyse

```
1. STRATEGISCHE VRAAG     →  Wat wil je weten?
         ↓
2. DATA VERZAMELEN        →  Jaarverslagen, financials, marktdata
         ↓
3. AI-ANALYSE UITVOEREN   →  Prompts schrijven, berekeningen laten maken
         ↓
4. VERIFICATIE            →  Formules checken, bronnen valideren
         ↓
5. DOCUMENTATIE           →  Alles vastleggen voor je team
```

---

## 📝 STAP 1: FORMULEER JE STRATEGISCHE VRAAG

### Wat je in Week 1 hebt gedaan

In Week 1 heb je met je team:

- **Bedrijven verdeeld**: Elk teamlid analyseert 1 Euronext-listed bedrijf
  - Jij hebt je "eigen" bedrijf gekozen
  - Je teamgenoten hebben 2-3 benchmark bedrijven gekozen (in dezelfde sector)
- Het jaarverslag van je bedrijf geanalyseerd (CEO letter, strategic report)
- Een strategische vraag geformuleerd (teambreed)
- Rollen verdeeld (Management vs Analisten)

**Voorbeelden van goede strategische vragen:**

| **Sector** | **Strategische Vraag** |
|------------|------------------------|
| Fashion Retail | Hoe kunnen we onze online sales margin verhogen zonder klantverlies? |
| Energy | Welke ROI heeft investering in wind energie vs. solar voor Ørsted? |
| Automotive | Kan Stellantis zijn debt-to-equity ratio verlagen door EV-transitie? |
| Banking | Wat is de impact van lagere rente op ING's net interest margin? |
| Real Estate | Loont het voor Unibail om meer woningen te bouwen vs. retail? |

### Vertaal naar Data-Vragen

Elke strategische vraag vereist **specifieke KPI's**:

**Voorbeeld:** "Hoe kunnen we onze online sales margin verhogen?"

**Data-vragen:**
- Wat is de huidige online vs. offline margin?
- Welke kostenposten verschillen tussen kanalen?
- Wat is de customer acquisition cost online vs. offline?
- Hoe ontwikkelen deze cijfers over tijd (trend)?

**→ Deze data ga je met AI ophalen en analyseren**

---

## 📝 STAP 2: VERZAMEL JE BRONNEN

### Wat je nodig hebt

Voor een goede financiële analyse heb je minimaal nodig:

**1. Jaarverslag (Annual Report)**
- Meestal beschikbaar op bedrijfswebsite → Investor Relations
- Bevat: Balance Sheet, Income Statement, Cash Flow Statement
- Let op: gebruik het meest recente **geauditeerde** verslag

**2. Koersinformatie**
- Euronext.com of Deutsche Börse voor actuele koersen
- Voor historische koersen: Yahoo Finance, Investing.com

**3. Sector Benchmarks (optioneel maar waardevol)**
- Gemiddelde ratio's in je sector
- Concurrenten voor vergelijking

### Praktisch Voorbeeld: Rheinmetall AG

Zie [Rheinmetall Financial Analysis](rheinmetall-analysis.html) voor een **compleet werkvoorbeeld**.

**Gebruikte bronnen:**
```
https://ir.rheinmetall.com/                              → Investor Relations
https://live.euronext.com/en/product/equities/...       → Koersdata
https://live.deutsche-boerse.com/equity/rheinmetall-ag  → Marktdata
```

**TIP:** Bookmark deze links in je browser voordat je start!

---

## 📝 STAP 3: SCHRIJF JE EERSTE PROMPT

### De Anatomie van een Goede Prompt

Een effectieve prompt heeft **3 componenten**:

```
1. CONTEXT     → Wie ben je? Wat is het doel?
2. OPDRACHT    → Wat wil je dat AI doet?
3. FORMAT      → Hoe wil je het resultaat zien?
```

### ✅ VOORBEELD: Goede Eerste Prompt

```
[CONTEXT]
Ik ben Business Analist voor de module ECONAN (HBO Bedrijfskunde).
Ik ga financiële analyses uitvoeren voor [BEDRIJF] in de [SECTOR] sector.
Ik wil leren hoe ik AI effectief kan inzetten voor data-analyse.

Hier zijn mijn bronnen:
- [Link naar jaarverslag / Investor Relations]
- [Link naar Euronext koersdata]

[OPDRACHT]
Voer een financial statement analysis uit voor [BEDRIJF].
Bereken de volgende ratio's voor fiscaal jaar [JAAR]:
1. Current Ratio (liquiditeit)
2. ROE (Return on Equity)
3. Debt-to-Equity Ratio (solvabiliteit)
4. Asset Turnover (efficiëntie)

[FORMAT]
Voor elke ratio wil ik zien:
- Formule
- Input values met bronvermelding (welke regel in financials?)
- Berekening
- Resultaat
- Interpretatie (wat betekent dit cijfer?)
```

### ❌ Voorbeeld: Slechte Prompt

```
Maak een analyse van Shell.
```

**Waarom slecht?**
- Geen context (wie ben je, wat is het doel?)
- Te vaag ("analyse" kan alles betekenen)
- Geen specifieke ratio's of focus
- Geen format instructies
- Geen bronnen

---

## 📝 STAP 4: BOUW STAP-VOOR-STAP OP

### Start Simpel, Ga Dieper

Gebruik de **"iteratieve aanpak"**: begin met basisanalyses en bouw uit.

### Fase 1: Basis Financial Ratios (10 min)

**Prompt:**
```
Bereken Current Ratio, ROE, Debt-to-Equity, Asset Turnover.
Toon formules, bronnen en resultaten.
```

**Wat je krijgt:**
- 4 basisratio's berekend
- Formules + data uit jaarverslag
- Eerste interpretaties

### Fase 2: Marktgebaseerde Ratio's (5 min)

**Prompt:**
```
Zoek de huidige aandelenkoers op en bereken de P/E ratio.
```

**Wat je krijgt:**
- AI zoekt actuele koers online
- Combineert met EPS uit jaarverslag
- Berekent P/E ratio

### Fase 3: Relaties Ontdekken (5 min)

**Prompt:**
```
Bereken 1/P/E × 100% (Earnings Yield) en vergelijk met ROE.
```

**Wat je krijgt:**
- Earnings Yield berekend
- Vergelijking met ROE
- Inzicht in marktexpectaties

### Fase 4: Geavanceerde Analyse (15 min)

**Prompt:**
```
Maak een DuPont analyse: splits ROE uit in Net Profit Margin,
Asset Turnover en Equity Multiplier.
```

**Wat je krijgt:**
- Complete ROE decompositie
- Inzicht waar waarde gecreëerd wordt
- Strategische aanbevelingen

### Fase 5: Documentatie (5 min)

**Prompt:**
```
Sla deze complete analyse op in een markdown bestand.
Voeg alle gebruikte prompts toe voor transparantie.
```

**Wat je krijgt:**
- Complete conversatie gedocumenteerd
- Reproduceerbaar
- Klaar om te delen met je team

**TOTAAL:** ~40 minuten voor complete analyse (eerste keer 1-2 uur)

---

## ✅ STAP 5: VERIFICATIE - ALTIJD CONTROLEREN!

### Waarom Verificatie Cruciaal Is

**AI is krachtig, maar niet feilloos:**
- ✅ Snel berekeningen uitvoeren
- ✅ Formules correct toepassen
- ❌ Bronnen kunnen verkeerd geïnterpreteerd worden
- ❌ Berekeningen moeten geverifieerd worden
- ❌ Toekomstvoorspellingen zijn speculatief

### Verificatie Checklist per Ratio

Voor **elke ratio** die AI berekent:

#### 1️⃣ Data Verificatie

```
[ ] Kloppen de cijfers met het originele jaarverslag?
[ ] Welke pagina/regel in het jaarverslag staat de data?
[ ] Is het de juiste periode (Q4 2024, FY 2024, etc.)?
[ ] Zijn de valuta's consistent (€ of $)?
```

**Praktisch:** Open het jaarverslag naast je AI-chat en check regel voor regel.

#### 2️⃣ Formule Verificatie

```
[ ] Is de formule correct? (Google de standaardformule)
[ ] Zijn alle componenten meegenomen?
[ ] Klopt de wiskundige uitwerking?
```

**Voorbeeld - Current Ratio:**
```
Formule: Current Assets / Current Liabilities

✅ CORRECT:
Current Assets = €15,234M
Current Liabilities = €8,123M
Current Ratio = 15,234 / 8,123 = 1.87

❌ FOUT:
Als AI "Total Assets" gebruikt i.p.v. "Current Assets"
```

#### 3️⃣ Interpretatie Verificatie

```
[ ] Is de conclusie logisch gegeven het cijfer?
[ ] Zijn er alternatieve verklaringen mogelijk?
[ ] Past het bij je BEDROM sector kennis?
[ ] Zijn er nuances gemist (seizoenseffecten, one-offs)?
```

**Voorbeeld:**
```
ROE = 18.1%

✅ GOEDE INTERPRETATIE:
"ROE van 18.1% ligt boven sector gemiddelde (12%).
Dit wijst op efficiënt gebruik van eigen vermogen.
Echter, DuPont toont hoge leverage (Equity Multiplier 3.21),
dus risico is ook hoger."

❌ SLECHTE INTERPRETATIE:
"ROE is hoog, dus dit is een goed bedrijf."
(Te simplistisch, mist nuance)
```

---

## 🧪 PRAKTIJKVOORBEELD: RHEINMETALL ANALYSE

### Zie Het in Actie

We hebben een **complete werkanalyse** gemaakt van Rheinmetall AG (Defense sector):

👉 **[Bekijk Rheinmetall Financial Analysis](rheinmetall-analysis.html)**

**Wat je ziet:**
1. **Alle 8 prompts** die gebruikt zijn
2. **Complete berekeningen** met formules en bronnen
3. **Iteratief proces** van simpel naar complex
4. **Verificatie** bij elke stap
5. **Didactische lessen** wat je leert van elk onderdeel

**Gebruik dit als template:** Pas de prompts aan voor jouw bedrijf!

---

## 🎓 JOUW OPDRACHT VOOR WEEK 2

### Opdracht 1: Kengetallen Analyse (Due: Week 3)

**Wat je gaat doen:**
1. Kies je bedrijf uit Week 1 (Euronext-listed in jouw sector)
2. Verzamel bronnen (jaarverslag, koersdata)
3. Voer basis financial analysis uit met AI
4. Bereken **minimaal 5 ratio's**, waarvan:
   - Minstens 1 sector-specifieke KPI
   - Liquiditeit, solvabiliteit, rentabiliteit, efficiëntie
5. Benchmark tegen 2-3 concurrenten
6. Interpreteer resultaten in business context
7. Documenteer alles (prompts, formules, bronnen, conclusies)

### Stappenplan Week 2

**Voorbereiding (thuis, 2-3 uur):**
1. **Selecteer je bedrijf** (doe je in Week 1 sessie)
2. **Download jaarverslag** (PDF) en bookmark Euronext pagina
3. **Werk deze tutorial door** stap voor stap
4. **Voer eerste analyse uit** met AI (basis ratio's)
5. **Documenteer je prompts en resultaten**

**Week 2 Sessie (in-class, 2 uur):**
1. **Teamoverleg** - deel je bevindingen met analisten
2. **Peer review** - check elkaars berekeningen
3. **Management alignment** - presenteer aan CFO
4. **Verfijn je analyse** op basis van feedback

**Week 3 Inleveren:**
- Complete analyse (markdown of PDF)
- Alle bronnen en formules gedocumenteerd
- Visualisaties (tabellen, grafieken)
- Business interpretatie met aanbevelingen

---

## 🧰 PROMPT LIBRARY - KOPIEER EN PAS AAN

### Basis Prompt Template

```
Ik ben Business Analist voor ECONAN (HBO Bedrijfskunde).
Ik analyseer [BEDRIJF NAAM] in de [SECTOR] sector voor fiscaal jaar [JAAR].

Bronnen:
- [Link naar jaarverslag]
- [Link naar Euronext/koersdata]

Bereken de volgende ratio's:
1. [Ratio 1]
2. [Ratio 2]
3. [Ratio 3]

Voor elke ratio: toon formule, input values (met bronvermelding),
berekening en interpretatie.
```

### Vervolg Prompts

**Marktdata toevoegen:**
```
Zoek de huidige aandelenkoers op en bereken de P/E ratio.
```

**Wiskundige bewerkingen:**
```
Bereken 1/P/E × 100% en interpreteer als Earnings Yield.
```

**Vergelijkingen:**
```
Vergelijk ROE met Earnings Yield. Wat zegt dit over marktexpectaties?
```

**Geavanceerde analyse:**
```
Maak een DuPont analyse: split ROE in Net Profit Margin,
Asset Turnover en Equity Multiplier.
```

**Trend analyse:**
```
Haal data op voor de laatste 3 jaar en toon de trend in ROE,
Net Profit Margin en Debt-to-Equity.
```

**Sector benchmarking:**
```
Vergelijk [BEDRIJF]'s ratio's met [CONCURRENT 1] en [CONCURRENT 2].
Wat zijn de belangrijkste verschillen?
```

**Documentatie:**
```
Sla deze analyse op in markdown format. Voeg alle gebruikte
prompts toe voor reproduceerbaarheid.
```

---

## ⚠️ VEELGEMAAKTE FOUTEN & HONDERRORS

### Fout #1: Te Vage Prompts

❌ **Slecht:** "Analyseer dit bedrijf"
✅ **Goed:** "Bereken Current Ratio, ROE en Debt-to-Equity voor FY2024 met bronvermelding"

### Fout #2: Niet Verifiëren

❌ **Slecht:** AI zegt het dus het klopt
✅ **Goed:** Check elke berekening tegen jaarverslag

### Fout #3: Geen Bronvermelding

❌ **Slecht:** ROE = 18.1%
✅ **Goed:** ROE = 18.1% (Jaarverslag 2024, p.42, Net Income / Shareholders Equity)

### Fout #4: Verkeerde Periode

❌ **Slecht:** Mixte cijfers uit Q3 2024 en FY 2023
✅ **Goed:** Alle cijfers uit FY 2024 Annual Report

### Fout #5: Geen Context bij Interpretatie

❌ **Slecht:** "ROE is 18.1%"
✅ **Goed:** "ROE is 18.1%, boven sector gemiddelde 12%, gedreven door hoge leverage (Equity Multiplier 3.21)"

### Fout #6: AI Overtuigingen Niet Challengen

❌ **Slecht:** Accepteer alle AI-interpretaties klakkeloos
✅ **Goed:** "Dit lijkt niet logisch. Kun je het uitleggen? Zijn er alternatieve verklaringen?"

---

## 🚀 NEXT STEPS NA DEZE TUTORIAL

### Je bent nu klaar om:

✅ **Week 2 opdracht te starten** - je eerste analyse uitvoeren
✅ **Effectief met AI te werken** - goede prompts schrijven
✅ **Kritisch te blijven** - altijd verificatie toepassen
✅ **Professioneel te documenteren** - reproduceerbare analyses maken

### Aanvullende Resources

**ECONAN Materiaal:**
- [CRISP-DM Methodology](../materiaal/#crisp-dm) - Volledige data science workflow
- [AI Prompt Templates](../materiaal/#ai-prompts) - Templates per CRISP-DM fase
- [Rheinmetall Complete Analysis](rheinmetall-analysis.html) - Werkvoorbeeld met alle details

**Externe Learning:**
- [Investopedia Financial Ratios Guide](https://www.investopedia.com/financial-ratios-4689817) - Uitleg alle ratio's
- [ChatGPT Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering) - Diepere prompt technieken

**Voor Vragen:**
- Brightspace Discussion Board
- Week 2 in-class Q&A sessie
- Office hours docent

---

## 📊 SELF-CHECK: BEN JE KLAAR VOOR WEEK 2?

### Checklist voor je start:

```
[ ] Ik begrijp het verschil tussen BEDROM (conceptueel) en ECONAN (kwantitatief)
[ ] Ik heb de Rheinmetall analyse bekeken en begrijp de workflow
[ ] Ik weet hoe ik een goede prompt schrijf (Context + Opdracht + Format)
[ ] Ik kan iteratief werken: simpel → complex
[ ] Ik weet hoe ik AI-output verifieer (data, formule, interpretatie)
[ ] Ik heb mijn bedrijf gekozen en bronnen verzameld
[ ] Ik weet waar ik hulp kan vragen als ik vastloop
```

**Als je 7/7 kunt afvinken:** Je bent klaar! 🎉

**Als je minder dan 5 hebt:** Lees de tutorial nogmaals door en bekijk het Rheinmetall voorbeeld.

---

## 💬 FEEDBACK & VRAGEN

Deze tutorial is levend materiaal. Heb je:
- **Onduidelijkheden?** Laat het weten!
- **Verbetervoorstellen?** Deel ze!
- **Extra voorbeelden nodig?** Vraag erom!

**Contact:** Via ECONAN website of in-class tijdens Week 2.

---

**Veel succes met je eerste AI-augmented analyse!** 🚀

**Remember:** AI is je **analysepartner**, niet je baas. Jij blijft de Business Analist die de strategische vragen stelt, de resultaten verifieert en de business interpretatie geeft. AI versnelt je werk, maar jouw kritische denken maakt het waardevol.

---

*Laatste update: 10 november 2025*
*ECONAN Module - HBO Bedrijfskunde - AI-Augmented Path*
