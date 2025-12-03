# Week 6 Sessie Draaiboek: Financial Wind Tunneling

**Duur:** 90 minuten
**Focus:** Scenario-analyse met DuPont stress testing + Intro Opdracht 3
**Methodologie:** Gebaseerd op [The Strategic Foresight Book](https://solferinoacademy.com/the-strategic-foresight-book/) (Solferino Academy)

---

## 📋 Pre-Sessie Vereisten

### Voor Studenten (VOOR de sessie afronden):

- [ ] **Opdracht 1 afgerond**: DuPont componenten (ROE, Profit Margin, Asset Turnover, Equity Multiplier) berekend
- [ ] **Opdracht 2 afgerond of in afrondingsfase**: Beta en risicoprofiel bekend
- [ ] **Laptop mee**: Excel/Power BI/Python/AI toegang

### Voor Docent:

- [ ] **A3 prints Wind Tunnel Canvas** (1 per team) - zie einde document
- [ ] Beamer voor theorie-intro
- [ ] Timer voor activiteiten
- [ ] Pulse Check link klaar: `https://hanbedrijfskunde.github.io/retrospective/?workshop=ECONAN%20WK6`

---

## 🎯 Learning Objectives Week 6

Na deze sessie kunnen studenten:

1. **LR-DUPONT-3**: De DuPont Identity toepassen om drivers van ROE te ontleden
2. **LR-FORESIGHT-1**: Externe trends (Foresight) vertalen naar financiële impact op Margin/Turnover/Multiplier
3. **LR-SGR-1**: De Sustainable Growth Rate (SGR) berekenen en interpreteren
4. **LR-SCENARIO-1**: Impact van disruptie kwantificeren via stress testing
5. **LR-INTERVENTION-1**: Strategische interventies ontwerpen om waardevernietiging tegen te gaan

---

## ⏱️ Sessie Planning (90 minuten)

| Blok | Tijd | Activiteit | Actieve Tijd Studenten |
|------|------|------------|------------------------|
| **1** | 15 min | Fase 1: De Motor Inspecteren (Nulmeting) | 80% |
| **2** | 25 min | Fase 2: De Storm (DuPont Stress Test) | 90% |
| **3** | 20 min | Fase 3: De Toekomst Radar (SGR & WACC) | 85% |
| **4** | 20 min | Fase 4: De Redding (CFO Interventie) | 90% |
| **5** | 10 min | Wrap-up & Link naar Opdracht 3 | 50% |
| **Totaal** | **90 min** | | **~80%** |

---

## 📖 Blok 1: Fase 1 - De Motor Inspecteren (15 min)

### Doel

De nulmeting bepalen: waar staat jullie bedrijf nu? (Base Case)

### Timing

- **0:00-0:05** (5 min): Opening + metafoor
- **0:05-0:15** (10 min): Teams vullen Deel 1 Canvas in

### Docentinstructie

**Opening met metafoor:**

> "Welkom bij Week 6! Vandaag gaan we jullie bedrijf in een **windtunnel** zetten.
>
> De metafoor: jullie bedrijf is een auto. In Opdracht 1 hebben jullie de motor geanalyseerd - hoe efficiënt is hij? Hoeveel pk levert hij? In Opdracht 2 hebben jullie gekeken naar het risico - hoe stabiel is de auto op de weg?
>
> Vandaag zetten we de auto in een windtunnel en **zetten de storm aan**. Hoe goed houdt jullie bedrijfsmodel stand onder druk?"

**DuPont Identity opfrisser (op bord):**

$$ROE = \text{Profit Margin} \times \text{Asset Turnover} \times \text{Equity Multiplier}$$

> "Dit zijn de drie knoppen waar je als CFO aan kunt draaien:
>
> 1. **Profit Margin** = Hoeveel winst per euro omzet? (Winstgevendheid)
> 2. **Asset Turnover** = Hoeveel omzet per euro activa? (Efficiëntie)
> 3. **Equity Multiplier** = Hoeveel activa per euro eigen vermogen? (Hefboom)
>
> Als één van deze knoppen draait door een externe trend, verandert je hele ROE."

**Activiteit:**

> "Pak het **Wind Tunnel Canvas** erbij. Vul nu Deel 1 in met de huidige waarden van jullie bedrijf uit Opdracht 1. Dit is jullie **Base Case** - de nulmeting."

*(Teams werken 10 minuten aan Deel 1)*

---

## 🌪️ Blok 2: Fase 2 - De Storm (25 min)

### Doel

De impact van een externe trend op de korte termijn (ROE) bepalen via stress testing.

### Timing

- **0:15-0:20** (5 min): Introductie Trend Cards
- **0:20-0:40** (20 min): Teams analyseren impact + berekenen nieuwe ROE

### Docentinstructie

**Introductie Trend Cards:**

> "Nu komt de storm. Kies één van deze trends die jullie bedrijf het hardst zou raken:"

**🎯 Trend Cards Tool:**
> **Ga naar:** [oefeningen/trend-cards.html](../oefeningen/trend-cards.html)
>
> *(URL op bord schrijven: `https://hanbedrijfskunde.github.io/econan/oefeningen/trend-cards.html`)*

Of gebruik de onderstaande lijst als fallback:

**Trend Cards (op bord of slides):**

| # | Trend | Typische Impact |
|---|-------|-----------------|
| 1 | **Stijgende energieprijzen** | COGS stijgt → Margin daalt |
| 2 | **Supply Chain disruptie** | Voorraden stijgen → Turnover daalt |
| 3 | **Recessie / Vraaguitval** | Activa renderen niet → Turnover daalt |
| 4 | **Credit Crunch** | Banken lenen niet → Multiplier moet omlaag |
| 5 | **AI-disruptie** | Marges onder druk OF efficiency-gains |
| 6 | **Klimaatregulering** | Compliance-kosten → Margin daalt |
| 7 | **[Eigen trend]** | Teams mogen ook eigen trend kiezen |

> "Kies één trend die jullie businessmodel **fundamenteel** bedreigt. Niet een klein ongemak, maar iets dat de kern raakt."

**Activiteit (Deel 2 Canvas):**

> "Vul nu Deel 2 van het Canvas in:
>
> 1. **Welke DuPont-variabele wordt geraakt?** (Margin, Turnover, of Multiplier)
> 2. **Hoe veel verandert die variabele?** Maak een schatting.
> 3. **Bereken de nieuwe ROE.**
>
> **Tips voor het schatten:**
>
> - *AI-optie:* Vraag ChatGPT/Claude: *'What was the impact of the 2008 crash on automotive profit margins?'* of *'How did supply chain disruptions in 2021 affect retail asset turnover?'*
> - *Python-optie:* Draai een Monte Carlo simulatie als je onzekerheid wilt modelleren
> - *Benchmark-optie:* Kijk naar wat concurrenten overkwam in vergelijkbare situaties"

*(Teams werken 20 minuten - docent loopt rond en stelt vragen)*

**Coaching vragen tijdens rondgang:**

- "Waarom denken jullie dat juist *deze* variabele geraakt wordt?"
- "Hoe komen jullie aan die schatting van X%?"
- "Wat als de impact twee keer zo groot is?"

---

## 📡 Blok 3: Fase 3 - De Toekomst Radar (20 min)

### Doel

De lange termijn impact bepalen: kan het bedrijf nog groeien? Wat doet dit met de waarde?

### Timing

- **0:40-0:45** (5 min): SGR uitleg
- **0:45-0:55** (10 min): Teams berekenen SGR + WACC impact
- **0:55-1:00** (5 min): Korte bespreking

### Docentinstructie

**SGR Uitleg:**

> "Een bedrijf kan op korte termijn een klap opvangen - je hebt reserves, je kunt bezuinigen. Maar wat betekent dit voor de **toekomst**?
>
> De **Sustainable Growth Rate (SGR)** vertelt je hoe snel een bedrijf kan groeien *zonder externe financiering*:"

$$SGR = ROE \times (1 - \text{Dividend Payout Ratio})$$

> "**Inzicht:** Als de ROE halveert door de trend, en de Dividend Payout Ratio blijft ongewijzigd, halveert ook het vermogen om autonoom te groeien.
>
> Stel: je oude SGR was 12% en de nieuwe is 4%. Dat betekent dat je niet meer kunt groeien met de markt (die misschien 5-6% groeit). Je bedrijf **krimpt relatief** - en dat is vaak het begin van een neerwaartse spiraal."

**Activiteit (Deel 3 Canvas):**

> "Vul Deel 3 in:
>
> **A. Sustainable Growth Rate:**
> - Bereken oude en nieuwe SGR
> - Gebruik 50% dividend payout ratio als je het niet weet
>
> **B. Risicoprofiel:**
> - Wat doet de trend met jullie Beta? (herinner Opdracht 2)
> - Wat doet dit met de perceptie van banken/investeerders?
> - Verwacht je dat de WACC (cost of capital) stijgt?"

*(Teams werken 10 minuten)*

**Korte bespreking (5 min):**

> "Wie heeft een SGR die onder de 5% uitkomt? Wat betekent dat voor jullie bedrijf?"

*(Laat 2-3 teams kort antwoorden)*

---

## 🛟 Blok 4: Fase 4 - De Redding (20 min)

### Doel

Strategische interventie ontwerpen om waarde te herstellen.

### Timing

- **1:00-1:05** (5 min): CFO Interventie intro
- **1:05-1:20** (15 min): Teams ontwerpen interventie

### Docentinstructie

**CFO Interventie Intro:**

> "CFO's, jullie zijn aan zet. De storm is extern - die kunnen jullie niet veranderen. Maar jullie kunnen wel de **stand van de zeilen** aanpassen.
>
> De kunst is: grijp in op een **andere variabele** dan de trend deed.
>
> Voorbeelden:"

| Als de trend raakt... | Overweeg interventie op... | Voorbeeld |
|-----------------------|---------------------------|-----------|
| **Margin** (kosten stijgen) | **Turnover** (efficiënter) | Voorraad reduceren, sneller factureren |
| **Turnover** (vraag daalt) | **Margin** (waardevoller) | Premium positionering, services toevoegen |
| **Multiplier** (krediet krap) | **Margin** of **Turnover** | Kosten snijden om cash te genereren |

> "Het idee: als je marge daalt door externe factoren, kun je misschien compenseren door efficiënter te worden (hogere turnover). Of andersom."

**Activiteit (Deel 4 Canvas):**

> "Ontwerp jullie **CFO Interventie**:
>
> 1. Kies een interventieniveau (Operationeel / Asset Management / Financieel)
> 2. Beschrijf de concrete maatregel
> 3. Schat het effect op de ROE
>
> **Wees concreet!** Niet 'kosten besparen' maar 'personeelsreductie van 10% in backoffice, bespaart €2M, margin +0.5%'"

*(Teams werken 15 minuten)*

---

## 🏁 Blok 5: Wrap-up & Link naar Opdracht 3 (10 min)

### Doel

Samenvatten, 2 teams laten pitchen, link naar Opdracht 3.

### Timing

- **1:20-1:25** (5 min): War Stories (2 teams pitchen)
- **1:25-1:30** (5 min): Link naar Opdracht 3 + Pulse Check

### War Stories

> "Wie wil kort (2 minuten) jullie scenario pitchen?
>
> Structuur: Welke trend? → Welke impact? → Welke interventie?"

*(Laat 2 teams pitchen)*

### Link naar Opdracht 3

> "Wat jullie vandaag met de hand hebben gedaan, gaan jullie in Opdracht 3 **digitaal en interactief** maken.
>
> **Opdracht 3: Simulatie & Scenario's**
>
> Jullie bouwen een tool waarin stakeholders zelf aan de knoppen kunnen draaien. Toolkeuze is vrij:
>
> - **Power BI:** Gebruik 'What-if parameters'
> - **Excel:** Gebruik Scenario Manager of Data Tables
> - **Python:** Jupyter Notebook met ipywidgets of Streamlit
> - **AI-augmented:** Laat AI helpen bij het bouwen van de simulatie
>
> Het Wind Tunnel Canvas van vandaag is jullie **conceptuele basis** voor Opdracht 3."

### Pulse Check

> "Voordat jullie gaan: vul de **Pulse Check** in (2 minuten). Dit helpt ons de module te verbeteren."

Link: `https://hanbedrijfskunde.github.io/retrospective/?workshop=ECONAN%20WK6`

---

## 🎯 PAM Framework Alignment

### Purpose (Waarom doen we dit?)

**Score: 5/5**

- **Realistische druk**: Bedrijven worden daadwerkelijk geconfronteerd met externe schokken
- **CFO-perspectief**: Studenten ervaren hoe strategische beslissingen onder druk worden genomen
- **Foresight integratie**: Verbinding tussen trends (BEDROM) en financiële impact (ECONAN)
- **Directe toepassing**: Output is input voor Opdracht 3

### Autonomy (Hoeveel controle hebben studenten?)

**Score: 5/5**

- **Eigen trend kiezen**: Teams selecteren de meest relevante bedreiging
- **Tool-vrij**: AI, Python, Excel, of handmatig - allemaal geaccepteerd
- **Interventievrijheid**: Teams ontwerpen eigen strategie
- **Tempo**: Teams bepalen eigen diepgang in elk deel

### Mastery (Ervaar ik groei?)

**Score: 5/5**

- **Integratie**: Combineert Opdracht 1 (ratio's) + Opdracht 2 (risico) + nieuwe concepten (SGR, Foresight)
- **Progressie zichtbaar**: Van passief analyseren → actief scenario's bouwen
- **Concrete output**: Wind Tunnel Canvas als tastbaar resultaat
- **Scaffolding**: Canvas biedt structuur, maar laat ruimte voor eigen invulling

---

## 🛡️ Risk Mitigatie

### Risico 1: Teams hebben Opdracht 1 data niet paraat

**Actie:**
- Laat teams snel opzoeken in hun Opdracht 1 document
- Bied fallback: "Gebruik sector-gemiddelden als noodoplossing"
- Benadruk: dit toont waarom je je eigen werk moet kennen

### Risico 2: Schattingen zijn willekeurig ("we gokken 50%")

**Actie:**
- Vraag naar onderbouwing: "Waar baseer je dat op?"
- Verwijs naar AI: "Vraag ChatGPT naar historische precedenten"
- Accepteer onzekerheid: "Maak dan een range: 30-70%"

### Risico 3: Teams kiezen makkelijke trends

**Actie:**
- Challenge: "Is dit echt de grootste bedreiging voor jullie bedrijf?"
- Bied alternatief: "Wat als ik zeg dat [X] gebeurt?"

### Risico 4: Interventies zijn vaag

**Actie:**
- Vraag om concreetheid: "Hoeveel euro? Hoeveel FTE? Welke afdeling?"
- Voorbeeld geven: "Niet 'kosten besparen' maar '10% personeelsreductie in logistiek'"

---

## 📎 Appendix: Wind Tunnel Canvas (A3 Print)

> **Printinstructie:** Print onderstaand canvas op A3 formaat, 1 per team

---

# FINANCIAL WIND TUNNEL CANVAS

**Team:** _________________________________ **Bedrijf:** _________________________________

---

## DEEL 1: DE NULMETING (Base Case)

*Hoe draait de motor vandaag? (Gebruik cijfers uit Opdracht 1)*

| DuPont Component | Formule | Huidige Waarde |
|------------------|---------|----------------|
| **1. Profit Margin** | Net Income / Sales | __________ % |
| **2. Asset Turnover** | Sales / Total Assets | __________ × |
| **3. Equity Multiplier** | Total Assets / Total Equity | __________ × |
| **= ROE** | 1 × 2 × 3 | __________ % |

---

## DEEL 2: DE STORM (Short Term Stress Test)

**Gekozen Trend:** ________________________________________________________________

### Welke DuPont-variabele wordt geraakt?

☐ **Margin** (kostenstijging, prijsdruk)
☐ **Turnover** (voorraadophoping, vraaguitval)
☐ **Multiplier** (kredietstop, herfinanciering)

### Impact Schatting

De variabele verandert van ________ naar ________.

**Bron/Onderbouwing:** _____________________________________________________________

**NIEUWE ROE:** ________ %

---

## DEEL 3: DE TOEKOMST RADAR (Long Term Impact)

### A. Groeicapaciteit (SGR)

**Formule:** SGR = ROE × (1 - Dividend Payout Ratio)

*Gebruik 50% dividend payout als onbekend*

| | Oud | Nieuw |
|---|-----|-------|
| **SGR** | ________ % | ________ % |

**Conclusie:** Kunnen we nog groeien met de markt? ☐ JA / ☐ NEE

### B. Risicoprofiel

Verwachte impact op WACC: ☐ Gelijk / ☐ Stijgt licht / ☐ Stijgt sterk

**Conclusie bedrijfswaarde:** _______________________________________________________

---

## DEEL 4: DE REDDING (CFO Interventie)

### Interventieniveau

☐ **Operationeel** (Margin: kosten snijden, prijzen verhogen)
☐ **Asset Management** (Turnover: activa afstoten, voorraad reduceren)
☐ **Financieel** (Multiplier: herfinancieren, equity ophalen)

### Concrete Maatregel

_________________________________________________________________________________

_________________________________________________________________________________

### Verwacht Effect

ROE herstelt naar: ________ %

---

**Versie:** 1.0 (DRAFT)
**Laatste update:** 2025-12-02
**Auteur:** ECONAN Teaching Team
**Methodologie:** [The Strategic Foresight Book](https://solferinoacademy.com/the-strategic-foresight-book/) (Solferino Academy)
