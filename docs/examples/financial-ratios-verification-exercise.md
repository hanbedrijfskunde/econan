# VERIFICATIE OEFENING: Spotting Financial Ratio Errors
## Voor ECONAN Week 2-3 - AI-Augmented & Conventional Paths

**Doelgroep:** Business Analisten (alle paths)
**Tijdsinvestering:** 30-45 minuten
**Leerdoel:** Leren kritisch kijken naar financiële data en wiskundige consistentie verifiëren

---

## 🎯 Leerdoelen

Na deze oefening kun je:

✅ **Financiële ratio identiteiten herkennen** (DuPont, Earnings Yield, P/B relaties)
✅ **Inconsistenties in datasets spotten** door wiskundige verificatie
✅ **Bepalen welke waarden correct zijn** en welke aangepast moeten worden
✅ **Systematisch verifiëren** - een essentiële skill voor data-analyse
✅ **AI-output controleren** - nooit blind vertrouwen!

---

## 📋 De Situatie

Je collega Business Analist heeft een benchmark analyse gemaakt van de Retail sector (Sustainable Fashion segment). Hij heeft de data uit verschillende bronnen verzameld en in een tabel gezet.

**Jouw opdracht:** Verifieer of alle cijfers kloppen. Als er fouten zitten, bepaal dan:
1. **Welke cijfers zijn fout?**
2. **Welke cijfers zijn correct?**
3. **Wat moeten de correcte waarden zijn?**

---

## 📊 De Dataset (BEVAT FOUTEN!)

### Retail Sector - Sustainable Fashion Benchmark (Financial Focus)

| Kental / Ratio | Bedrijf A | Bedrijf B | Bedrijf C | Sector Avg |
|----------------|-----------|-----------|-----------|------------|
| **💧 Liquiditeit** | | | | |
| Current Ratio | 1.8 | 2.1 | 1.4 | 1.8 |
| Quick Ratio | 0.9 | 1.2 | 0.7 | 0.9 |
| **⚖️ Financial Leverage** | | | | |
| Debt-Equity Ratio | 0.6 | 0.8 | 1.2 | 0.9 |
| Equity Multiplier | 1.6 | 1.8 | 2.2 | 1.9 |
| **🔄 Turnover (Efficiëntie)** | | | | |
| Asset Turnover | 1.8 | 1.5 | 2.2 | 1.8 |
| Inventory Turnover | 6.5 | 5.8 | 8.2 | 6.8 |
| **💰 Rendement** | | | | |
| ROE (%) | **14.2** | **16.8** | **12.1** | **14.4** |
| Profit Margin (%) | 7.3 | 8.9 | 5.2 | 7.1 |
| **📈 Markt** | | | | |
| P/E Ratio | 18.5 | 22.3 | 14.7 | 18.5 |
| Market-to-Book | **2.6** | **3.7** | **1.8** | **2.7** |

---

## 🔍 OPDRACHT 1: Herken de Fouten (10 minuten)

### Stap 1: Welke Wiskundige Relaties Bestaan?

Denk na over de fundamentele identiteiten:

1. **DuPont Identity**
   ```
   ROE = Net Profit Margin × Asset Turnover × Equity Multiplier
   ```

2. **Earnings Yield**
   ```
   Earnings Yield = 1 / P/E Ratio × 100%
   ```

3. **Valuation Bridge**
   ```
   Earnings Yield = ROE / Market-to-Book (P/B)
   ```

### Stap 2: Bereken en Verifieer

**Voor elk bedrijf:**

1. Bereken ROE via DuPont formule
2. Bereken Earnings Yield via P/E
3. Verifieer: Earnings Yield = ROE / P/B

**Noteer waar het NIET klopt!**

---

## 🧮 OPDRACHT 2: Bereken de Correcte Waarden (15 minuten)

### Bedrijf A

**Gegeven data:**
- Net Profit Margin: 7.3%
- Asset Turnover: 1.8
- Equity Multiplier: 1.6
- P/E Ratio: 18.5
- ROE (gerapporteerd): 14.2%
- P/B (gerapporteerd): 2.6

**Jouw berekeningen:**

1. **DuPont ROE:**
   ```
   ROE = ___% × ___ × ___
   ROE = ___%
   ```

2. **Earnings Yield:**
   ```
   Earnings Yield = 1 / ___ × 100%
   Earnings Yield = ___%
   ```

3. **Correcte P/B via Valuation Bridge:**
   ```
   P/B = ROE / Earnings Yield
   P/B = ___% / ___%
   P/B = ___
   ```

**Conclusie voor Bedrijf A:**
- [ ] ROE klopt (14.2%)
- [ ] ROE moet zijn: ____%
- [ ] P/B klopt (2.6)
- [ ] P/B moet zijn: ____

---

### Bedrijf B

**Gegeven data:**
- Net Profit Margin: 8.9%
- Asset Turnover: 1.5
- Equity Multiplier: 1.8
- P/E Ratio: 22.3
- ROE (gerapporteerd): 16.8%
- P/B (gerapporteerd): 3.7

**Jouw berekeningen:**

1. **DuPont ROE:**
   ```
   ROE = ___% × ___ × ___
   ROE = ___%
   ```

2. **Earnings Yield:**
   ```
   Earnings Yield = 1 / ___ × 100%
   Earnings Yield = ___%
   ```

3. **Correcte P/B:**
   ```
   P/B = ROE / Earnings Yield
   P/B = ___
   ```

**Conclusie voor Bedrijf B:**
- [ ] ROE klopt (16.8%)
- [ ] ROE moet zijn: ____%
- [ ] P/B klopt (3.7)
- [ ] P/B moet zijn: ____

---

### Bedrijf C

**Gegeven data:**
- Net Profit Margin: 5.2%
- Asset Turnover: 2.2
- Equity Multiplier: 2.2
- P/E Ratio: 14.7
- ROE (gerapporteerd): 12.1%
- P/B (gerapporteerd): 1.8

**Jouw berekeningen:**

1. **DuPont ROE:**
   ```
   ROE = ___% × ___ × ___
   ROE = ___%
   ```

2. **Earnings Yield:**
   ```
   Earnings Yield = 1 / ___ × 100%
   Earnings Yield = ___%
   ```

3. **Correcte P/B:**
   ```
   P/B = ROE / Earnings Yield
   P/B = ___
   ```

**Conclusie voor Bedrijf C:**
- [ ] ROE klopt (12.1%)
- [ ] ROE moet zijn: ____%
- [ ] P/B klopt (1.8)
- [ ] P/B moet zijn: ____

---

## 📝 OPDRACHT 3: Reflectie (10 minuten)

### Vragen voor Discussie

1. **Welke parameter was leidend?**
   - Waarom kun je de Equity Multiplier, Asset Turnover en Profit Margin NIET aanpassen?
   - Waarom moet ROE aangepast worden (en niet de DuPont componenten)?

2. **Hoe kon je de fout ontdekken?**
   - Welke verificatie stappen heb je gebruikt?
   - In welke volgorde heb je gecontroleerd?

3. **Wat leer je hiervan voor je eigen analyses?**
   - Hoe voorkom je dit bij AI-gegenereerde output?
   - Welke checks bouw je in bij je eigen werk?

4. **Sector Gemiddelde:**
   - Bereken de correcte Sector Avg ROE en P/B
   - Klopt deze met het gemiddelde van de drie bedrijven?

---

## ✅ ANTWOORDENBLAD

<details>
<summary>🔓 Klik hier om antwoorden te zien (doe eerst zelf de oefening!)</summary>

### Bedrijf A - Correcties

**DuPont ROE:**
```
ROE = 7.3% × 1.8 × 1.6
ROE = 21.0% ✅ (was fout: 14.2%)
```

**Earnings Yield:**
```
Earnings Yield = 1 / 18.5 × 100%
Earnings Yield = 5.41%
```

**Correcte P/B:**
```
P/B = ROE / Earnings Yield
P/B = 21.0% / 5.41%
P/B = 3.88 ✅ (was fout: 2.6)
```

**Conclusie:**
- ❌ ROE was fout (14.2%) → moet zijn **21.0%**
- ❌ P/B was fout (2.6) → moet zijn **3.88**

---

### Bedrijf B - Correcties

**DuPont ROE:**
```
ROE = 8.9% × 1.5 × 1.8
ROE = 24.0% ✅ (was fout: 16.8%)
```

**Earnings Yield:**
```
Earnings Yield = 1 / 22.3 × 100%
Earnings Yield = 4.48%
```

**Correcte P/B:**
```
P/B = ROE / Earnings Yield
P/B = 24.0% / 4.48%
P/B = 5.36 ✅ (was fout: 3.7)
```

**Conclusie:**
- ❌ ROE was fout (16.8%) → moet zijn **24.0%**
- ❌ P/B was fout (3.7) → moet zijn **5.36**

---

### Bedrijf C - Correcties

**DuPont ROE:**
```
ROE = 5.2% × 2.2 × 2.2
ROE = 25.2% ✅ (was fout: 12.1%)
```

**Earnings Yield:**
```
Earnings Yield = 1 / 14.7 × 100%
Earnings Yield = 6.80%
```

**Correcte P/B:**
```
P/B = ROE / Earnings Yield
P/B = 25.2% / 6.80%
P/B = 3.71 ✅ (was fout: 1.8)
```

**Conclusie:**
- ❌ ROE was fout (12.1%) → moet zijn **25.2%**
- ❌ P/B was fout (1.8) → moet zijn **3.71**

---

### Sector Average - Correcties

**DuPont ROE:**
```
ROE = 7.1% × 1.8 × 1.9
ROE = 24.3% ✅ (was fout: 14.4%)
```

**Earnings Yield:**
```
Earnings Yield = 1 / 18.5 × 100%
Earnings Yield = 5.41%
```

**Correcte P/B:**
```
P/B = ROE / Earnings Yield
P/B = 24.3% / 5.41%
P/B = 4.49 ✅ (was fout: 2.7)
```

**Verificatie met gemiddelden:**
```
Gemiddelde ROE = (21.0 + 24.0 + 25.2) / 3 = 23.4% (≈ 24.3% ✓)
Gemiddelde P/B = (3.88 + 5.36 + 3.71) / 3 = 4.32 (≈ 4.49 ✓)
```

---

### Gecorrigeerde Tabel

| Kental / Ratio | Bedrijf A | Bedrijf B | Bedrijf C | Sector Avg |
|----------------|-----------|-----------|-----------|------------|
| ROE (%) | **21.0** ✅ | **24.0** ✅ | **25.2** ✅ | **24.3** ✅ |
| Profit Margin (%) | 7.3 | 8.9 | 5.2 | 7.1 |
| Asset Turnover | 1.8 | 1.5 | 2.2 | 1.8 |
| Equity Multiplier | 1.6 | 1.8 | 2.2 | 1.9 |
| P/E Ratio | 18.5 | 22.3 | 14.7 | 18.5 |
| Market-to-Book | **3.88** ✅ | **5.36** ✅ | **3.71** ✅ | **4.49** ✅ |

---

### Reflectie Antwoorden

**1. Welke parameter was leidend?**

De **Profit Margin, Asset Turnover en Equity Multiplier** zijn leidend omdat deze direct gemeten worden uit de financials:
- Profit Margin = Net Income / Sales (uit Income Statement)
- Asset Turnover = Sales / Total Assets (uit Income Statement + Balance Sheet)
- Equity Multiplier = Total Assets / Equity (uit Balance Sheet)

ROE kan op twee manieren berekend worden:
- **Direct:** Net Income / Equity
- **Via DuPont:** Margin × Turnover × Multiplier

Als er een inconsistentie is, moet ROE aangepast worden aan de DuPont componenten (want die zijn direct gemeten).

**2. Hoe kon je de fout ontdekken?**

**Verificatie stappenplan:**
```
Stap 1: DuPont check → ROE = Margin × Turnover × Multiplier
        → Ontdekking: ROE klopt niet!

Stap 2: Earnings Yield berekenen → 1 / P/E
        → Baseline voor P/B berekening

Stap 3: Valuation Bridge check → Earnings Yield = ROE / P/B
        → Met correcte ROE: P/B moet ook aangepast

Stap 4: Verificatie → Check alle drie identiteiten
        ✓ DuPont klopt
        ✓ Earnings Yield klopt
        ✓ Valuation Bridge klopt
```

**3. Wat leer je hiervan voor je eigen analyses?**

**Voor AI-augmented analisten:**
- ✅ Vertrouw AI NIET blind - altijd verifiëren!
- ✅ Bouw systematische checks in (DuPont, Earnings Yield, P/B relatie)
- ✅ Als één cijfer niet klopt, check gerelateerde ratio's ook
- ✅ Gebruik wiskundige identiteiten als verificatie-tool

**Voor Conventional analisten:**
- ✅ Excel formules kunnen copy-paste fouten bevatten
- ✅ Data uit verschillende bronnen kan inconsistent zijn
- ✅ Altijd cross-check tussen gerelateerde metrics
- ✅ Bouw formule-verificatie in je spreadsheet

**Algemeen:**
- ✅ Maak een verificatie checklist voor elke analyse
- ✅ Document welke identiteiten je hebt gecontroleerd
- ✅ Bij twijfel: herbereken vanaf gronddata
- ✅ Peer review: laat collega je werk controleren

**4. Sector Gemiddelde:**

**Correcte berekening:**
```
Sector Avg ROE = 7.1% × 1.8 × 1.9 = 24.3%
Sector Avg P/B = 24.3% / 5.41% = 4.49

Alternatief (gemiddelde van bedrijven):
Gemiddelde ROE = (21.0 + 24.0 + 25.2) / 3 = 23.4%
Gemiddelde P/B = (3.88 + 5.36 + 3.71) / 3 = 4.32
```

**Observatie:** Kleine verschillen tussen "berekend gemiddelde" en "gemiddelde van bedrijven" zijn normaal door afrondingen en verschillende wegingen.

</details>

---

## 🎓 Didactische Lessen

### Les 1: Financial Ratios zijn een Ecosysteem

**Niet geïsoleerde cijfers, maar een netwerk:**
- ROE hangt samen met Profit Margin, Asset Turnover en Equity Multiplier
- P/B hangt samen met ROE en P/E (via Earnings Yield)
- Eén fout verspreidt zich door het hele systeem

**Visualisatie:**
```
        Net Profit Margin
              ×
        Asset Turnover
              ×                    ROE
        Equity Multiplier    =     ↓
                              Earnings Yield = ROE / P/B
                                     ↑
                              1 / P/E Ratio
```

### Les 2: Verificatie is een Vaardigheid

**Systematische verificatie voorkomt fouten:**

1. **Interne consistentie:** DuPont identity moet kloppen
2. **Cross-ratio verificatie:** Earnings Yield via twee wegen
3. **Valuation logic:** P/B moet passen bij ROE en P/E
4. **Sector sense-check:** Zijn de cijfers realistisch?

### Les 3: AI en Excel zijn Tools, Geen Waarheid

**Beide kunnen fouten maken:**
- AI kan formules verkeerd toepassen of data verkeerd interpreteren
- Excel kan copy-paste fouten bevatten of verkeerde celreferenties
- **Jouw taak:** Kritisch verifiëren, niet blind vertrouwen

**Good practice:**
```
✅ Schrijf je eigen verificatie formules
✅ Gebruik meerdere methoden om hetzelfde te berekenen
✅ Cross-check met benchmarks en sector data
✅ Documenteer je verificatie stappen
```

### Les 4: Fouten Zijn Leerkansen

**Deze oefening komt uit echte situatie:**
- Originele tabel had deze fouten
- Studenten zouden dit kunnen gebruiken zonder verificatie
- Door fouten te spotten, leer je beter dan met perfecte data

**Wat je leert:**
- Hoe fouten ontstaan (verkeerde berekening, data mismatch)
- Hoe je ze systematisch opspoort (verificatie stappenplan)
- Hoe je ze voorkomt (checks inbouwen)
- Hoe je ermee omgaat (correct, documenteer, leer)

---

## 🔄 Gebruik in ECONAN

### Week 2: Tijdens KPI Harmonisatie Workshop

**Timing:** 15-20 minuten in sessie

**Activiteit:**
1. Docent toont foute tabel op beamer
2. Studenten werken in pairs (5 min): "Wat klopt hier niet?"
3. Plenair: Teams delen bevindingen (5 min)
4. Docent demonstreert verificatie stappenplan (5 min)
5. Takeaway: "Dit is jullie checklist voor eigen analyses"

### Week 2-3: Homework Verificatie Oefening

**Opdracht:**
- Werk deze oefening individueel door
- Document je verificatie stappen
- Upload je uitwerking (voor peer review in Week 3)
- In Week 3: Peer review elkaars verificaties

### Week 3: Peer Review van Opdracht 1

**Gebruik deze checklist:**

Wanneer je een teamgenoot's analyse reviewt:
- [ ] Controleer DuPont identity voor elke bedrijf
- [ ] Verifieer Earnings Yield berekening
- [ ] Check Valuation Bridge (Earnings Yield = ROE / P/B)
- [ ] Zijn alle bronnen vermeld?
- [ ] Zijn formules correct toegepast?

---

## 📚 Aanvullende Resources

**ECONAN Materiaal:**
- [Financial Analysis Tutorial](financial-analysis-tutorial.html) - Volledige AI-augmented workflow
- [Rheinmetall Complete Analysis](rheinmetall-analysis.html) - Werkvoorbeeld met correcte verificaties
- [Strategic Framework - IST Fase](../strategic-framework/#ist) - KPI's en ratio's in context

**Verificatie Templates:**
- DuPont Verification Spreadsheet (Excel) - komt beschikbaar Week 2
- Financial Ratios Checklist (PDF) - komt beschikbaar Week 2

**Externe References:**
- [Investopedia: DuPont Analysis](https://www.investopedia.com/terms/d/dupontanalysis.asp)
- [Investopedia: Earnings Yield](https://www.investopedia.com/terms/e/earningsyield.asp)

---

## ✏️ Notities

Gebruik deze ruimte voor je eigen notities tijdens de oefening:

**Mijn grootste takeaway:**
```




```

**Verificatie stappen die ik ga gebruiken in mijn eigen analyses:**
```
1.
2.
3.
```

**Vragen die ik nog heb:**
```




```

---

**Veel succes met de oefening!**

Remember: Fouten maken is menselijk. Fouten **niet controleren** is onprofessioneel. Leer systematisch verifiëren - het is een skill die je je hele carrière gebruikt! 🎯

---

*Laatste update: 10 november 2025*
*ECONAN Module - HBO Bedrijfskunde - Verificatie Oefening*
*Gebaseerd op echte dataset inconsistenties - educatieve case study*
