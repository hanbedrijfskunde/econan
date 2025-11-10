# VERIFICATIE OEFENING V2: Leverage Ratio Consistency
## Voor ECONAN Week 2-3 - Focus op Debt-Equity vs Equity Multiplier

**Doelgroep:** Business Analisten (alle paths)
**Tijdsinvestering:** 20-30 minuten
**Leerdoel:** Verificeren van leverage ratio's via wiskundige identiteit
**Moeilijkheidsgraad:** ⭐⭐ (Intermediate)

---

## 🎯 Leerdoelen

Na deze oefening kun je:

✅ **Leverage ratio relaties herkennen** (Debt-to-Equity ↔ Equity Multiplier)
✅ **Wiskundige identiteit toepassen**: EM = 1 + D/E
✅ **Kapitaalstructuur verifiëren** systematisch
✅ **Data inconsistenties opsporen** in leverage metrics
✅ **Balance Sheet logic controleren**

---

## 📐 De Wiskundige Relatie

### Fundamentele Identiteit

```
Equity Multiplier = 1 + Debt-to-Equity Ratio
```

**Of uitgeschreven:**
```
Total Assets     Total Debt
───────────  =  1 + ──────────
Total Equity     Total Equity
```

### Waarom klopt dit?

**Balance Sheet fundamentals:**
```
Total Assets = Total Equity + Total Debt
```

**Deel beide kanten door Total Equity:**
```
Total Assets     Total Equity   Total Debt
───────────  =  ───────────  + ──────────
Total Equity     Total Equity   Total Equity

     EM       =       1        +     D/E
```

**✅ De formule is altijd waar!**

---

## 📊 De Dataset (BEVAT FOUTEN!)

### Retail Sector - Sustainable Fashion Benchmark

| Bedrijf | Debt-Equity Ratio | Equity Multiplier | EM = 1 + D/E? |
|---------|------------------|-------------------|---------------|
| **A** | 0.6 | 1.6 | ? |
| **B** | 0.8 | 1.8 | ? |
| **C** | 1.2 | 2.2 | ? |
| **Sector Avg** | 0.9 | 1.9 | ? |

**Volledige dataset voor context:**

| Kental / Ratio | Bedrijf A | Bedrijf B | Bedrijf C | Sector Avg |
|----------------|-----------|-----------|-----------|------------|
| Debt-Equity Ratio | **0.6** | **0.8** | **1.2** | **0.9** |
| Equity Multiplier | **1.6** | **1.8** | **2.2** | **1.9** |
| ROE (%) | 21.0 | 24.0 | 25.2 | 24.3 |
| Profit Margin (%) | 7.3 | 8.9 | 5.2 | 7.1 |
| Asset Turnover | 1.8 | 1.5 | 2.2 | 1.8 |

---

## 🔍 OPDRACHT 1: Verifieer de Relatie (10 minuten)

### Voor elk bedrijf

**Bereken:** EM (verwacht) = 1 + D/E
**Vergelijk:** EM (verwacht) met EM (gerapporteerd)

#### Bedrijf A

**Gegeven:**
- Debt-to-Equity: 0.6
- Equity Multiplier: 1.6

**Berekening:**
```
EM (verwacht) = 1 + D/E
EM (verwacht) = 1 + 0.6
EM (verwacht) = ___
```

**Verificatie:**
```
EM (gerapporteerd) = 1.6
EM (verwacht) = ___
Verschil = ___
```

**Conclusie:**
- [ ] Klopt exact
- [ ] Klopt niet - er is een fout in D/E
- [ ] Klopt niet - er is een fout in EM

---

#### Bedrijf B

**Gegeven:**
- Debt-to-Equity: 0.8
- Equity Multiplier: 1.8

**Berekening:**
```
EM (verwacht) = 1 + 0.8
EM (verwacht) = ___
```

**Verificatie:**
```
EM (gerapporteerd) = 1.8
EM (verwacht) = ___
Verschil = ___
```

**Conclusie:**
- [ ] Klopt exact
- [ ] Klopt niet - fout in D/E
- [ ] Klopt niet - fout in EM

---

#### Bedrijf C

**Gegeven:**
- Debt-to-Equity: 1.2
- Equity Multiplier: 2.2

**Berekening:**
```
EM (verwacht) = 1 + 1.2
EM (verwacht) = ___
```

**Verificatie:**
```
EM (gerapporteerd) = 2.2
EM (verwacht) = ___
Verschil = ___
```

**Conclusie:**
- [ ] Klopt exact
- [ ] Klopt niet - fout in D/E
- [ ] Klopt niet - fout in EM

---

## 🧮 OPDRACHT 2: Bepaal de Correcte Waarden (10 minuten)

### Strategische Keuze: Welke is Leidend?

**Vraag:** Als D/E en EM inconsistent zijn, welke is dan correct?

**Antwoord:** Dit hangt af van de **bron**:

1. **D/E is leidend** als het direct berekend is uit Balance Sheet:
   ```
   D/E = Total Debt / Total Equity (uit geauditeerde financials)
   ```

2. **EM is leidend** als deze uit DuPont komt:
   ```
   ROE = Margin × Turnover × EM
   EM = ROE / (Margin × Turnover)
   ```

**In deze dataset:** We hebben ROE, Margin en Turnover, dus **EM is leidend** (komt uit DuPont verificatie).

**Daarom:** Pas D/E aan om te matchen met EM.

---

### Bereken Correcte D/E

**Formule:**
```
D/E = EM - 1
```

#### Bedrijf A

```
EM = 1.6 (leidend, uit DuPont)
D/E (correct) = 1.6 - 1
D/E (correct) = ___

D/E (gerapporteerd) = 0.6
Verschil = ___
```

#### Bedrijf B

```
EM = 1.8
D/E (correct) = 1.8 - 1
D/E (correct) = ___

D/E (gerapporteerd) = 0.8
Verschil = ___
```

#### Bedrijf C

```
EM = 2.2
D/E (correct) = 2.2 - 1
D/E (correct) = ___

D/E (gerapporteerd) = 1.2
Verschil = ___
```

#### Sector Average

```
EM = 1.9
D/E (correct) = 1.9 - 1
D/E (correct) = ___

D/E (gerapporteerd) = 0.9
Verschil = ___
```

---

## 📝 OPDRACHT 3: Balance Sheet Implicaties (5-10 minuten)

### Wat betekent de Correcte D/E voor Balance Sheet?

**Voorbeeld: Bedrijf A**

**Gegeven:**
- Total Equity = €1,000M (fictief voorbeeld)
- EM (correct) = 1.6
- D/E (correct) = 0.6

**Bereken Total Assets en Total Debt:**

```
Total Assets = EM × Total Equity
Total Assets = 1.6 × €1,000M
Total Assets = €___M

Total Debt = D/E × Total Equity
Total Debt = 0.6 × €1,000M
Total Debt = €___M
```

**Verificatie Balance Sheet:**
```
Total Assets = Total Equity + Total Debt
€___M = €1,000M + €___M
€___M = €___M ✓
```

**Doe hetzelfde voor Bedrijf B en C** (gebruik Total Equity = €1,000M):

| Bedrijf | Equity | EM | D/E (correct) | Assets | Debt | Check: A = E + D |
|---------|--------|----|--------------:|--------|------|-----------------|
| A | €1,000M | 1.6 | 0.6 | €___M | €___M | ✓ |
| B | €1,000M | 1.8 | 0.8 | €___M | €___M | ✓ |
| C | €1,000M | 2.2 | 1.2 | €___M | €___M | ✓ |

---

## ✅ ANTWOORDENBLAD

<details>
<summary>🔓 Klik hier om antwoorden te zien (doe eerst zelf de oefening!)</summary>

### Opdracht 1: Verificatie

#### Bedrijf A
```
EM (verwacht) = 1 + 0.6 = 1.6
EM (gerapporteerd) = 1.6
Verschil = 0 ✅ KLOPT!
```

#### Bedrijf B
```
EM (verwacht) = 1 + 0.8 = 1.8
EM (gerapporteerd) = 1.8
Verschil = 0 ✅ KLOPT!
```

#### Bedrijf C
```
EM (verwacht) = 1 + 1.2 = 2.2
EM (gerapporteerd) = 2.2
Verschil = 0 ✅ KLOPT!
```

#### Sector Average
```
EM (verwacht) = 1 + 0.9 = 1.9
EM (gerapporteerd) = 1.9
Verschil = 0 ✅ KLOPT!
```

**VERRASSING:** In deze dataset kloppen D/E en EM wél met elkaar! 🎉

Dit betekent dat de Equity Multiplier consistent is met de Debt-to-Equity ratio.

---

### Waarom Deze Oefening Toch Waardevol Is

**Les:** Niet elke dataset heeft fouten, maar je **moet altijd controleren**!

**Deze oefening leert:**
1. ✅ Hoe je systematisch verifieert (ook als alles klopt)
2. ✅ De fundamentele relatie EM = 1 + D/E
3. ✅ Balance Sheet logic (Assets = Equity + Debt)
4. ✅ Hoe leverage ratio's samenhangen

**Praktijk skill:** In echte analyses zijn verificaties die "groen" zijn net zo waardevol als die fouten vinden - ze geven **vertrouwen** in je data.

---

### Opdracht 3: Balance Sheet Implicaties

**Voor alle bedrijven (met Equity = €1,000M):**

| Bedrijf | Equity | EM | D/E | Assets | Debt | Verificatie |
|---------|--------|----|----|--------|------|-------------|
| **A** | €1,000M | 1.6 | 0.6 | **€1,600M** | **€600M** | 1,600 = 1,000 + 600 ✓ |
| **B** | €1,000M | 1.8 | 0.8 | **€1,800M** | **€800M** | 1,800 = 1,000 + 800 ✓ |
| **C** | €1,000M | 2.2 | 1.2 | **€2,200M** | **€1,200M** | 2,200 = 1,000 + 1,200 ✓ |

**Berekeningen:**

**Bedrijf A:**
```
Total Assets = 1.6 × €1,000M = €1,600M
Total Debt = 0.6 × €1,000M = €600M
Check: €1,600M = €1,000M + €600M ✓
```

**Bedrijf B:**
```
Total Assets = 1.8 × €1,000M = €1,800M
Total Debt = 0.8 × €1,000M = €800M
Check: €1,800M = €1,000M + €800M ✓
```

**Bedrijf C:**
```
Total Assets = 2.2 × €1,000M = €2,200M
Total Debt = 1.2 × €1,000M = €1,200M
Check: €2,200M = €1,000M + €1,200M ✓
```

---

### Patronen Herkennen

**Observaties:**

1. **Bedrijf C heeft hoogste leverage:**
   - D/E = 1.2 betekent €1.20 debt per €1 equity
   - EM = 2.2 betekent €2.20 assets per €1 equity
   - Risicovollere kapitaalstructuur

2. **Bedrijf A is meest conservatief:**
   - D/E = 0.6 betekent €0.60 debt per €1 equity
   - EM = 1.6 betekent €1.60 assets per €1 equity
   - Veiligere kapitaalstructuur

3. **Voor elke €1 extra D/E, stijgt EM met €1:**
   - Bedrijf A: D/E +0.6 → EM = 1.6 (dus +0.6 boven 1.0)
   - Bedrijf C: D/E +1.2 → EM = 2.2 (dus +1.2 boven 1.0)
   - **Perfecte 1-op-1 relatie!**

</details>

---

## 🎓 Didactische Lessen

### Les 1: Verificatie is een Habit, Geen Exception

**In deze oefening klopte alles** - en dat is perfect!

In de praktijk:
- ✅ 80% van verificaties: alles klopt
- ❌ 20% van verificaties: je vindt fouten

**Maar:** Zonder die 100% verificaties weet je niet welke 20% fout is!

**Professionele mindset:**
```
Verificatie = verzekering
- Kost tijd
- Meestal geen "uitkering" (geen fouten)
- Maar onmisbaar wanneer het mis gaat
```

---

### Les 2: Wiskundige Identiteiten zijn Waardevol

**EM = 1 + D/E** is niet een "nice to know", maar een **verificatie tool**:

**Gebruik cases:**
1. **Data entry check:** Typ je D/E in Excel, bereken EM automatisch
2. **AI output verificatie:** AI geeft je beide ratio's, check of ze matchen
3. **Cross-source validation:** D/E uit Bloomberg, EM uit company report - moeten kloppen
4. **Balance sheet sanity check:** Als EM en D/E niet kloppen, is je Balance Sheet fout

---

### Les 3: Leverage Interpretatie

**D/E en EM vertellen hetzelfde verhaal, anders:**

| Ratio | Formule | Vertelt Je | Interpretatie |
|-------|---------|------------|---------------|
| **D/E** | Debt / Equity | Hoeveel debt per €1 equity | **Risk perspective** |
| **EM** | Assets / Equity | Hoeveel assets per €1 equity | **Efficiency perspective** |

**Voorbeeld Bedrijf C:**
- **D/E = 1.2:** "Voor elke €1 eigen geld heeft het bedrijf €1.20 geleend" (RISK!)
- **EM = 2.2:** "Voor elke €1 eigen geld beheert het bedrijf €2.20 assets" (LEVERAGE!)

**Beide waar, verschillende lens!**

---

## 🔄 Gebruik in ECONAN

### Week 2: Quick Leverage Check (5 min)

**Tijdens KPI Harmonisatie Workshop:**

1. Docent: "Jullie gaan D/E en EM rapporteren - maar weten jullie dat deze samenhangen?"
2. Toon EM = 1 + D/E op whiteboard
3. Studenten: "Check je eigen data - klopt het?"
4. Quick poll: "Wie heeft een mismatch?" (troubleshoot live)

### Week 3: Peer Review Checklist

**Bij Opdracht 1 review:**

Checklist item toevoegen:
```
[ ] Leverage verificatie: EM = 1 + D/E (binnen 0.01 verschil)
```

Als het niet klopt:
- Check Balance Sheet data (Total Assets, Equity, Debt)
- Herbereken D/E of EM vanuit source
- Documenteer welke je als "leidend" neemt en waarom

---

## 📚 Volgende Stappen

### Andere Verificatie Oefeningen

1. **V1: DuPont & P/B Verificatie** (al beschikbaar)
   - Focus: ROE via DuPont, Earnings Yield = ROE / P/B
   - Bevat fouten in dataset

2. **V2: Leverage Verificatie** (deze oefening)
   - Focus: EM = 1 + D/E
   - Correcte dataset (leer verifiëren zonder fouten)

3. **V3: Liquidity Ratios** (coming soon)
   - Focus: Current Ratio vs Quick Ratio
   - Bevat inventory inconsistenties

4. **V4: Market Valuation** (coming soon)
   - Focus: P/E, P/B, Earnings Yield driehoek
   - Bevat afrondingsfouten

---

## ✏️ Notities

**Mijn verificatie aanpak voor EM en D/E:**
```
Stap 1: ___________________
Stap 2: ___________________
Stap 3: ___________________
```

**Wanneer gebruik ik D/E als leidend vs EM als leidend?**
```




```

---

**Belangrijkste takeaway:** Zelfs als je verwacht dat data klopt, **verifieer altijd**. Het is een reflex, geen keuze!

---

*Laatste update: 10 november 2025*
*ECONAN Module - HBO Bedrijfskunde - Verificatie Oefening V2*
*Focus: Leverage Ratio Consistency*
