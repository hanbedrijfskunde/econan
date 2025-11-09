# AI-Augmented Path: Prompt Templates voor CRISP-DM

**Versie**: 1.0
**Datum**: 9 November 2025
**Doel**: Prompt templates voor Junior Analisten die AI gebruiken om door CRISP-DM te navigeren

---

## Introductie

Als Analist die het **AI-Augmented Path** kiest, gebruik je AI assistants (zoals ChatGPT, Claude, of andere LLMs) om je door de CRISP-DM systematiek te leiden. Deze templates helpen je **effectieve prompts** te schrijven voor elke fase.

### Belangrijke Principes

1. **AI is een tool, geen vervanger**: Jij blijft verantwoordelijk voor kwaliteit en validatie
2. **Iteratief prompting**: Eerste prompt is zelden perfect - verfijn op basis van output
3. **Kritische evaluatie**: Vraag altijd: "Klopt dit? Hoe weet ik dat zeker?"
4. **Documentatie**: Log je prompts + AI outputs + jouw validatie

---

## CRISP-DM Fase 1: Business Understanding

### Doel
Vertaal de strategische vraag van je Senior stakeholder naar concrete data-analyse vragen.

### Template 1.1: Strategische Vraag Decompositie

```
[CONTEXT]
Ik ben Junior Analist voor [SECTOR] bedrijf. Mijn Senior stakeholder ([ROL: CEO/CFO/etc.])
heeft de volgende strategische vraag:

"[STRATEGISCHE VRAAG VAN SENIOR]"

[BEDROM CONTEXT]
In de vorige module (BEDROM) analyseerden we deze sector conceptueel. Belangrijkste inzichten:
- [Inzicht 1 uit BEDROM]
- [Inzicht 2 uit BEDROM]
- [Inzicht 3 uit BEDROM]

[TAAK]
Help me deze strategische vraag om te zetten in concrete, data-gedreven sub-vragen die ik kan
beantwoorden met data-analyse. Geef minimaal 5 sub-vragen die:
1. Specifiek genoeg zijn om te meten
2. Relevant zijn voor de strategische beslissing
3. Haalbaar zijn met beschikbare data types (verkoop, financieel, operationeel, extern)

[OUTPUT FORMAT]
Voor elke sub-vraag:
- Sub-vraag: [vraag]
- Data nodig: [welke data types]
- Analyse type: [descriptief/predictief/prescriptief]
- Business impact: [hoe helpt dit de strategische vraag beantwoorden]
```

**Voorbeeld Output Validatie:**
- ✅ Check: Zijn de sub-vragen SMART?
- ✅ Check: Kan ik deze vragen beantwoorden met data (niet alleen expert opinion)?
- ✅ Check: Zijn deze vragen relevant voor mijn Senior stakeholder?

---

### Template 1.2: Success Criteria Definitie

```
[CONTEXT]
Strategische vraag: "[VRAAG]"

Mijn Senior stakeholder ([ROL]) zal mijn analyse gebruiken om een beslissing te nemen tussen:
- Optie A: [beschrijving]
- Optie B: [beschrijving]

[TAAK]
Help me definiëren wat "succes" betekent voor deze analyse. Wat moet ik kunnen aantonen
zodat mijn stakeholder een weloverwogen beslissing kan nemen?

[OUTPUT FORMAT]
1. **Key Performance Indicators (KPIs)**: Welke metrieken moet ik meten?
2. **Decision Criteria**: Bij welke uitkomsten adviseer ik Optie A vs. B?
3. **Risk Factors**: Welke onzekerheden moet ik expliciet adresseren?
4. **Stakeholder Communication**: Hoe presenteer ik resultaten zodat [ROL] het begrijpt?
```

**Voorbeeld Output Validatie:**
- ✅ Check met Senior: "Klopt het dat je deze KPIs wilt zien?"
- ✅ Check: Zijn decision criteria helder en ondubbelzinnig?

---

## CRISP-DM Fase 2: Data Understanding

### Template 2.1: Data Source Exploratie

```
[CONTEXT]
Ik werk aan vraagstuk: "[VRAAG]"

Beschikbare datasets:
- Dataset 1: [naam, beschrijving, periode, aantal rijen]
- Dataset 2: [naam, beschrijving, periode, aantal rijen]
- Dataset 3: [etc.]

[TAAK DEEL 1: Relevantie Check]
Voor elke dataset, beoordeel:
1. Relevantie: Op schaal 1-5, hoe relevant is deze data voor mijn vraagstuk?
2. Reden: Waarom wel/niet relevant?
3. Key variables: Welke kolommen zijn waarschijnlijk het belangrijkst?

[TAAK DEEL 2: Gap Analysis]
Welke data ONTBREEKT nog die cruciaal is voor mijn analyse?
Voor elke gap:
- Wat ontbreekt: [beschrijving]
- Waarom cruciaal: [business rationale]
- Mogelijk alternatief: [proxy data of andere benadering]
```

**Voorbeeld Output Validatie:**
- ✅ Check: Upload sample van data naar AI en vraag: "Beschrijf deze dataset"
- ✅ Check: Vergelijk AI output met echte data preview (first 10 rows)
- ❌ **Waarschuwing**: AI kan niet IN je data kijken tenzij je het uploadt!

---

### Template 2.2: Data Quality Assessment

```
[CONTEXT]
Ik heb dataset: [NAAM]
Sample data (eerste 10 rijen):
[PLAK HIER SAMPLE DATA]

Metadata:
- Kolommen: [lijst van kolommen met data types]
- Periode: [van wanneer tot wanneer]
- Bron: [waar komt data vandaan]

[TAAK]
Analyseer potentiële data quality issues:

1. **Completeness**: Welke kolommen hebben waarschijnlijk missing values? Hoe erg is dat?
2. **Consistency**: Zie je inconsistenties (bijv. verschillende formats, spelfouten)?
3. **Accuracy**: Zijn er waarden die verdacht lijken (outliers, impossible values)?
4. **Timeliness**: Is deze data recent genoeg voor mijn analyse?
5. **Relevance**: Zijn alle kolommen relevant, of is er ruis?

Voor elk issue, suggereer een **behandeling** (bijv. imputation, removal, transformation).
```

**Voorbeeld Output Validatie:**
- ✅ Check: Run descriptive statistics (mean, median, min, max) om AI's vermoedens te checken
- ✅ Check: Visualiseer distributie van key variables
- ⚠️ **Kritisch**: AI kan data issues MIS-INTERPRETEREN - altijd zelf checken!

---

## CRISP-DM Fase 3: Data Preparation

### Template 3.1: Data Cleaning Strategy

```
[CONTEXT]
Dataset: [NAAM]
Geïdentificeerde quality issues:
1. [Issue 1]: [beschrijving]
2. [Issue 2]: [beschrijving]
3. [etc.]

Business vraagstuk: [VRAAG]

[TAAK]
Stel een data cleaning plan op:

Voor elk issue:
1. **Behandeling**: Wat ga ik doen? (remove, impute, transform, ignore)
2. **Rationale**: Waarom is dit de beste keuze voor MÍ JN specifieke vraagstuk?
3. **Impact**: Hoe beïnvloedt dit mijn analyse? (bias, sample size, etc.)
4. **Implementation**: Beschrijf in pseudo-code HOE ik dit doe

[CONSTRAINT]
Geef me ALTIJD meerdere opties per issue met trade-offs, zodat ik kan kiezen wat past
bij mijn business context.
```

**Voorbeeld Output Validatie:**
- ✅ Check: Begrijp ik WHY deze cleaning stap nodig is?
- ✅ Check: Kan ik de cleaning implementeren (in Python/R/Excel/Power BI)?
- ✅ **Documenteer**: Log welke cleaning je deed + rationale (voor assessment!)

---

### Template 3.2: Feature Engineering Suggesties

```
[CONTEXT]
Cleaned dataset met kolommen:
- [Kolom 1]: [type, beschrijving]
- [Kolom 2]: [type, beschrijving]
- [etc.]

Business vraagstuk: [VRAAG]

[TAAK]
Suggereer nieuwe features (afgeleide variabelen) die relevant zijn:

Voor elke feature:
1. **Naam**: [feature naam]
2. **Formule**: Hoe bereken je deze? (pseudo-code)
3. **Business rationale**: Waarom is deze feature relevant voor mijn vraagstuk?
4. **Voorbeeld**: Toon berekening met sample data

[COMPLEXITY LEVEL]
Ik target [Foundation / Analytical / Advanced] niveau.
- Foundation: Basis features (ratios, differences, categorization)
- Analytical: Time-based features (trends, rolling averages, seasonality)
- Advanced: Interaction features, transformations (log, scaling)
```

**Voorbeeld Output Validatie:**
- ✅ Check: Kan ik de feature berekenen met mijn data?
- ✅ Check: Maakt deze feature business sense (niet alleen statistisch)?
- ✅ **Senior Check**: Laat feature aan Senior zien - "Maakt dit sense voor jou?"

---

## CRISP-DM Fase 4: Modeling

### Template 4.1: Analysis Method Selectie

```
[CONTEXT]
Business vraagstuk: [VRAAG]
Type vraag: [descriptief / correlatie / causaal / predictief]
Beschikbare data: [summary]
Target complexity: [Foundation / Analytical / Advanced]

[TAAK]
Adviseer welke analyse methoden geschikt zijn:

Voor elke methode:
1. **Methode naam**: [bijv. Linear Regression, Descriptive Statistics, Scenario Analysis]
2. **Wanneer gebruiken**: In welke situatie is dit geschikt?
3. **Vereisten**: Welke data assumptiesAssertions moet ik checken?
4. **Interpretatie**: Hoe interpreteer ik de output in business termen?
5. **Limitations**: Wat kan deze methode NIET?

[RANKING]
Rank de methoden op:
- Geschiktheid voor mijn vraagstuk (1-5)
- Haalbaarheid voor mijn niveau (1-5)
- Communicatie naar niet-technische stakeholder (1-5)
```

**Voorbeeld Output Validatie:**
- ✅ Check: Snap ik HOE deze methode werkt (niet alleen wat-ie doet)?
- ✅ Check: Kan ik de assumptiesAssertions testen met mijn data?
- ⚠️ **Kritisch**: Kies niet de "coolste" methode, maar de meest PASSENDE!

---

### Template 4.2: Results Interpretation

```
[CONTEXT]
Methode gebruikt: [METHODE]
Output:
[PLAK HIER RESULTATEN: coefficients, p-values, R-squared, tables, etc.]

Business vraagstuk: [OORSPRONKELIJKE VRAAG]
Stakeholder: [ROL - CEO/CFO/etc.]

[TAAK DEEL 1: Technische Interpretatie]
Leg de resultaten uit:
1. **Wat zeggen de cijfers?**: Interpreteer key metrics (bijv. coefficient betekent X% change in Y)
2. **Statistische significance**: Zijn resultaten betrouwbaar? (check p-values, confidence intervals)
3. **Effect size**: Is het effect groot genoeg om business relevant te zijn?

[TAAK DEEL 2: Business Vertaling]
Vertaal technische resultaten naar business taal:
1. **Eén-zin conclusie**: Als ik maar één ding mag zeggen aan mijn stakeholder, wat is het?
2. **Actionable insight**: Wat betekent dit voor de strategische beslissing?
3. **Caveats**: Welke nuances of beperkingen moet ik melden?

[TASK DEEL 3: Visualisatie Advies]
Hoe visualiseer ik dit het best voor mijn [ROL] stakeholder?
```

**Voorbeeld Output Validatie:**
- ✅ Check: Snap mijn Senior de interpretatie? (test met verbal explanation)
- ✅ Check: Zijn de cijfers in lijn met business intuïtie? (sanity check)
- ⚠️ **Kritisch**: AI kan statistical significance MIS-INTERPRETEREN - check zelf!

---

### Template 4.3: Scenario Analysis Prompt

```
[CONTEXT]
Business vraagstuk: [VRAAG met opties A en B]
Key variables uit analyse:
- Variable 1: [naam, huidige waarde, range]
- Variable 2: [naam, huidige waarde, range]
- [etc.]

[TAAK]
Help me scenario analyse opzetten:

**Base Case (status quo)**:
- Assumpties: [huidige waarden]
- Verwacht outcome: [KPI voorspelling]

**Scenario A: [beschrijving Optie A]**
- Wat verandert: [welke variables, naar welke waarden]
- Rationale: [waarom deze waarden]
- Verwacht outcome: [KPI voorspelling]
- Risks: [wat kan misgaan]

**Scenario B: [beschrijving Optie B]**
- [zelfde structuur]

**Sensitivity Analysis**:
Welke variable heeft MEESTE impact op outcome? Hoe weet ik dat?

[OUTPUT]
Creëer een comparison table + advies over welk scenario robuuster is.
```

**Voorbeeld Output Validatie:**
- ✅ Check: Zijn scenario assumpties realistisch? (ask Senior!)
- ✅ Check: Begrijp ik de logic achter de voorspellingen?
- ✅ **Documenteer**: Log je assumpties - deze zijn cruciaal voor transparantie!

---

## CRISP-DM Fase 5: Evaluation

### Template 5.1: Model/Analysis Validatie

```
[CONTEXT]
Uitgevoerde analyse: [beschrijving]
Resultaten: [summary]
Methode gebruikt: [naam]

[TAAK]
Help me de kwaliteit van mijn analyse evalueren:

**1. Internal Validity**
- Heb ik alle CRISP-DM stappen correct uitgevoerd?
- Zijn mijn assumpties realistisch?
- Heb ik biases in mijn data/analysis aangepakt?

**2. Business Validity**
- Beantwoordt mijn analyse de oorspronkelijke strategische vraag?
- Is het outcome actionable (kan stakeholder ermee aan de slag)?
- Maakt het business sense (niet alleen statistical sense)?

**3. Robustness Check**
- Als ik iets anders had gedaan (andere method, andere cleaning), veranderen conclusies dan?
- Wat zijn de limitations van mijn analyse?
- Welke vragen kan ik NIET beantwoorden met deze data/methode?

[OUTPUT]
Geef me een "Limitations" sectie die ik in mijn rapport kan gebruiken.
```

**Voorbeeld Output Validatie:**
- ✅ Check: Ben ik eerlijk over wat ik NIET kan concluderen?
- ✅ Check: Heb ik assumpties expliciet gemaakt (niet verborgen)?
- ✅ **Assessment**: Limitation awareness is teken van mastery!

---

### Template 5.2: Alternative Explanations

```
[CONTEXT]
Mijn conclusie: [hoofdconclusie van analyse]
Data gebruikt: [beschrijving]
Methode: [naam]

[TAAK]
Speel "Devil's Advocate":

1. **Alternatieve verklaringen**: Wat zou ook deze data kunnen verklaren?
2. **Confounding factors**: Welke variabelen heb ik NIET gemeten die outcome beïnvloeden?
3. **Causality vs Correlation**: Claim ik causality? Is dat gerechtvaardigd?
4. **Cherry-picking risk**: Zou mijn conclusie anders zijn met andere tijdsperiode/sample?

[OUTPUT]
Voor elke alternatieve verklaring:
- Hoe plausibel (1-5)?
- Kan ik dit testen met aanvullende analyse?
- Moet ik mijn conclusie aanpassen?
```

**Voorbeeld Output Validatie:**
- ✅ Check: Ben ik intellectueel eerlijk? (niet confirmation bias)
- ✅ Check: Kan ik alternatieve verklaringen uitsluiten, of moet ik ze melden?
- ✅ **Senior Feedback**: Laat Senior alternatieve scenarios reviewen

---

## CRISP-DM Fase 6: Deployment

### Template 6.1: Strategische Aanbeveling Formulatie

```
[CONTEXT]
Strategische vraag: [OORSPRONKELIJKE VRAAG VAN SENIOR]
Rol stakeholder: [CEO/CFO/etc.]
Key findings: [3 belangrijkste inzichten uit analyse]

[TAAK]
Help me een strategische aanbeveling formuleren:

**Structuur:**
1. **Situatie**: Wat is het dilemma? (1-2 zinnen)
2. **Analyse**: Wat hebben we onderzocht? (2-3 zinnen, focus op aanpak)
3. **Inzichten**: Wat heeft de data ons geleerd? (3 key findings, elk met cijfer/bewijs)
4. **Aanbeveling**: Wat adviseer ik? (duidelijke keuze met rationale)
5. **Implementatie**: Wat zijn next steps?
6. **Risks & Mitigation**: Wat kan misgaan en hoe reduceren we risico?

[TONE]
- Zelfverzekerd maar niet arrogant
- Data-driven maar niet techno-babble
- Actionable niet alleen descriptief
- Geschikt voor [ROL] audience (aanpassen aan hun prioriteiten)
```

**Voorbeeld Output Validatie:**
- ✅ Check: Is mijn aanbeveling SPECIFIC (niet "we should consider...")?
- ✅ Check: Heb ik cijfers ter onderbouwing (niet alleen "data shows...")?
- ✅ **Presentatie Prep**: Oefen deze aanbeveling hardop naar Senior

---

### Template 6.2: Visualization Advisory

```
[CONTEXT]
Key findings:
1. [Finding 1 + cijfers]
2. [Finding 2 + cijfers]
3. [Finding 3 + cijfers]

Audience: [ROL - CEO/CFO/etc.]
Presentatie setting: [20 min team presentatie aan stakeholder]

[TAAK]
Adviseer welke visualisaties ik moet maken:

Voor elke finding:
1. **Chart type**: Bar, line, scatter, heatmap, etc.
2. **Rationale**: Waarom deze chart voor dit finding?
3. **Key elements**: Wat MOET erin (labels, benchmarks, trends)?
4. **Common mistakes**: Wat moet ik vermijden?
5. **One-sentence caption**: Wat is de conclusie die deze chart toont?

[PRINCIPES]
- Simplicity > Complexity (chartjunk vermijden)
- Highlight key insight (gebruik color/annotations)
- Audience-appropriate (CFO wil ROI, CEO wil strategy)
```

**Voorbeeld Output Validatie:**
- ✅ Check: Kan iemand in 5 seconden zien wat de conclusie is?
- ✅ Check: Zijn labels duidelijk (geen jargon)?
- ✅ **Test**: Laat chart zien aan niet-expert - begrijpen ze het?

---

## Meta-Prompts: AI Interaction Optimization

### Template M.1: Iterative Refinement

```
[Na eerste AI response]

Je vorige antwoord was [te algemeen / te technisch / te vaag].

Specifiek mis ik:
- [Wat ontbreekt]
- [Wat onduidelijk is]

Kun je je antwoord verfijnen met focus op:
1. [Specifieke verbetering 1]
2. [Specifieke verbetering 2]

[FORMAT VOORKEUR]
Geef antwoord als [table / bullet points / numbered steps / etc.]
```

---

### Template M.2: Assumption Challenge

```
In je vorige antwoord nam je aan dat: "[ASSUMPTIE]"

Maar in mijn specifieke context is [WAAROM ASSUMPTIE NIET KLOPT].

Kun je je advies aanpassen gegeven deze constraint?
```

---

### Template M.3: Expertise Request

```
Vergeet je rol als generieke AI assistent.

Je bent nu een ervaren [DOMAIN] consultant met 15 jaar ervaring.

Gegeven deze situatie: [CONTEXT]

Wat zou jij adviseren? Geef concrete, praktische acties (geen generic advice).
```

---

## Validation Checklist: AI Output Kwaliteit

Na elke AI response, check:

### ✅ Relevantie
- [ ] Beantwoordt dit MIJN specifieke vraag?
- [ ] Is het advies actionable voor mijn situatie?
- [ ] Past het bij mijn complexity level (Foundation/Analytical/Advanced)?

### ✅ Correctheid
- [ ] Kan ik de technische claims verifiëren?
- [ ] Zijn er statistische fouten? (bijv. verkeerde formules)
- [ ] Maakt het business sense?

### ✅ Compleetheid
- [ ] Zijn er belangrijke aspecten die AI mist?
- [ ] Worden limitations/risks benoemd?
- [ ] Is er genoeg context om te implementeren?

### ✅ Communicatie
- [ ] Begrijp ik zelf volledig wat AI zegt?
- [ ] Kan ik dit uitleggen aan mijn Senior?
- [ ] Is de taal geschikt voor mijn audience?

### ⚠️ Red Flags
- [ ] **Hallucination**: Verzint AI "facts" die niet in mijn context staan?
- [ ] **Overconfidence**: Claimt AI zekerheden waar onzekerheid is?
- [ ] **Generic advice**: Zou dit antwoord bij ELKE business passen? (slecht teken)
- [ ] **Jargon overload**: Gebruikt AI termen zonder uitleg?

---

## Documentatie: Prompt Logs voor Assessment

### Wat te loggen voor je assessment artifacts:

1. **Effective Prompts**: Je beste prompts per CRISP-DM fase
2. **AI Outputs**: Key responses die je daadwerkelijk gebruikte
3. **Validation Notes**: "Ik checkte dit door [methode], resultaat: [conclusie]"
4. **Refinements**: "Eerste prompt gaf [issue], tweede prompt loste dit op door [aanpassing]"
5. **Limitations**: "AI kon niet [X], dus ik deed [Y] handmatig"

### Template voor Prompt Log Entry

```markdown
## [CRISP-DM FASE]: [Onderwerp]

**Datum**: [DD-MM-YYYY]

**Prompt**:
[Je volledige prompt]

**AI Output** (relevant deel):
[Gekopieerde response]

**Validation**:
- Check 1: [Wat ik checkte] → [Resultaat: ✅ correct / ⚠️ issue gevonden]
- Check 2: [...]

**Refinement** (indien nodig):
[Wat ik aanpaste in tweede prompt]

**Business Application**:
[Hoe ik dit gebruikte in mijn analyse]
```

---

## Advanced Techniques (voor gevorderden)

### Chain-of-Thought Prompting

```
Los dit stap-voor-stap op:

1. Eerst, identificeer...
2. Dan, bereken...
3. Vervolgens, interpreteer...
4. Tenslotte, concludeer...

Leg bij elke stap je reasoning uit.
```

### Few-Shot Learning

```
Hier zijn twee voorbeelden van hoe ik data wil interpreteren:

**Voorbeeld 1**:
Input: [data]
Output: [interpretatie]

**Voorbeeld 2**:
Input: [data]
Output: [interpretatie]

Nu, doe hetzelfde voor MIJN data:
Input: [jouw data]
Output: ?
```

### Socratic Prompting

```
Stel me vragen die me helpen mijn eigen conclusie te trekken.

Context: [beschrijf je situatie]

Vraag me over:
- Welke assumpties ik maak
- Welke alternatieven ik overweeg
- Welke risico's ik zie
- Hoe ik mijn conclusie zou veranderen als [X]

Geef geen directe antwoorden, alleen vragen.
```

---

## Common Pitfalls & Solutions

### ❌ Pitfall 1: "AI als Oracle"
**Probleem**: Blindelings vertrouwen op AI output zonder validatie
**Oplossing**: Treat AI als analist - check everything!

### ❌ Pitfall 2: "Garbage In, Garbage Out"
**Probleem**: Vage prompts leiden tot vage antwoorden
**Oplossing**: Gebruik templates, geef context, wees specifiek

### ❌ Pitfall 3: "Technische Showboating"
**Probleem**: AI suggereert complexe methoden die je niet begrijpt
**Oplossing**: Vraag om Foundation-level uitleg, pas toe als je het snapt

### ❌ Pitfall 4: "Lost in Translation"
**Probleem**: AI gebruikt jargon dat je niet kunt uitleggen aan Senior
**Oplossing**: Vraag: "Leg dit uit alsof ik het aan een CEO moet vertellen"

### ❌ Pitfall 5: "Hallucination Acceptance"
**Probleem**: AI verzint "facts" of cijfers
**Oplossing**: Verify elke claim met echte data source

---

## Resources

### AI Tools
- **ChatGPT** (OpenAI): https://chat.openai.com
- **Claude** (Anthropic): https://claude.ai
- **Copilot** (Microsoft): https://copilot.microsoft.com

### Learning
- Prompt engineering guide: https://www.promptingguide.ai
- CRISP-DM methodology: https://www.datascience-pm.com/crisp-dm-2/

### ECONAN Specific
- Conventional Path comparison: zie `/docs/materiaal/conventional-pad.html`
- Assessment rubric: zie `/docs/assessment/rubric.html`
- Sector cases: zie `/docs/sectoren/`

---

**Volgende Stap**: Start met Template 1.1 om je strategische vraag te decompositie

**Need Help?**: Office hours voor AI Path studenten: [zie weekplanning]

**Assessment Tip**: Je prompt quality + validation rigor tellen zwaar mee in Criterium G (Mastery)!

---

**Einde Document**
