# Week 3 Sessie Draaiboek: Ratio Analyse & Triangulatie

**Duur:** 120 minuten (2 uur exact)
**Focus:** Hands-on ratio analyse met foutdetectie + AI triangulatie methodologie
**Output:** AI Verificatie Checklist + Benchmark Coördinatie Plan

---

## 📋 Pre-Sessie Vereisten

### Voor Studenten (VOOR de sessie afronden):

- [ ] **Boek hoofdstuk gelezen**: Ratio analyse, DuPont methode, triangulatie principes
- [ ] **Template-based data extraction compleet**: Alle 3 benchmark bedrijven (Week 2 homework)
- [ ] **Team charter voltooid**: Rolverdeling duidelijk (Week 1)
- [ ] **3 Euronext bedrijven geselecteerd**: 1 "eigen" + 2 benchmarks

### Voor Docent:

- [ ] Beamer/projector beschikbaar voor DuPont visual
- [ ] **CFO Answer Sheets** geprint (1 per CFO team, 5 sectoren beschikbaar)
  - Download vanuit: `/docs/instructors/index.html` → Week 3 → CFO Answer Sheets
  - Open HTML in browser → Print to PDF (Landscape) → Print
  - Elk blad bevat: tabel met gemarkeerde fouten, hints, cheatsheet, DuPont visual
  - Kies sector die matcht met team (Retail, Technology, Energy, Food & Beverage, Healthcare)
- [ ] Backup ruimte voor CFOs (of stille hoek buiten lokaal)
- [ ] Blanco A4 papier voor AI checklist ontwikkeling
- [ ] Zorg dat Business Analisten laptops hebben voor online tool

---

## 🎯 Learning Objectives Week 3

Na deze sessie kunnen studenten:

1. **LR-FSA-4**: Financiële ratio's correct berekenen én fouten detecteren via triangulatie
2. **LR-CRISP-1**: Data Preparation stap toepassen (ratio calculations voor Opdracht 1)
3. **LR-AI-2**: AI prompts schrijven die zelfcontrole (triangulatie) inbouwen
4. **LR-TEAM-1**: CFO rol als "Primus Inter Pares" - kennisoverdracht aan team

---

## ⏱️ Sessie Planning (120 minuten)

| Blok | Tijd | Activiteit | Actieve Tijd Studenten |
|------|------|------------|------------------------|
| **1** | 10 min | Check Pre-reading & Snelle Recap | 30% (Q&A) |
| **2** | 50 min | "Spot de Fout" Oefening (gedifferentieerd) | 100% |
| **3** | 35 min | Knowledge Transfer (CFOs als instructeurs) | 90% |
| **4** | 20 min | Benchmark Coördinatie & Opdracht 1 Planning | 100% |
| **5** | 5 min | Afsluiting & Homework | 50% |
| **Totaal** | **120 min** | | **~90%** |

---

## 📖 Blok 1: Check Pre-reading & Snelle Recap (10 min)

### Doel
Verifiëren dat studenten het boek hoofdstuk hebben bestudeerd, quick refresh van kernconcepten.

### Timing
- **0:00-0:02** (2 min): Check pre-reading (toon handen poll)
- **0:02-0:07** (5 min): Snelle Q&A over boek hoofdstuk
- **0:07-0:10** (3 min): DuPont visual recap + overgang

### Docentinstructie

**Start met check (2 min):**
> "Goedemorgen/middag! Welkom bij Week 3. We gaan vandaag hands-on werken met ratio analyse. Dit werkt alleen als jullie het boek hoofdstuk hebben gelezen."
>
> **Poll: Wie heeft het hoofdstuk over ratio analyse en DuPont methode gelezen? Steek je hand op.**
>
> *(Tel handen, minstens 80% zou gelezen moeten hebben)*

**Als >80% gelezen heeft:**
> "Prima! Dan kunnen we snel door naar de praktijk."

**Als <80% gelezen heeft:**
> "Oké, ik zie dat niet iedereen het gelezen heeft. We hebben dan 5 minuten extra nodig voor uitleg straks. Lees het vanavond absoluut nog, anders red je Opdracht 1 niet."

**Q&A (5 min):**
> "Hebben jullie vragen over wat je hebt gelezen? DuPont formule? Triangulatie principe? Maximaal 5 minuten Q&A."

*(Beantwoord vragen kort, verwijs naar boek voor details)*

**DuPont Visual Recap (3 min):**

*Projecteer DuPont breakdown visual op beamer:*

> "Even snel: dit is wat jullie vandaag gaan toepassen. DuPont analyse breekt Return on Assets (ROA) af in twee componenten:"
>
> 1. **EBIT Margin** = EBIT / Sales → "Hoeveel winst halen we uit elke euro omzet?"
> 2. **Total Assets Turnover** = Sales / Total Assets → "Hoe efficiënt gebruiken we onze assets?"
>
> **ROA = EBIT Margin × Total Assets Turnover**
>
> "De kracht van triangulatie: je kunt ROA op **twee manieren** berekenen:"
> - Direct: EBIT / Total Assets
> - Via DuPont: (EBIT / Sales) × (Sales / Total Assets)
>
> "Als beide uitkomsten niet matchen → er zit een fout in je data. Dat is precies wat we vandaag gaan oefenen."

**Overgang naar Blok 2:**
> "Jullie gaan nu 50 minuten hands-on werken met een oefening vol fouten. Business Analisten werken online op jullie laptops. CFOs krijgen een printed answer sheet en gaan naar een apart lokaal. Jullie hebben verschillende rollen vandaag."

---

## 🔍 Blok 2: "Spot de Fout" Oefening - Gedifferentieerd (50 min)

### Doel
Business Analisten oefenen ratio analyse hands-on. CFOs leren met hints en bereiden knowledge transfer voor.

### Timing
- **0:10-0:15** (5 min): Instructie + verdeling ruimtes
- **0:15-0:55** (40 min): Parallelle werksessies
- **0:55-1:00** (5 min): CFOs komen terug, voorbereiden presentatie

### Setup & Instructie (5 min)

**Verdeel materiaal:**
- **Business Analisten**: Gebruiken eigen laptop voor online tool
- **CFOs**: Krijgen printed PDF Answer Sheet (met gemarkeerde fouten, hints, cheatsheet, DuPont visual)

**Instructie aan Business Analisten:**
> "Business Analisten: jullie gaan online werken met de 'Spot de Fout' tool. Dit zijn 3 bedrijven uit dezelfde sector met financiële ratio's. In **elk bedrijf** zit **één fout**."
>
> - Bedrijf A: **Makkelijke fout** (DuPont Identity)
> - Bedrijf B: **Gemiddelde fout** (Leverage relatie)
> - Bedrijf C: **Moeilijke fout** (Market ratios)
>
> "Jullie taak: vind de fout, bereken de correcte waarde, leg uit welke identiteit je gebruikt hebt."
>
> **Ga naar:** `https://[url]/oefeningen/spot-de-fout.html` *(URL op bord schrijven)*
>
> **Jullie mogen:**
> - Je boek gebruiken
> - Samen werken met andere Analisten in je team
> - Rekenmachine gebruiken
> - De 💡 **Hints** button gebruiken (rechtsbovenin) **als je vast zit**
> - De 📚 **Financial Ratios Cheatsheet** uitklappen (onder instructies)
>
> **Jullie mogen NIET:**
> - CFOs vragen (die zijn er niet)
>
> "Maak notities van je antwoorden. Over 40 minuten komen de CFOs terug om met jullie de oplossingen te bespreken."

**Instructie aan CFOs:**
> "CFOs: jullie krijgen een printed answer sheet. Maar eerst: waarom jullie?"
>
> **WHY - Jullie rol als Primus Inter Pares:**
> "Jullie zijn eerste onder gelijken. Dat betekent niet dat jullie de baas zijn, maar dat jullie verantwoordelijk zijn voor kwaliteit."
> - Jullie **controleren** wat je analisten produceren
> - Jullie **instrueren** je team hoe ze AI correct gebruiken
> - Jullie **zorgen** dat AI zichzelf controleert via triangulatie
>
> **HOW - Hoe gaan jullie dat doen:**
> 1. **Controleren**: Als een analist zegt "ROE = 24.5%", kunnen jullie dat checken
> 2. **Instrueren**: Jullie leren je team hoe ze AI moeten vragen:
>    - "Bereken ROE direct EN via DuPont"
>    - "Check of beide uitkomsten matchen"
>    - "Als ze verschillen, zoek de fout"
> 3. **AI Triangulatie**: Jullie ontwikkelen voorbeelden hoe analisten AI prompts schrijven met ingebouwde verificatie
>
> **WHAT - Wat gaan jullie nu doen (40 min):**
> - Bestudeer het answer sheet dat jullie krijgen:
>   - **Rode omcirkeling** = waar de fout zit
>   - **Hints** = hoe je de fout detecteert
>   - **Cheatsheet** = alle ratio formules
>   - **DuPont visual** = triangulatie methodologie
>
> **Jullie eindproduct:**
> - Je kunt de 3 fouten uitleggen aan je team
> - Je hebt 3 voorbeelden hoe analisten AI moeten instrueren voor triangulatie
> - Je weet hoe je kwaliteitscontrole uitvoert
>
> "Over 40 minuten komen jullie terug. Jullie krijgen dan 5 minuten om je presentatie voor te bereiden."

**Deel CFO Answer Sheets uit & stuur CFOs weg (5 min):**
> "Oké CFOs, pak jullie answer sheet. Jullie hebben nu 40 minuten. Ga naar de backup ruimte. Tot over 40 minuten!"

*(CFOs verlaten het lokaal met printed answer sheet)*

### Werksessie Business Analisten (40 min)

**Zorg dat alle Analisten online zijn:**
- Check dat iedereen de website heeft geopend
- Check dat ze een sector hebben geselecteerd

**Docent rol tijdens deze 40 minuten:**
- **Observeren**: Loop rond, kijk hoe studenten werken
- **Minimaal ingrijpen**: Laat ze zelf zoeken, denken, proberen
- **Hints alleen bij vastzitten**: Als een team compleet vast zit na 15 minuten:
  - "Heb je de 💡 Hints button al geprobeerd?"
  - "Kijk nog eens naar de DuPont formule in de cheatsheet"
  - "Check de 'DuPont Identity Check' rij onderaan de tabel"

**Wat je ziet (verwacht gedrag):**
- Eerste 10 min: Studenten lezen de tabel, proberen uit te vogelen waar te beginnen, sommigen openen hints
- Minuut 10-25: Actief rekenen, cheatsheet raadplegen, onderling overleggen
- Minuut 25-40: Sommigen klaar, anderen nog bezig met moeilijke fout (Bedrijf C)

**Signaal bij 40 minuten:**
> "Oké teams, nog 5 minuten. De CFOs komen zo terug. Sluit je notities af."

### CFOs Voorbereiden (5 min)

**Bij 40 minuten: Bel/app CFOs:**
> "CFOs, tijd om terug te komen. Jullie hebben 5 minuten om je presentatie voor te bereiden zodra je terug bent."

**Als CFOs terug zijn (50 min mark):**
> "CFOs, ga even kort met je team zitten. Jullie krijgen zo dadelijk 35 minuten om jullie kennis over te dragen. Bedenk kort hoe je dat gaat doen."

---

## 👨‍🏫 Blok 3: Knowledge Transfer - CFOs als Instructeurs (35 min)

### Doel
CFOs leiden teaching moment, vertalen inzichten naar AI prompt instructies voor triangulatie.

### Timing
- **1:00-1:25** (25 min): CFO presentaties per team + discussie
- **1:25-1:35** (10 min): AI Verificatie Checklist maken

### Instructie aan CFOs (1 min)

> "CFOs, jullie hebben net de oefening gedaan met hints. Nu gaan jullie **leraar** spelen voor je team."
>
> **Jullie hebben 25 minuten om:**
> 1. Uit te leggen hoe je de fouten vindt (gebruik DuPont visual!)
> 2. De antwoorden door te nemen (maar niet direct geven - laat team zelf denken)
> 3. Te vertalen naar **AI triangulatie instructies**
>
> "Per team, de CFO leidt dit. Analisten: luister, stel vragen, maak notities."

### CFO-geleide Sessies (25 min)

**Docent rol:**
- Loop langs teams, luister mee
- Help CFOs die moeite hebben met uitleggen
- Zorg dat focus blijft op **leerproces**, niet alleen antwoorden

**Wat CFOs zouden moeten doen** (stuur bij als je dit niet ziet):
1. **Start met makkelijke fout (Bedrijf A)**:
   - "Oké team, Bedrijf A heeft een DuPont fout. Wie heeft de ROE direct berekend?"
   - "En wie heeft PM × AT × EM berekend?"
   - "Matchen ze? Nee? Daar zit de fout."

2. **Gebruik DuPont visual**:
   - "Kijk naar deze breakdown. ROA kun je op twee manieren berekenen..."
   - Laat teams visual gebruiken als referentie

3. **Vertaal naar AI triangulatie**:
   - "Als we AI vragen om dit te doen, hoe zorgen we dat AI zichzelf checkt?"
   - "We kunnen AI vragen: 'Bereken ROE direct, en via DuPont. Zijn ze gelijk?'"

**Als teams snel klaar zijn** (<20 min):
> "Mooi! Ga nu alvast door naar de AI Verificatie Checklist. Welke checks wil je dat AI doet?"

### AI Verificatie Checklist Maken (10 min)

**Instructie aan alle teams** (bij 25 min mark):
> "Laatste 10 minuten van dit blok: maken jullie een **AI Verificatie Checklist**."
>
> "Dit is een lijst met checks die jullie AI gaan vragen te doen, zodat AI z'n eigen werk controleert. Triangulatie in de praktijk."
>
> **Voorbeeld checks:**
> - [ ] Bereken ROE direct (NI / Equity)
> - [ ] Bereken ROE via DuPont (PM × AT × EM)
> - [ ] Check: Zijn beide ROE's gelijk? (binnen 1% marge)
> - [ ] Bereken ROA direct (EBIT / Total Assets)
> - [ ] Bereken ROA via DuPont (EBIT Margin × Asset Turnover)
> - [ ] Check: Zijn beide ROA's gelijk?
> - [ ] Bereken D/E en check: EM - 1 = D/E?
>
> "Schrijf minimaal **5 checks** op die jullie in AI prompts gaan gebruiken. Deze checklist gebruik je bij Opdracht 1."

**Geef blanco A4 papier** per team om checklist op te schrijven.

**Output**: Elk team heeft een A4 met AI Verificatie Checklist (5+ checks)

---

## 🤝 Blok 4: Benchmark Coördinatie & Opdracht 1 Planning (20 min)

### Doel
3 Analisten stemmen KPI's af. Teams plannen Opdracht 1 afronding.

### Timing
- **1:35-1:50** (15 min): Analisten coördinatie (onderling)
- **1:50-1:55** (5 min): Management strategische vraag formuleren

### Analisten Coördinatie (15 min)

**Instructie aan Analisten:**
> "Business Analisten, de komende 15 minuten gaan jullie binnen je team coordineren. Jullie hebben elk één bedrijf geanalyseerd. Nu gaan jullie benchmarks vergelijken."
>
> **Coördinatie checklist:**
> 1. **Data extraction status check**: Hebben alle 3 Analisten de template-based extraction compleet?
>    - Zo niet: wie heeft wat nog nodig?
> 2. **KPI definities afstemmen**: Gebruiken jullie dezelfde formules?
>    - ROE: Net Income / Equity (ja?)
>    - ROA: EBIT / Total Assets OF Net Income / Total Assets?
>    - D/E: Total Debt / Equity OF Total Liabilities / Equity?
>    - **Kies één definitie en gebruik die consistent!**
> 3. **Ratio berekeningen verdelen**: Wie berekent welke ratio's voor zijn bedrijf?
>    - Profitability: ROE, ROA, Profit Margins
>    - Solvency: D/E, Equity Multiplier, Interest Coverage
>    - Efficiency: Asset Turnover, Inventory Turnover
>    - Market: P/E, Market-to-Book
> 4. **Tijdlijn afspreken**: Wanneer hebben we alle berekeningen klaar?
>    - Vóór Week 4 sessie: Alle ratio's berekend
>    - Vóór Opdracht 1 deadline: Benchmark vergelijking compleet

**Docent rol:**
- Loop langs teams
- Check of ze daadwerkelijk KPI definities vergelijken
- Help bij conflicten ("Welke formule gebruiken we nou?")
- Zorg dat ze het opschrijven (geen loze afspraken)

**Output**: Teams hebben schriftelijk:
- Status check voltooid
- KPI definities afgestemd (1 lijst voor hele team)
- Taakverdeling ratio berekeningen
- Tijdlijn

### Management Strategische Vraag (5 min)

**Instructie aan Management (CFO + andere C-suite rollen):**
> "Management, terwijl de Analisten coördineren: wat is jullie strategische vraag voor Opdracht 1?"
>
> **Opdracht 1 vraag: "Waar staan we competitief gezien?"**
>
> "Maak dit specifiek voor jullie bedrijf en sector. Bijvoorbeeld:"
> - "Is onze ROE hoger of lager dan sectorgemiddelde?"
> - "Waarom heeft concurrent X een betere Asset Turnover?"
> - "Moeten we meer schuld opnemen om competitief te blijven? (D/E analyse)"
>
> "Schrijf in 1-2 zinnen jullie strategische vraag op. Deze gaat in Opdracht 1 rapport."

**Output**: Elk team heeft strategische vraag geformuleerd (1-2 zinnen)

---

## 📚 Blok 5: Afsluiting & Homework (5 min)

### Doel
Duidelijke homework afspraken, preview Week 4.

### Timing
- **1:55-2:00** (5 min): Homework checklist + Week 4 preview

### Homework Checklist

> "Oké teams, let op. Dit is jullie homework voor volgende week:"
>
> **1. Ratio's berekenen** (alle 3 Analisten):
> - Bereken voor jouw bedrijf minimaal:
>   - Profitability: ROE, ROA, Net Profit Margin
>   - Solvency: D/E ratio, Equity Multiplier
>   - Efficiency: Asset Turnover
>   - Market: P/E, Market-to-Book (als data beschikbaar)
> - Gebruik de **AI Verificatie Checklist** die jullie vandaag hebben gemaakt
> - Laat AI triangulatie doen (twee berekenwegen, check of ze matchen)
>
> **2. Opdracht 1 voorbereiden** (heel team):
> - IST-situatie bepalen: "Waar staan we nu?"
> - Benchmark vergelijking: "Hoe presteren we vs concurrenten?"
> - Deadline Opdracht 1: *(vul deadline in)*
>
> **3. Week 4 checkpoint voorbereiden** (Management leidt):
> - Korte presentatie (5 min): Wat hebben we tot nu toe?
> - Laat ratio's zien, eerste inzichten benchmarks
> - Management presenteert, Analisten ondersteunen met data

### Week 4 Preview

> "Volgende week: **Checkpoint presentaties**. Elk team presenteert 5 minuten over hun voortgang. Management leidt presentatie, Analisten tonen data."
>
> "Zorg dat je ratio's berekend hebt, want je moet laten zien wat je hebt gevonden. Dit is jullie eerste 'tussenrapportage' aan mij als opdrachtgever."

**Sluit sessie af:**
> "Succes met de homework. Zie jullie volgende week!"

---

## 🎯 PAM Framework Alignment

### Purpose (Waarom doen we dit?)
**Score: 5/5**

- **Real-world relevantie**: Fouten in financiële data komen voor in echte jaarrekeningen (restatements, audit findings)
- **Direct bruikbaar**: Triangulatie checklist gebruiken in Opdracht 1 (30% van cijfer)
- **Professionele skill**: Zelfs AI heeft verificatie nodig - studenten leren AI te "auditen"

**Student quote (verwacht):**
> "Nu snap ik waarom grote bedrijven accountants hebben. Eén foutje en je ratio's kloppen niet meer."

### Autonomy (Hoeveel controle hebben studenten?)
**Score: 5/5**

- **Gedifferentieerde aanpak**: Business Analisten (hands-on) vs CFOs (hints + teaching)
- **Vrije keuzes**:
  - Welke sector kiezen voor oefening?
  - Hoe leg je het uit aan je team? (CFO bepaalt)
  - Welke AI tool gebruiken? (Claude, ChatGPT, Copilot)
  - Welke KPI definities kiezen bij conflict?
- **Peer teaching**: CFO als leraar (niet docent)

**Student quote (verwacht):**
> "Ik mocht zelf beslissen hoe ik het uitlegde. Voelde echt als leider van het team."

### Mastery (Ervaar ik groei?)
**Score: 5/5**

- **Progressieve moeilijkheid**: Easy → Medium → Hard fouten
- **Scaffolding**: CFOs krijgen hints, Analisten niet (maar kunnen boek raadplegen)
- **Metacognitie**: Van "fout vinden" → "AI leren fouten te vinden" (hogere orde denken)
- **Directe feedback**: Teams checken elkaars werk, CFO geeft uitleg

**Mastery progression:**
1. Week 2: Data extraction (mechanical)
2. Week 3: Ratio calculation + error detection (analytical)
3. Week 4+: AI triangulatie toepassen (metacognitive)

---

## 🛡️ Risk Mitigatie

### Risico 1: Studenten hebben boek niet gelezen

**Symptoom**: <50% steekt hand op bij pre-reading check

**Actie**:
1. Blok 1 uitbreiden naar 15 minuten (5 min extra uitleg)
2. Snelle recap DuPont formule, leverage identity, market ratios
3. Blok 2 verkorten naar 45 minuten
4. Na sessie: email naar hele klas met reminder boek lezen

**Preventie**: Week 2 al aankondigen: "Week 3 werkt alleen als je hoofdstuk X gelezen hebt."

### Risico 2: CFOs vinden geen rustige plek buiten lokaal

**Symptoom**: CFOs komen terug na 10 minuten: "We kunnen nergens heen"

**Actie**:
1. Plan B: CFOs gaan naar hoek van zelfde lokaal, gebruiken koptelefoon
2. Analisten mogen niet naar CFOs kijken/vragen
3. CFOs draaien stoelen om, vormen eigen 'pod'

**Preventie**: Van tevoren backup ruimte regelen (ander lokaal, studiehoek reserveren)

### Risico 3: Analisten zitten compleet vast (geen enkele fout gevonden na 20 min)

**Symptoom**: Teams staren naar papier, geen berekeningen zichtbaar

**Actie**:
1. Docent geeft "level 1 hint" aan alle teams:
   - "Begin met Bedrijf A. Bereken ROE op twee manieren."
2. Als nog steeds vast (na 30 min), "level 2 hint":
   - "Kijk naar de DuPont identity check rij onderaan de tabel. Klopt die?"
3. Uiterste redmiddel (35 min mark): Geef antwoord Bedrijf A, laat ze B en C zelf doen

**Preventie**: Zorg dat boek hoofdstuk echt gelezen is (zie Risico 1)

### Risico 4: CFOs kunnen niet goed uitleggen aan hun team

**Symptoom**: CFO zegt alleen antwoorden voor, geen uitleg proces

**Actie**:
1. Docent interveniëren: "Stop even. Leg uit HOE je de fout vond, niet alleen WAT de fout is."
2. Geef voorbeeld: "Stel je vraag als leraar: 'Wat krijg je als je PM × AT × EM berekent?'"
3. Vraag Analisten: "Begrijpen jullie het? Laat zien met berekening."

**Preventie**: In Blok 2 instructie benadrukken: "CFOs, jullie zijn leraar straks, niet antwoordenmachine."

### Risico 5: Teams hebben niet alle 3 bedrijven extracted (Week 2 homework niet af)

**Symptoom**: Bij Blok 4 blijkt >30% teams data incompleet

**Actie**:
1. Blok 4 wordt "data extraction sprint" (15 min werken aan missing data)
2. Teams met complete data: beginnen al met ratio berekeningen
3. Extra homework: Alles af hebben vóór Week 4
4. Waarschuwing: "Zonder complete data kan je Opdracht 1 niet halen"

**Preventie**: Week 2 einde al checken: "Wie heeft alle 3 bedrijven extracted? Steek hand op."

---

## 📎 Appendix: Voorbeeld AI Triangulatie Prompts

### Prompt 1: DuPont Verificatie

```
Ik heb de volgende financiële data voor Bedrijf X:
- Net Income: €2.5M
- Sales: €87M
- Total Assets: €45M
- Total Equity: €14M

Bereken Return on Equity (ROE) op TWEE manieren:
1. Direct: ROE = Net Income / Equity
2. Via DuPont: ROE = Profit Margin × Asset Turnover × Equity Multiplier

Toon beide berekeningen stap-voor-stap.
Controleer: zijn beide uitkomsten gelijk? (binnen 0.1% verschil)
Als ze NIET gelijk zijn: waar zit de fout?
```

### Prompt 2: Leverage Identiteit Check

```
Voor Bedrijf Y heb ik:
- Total Assets: €52M
- Total Equity: €11M
- Debt-to-Equity Ratio: 1.7 (uit jaarverslag)

Verificatie opdracht:
1. Bereken Equity Multiplier: EM = Total Assets / Equity
2. Bereken D/E via identiteit: D/E = EM - 1
3. Vergelijk berekende D/E met gerapporteerde D/E (1.7)
4. Als ze verschillen: leg uit waar de discrepantie vandaan komt

Toon je berekeningen.
```

### Prompt 3: ROA Triangulatie (DuPont Breakdown Visual)

```
Bedrijf Z data:
- EBIT: €4.1M
- Sales: €32M
- Total Assets: €28M

Bereken Return on Assets (ROA) op twee manieren:
1. Direct: ROA = EBIT / Total Assets
2. Via breakdown:
   - EBIT Margin = EBIT / Sales
   - Asset Turnover = Sales / Total Assets
   - ROA = EBIT Margin × Asset Turnover

Maak een visual breakdown (zoals DuPont schema).
Controleer of beide ROA's exact gelijk zijn.
```

### Prompt 4: Market Ratio Triangulatie

```
Voor Bedrijf W:
- ROE: 24.5%
- P/E Ratio: 28.42
- Market-to-Book (uit rapport): 6.95

Verificatie:
1. Gebruik identiteit: ROE = (Market-to-Book) / (P/E)
2. Herrangschik: Market-to-Book = ROE × P/E
3. Bereken verwachte Market-to-Book
4. Vergelijk met gerapporteerde 6.95
5. Geef oordeel: klopt de data? Waar zit eventuele fout?
```

---

## 📚 Referenties

- **"Spot de Fout" tool**: `/docs/oefeningen/spot-de-fout.html`
- **DuPont breakdown visual**: `/docs/background-docs/subjects/roi-for-dupont-analysis-which-included-sale-total-assets-in-formula-for-calculation-for-financial-analysis-vector.jpg`
- **Week 2 sessie**: `/docs/draaiboeken/week-2-sessie.html`
- **Opdracht 1 rubric**: `/docs/assessment/index.html` (CRISP-DM criteria)
- **Instructors antwoordmodel**: `/docs/instructors/index.html#spot-de-fout-antwoorden`

---

**Versie**: 1.0
**Laatste update**: 2025-01-23
**Auteur**: ECONAN Teaching Team (met Claude Code)
