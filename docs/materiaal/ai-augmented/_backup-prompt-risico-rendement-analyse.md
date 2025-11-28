# AI Prompt: Risico & Rendement Analyse

---

## CRISP-DM Fasering

Deze analyse volgt het CRISP-DM framework:

| Fase | Stappen in deze Prompt |
|------|------------------------|
| **1. Business Understanding** | Context (waarom deze analyse?) |
| **2. Data Understanding** | Databronnen, STAP 1 |
| **3. Data Preparation** | STAP 1b, STAP 2, STAP 3 |
| **4. Modeling** | STAP 4, STAP 5 |
| **5. Evaluation** | STAP 6 |
| **6. Deployment** | Eindrapportage, Logboek |

---

# FASE 1: BUSINESS UNDERSTANDING

## Context
Je bent een data-analist die een risico- en rendementanalyse uitvoert voor een beursgenoteerd bedrijf
ten opzichte van twee marktindices. Je werkt met wekelijkse koersdata over een periode van 5 jaar.

**Doel van de analyse**: Bepaal het systematisch risico (beta) en de risico-gecorrigeerde performance (alpha) van het bedrijf om beleggingsbeslissingen te ondersteunen.

---

# FASE 2: DATA UNDERSTANDING

## Databronnen
- **Bedrijf**: [BEDRIJFSNAAM] - ticker: [TICKER]
- **Index 1**: [INDEX1_NAAM] (bijv. S&P 500, AEX, FTSE)
- **Index 2**: [INDEX2_NAAM] (bijv. DAX, CAC40, sectorindex)
- **Periode**: [STARTDATUM] tot [EINDDATUM]
- **Frequentie**: Wekelijks (closing prices)

## Instructies

Voer de analyse uit in de onderstaande stappen. **Log elke stap** in een overzicht met:
- Stap nummer en naam
- Input data
- Uitgevoerde actie
- Output/resultaat
- Eventuele waarschuwingen of aandachtspunten

---

### STAP 1: Data Inlezen en Valideren

#### 1.1 Data Extractie
- Lees de closing prices in voor alle drie de datasets (bedrijf + 2 indices)
- Als de data in dagfrequentie is: converteer naar weekdata (gebruik vrijdag-slotkoers of laatste handelsdag van de week)
- Noteer per dataset: bron, aantal datapunten, eerste datum, laatste datum

#### 1.2 Datum Synchronisatie Check
Controleer of de meetmomenten (datums) overeenkomen tussen de drie datasets:
- Vergelijk de datumreeksen
- Identificeer ontbrekende datums per dataset
- **Als er verschillen zijn**: synchroniseer door alleen datums te gebruiken die in ALLE drie datasets voorkomen

#### 1.3 Data Kwaliteit Check
- Check op ontbrekende waarden (nulls/NaN)
- Check op uitschieters (prijzen die >50% afwijken van vorige week)
- Check of prijzen positief zijn
- Rapporteer eventuele data-issues

**LOG OUTPUT STAP 1:**
| Dataset | Bron | Ruwe datapunten | Na synchronisatie | Eerste datum | Laatste datum | Issues |
|---------|------|-----------------|-------------------|--------------|---------------|--------|
| [Bedrijf] | | | | | | |
| [Index 1] | | | | | | |
| [Index 2] | | | | | | |

---

# FASE 3: DATA PREPARATION

### STAP 1b: Data Cleaning & Repairing

#### 1b.1 Missing Values Behandelen
Als er ontbrekende waarden zijn geïdentificeerd in Stap 1.3:
- **Optie A**: Verwijder rijen met missings (als < 5% van data)
- **Optie B**: Interpoleer (lineair) voor tussenliggende datums
- **Optie C**: Forward-fill (laatste bekende waarde gebruiken)
- Documenteer welke methode je kiest en waarom

#### 1b.2 Outlier Treatment
Voor geïdentificeerde uitschieters:
- Controleer of uitschieter correct is (bijv. stock split, dividend, grote nieuwsgebeurtenis)
- Als data-fout: corrigeer of verwijder
- Als legitieme uitschieter: behoud maar documenteer impact op analyse

#### 1b.3 Data Transformatie
- Converteer prijsdata naar consistent format (decimalen, valuta)
- Zorg dat alle datums hetzelfde formaat hebben (YYYY-MM-DD)
- Sorteer data chronologisch (oudste eerst)

**LOG OUTPUT STAP 1b:**
| Issue Type | Aantal | Behandeling | Rationale |
|------------|--------|-------------|-----------|
| Missing values | | | |
| Outliers | | | |
| Format issues | | | |

---

### STAP 2: Rendementen Berekenen

#### 2.1 Wekelijkse Rendementen
Bereken voor elke dataset het wekelijkse procentuele rendement:
```
Rendement_t = ((Prijs_t - Prijs_{t-1}) / Prijs_{t-1}) × 100%
```

#### 2.2 Beschrijvende Statistieken
Bereken per dataset:
- Gemiddeld wekelijks rendement
- Standaarddeviatie (volatiliteit)
- Minimum en maximum rendement
- Aantal observaties

#### 2.3 Sanity Check
- Controleer of het cumulatief rendement over de hele periode overeenkomt met (Eindprijs/Beginprijs - 1)
- Vergelijk de berekende standaarddeviatie met bekende marktvolatiliteit

**LOG OUTPUT STAP 2:**
| Dataset | Gem. Rendement | Std. Dev | Min | Max | N | Cumulatief Check ✓/✗ |
|---------|----------------|----------|-----|-----|---|----------------------|
| [Bedrijf] | | | | | | |
| [Index 1] | | | | | | |
| [Index 2] | | | | | | |

---

### STAP 3: Tijdreeks Visualisatie

#### 3.1 Gecombineerde Lijngrafiek
Maak een lijngrafiek met:
- X-as: Tijd (weken)
- Y-as: Wekelijks rendement (%)
- Drie lijnen: Bedrijf, Index 1, Index 2
- Duidelijke legenda
- Nul-lijn markeren

#### 3.2 Visuele Analyse
Beantwoord op basis van de grafiek:
- Welke reeks toont de hoogste volatiliteit?
- Zijn er periodes met extreme uitschieters?
- Bewegen de reeksen grofweg samen of onafhankelijk?

**LOG OUTPUT STAP 3:**
- Grafiek gegenereerd: [JA/NEE]
- Observaties volatiliteit: [...]
- Observaties co-movement: [...]

---

# FASE 4: MODELING

### STAP 4: Regressie Analyse - Scatter Plots

#### 4.1 Scatter Plot Bedrijf vs Index 1
- X-as: Rendement Index 1 (%)
- Y-as: Rendement Bedrijf (%)
- Voeg regressielijn toe

#### 4.2 Scatter Plot Bedrijf vs Index 2
- X-as: Rendement Index 2 (%)
- Y-as: Rendement Bedrijf (%)
- Voeg regressielijn toe

#### 4.3 Visuele Beoordeling
- Is er een duidelijk lineair verband zichtbaar?
- Hoe "strak" liggen de punten rond de regressielijn?
- Zijn er duidelijke uitschieters?

**LOG OUTPUT STAP 4:**
- Scatter plot 1 (vs Index 1): [GEGENEREERD]
- Scatter plot 2 (vs Index 2): [GEGENEREERD]
- Visuele correlatie Index 1: [ZWAK/MATIG/STERK]
- Visuele correlatie Index 2: [ZWAK/MATIG/STERK]

---

### STAP 5: Regressie Parameters Berekenen

#### 5.1 Lineaire Regressie: Bedrijf = α + β × Index
Bereken voor beide index-combinaties:
- **Alpha (α)**: Intercept - gemiddeld excess rendement t.o.v. markt
- **Beta (β)**: Helling - gevoeligheid voor marktbewegingen
- **R²**: Verklaringskracht - % variatie verklaard door markt

#### 5.2 Interpretatie Framework
| Parameter | Waarde | Interpretatie |
|-----------|--------|---------------|
| β < 0.5 | Laag | Aandeel beweegt grotendeels onafhankelijk van markt (veel idiosyncratisch risico) |
| β = 0.5-1.0 | Defensief | Aandeel beweegt minder dan markt |
| β = 1.0-1.5 | Neutraal/Agressief | Aandeel beweegt (iets meer dan) markt |
| β > 1.5 | Hoog risico | Aandeel versterkt marktbewegingen |
| α > 0 | Positief | Outperformance t.o.v. verwacht rendement |
| α < 0 | Negatief | Underperformance t.o.v. verwacht rendement |
| R² < 10% | Laag | Markt verklaart weinig; risico is bedrijfsspecifiek |
| R² > 50% | Hoog | Aandeel beweegt grotendeels mee met markt |

**LOG OUTPUT STAP 5:**
| Regressie | Alpha (α) | Beta (β) | R² | Interpretatie |
|-----------|-----------|----------|-----|---------------|
| vs Index 1 | | | | |
| vs Index 2 | | | | |

---

# FASE 5: EVALUATION

### STAP 6: Triangulatie en Validatie

#### 6.1 Interne Consistentie Checks
- [ ] **Beta consistentie**: Zijn de beta's t.o.v. beide indices vergelijkbaar? (grote verschillen kunnen wijzen op data-issues)
- [ ] **Volatiliteit check**: Is Std.Dev(bedrijf) > Std.Dev(index)? (individuele aandelen zijn meestal volatieler)
- [ ] **R² plausibiliteit**: Is R² < 100%? (exacte fit wijst op fout)
- [ ] **Alpha magnitude**: Is |α| < 2% per week? (extreme waarden zijn verdacht)

#### 6.2 Externe Validatie
- [ ] Vergelijk berekende beta met gepubliceerde beta (Yahoo Finance, Bloomberg)
- [ ] Controleer of volatiliteit in lijn is met sector-gemiddelden
- [ ] Vergelijk alpha met bekende performance van het aandeel

#### 6.3 Gevoeligheidsanalyse
- Herbereken met andere tijdsperiode (bijv. laatste 3 jaar ipv 5 jaar)
- Zijn de conclusies robuust?

**LOG OUTPUT STAP 6:**
| Check | Resultaat | Opmerking |
|-------|-----------|-----------|
| Beta consistentie | ✓/✗ | |
| Volatiliteit check | ✓/✗ | |
| R² plausibiliteit | ✓/✗ | |
| Alpha magnitude | ✓/✗ | |
| Externe beta validatie | ✓/✗ | Bron: |
| Gevoeligheidsanalyse | ✓/✗ | |

---

# FASE 6: DEPLOYMENT

## Eindrapportage

Vat de analyse samen in maximaal 200 woorden:
1. Wat is de beta van [BEDRIJF] t.o.v. de markt?
2. Hoeveel van het risico is systematisch (markt) vs. idiosyncratisch (bedrijfsspecifiek)?
3. Heeft het aandeel outperformed of underperformed (alpha)?
4. Wat betekent dit voor een belegger?

---

## Volledig Logboek

Voeg aan het einde een compleet logboek toe met alle stappen, timestamps, en eventuele beslissingen/aanpassingen die zijn gemaakt.

---

# Instructies voor Gebruik

1. **Kopieer de prompt** naar je AI-tool (Claude, ChatGPT, etc.)
2. **Vervang de placeholders** [BEDRIJFSNAAM], [TICKER], etc. met je eigen data
3. **Upload je databestanden** (CSV, Excel, of PDF van koersdata)
4. **Vraag de AI om stap-voor-stap** te werken en na elke stap te wachten op bevestiging
5. **Bewaar alle log-outputs** voor je eindrapport

## Verwachte Output per Stap

| Stap | CRISP-DM Fase | Output |
|------|---------------|--------|
| 1 | Data Understanding | Tabel met data-overzicht + synchronisatie-rapport |
| 1b | Data Preparation | Tabel met cleaning decisions |
| 2 | Data Preparation | Tabel met beschrijvende statistieken |
| 3 | Data Preparation | Lijngrafiek + observaties |
| 4 | Modeling | Twee scatter plots |
| 5 | Modeling | Regressie parameters tabel |
| 6 | Evaluation | Validatie checklist |

## Voorbeeld Invulling

```
## Databronnen
- **Bedrijf**: Rheinmetall AG - ticker: RHM.DE
- **Index 1**: S&P 500 - ticker: .SPX
- **Index 2**: DAX - ticker: .GDAXI
- **Periode**: November 2020 tot November 2025
- **Frequentie**: Wekelijks (closing prices)
```

## Werkvoorbeeld

Bekijk een volledig uitgewerkt voorbeeld met Rheinmetall data:
→ [Weekly Returns Analysis - Rheinmetall](../examples/weekly-returns-tabs.html)
