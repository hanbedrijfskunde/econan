# INSTRUCTIE: RISICO & RENDEMENT ANALYSE
## Van Koersdata naar Beta, Alpha en R²

**Module:** ECONAN - Economic Analysis
**Doelgroep:** Business Analisten (Week 4-5)
**Werkwijze:** AI-Augmented Path
**Tijdsinvestering:** 2-3 uur voor eerste analyse
**Tools:** ChatGPT, Claude, Gemini, of Mistral AI

---

## Voorbereiding

Deze instructie begeleidt je door een complete risico-rendement analyse met AI, inclusief regressie en evaluatieopdrachten.

**Bestudeer vooraf:**
- **Hillier H11**: Lessons from Recent Capital Market History
- **Hillier H12**: Return, Risk and the Security Market Line
- **Brightspace**: [Week 4 Tutorial](https://leren.han.nl/d2l/le/lessons/85530/topics/528571)

---

## Wat ga je leren?

Na deze instructie kun je:

- **Koersdata verzamelen** van je bedrijf en benchmark index
- **Wekelijkse rendementen berekenen** uit slotkoersen
- **Regressie uitvoeren** om Beta, Alpha en R² te berekenen
- **Resultaten interpreteren** in business context
- **AI-output valideren** door triangulatie met externe bronnen

---

## Van Opdracht 1 naar Opdracht 2

### Wat je in Opdracht 1 hebt gedaan

In Opdracht 1 heb je gekeken naar **hoe presteert dit bedrijf?**:
- ROE, ROA, marges
- Debt-to-Equity ratio's
- Benchmark vergelijking met concurrenten
- IST-situatie analyse

**Voorbeeld uit Opdracht 1 (Rheinmetall):**
> "ROE = 18.1%, boven sector gemiddelde 12%. DuPont analyse toont hoge leverage (Equity Multiplier 3.21)."

### Wat je in Opdracht 2 gaat doen

In Opdracht 2 voeg je **risico** toe aan je analyse:
- Hoeveel risico loop je voor dat rendement?
- Hoe beweegt het aandeel ten opzichte van de markt?
- Welk deel van het risico kun je wegdiversifiëren?

**Voorbeeld uit Opdracht 2 (Rheinmetall):**
> "Beta = 1.35 ten opzichte van S&P 500, R² = 0.42. Dit betekent dat 42% van het risico systematisch is (marktrisico). De overige 58% is idiosyncratisch risico dat je kunt wegdiversifiëren."

**De brug:** Van "dit bedrijf presteert goed" → "dit is het risico dat je loopt voor die prestatie"

---

## De 6 CRISP-DM Stappen

```
1. DATA INLEZEN EN VALIDEREN    →  Koersdata ophalen en checken
         ↓
2. RETURNS BEREKENEN            →  Wekelijkse rendementen uit slotkoersen
         ↓
3. TIJDREEKS VISUALISATIE       →  Returns plotten om volatiliteit te begrijpen
         ↓
4. REGRESSIE SCATTER PLOTS      →  Bedrijf vs. index visualiseren
         ↓
5. REGRESSIE PARAMETERS         →  Beta, Alpha en R² berekenen
         ↓
6. TRIANGULATIE EN VALIDATIE    →  Vergelijken met externe bronnen
```

---

## Stap 1: Data Verzamelen

### Wat je nodig hebt

**1. Koersdata van je bedrijf**

Bronnen voor koersdata:
- [Yahoo Finance UK](https://uk.finance.yahoo.com/) - CSV download beschikbaar
- [Google Finance](https://www.google.com/finance/?hl=en) - Overzichtelijk, geen CSV
- [Reuters Markets](https://www.reuters.com/markets/stocks/) - Professionele data
- [Euronext](https://live.euronext.com) - Europese beurzen

Vereisten:
- Periode: minimaal 52 weken (1 jaar), bij voorkeur 2-3 jaar
- Frequentie: wekelijkse slotkoersen (adjusted close)

**2. Koersdata van benchmark index**
- Voor Europese bedrijven: DAX, STOXX Europe 600, of sector-specifieke index
- Voor vergelijking met US: S&P 500
- Dezelfde periode als je bedrijf!

**3. Voorbeeld: Rheinmetall**
```
Bedrijf: Rheinmetall AG (RHM.DE)
Benchmark 1: S&P 500 (^GSPC)
Benchmark 2: DAX (^GDAXI)
Periode: December 2020 - December 2024
Frequentie: Wekelijks (52 × 4 = 208 datapunten)
```

### Praktische Tips

**Yahoo Finance download:**
1. Ga naar finance.yahoo.com
2. Zoek je ticker (bijv. "RHM.DE")
3. Klik op "Historical Data"
4. Selecteer: Time Period = 3 Year, Frequency = Weekly
5. Download CSV

**Let op:** Zorg dat bedrijf en index **dezelfde weken** hebben!

---

## Stap 2: AI Prompt - Complete Analyse

### De Anatomie van een Goede Prompt

Een effectieve prompt voor risico-analyse heeft **4 componenten**:

```
1. CONTEXT     → Wie ben je? Wat is het doel?
2. DATA        → Welke koersdata heb je?
3. OPDRACHT    → Welke berekeningen wil je?
4. FORMAT      → Hoe wil je het resultaat zien?
```

### Template C: Risico & Rendement Analyse

```
[CONTEXT]
Ik ben Business Analist voor ECONAN (HBO Bedrijfskunde).
Ik analyseer [BEDRIJF] in de [SECTOR] sector.
Ik wil de risico-rendement karakteristieken bepalen.

[DATA]
Ik heb wekelijkse koersdata voor:
- [BEDRIJF] ticker: [TICKER]
- Benchmark: [INDEX] ticker: [TICKER]
- Periode: [START DATUM] tot [EIND DATUM]

[OPDRACHT - 6 CRISP-DM STAPPEN]

**Stap 1: Data Inlezen en Valideren**
- Lees de bijgevoegde CSV bestanden in
- Check op missende waardes en outliers
- Rapporteer: aantal datapunten, periode, eventuele gaps

**Stap 2: Returns Berekenen**
- Bereken wekelijkse returns: R_t = (P_t - P_{t-1}) / P_{t-1} × 100%
- Toon de eerste 5 en laatste 5 datapunten als verificatie

**Stap 3: Tijdreeks Visualisatie**
- Maak een lijnplot van beide return-reeksen over tijd
- Bereken en toon: gemiddeld rendement, standaarddeviatie, min/max

**Stap 4: Regressie Scatter Plots**
- Maak een scatter plot: X-as = index returns, Y-as = bedrijf returns
- Voeg regressielijn toe
- Label assen en voeg titel toe

**Stap 5: Regressie Parameters**
- Voer lineaire regressie uit: R_bedrijf = α + β × R_index + ε
- Rapporteer:
  - Beta (β): met interpretatie
  - Alpha (α): met interpretatie (geannualiseerd indien nodig)
  - R² (R-squared): met interpretatie
  - Standaardfout van Beta

**Stap 6: Triangulatie en Validatie**
- Vergelijk je berekende Beta met gepubliceerde Beta's van:
  - Yahoo Finance
  - Reuters/Refinitiv
  - Bloomberg (indien beschikbaar)
- Verklaar eventuele verschillen (periode, index, frequentie)

[FORMAT]
Voor elke stap wil ik zien:
- Wat je gedaan hebt (methode)
- De resultaten (cijfers, grafieken)
- Interpretatie in business context

[ATTACHMENTS]
- [bedrijfsnaam]-weekly-prices.csv
- [indexnaam]-weekly-prices.csv
```

---

## Stap 3: Begrip - Wat betekenen de resultaten?

### Beta (β) Interpretatie

| Beta waarde | Betekenis | Voorbeeld |
|-------------|-----------|-----------|
| β = 1.0 | Beweegt precies mee met de markt | Index tracker ETF |
| β > 1.0 | **Agressief** - sterker dan markt | Tech startups, growth stocks |
| β < 1.0 | **Defensief** - zwakker dan markt | Utilities, consumer staples |
| β < 0 | **Inverse** - tegengesteld aan markt | Goud, sommige hedgefunds |

**Voorbeeld:**
> Beta = 1.35 betekent: als de markt met 10% stijgt, verwacht je dat dit aandeel met ~13.5% stijgt. Maar ook: als de markt 10% daalt, daalt dit aandeel ~13.5%.

### Alpha (α) Interpretatie

Alpha meet het **extra rendement** boven wat je zou verwachten gegeven het risico (beta).

| Alpha waarde | Betekenis |
|--------------|-----------|
| α > 0 | Outperformance: beter dan verwacht |
| α = 0 | Precies zoals verwacht |
| α < 0 | Underperformance: slechter dan verwacht |

**Let op:** Alpha is vaak **niet statistisch significant** bij korte periodes!

### R² Interpretatie

R² vertelt welk deel van de beweging **verklaard** wordt door de markt.

| R² waarde | Betekenis |
|-----------|-----------|
| R² = 1.0 | 100% verklaard door markt (alleen systematisch risico) |
| R² = 0.5 | 50% markt, 50% bedrijfsspecifiek |
| R² = 0.0 | Geen relatie met markt (alleen idiosyncratisch risico) |

**Voorbeeld:**
> R² = 0.42 betekent: 42% van het risico is systematisch (marktrisico). De overige 58% is idiosyncratisch risico dat je kunt wegdiversifiëren door meer aandelen te kopen.

---

## Stap 4: Verificatie - Altijd Controleren!

### Verificatie Checklist

Voor elke regressie die AI uitvoert:

#### 1. Data Verificatie
```
[ ] Zijn er evenveel datapunten voor bedrijf en index?
[ ] Is de periode correct (start en einddatum)?
[ ] Zijn er geen missende weken (feestdagen, trading halts)?
[ ] Klopt de return berekening? (check 2-3 handmatig)
```

**Handmatige check voorbeeld:**
```
Rheinmetall 7 dec 2020: €78.64
Rheinmetall 14 dec 2020: €79.86
Return = (79.86 - 78.64) / 78.64 × 100% = 1.55%

→ Vergelijk dit met wat AI rapporteert!
```

#### 2. Regressie Verificatie
```
[ ] Is beta realistisch voor deze sector?
[ ] Ligt R² tussen 0 en 1?
[ ] Is alpha in dezelfde eenheid als de returns (% per week)?
```

**Sanity checks:**
- Tech bedrijf met beta < 0.5? → Waarschijnlijk fout
- R² > 0.9 voor individueel aandeel? → Check of je niet per ongeluk de index op zichzelf regresseert

#### 3. Triangulatie
```
[ ] Vergelijk met Yahoo Finance Beta
[ ] Vergelijk met Reuters/Bloomberg
[ ] Verschil > 0.3? → Onderzoek oorzaak (periode, index, frequentie)
```

**Voorbeeld triangulatie:**
```
Jouw berekende Beta: 1.35 (vs S&P 500, 3 jaar wekelijks)
Yahoo Finance Beta: 1.42 (vs S&P 500, 5 jaar maandelijks)
Reuters Beta: 1.28 (vs DAX, 2 jaar dagelijks)

Conclusie: Alle drie wijzen op beta > 1.0 (agressief).
Verschillen verklaard door andere periodes en frequenties.
```

---

## Stap 5: Evaluatie - Zelf Uitwerken

### Vraag 1: Beta Interpretatie

1. Zoek de gepubliceerde beta van je bedrijf op (Yahoo Finance, Reuters)
2. Vergelijk met je zelf berekende beta
3. Verklaar het verschil

**Reflectievraag:**
> Welke periode en frequentie gebruikt Yahoo Finance? Hoe beïnvloedt dit de beta?

**Jouw antwoord:**
_________________________________________________
_________________________________________________
_________________________________________________

### Vraag 2: R² en Diversificatie

1. Haal de R² uit je regressie
2. Bereken: Idiosyncratisch risico = 1 - R²
3. Wat betekent dit voor een belegger die alleen dit aandeel bezit?

**Reflectievraag:**
> Als je R² = 0.40, hoeveel procent van het risico kun je wegdiversifiëren door meer aandelen te kopen?

**Jouw antwoord:**
_________________________________________________
_________________________________________________
_________________________________________________

### Vraag 3: Alpha Significantie

1. Bekijk de alpha uit je regressie
2. Bereken de t-statistiek: t = alpha / standaardfout(alpha)
3. Is alpha statistisch significant? (|t| > 2 voor 95% zekerheid)

**Reflectievraag:**
> Waarom is alpha vaak niet significant bij korte periodes? Wat zegt dit over "stock picking"?

**Jouw antwoord:**
_________________________________________________
_________________________________________________
_________________________________________________

### Vraag 4: CAPM en Hurdle Rate

De CAPM formule is: E(R) = Rf + β × (Rm - Rf)

Gegeven:
- Risk-free rate (Rf) = 3% (10-jaar staatsobligatie)
- Market risk premium (Rm - Rf) = 6% (historisch gemiddelde)
- Jouw berekende beta = [vul in]

1. Bereken de expected return volgens CAPM
2. Vergelijk met de actual return van je bedrijf over dezelfde periode
3. Wat betekent dit voor de investment decision?

**Reflectievraag:**
> Als je bedrijf een actual return heeft die hoger is dan de CAPM expected return, wat zegt dit dan?

**Jouw antwoord:**
_________________________________________________
_________________________________________________
_________________________________________________

---

## Veelgemaakte Fouten

### Fout #1: Verkeerde Return Berekening

❌ **Slecht:** Return = P_t - P_{t-1} (absolute change)
✅ **Goed:** Return = (P_t - P_{t-1}) / P_{t-1} × 100% (percentage change)

### Fout #2: Niet-overeenkomende Periodes

❌ **Slecht:** Bedrijf 2020-2024, Index 2019-2024
✅ **Goed:** Beide exact dezelfde weken

### Fout #3: Adjusted vs. Non-Adjusted Prices

❌ **Slecht:** Gewone slotkoersen (niet gecorrigeerd voor splits/dividends)
✅ **Goed:** Adjusted Close (gecorrigeerd voor corporate actions)

### Fout #4: Verkeerde Index Keuze

❌ **Slecht:** Europees bedrijf vergelijken met Nikkei (Japan)
✅ **Goed:** Europees bedrijf met DAX of STOXX Europe 600

### Fout #5: Te Korte Periode

❌ **Slecht:** 10 weken data → te weinig datapunten
✅ **Goed:** Minimaal 52 weken, bij voorkeur 2-3 jaar

### Fout #6: Resultaten Niet Trianguleren

❌ **Slecht:** "De AI zegt beta = 2.5, dus dat klopt"
✅ **Goed:** Vergelijk met Yahoo Finance, Reuters, Bloomberg

---

## Voorbeeld: Rheinmetall Regressie

Bekijk de [interactieve Rheinmetall Weekly Returns Analyse](../examples/weekly-returns-tabs.html) voor een compleet werkvoorbeeld:

**Tab "Rheinmetall"**: Wekelijkse koersen en returns
**Tab "Rendementen"**: Vergelijking met S&P 500 en DAX
**Tab "Regressie"**: Scatter plots met Beta, Alpha, R²

**Key resultaten:**
```
Rheinmetall vs S&P 500 (Dec 2020 - Dec 2024):
- Beta: 1.35
- Alpha: 0.12% per week (6.2% geannualiseerd)
- R²: 0.42

Interpretatie:
- Rheinmetall is 35% volatieler dan de markt (beta > 1)
- 42% van het risico is systematisch, 58% idiosyncratisch
- Positieve alpha suggereert outperformance, maar check significantie!
```

---

## Next Steps

### Je bent nu klaar om:

- **Opdracht 2 te starten** - data verzamelen voor je eigen bedrijf
- **Regressie uit te voeren** - met AI of conventionele tools
- **Beta te interpreteren** - in context van investment decision
- **Resultaten te trianguleren** - met externe bronnen

### Inleveren Opdracht 2

- Complete regressie analyse (markdown of PDF)
- Grafieken: scatter plot met regressielijn
- Interpretatie: Beta, Alpha, R² in business context
- Triangulatie: vergelijking met gepubliceerde waarden
- AI prompts gedocumenteerd (voor transparantie)

---

## Referenties

**ECONAN Materiaal:**
- [Template C: Risico & Rendement Analyse](../materiaal/index.html#ai-risico-rendement)
- [Weekly Returns Analyse (interactief)](../examples/weekly-returns-tabs.html)
- [Corporate Finance Decisions schema](../background-docs/subjects/corporate-finance-decisions.html)

**Externe Bronnen:**
- [Yahoo Finance](https://finance.yahoo.com) - koersdata en gepubliceerde beta's
- [Investopedia: Beta](https://www.investopedia.com/terms/b/beta.asp)
- [Investopedia: CAPM](https://www.investopedia.com/terms/c/capm.asp)

**Literatuur:**
- Hillier H11: Lessons from Recent Capital Market History
- Hillier H12: Return, Risk and the Security Market Line

---

*Laatste update: December 2025*
*ECONAN Module - HBO Bedrijfskunde - AI-Augmented Path*
