# **Van Regressie naar Risico: Een Pedagogische Verdiepingsslag op het Market Model en CAPM voor het HBO Bedrijfskunde**

## **Deel 1: Analyse en Verfijning van het Huidige Regressiemodel**

Het initiatief om lineaire regressie en het Capital Asset Pricing Model (CAPM) te koppelen middels een praktische spreadsheet-opdracht is pedagogisch zeer waardevol. Het biedt studenten een directe, tastbare toepassing van een statistische techniek binnen hun vakgebied. De hier gepresenteerde analyse en suggesties zijn bedoeld als constructieve feedback om de lesmodule methodologisch aan te scherpen en de leerervaring significant te verrijken.

### **1.1. Vaststelling van de Variabelen (X vs. Y)**

Allereerst is er een kleine discrepantie tussen de ingediende query en de uitvoering in het spreadsheet.1 De query stelt: "een regressie van de returns van een stock index op de returns (y) van een specifiek aandeel (x)". Dit zou betekenen dat het aandeel de onafhankelijke variabele (X-as) is en de index de afhankelijke (Y-as).

De grafiek "R GE vs R S\&P500" op pagina 1 van het document 1 toont echter de correcte, standaard financiële opzet. De Y-as (afhankelijke variabele) is "R General Electric Co" en de X-as (onafhankelijke variabele) is "R S\&P500". De regressielijn wordt gegeven als $y \= 1.18 x \+ \-1.6E-03$.1

Dit rapport gaat uit van de (correcte) uitvoering in het spreadsheet, waarbij het model de volgende vorm heeft:

$$R\_{GE,t} \= \\alpha \+ \\beta \\cdot R\_{S\\\&P500,t} \+ \\epsilon\_t$$  
Op basis van de output 1 zijn de geschatte parameters:

* **Intercept ($\\alpha$):** $-1.6E-03$ (oftewel \-0.0016, of \-0.16%)  
* **Helling ($\\beta$):** $1.18$  
* **Verklaringskracht ($R^2$):** $0.436$

### **1.2. De Cruciale Opmerking: U heeft het Market Model geschat, niet het CAPM**

De belangrijkste methodologische opmerking is dat het uitgevoerde model, hoewel nuttig, niet het *Capital Asset Pricing Model* (CAPM) is. Het is het **Market Model (MM)**.

* Het **Market Model (MM)** is een *statistisch* model dat de lineaire relatie tussen de *totale returns* van een aandeel ($R\_i$) en de *totale returns* van de markt ($R\_m$) beschrijft.2 Het is een toepassing van lineaire regressie zonder diepe economische onderbouwing.  
* Het **Capital Asset Pricing Model (CAPM)** is een *economische evenwichtstheorie* over de *verwachte* rendementen.3 Het stelt dat het *verwachte* rendement van een aandeel *bovenop de risicovrije rente ($R\_f$)*, evenredig is aan de *verwachte* marktrisicopremie (het marktrendement *bovenop $R\_f$*).

De formele CAPM-theorie luidt:

$$E \- R\_f \= \\beta\_i (E \- R\_f)$$  
Om deze theorie te testen met een regressie, moet de regressie-vergelijking in dezelfde termen worden opgesteld. Dit leidt tot de Security Characteristic Line (SCL), wat de feitelijke regressie is die het CAPM toetst. Deze SCL vereist het gebruik van excess returns (rendementen minus de risicovrije rente) 2:

$$(R\_{i,t} \- R\_{f,t}) \= \\alpha\_i \+ \\beta\_i (R\_{m,t} \- R\_{f,t}) \+ \\epsilon\_t$$  
Door de *ruwe returns* (Total Returns) te gebruiken in plaats van *excess returns*, mist de huidige analyse de kern van de CAPM-theorie.

### **1.3. De Implicaties van de Fout: De Betekenis van de Intercept ($\\alpha$)**

Deze methodologische keuze heeft een cruciale implicatie voor de interpretatie van de intercept ($\\alpha$).

* **Interpretatie van de huidige $\\alpha$ (Market Model):** De gevonden $\\alpha$ van \-0.16% 1 heeft een beperkte economische betekenis. Het betekent statistisch gezien: "Als de S\&P 500 in een week een rendement van 0% heeft, is het voorspelde rendement van General Electric (GE) \-0.16%."  
* **Interpretatie van de correcte $\\alpha$ (Jensen's Alpha):** In de SCL-regressie (met excess returns) is de $\\alpha$ bekend als **Jensen's Alpha**. Dit is een van de meest gebruikte maatstaven voor *abnormaal rendement*.4 Het meet het gemiddelde rendement van het aandeel *nadat* is gecorrigeerd voor het systematische marktrisico dat het heeft genomen.

De centrale voorspelling van de CAPM-theorie is dat de markt efficiënt is en dat een aandeel gemiddeld *precies* het rendement oplevert dat past bij het risico. Daarom *voorspelt* de CAPM-theorie dat **$\\alpha \= 0$**.2

Door de SCL-regressie uit te voeren, kunnen studenten de p-waarde van de $\\alpha$ toetsen.

* Als $\\alpha$ statistisch significant *positief* is, heeft het aandeel de markt *verslagen* op een voor risico gecorrigeerde basis (waarde gecreëerd).  
* Als $\\alpha$ statistisch significant *negatief* is, heeft het aandeel *slechter* gepresteerd dan verwacht (waarde vernietigd).

De huidige aanpak mist deze financiële 'punchline'. De vraag "Heeft GE het over de periode 2000-2019 goed of slecht gedaan, gegeven het risico?" kan niet worden beantwoord.

### **1.4. Methodologische Correctie: De Risicovrije Rente ($R\_f$) Toevoegen**

Om van het Market Model naar de SCL te transformeren, moet de risicovrije rente ($R\_f$) in de analyse worden opgenomen. Het spreadsheet 1 mist deze datakolom.

1. **Data Frequentie:** De data in het spreadsheet 1 is *wekelijks* (bv. 31/12/1999, 07/01/2000, 14/01/2000). Er is dus een *wekelijkse* $R\_f$ proxy nodig voor de periode 2000-2019.  
2. **Data Bron:** Een standaard proxy voor de $R\_f$ is de U.S. Treasury Bill (een staatsobligatie met korte looptijd, bv. 3 maanden of 1 jaar). Deze data is publiek beschikbaar via bronnen als de Federal Reserve Economic Data (FRED) 5 of het U.S. Department of the Treasury.7  
3. **Pedagogische Oefening:** Dit creëert een uitstekende dataverwerkingsles. De T-bill *rates* worden doorgaans op jaarbasis (annualized) en als dag- of maandreeks gepubliceerd. Studenten moeten deze data:  
   * Matchen op de wekelijkse data (bv. de rate aan het begin van de week nemen).  
   * Omzetten van een jaar-rate naar een *wekelijks rendement*. De correcte formule hiervoor is: $R\_{f, \\text{wekelijks}} \= (1 \+ R\_{f, \\text{jaarlijks}})^{1/52} \- 1$.  
4. **Contextuele Impact van $R\_f$:** De gekozen dataperiode (2000-2019) 1 omspant twee zeer verschillende macro-economische regimes.  
   * **2000-2007:** Een periode met substantiële $R\_f$ (bv. 5-6% in 2000).8  
   * **2009-2019:** De periode na de financiële crisis, gekenmerkt door ZIRP (Zero Interest-Rate Policy), waar $R\_f \\approx 0$.  
   * Dit is een krachtig didactisch punt. In de ZIRP-periode zal het *numerieke* verschil tussen het MM en de SCL klein zijn (omdat $R\_i \- 0 \\approx R\_i$). Echter, in de 2000-2007 periode leidt het weglaten van $R\_f$ tot een significante *omitted variable bias* (vertekening door een weggelaten variabele). Het laat studenten zien hoe het monetaire beleid van de centrale bank de parameterschatting van financiële modellen direct beïnvloedt.

### **1.5. Conclusie Deel 1: Een Conceptuele Vergelijking**

De correctie kan worden samengevat in de volgende conceptuele vergelijking, die als basis voor de les kan dienen.

**Tabel 1: Conceptuele Vergelijking: Market Model vs. SCL (CAPM)**

| Kenmerk | Market Model (MM) (Huidige model) | Security Characteristic Line (SCL) (Correcte CAPM-test) |
| :---- | :---- | :---- |
| **Formule** | $R\_i \= \\alpha \+ \\beta R\_m \+ \\epsilon$ | $(R\_i \- R\_f) \= \\alpha \+ \\beta(R\_m \- R\_f) \+ \\epsilon$ |
| **Variabelen** | Ruwe (totale) returns | Excess returns (rendementen boven $R\_f$) |
| **Doel** | Statistisch: Hoeveel beweegt $R\_i$ als $R\_m$ beweegt? | Economisch: Testen van de CAPM-theorie.2 |
| **Interpretatie $\\alpha$** | Voorspeld rendement $R\_i$ als $R\_m \= 0$. | **Jensen's Alpha**: Abnormaal (risicogecorrigeerd) rendement. |
| **CAPM-test?** | Nee. | Ja, door te testen of $\\alpha \= 0$.4 |

## **Deel 2: Een Rijkere Leerervaring \- Van Statistiek naar Financiële Inzichten**

De methodologische correctie opent de deur naar een veel rijkere leerervaring. De volgende suggesties integreren de onderwerpen regressie en CAPM dieper en maken maximaal gebruik van de data.

### **2.1. Suggestie 1: Decompositie van Risico (De Ware Kracht van $R^2$)**

De huidige analyse identificeert $R^2 \= 0.436$ 1, wat waarschijnlijk wordt geïnterpreteerd als "de 'fit' van het model" (d.w.z. "43.6% van de beweging in GE wordt verklaard door de S\&P 500"). Dit is correct, maar het mist de diepere financiële betekenis: **$R^2$ is de maatstaf voor diversificatie.**

De financiële theorie stelt dat het totale risico van een aandeel (gemeten als variantie, $\\sigma\_i^2$) kan worden opgesplitst in twee componenten:

1. **Systematisch Risico:** Marktrisico dat *niet* kan worden weggediversifieerd. Dit wordt in het model vastgelegd als $\\beta^2 \\sigma\_m^2$. Volgens het CAPM is dit het *enige* risico waarvoor beleggers worden beloond.  
2. **Idiosyncratisch (of Uniek) Risico:** Bedrijfsspecifiek risico dat *wel* kan worden weggediversifieerd (bv. een staking, een productfout). Dit is de variantie van de residuen ($\\sigma\_\\epsilon^2$).

De $R^2$ van een lineaire regressie is wiskundig gedefinieerd als de fractie van de totale variantie die door het model wordt verklaard. In deze context betekent dit:

$$R^2 \= \\frac{\\text{Verklaarde Variantie}}{\\text{Totale Variantie}} \= \\frac{\\text{Systematisch Risico}}{\\text{Totaal Risico}} \= \\frac{\\beta^2 \\sigma\_m^2}{\\sigma\_i^2}$$  
**Praktische Oefening:** Laat studenten dit zelf *bewijzen* met de data uit het spreadsheet 1:

1. **Totaal Risico ($\\sigma\_{GE}^2$):** De SD van GE is 4.25%. De variantie is $(0.0425)^2 \= 0.001806$.  
2. **Markt Risico ($\\sigma\_{S\\\&P500}^2$):** De SD van de S\&P 500 is 2.36%. De variantie is $(0.0236)^2 \= 0.000557$.  
3. **Beta ($\\beta$):** De geschatte coëfficiënt is $1.18$.  
4. **Bereken Systematisch Risico:** $\\beta^2 \\sigma\_m^2 \= (1.18)^2 \\times 0.000557 \= 1.3924 \\times 0.000557 \= 0.000776$.  
5. **Bereken de Ratio:** $\\frac{\\text{Systematisch Risico}}{\\text{Totaal Risico}} \= \\frac{0.000776}{0.001806} \= 0.430$.

Dit berekende getal (0.430) is nagenoeg identiek aan de $R^2$ van de regressie (0.436). Dit is een krachtig "Aha-Erlebnis" voor studenten. Het bewijst dat 43.6% van het totale risico van GE systematisch (markt-)risico is.

De resterende 56.4% ($1 \- R^2$) is het idiosyncratische, *diversifieerbare* risico. Dit visualiseert perfect *waarom* portefeuilleleer werkt en waarom beleggers (volgens CAPM) geen extra rendement krijgen voor het dragen van dit unieke risico.

**Tabel 2: Risicodecompositie van General Electric (2000-2019)**

| Risicocomponent | Formule | Berekening | Resultaat (Variantie) | Proportie |
| :---- | :---- | :---- | :---- | :---- |
| Totaal Risico | $\\sigma\_{GE}^2$ | $(0.0425)^2$ | 0.001806 | 100.0% |
| Systematisch Risico | $\\beta^2 \\sigma\_{S\\\&P500}^2$ | $(1.18)^2 \\times (0.0236)^2$ | 0.000776 | 43.0% (Gelijk aan $R^2$) |
| Idiosyncratisch Risico | $\\sigma\_{GE}^2 \- \\beta^2 \\sigma\_{S\\\&P500}^2$ | $0.001806 \- 0.000776$ | 0.001030 | 57.0% (Gelijk aan $1-R^2$) |

### **2.2. Suggestie 2: Het Testen van de Regressie-aannames (De "HBO-plus" Stap)**

De opdracht verbindt twee onderwerpen: regressie en CAPM. Dit is een ideale kans om de SCL-regressie te gebruiken als een *casestudy* voor het toetsen van de aannames van lineaire regressie (OLS).9

1. **Aanname 1: Lineariteit.** Deze kan visueel worden getoetst met de scatter plot "R GE vs R S\&P500".1 De relatie lijkt redelijk lineair.  
2. **Aanname 2: Homoscedasticiteit (constante variantie van residuen).** Deze aanname wordt *duidelijk geschonden*. De tijdreeksgrafiek "R\_GE and R\_S\&P500" 1 toont extreme *volatiliteitsclustering*. De returns (en dus de fouttermen) zijn 'wild' tijdens de dot-com crisis (2000-2002) en de financiële crisis (2008-2009), en veel 'rustiger' daartussen.  
   * **Implicatie:** Heteroscedasticiteit betekent dat de OLS-schatter ($\\beta=1.18$) nog steeds *unbiased* (zuiver) is, maar dat de *standaardfouten* (en dus de t-statistieken en p-waarden) *onbetrouwbaar* zijn. Dit is een cruciaal inzicht: de significantie-toetsen die Excel produceert, zijn waarschijnlijk fout.  
3. **Aanname 3: Normaliteit van Residuen.** De histogrammen in het document 1 suggereren al dat de data niet normaal verdeeld is. Financiële returns staan bekend om *leptokurtosis* ("fat tails") – extreme gebeurtenissen (zoals de \-20.46% return voor GE in september 2001 1) komen veel vaker voor dan de normale verdeling voorspelt.  
   * **Les:** Laat studenten de *kurtosis* en *skewness* van de residuen berekenen. Dit voegt een kritische, analytische laag toe en leert studenten de output van software niet blindelings te vertrouwen.

### **2.3. Suggestie 3: De Instabiliteit van Beta (De Limitaties van Historische Data)**

Een belangrijke beperking van het CAPM is de afhankelijkheid van *historische data* om *toekomstig* risico te voorspellen.11 De $\\beta \= 1.18$ 1 is een *gemiddelde* over een zeer lange en turbulente periode van 20 jaar (2000-2019).1

De vraag is of $\\beta$ wel stabiel is over die periode. General Electric is *radicaal* veranderd. Het bedrijf van 2000 was een conglomeraat met een enorme financiële tak (GE Capital), die bijna failliet ging in 2008\. Het bedrijf van 2019 was een afgeslankt industrieel bedrijf. Hun risicoprofiel was fundamenteel anders.

**Praktische Oefening:** Laat studenten de dataset in tweeën splitsen en twee afzonderlijke regressies uitvoeren:

1. **Regressie 1: 2000-2009** (de 'oude' GE, inclusief de financiële crisis).  
2. **Regressie 2: 2010-2019** (de 'nieuwe' GE, in de post-crisis ZIRP-periode).

De hypothese is dat de $\\beta$ (en de $\\alpha$\!) in deze twee periodes significant van elkaar zullen verschillen. Dit toont studenten de *dynamische* aard van risico en de beperkingen van het gebruiken van één enkel, langetermijn-gemiddelde.

### **2.4. Suggestie 4: De Kritische Discussie (De Aannames van het *Economische* Model)**

Nadat de *statistische* aannames (Suggestie 2.2) zijn behandeld, moet de *economische theorie* zelf worden bekritiseerd. Het CAPM is berucht om zijn onrealistische aannames.12

**Discussiepunten voor de klas:**

* Het model neemt aan dat alle investeerders rationeel, risico-avers zijn en identieke (homogene) verwachtingen hebben.11 Is dit realistisch?  
* Het model neemt aan dat men onbeperkt kan lenen en uitlenen tegen de risicovrije rente.12 Kan een student lenen tegen dezelfde rente als de staat?  
* Het model negeert transactiekosten en belastingen.14  
* Het model gebruikt een 'enkel-periode' tijdshorizon.12 Plannen studenten hun beleggingen slechts voor één periode (bv. één jaar)?

Dit is de essentie van hoger onderwijs: niet alleen *toepassen*, maar ook *kritisch reflecteren*. Waarom gebruiken we een model waarvan we weten dat de aannames onjuist zijn? (Een mogelijk antwoord: "Alle modellen zijn fout, maar sommige zijn nuttig." Het CAPM biedt, ondanks zijn gebreken, een eenvoudige en intuïtieve basis voor het denken over de relatie tussen risico en rendement 3).

## **Deel 3: Concreet Stappenplan voor de Vernieuwde Lesmodule**

Dit alles kan worden geïntegreerd in een logische, stapsgewijze lesmodule.

### **3.1. Stap 1: De Start (Het Market Model)**

* Voer de regressie uit zoals nu gedaan: $R\_{GE}$ op $R\_{S\\\&P500}$.1  
* Resultaat: $\\beta=1.18$, $\\alpha=-0.16\\%$, $R^2=0.436$.1  
* Basisinterpretatie: "$\\beta \> 1$ betekent een 'agressief' aandeel, het beweegt sterker dan de markt. $R^2$ is de 'fit' van het model."

### **3.2. Stap 2: De Eerste Verdieping (Statistiek $\\rightarrow$ Finance)**

* Integreer **Suggestie 2.1 (Risicodecompositie)**.  
* Stel de vraag: "Wat betekent die $R^2 \= 0.436$ *echt* voor een bedrijfskundige?"  
* Laat studenten de berekening uit Tabel 2 uitvoeren met $\\sigma\_{GE}$ en $\\sigma\_{S\\\&P500}$ 1 en *bewijzen* dat $R^2$ de fractie systematisch risico is.  
* Conclusie: 56.4% van het risico van GE is uniek en had (in theorie) weggediversifieerd kunnen worden.

### **3.3. Stap 3: De Theoretische Correctie (Introductie CAPM)**

* Introduceer de *theorie* van CAPM (Deel 1.2).2 Leg uit *waarom* risico alleen beloond wordt *bovenop* een basisvergoeding (de risicovrije rente $R\_f$).  
* Introduceer de *correcte* SCL-formule: $(R\_i \- R\_f) \= \\alpha \+ \\beta(R\_m \- R\_f) \+ \\epsilon$.2

### **3.4. Stap 4: De Data-oefening (Praktische Vaardigheden)**

* Identificeer de 'missende variabele' $R\_f$ in de 1\-data (Deel 1.4).  
* **Opdracht:** "Zoek de historische (wekelijkse) 3-maands T-bill rate op voor 2000-2019".5  
* **Opdracht:** "Importeer deze data en converteer de jaar-rate naar een wekelijks rendement."  
* **Opdracht:** "Maak twee nieuwe kolommen in de spreadsheet: $R\_{GE,excess} \= R\_{GE} \- R\_{f,wekelijks}$ en $R\_{S\\\&P500,excess} \= R\_{S\\\&P500} \- R\_{f,wekelijks}$."

**Tabel 3: Voorbeeld Gecorrigeerde Dataset (Illustratief)**

| Datum | RGE​ | RS\&P500​ | Rf​ (jaarbasis, bv.) | Rf​ (wekelijks, berekend) | RGE,excess​ | RS\&P500,excess​ |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 07/01/2000 | \-2.22% | \-1.89% | 5.74% 8 | 0.107% | \-2.327% | \-1.997% |
| 14/01/2000 | \-0.33% | 1.64% | 5.74% 8 | 0.107% | \-0.437% | 1.533% |
| ... | ... | ... | ... | ... | ... | ... |

### **3.5. Stap 5: De Echte Analyse (Het Testen van CAPM)**

* Voer de *nieuwe* regressie uit (SCL) met de *excess* return kolommen.  
* Vergelijk de *nieuwe* $\\beta$ en $\\alpha$ met de oude.  
* Focus op de *nieuwe* $\\alpha$ (Jensen's Alpha). Kijk naar de **p-waarde** van deze intercept (Deel 1.3).  
* Stel de hamvraag: "Is de $\\alpha$ significant verschillend van nul?".4  
* *Discussie:* Wat betekent dit? Heeft GE waarde gecreëerd of vernietigd op een risicogecorrigeerde basis?

### **3.6. Stap 6: De Kritische Reflectie (De "Reality Check")**

* Integreer **Suggestie 2.2 (OLS Aannames)**: "Mogen we de p-waarde uit Stap 5 wel vertrouwen?" Wijs op de volatiliteitsclustering (heteroscedasticiteit) in de data.1  
* Integreer **Suggestie 2.3 (Beta Stabiliteit)**: "Is deze $\\beta$ wel stabiel over 20 jaar?" Laat ze de gesplitste regressie (2000-2009 vs 2010-2019) uitvoeren.11  
* Integreer **Suggestie 2.4 (CAPM Aannames)**: "En moeten we dit *economische* model überhaupt geloven?".12

## **Deel 4: Conclusies en Aanbevelingen**

De huidige aanpak (het Market Model) is een uitstekend *startpunt*. Het is echter methodologisch en conceptueel onvolledig om dit direct als een demonstratie van het CAPM te presenteren.

De verrijking zit in één cruciale aanpassing: de overstap van *ruwe (totale) returns* naar *excess returns* (returns minus $R\_f$). Deze enkele aanpassing transformeert de lesmodule fundamenteel:

1. Het verandert van een simpele *statistische fit* in een *economische theorietest*.  
2. Het geeft de **intercept ($\\alpha$)** een krachtige betekenis (Jensen's Alpha), wat de kern van prestatieanalyse is.4  
3. Het geeft de **R-kwadraat ($R^2$)** een diepere financiële betekenis (risicodecompositie en diversificatie).  
4. Het creëert een noodzaak voor een praktische *dataverwerkings-oefening* (het vinden en omzetten van $R\_f$).  
5. Het opent de deur naar een *kritische analyse* van zowel de statistische aannames (heteroscedasticiteit) als de economische aannames (onrealistisch).

Door deze voorgestelde stappen te volgen, worden de twee losse onderwerpen (lineaire regressie en CAPM) één geïntegreerd, krachtig en kritisch analyse-instrument. Studenten leren niet alleen het model toe te passen, maar ook de data te prepareren, de statistische validiteit te bevragen en de onderliggende economische theorie te bekritiseren. Dit sluit perfect aan bij de eindtermen van een HBO Bedrijfskunde-opleiding.

#### **Works cited**

1. Risico en rendement \- uitwerking GE \- Returns.pdf  
2. Lecture 8 CAPM as a Regression, accessed on November 9, 2025, [https://www.bauer.uh.edu/rsusmel/phd/lecture%208.pdf](https://www.bauer.uh.edu/rsusmel/phd/lecture%208.pdf)  
3. Capital asset pricing model \- Wikipedia, accessed on November 9, 2025, [https://en.wikipedia.org/wiki/Capital\_asset\_pricing\_model](https://en.wikipedia.org/wiki/Capital_asset_pricing_model)  
4. CAPM \- Expected vs. actual returns \- Quantitative Finance Stack Exchange, accessed on November 9, 2025, [https://quant.stackexchange.com/questions/47248/capm-expected-vs-actual-returns](https://quant.stackexchange.com/questions/47248/capm-expected-vs-actual-returns)  
5. Table Data \- 3-Month Treasury Bill Secondary Market Rate, Discount Basis \- FRED, accessed on November 9, 2025, [https://fred.stlouisfed.org/data/tb3ms](https://fred.stlouisfed.org/data/tb3ms)  
6. Interest Rate, Treasury, 3-Month \- Economic Data Series | FRED | St. Louis Fed, accessed on November 9, 2025, [https://fred.stlouisfed.org/tags/series?t=3-month%3Binterest+rate%3Btreasury](https://fred.stlouisfed.org/tags/series?t=3-month;interest+rate;treasury)  
7. Interest Rate Statistics | U.S. Department of the Treasury, accessed on November 9, 2025, [https://home.treasury.gov/policy-issues/financing-the-government/interest-rate-statistics](https://home.treasury.gov/policy-issues/financing-the-government/interest-rate-statistics)  
8. 3-Month Treasury Bill Rate: Auction Average (DISCONTINUED) (TB3MA) \- FRED, accessed on November 9, 2025, [https://fred.stlouisfed.org/series/TB3MA](https://fred.stlouisfed.org/series/TB3MA)  
9. Gevolg van verschil in aannames tussen OLS en MLE voor lineaire regressie \- Reddit, accessed on November 9, 2025, [https://www.reddit.com/r/AskStatistics/comments/u7ftbh/consequence\_of\_difference\_in\_assumptions\_between/?tl=nl](https://www.reddit.com/r/AskStatistics/comments/u7ftbh/consequence_of_difference_in_assumptions_between/?tl=nl)  
10. Linear Regression Assumptions: 7 assumpties bij lineaire regressie \- Data Science Partners, accessed on November 9, 2025, [https://datasciencepartners.nl/linear-regression-assumptions/](https://datasciencepartners.nl/linear-regression-assumptions/)  
11. Capital Asset Pricing Model (CAPM): Meaning & Assumptions \- CoinSwitch, accessed on November 9, 2025, [https://coinswitch.co/switch/personal-finance/capital-asset-pricing-model/](https://coinswitch.co/switch/personal-finance/capital-asset-pricing-model/)  
12. Capital Asset Pricing Model (CAPM): Definition & Formula \- Trading 212, accessed on November 9, 2025, [https://www.trading212.com/learn/investing-101/capital-asset-pricing-model-capm](https://www.trading212.com/learn/investing-101/capital-asset-pricing-model-capm)  
13. The capital asset pricing model – part 3 \- ACCA Global, accessed on November 9, 2025, [https://www.accaglobal.com/gb/en/student/exam-support-resources/fundamentals-exams-study-resources/f9/technical-articles/CAPM-theory.html](https://www.accaglobal.com/gb/en/student/exam-support-resources/fundamentals-exams-study-resources/f9/technical-articles/CAPM-theory.html)  
14. Understanding the CAPM: Key Formula, Assumptions, and Applications \- Investopedia, accessed on November 9, 2025, [https://www.investopedia.com/terms/c/capm.asp](https://www.investopedia.com/terms/c/capm.asp)  
15. (PDF) The Limitaitons and Alternatives of CAPM \- ResearchGate, accessed on November 9, 2025, [https://www.researchgate.net/publication/377180000\_The\_Limitaitons\_and\_Alternatives\_of\_CAPM](https://www.researchgate.net/publication/377180000_The_Limitaitons_and_Alternatives_of_CAPM)