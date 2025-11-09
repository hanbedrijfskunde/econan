# Conventional Tools Path: Gids voor Data-Analyse Tools

**Versie**: 1.0
**Datum**: 9 November 2025
**Doel**: Tool tutorials en workflows voor Junior Analisten die conventionele data-analyse tools gebruiken

---

## Introductie

Als Business Analyst die het **Conventional Tools Path** kiest, werk je hands-on met data-analyse tools zoals Power BI, Tableau, Python, of R. Deze gids helpt je de juiste tool te kiezen en effectief in te zetten door de CRISP-DM systematiek.

### Belangrijke Principes

1. **Tool is middel, niet doel**: Focus op CRISP-DM proces, niet op "coolste feature"
2. **Start simple, scale up**: Begin met basis functionaliteit, voeg complexity toe als nodig
3. **Reproducibility**: Documenteer je stappen zodat anderen (en jijzelf over 3 weken) kunnen volgen
4. **Business-first**: Elke technische keuze moet business rationale hebben

---

## Tool Selectie Matrix

### Overzicht Tools per Use Case

| **Tool** | **Beste Voor** | **Leercurve** | **Visualisatie** | **Modeling** | **Automation** | **Cost** |
|----------|----------------|---------------|------------------|--------------|----------------|----------|
| **Power BI** | Business dashboards, interactieve rapporten | Middel | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | Gratis (Desktop) |
| **Tableau** | Executive dashboards, storytelling | Middel | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | Student license |
| **Python (Pandas/Matplotlib)** | Data wrangling, custom analysis | Hoog | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Gratis |
| **R (Tidyverse/ggplot2)** | Statistical analysis, academic rigor | Hoog | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Gratis |
| **Excel (Advanced)** | Quick analysis, tabular data | Laag | ⭐⭐ | ⭐⭐ | ⭐⭐ | Microsoft 365 |

### Keuze Hulp: Welke Tool Voor Jou?

#### Kies **Power BI** als:
- ✅ Je prioriteit is: Interactieve dashboards voor stakeholders
- ✅ Je wilt: Drag-and-drop interface (minder coding)
- ✅ Je complexity level: Foundation of Analytical
- ✅ Je Senior verwacht: Visueel aantrekkelijk dashboard

#### Kies **Tableau** als:
- ✅ Je prioriteit is: Storytelling met data (presentatie-focus)
- ✅ Je wilt: Beste-in-class visualisaties
- ✅ Je complexity level: Foundation of Analytical
- ✅ Je Senior verwacht: Executive summary met visuals

#### Kies **Python** als:
- ✅ Je prioriteit is: Flexibiliteit en custom analysis
- ✅ Je wilt: Leren programmeren (toekomstbestendig)
- ✅ Je complexity level: Analytical of Advanced
- ✅ Je Senior verwacht: Diepgaande statistische analyse

#### Kies **R** als:
- ✅ Je prioriteit is: Statistical rigor (p-values, confidence intervals)
- ✅ Je wilt: Academic-grade analysis
- ✅ Je complexity level: Analytical of Advanced
- ✅ Je Senior verwacht: Peer-review kwaliteit insights

#### Kies **Excel** als:
- ✅ Je prioriteit is: Snelheid (quick & dirty analysis)
- ✅ Je wilt: Tool die je al kent
- ✅ Je complexity level: Foundation
- ✅ Je Senior verwacht: Simpel, direct antwoord

---

## CRISP-DM Workflows per Tool

---

## 1. Power BI Workflow

### Setup (Eenmalig, ~30 min)

**Download & Install**:
- Windows: https://aka.ms/pbidesktop
- Mac: Gebruik Power BI Service (web) of Parallels/Bootcamp

**Initial Configuration**:
```
1. Open Power BI Desktop
2. File → Options → Data Load
   - ✅ Type detection for unstructured sources (aan)
   - ✅ Default to relationship detection (aan)
3. View → Query Editor → Enable Preview features
   - ✅ Enhanced dataset metadata (aan)
```

---

### Fase 1: Business Understanding (in Power BI)

**Doel**: Vertaal strategische vraag naar data model

**Stappen**:
1. **Stakeholder Interview Notes** (in OneNote/Word, niet Power BI):
   - Wat is de strategische vraag?
   - Welke KPIs zijn relevant?
   - Hoe ziet de ideale output eruit? (sketch met pen & paper!)

2. **Data Model Design** (op papier eerst!):
   - Welke tabellen heb ik nodig?
   - Hoe relateren ze? (1-to-many, many-to-many)
   - Welke calculated columns/measures?

**Output**: Data model diagram (scan en voeg toe aan documentatie)

---

### Fase 2: Data Understanding (Power Query)

**Stappen**:

1. **Data Importeren**:
```
Home → Get Data → [bron type]
Ondersteunde bronnen:
- Excel/CSV: Voor files
- SQL Database: Voor enterprise data
- Web: Voor online datasets
- Folder: Voor meerdere files tegelijk
```

2. **Initial Exploration** (in Query Editor):
```
Transform tab:
- Data type check: Kloppen de types? (text vs. number vs. date)
- Column distribution: Zie je outliers/missing values?
- Column quality: Hoeveel % valid/error/empty?
- Column profile: Min/max/mean stats
```

3. **Data Profiling Checklist**:
```
Voor elke belangrijke kolom:
□ Data type correct?
□ Missing values aanwezig? Hoeveel %?
□ Outliers zichtbaar in distributie?
□ Dubbele waarden (indien niet verwacht)?
□ Format consistent? (bijv. datum: DD-MM vs MM-DD)
```

**Output**: Screenshot van data profiling + notes over quality issues

---

### Fase 3: Data Preparation (Power Query)

**Stappen**:

1. **Cleaning Steps** (Query Editor):

```text
Typische transformaties:

a) Missing Values Behandelen:
   - Remove Rows → Remove Errors (als weinig missings)
   - Replace Values → null met [0 of gemiddelde] (documenteer keuze!)
   - Fill Down/Up (voor time series met repeated values)

b) Data Type Conversie:
   - Change Type → naar correct type (ALTIJD doen vóór calculations!)

c) Text Cleaning:
   - Transform → Trim (verwijder spaties begin/eind)
   - Transform → Clean (verwijder non-printable chars)
   - Transform → Uppercase/Lowercase/Capitalize (consistentie)

d) Dubbele Rijen:
   - Remove Rows → Remove Duplicates (op key kolommen)

e) Filteren:
   - Filter rows waar [conditie]
   - Bijvoorbeeld: Verwijder test data, outliers (MET rationale!)
```

**Voorbeeld: Retail Sales Cleaning**:
```text
Applied Steps (zichtbaar in Query Editor rechterpanel):
1. Source (geïmporteerde data)
2. Changed Type (datum naar Date, sales naar Currency)
3. Filtered Rows (removed null Sales)
4. Removed Errors (in Product ID kolom)
5. Trimmed Text (Product Name)
6. Removed Duplicates (op Transaction ID)
```

2. **Feature Engineering** (Add Column tab):

```text
Nieuwe kolommen maken:

a) Conditional Column:
   IF-THEN logic via GUI
   Voorbeeld: IF Sales > 1000 THEN "High" ELSE "Low"

b) Custom Column (M language):
   [Unit Price] * [Quantity]
   Text.Length([Product Name])
   Date.Year([Order Date])

c) Merge Queries (joins):
   Home → Merge Queries → Select tables + join keys

d) Append Queries (union):
   Home → Append Queries → Combine meerdere tables
```

**Foundation Level Features** (max 7.0):
- Ratios: [Gross Margin] = [Revenue] - [Cost]
- Categories: IF Sales > threshold THEN "High"
- Time extracts: Year, Month, Quarter van datum

**Analytical Level Features** (max 8.5):
- Running totals: CALCULATE(SUM(Sales), FILTER(...))
- YoY Growth: (This Year - Last Year) / Last Year
- Moving averages: 3-month rolling average

**Advanced Level Features** (max 10):
- Complex DAX: RANKX, SWITCH, time intelligence
- Calculated tables voor scenario modeling

**Output**:
- Query dependencies diagram (View → Query Dependencies)
- Documentatie: "Applied Steps" lijst met rationale per step

---

### Fase 4: Modeling (Relationships & DAX)

**Stappen**:

1. **Relationships Definiëren**:
```
Model view → Drag lines tussen tables
Configuratie:
- Cardinality: Usually 1-to-Many (dimension → fact)
- Cross filter direction: Single (meest gebruikt)
- Active: ✅ (tenzij je multiple relationships hebt)
```

**Voorbeeld Data Model: Retail**:
```
Sales (fact)
├── 1:Many → Products (dimension) via Product ID
├── 1:Many → Customers (dimension) via Customer ID
└── 1:Many → Calendar (dimension) via Order Date

Best practice: Star schema (1 fact, meerdere dimensions)
```

2. **Measures Creëren** (DAX):

```dax
-- Foundation Level: Basis aggregaties

Total Sales = SUM(Sales[Amount])

Avg Order Value = AVERAGE(Sales[Amount])

Transaction Count = COUNTROWS(Sales)

-- Analytical Level: Time intelligence

Sales YTD = TOTALYTD([Total Sales], Calendar[Date])

Sales Last Year = CALCULATE([Total Sales], SAMEPERIODLASTYEAR(Calendar[Date]))

YoY Growth % =
DIVIDE(
    [Total Sales] - [Sales Last Year],
    [Sales Last Year],
    0
)

-- Advanced Level: Complex logic

Customer Lifetime Value =
SUMX(
    VALUES(Customers[Customer ID]),
    CALCULATE(
        [Total Sales],
        FILTER(
            ALL(Calendar),
            Calendar[Date] <= MAX(Calendar[Date])
        )
    )
)

Market Share % =
DIVIDE(
    [Total Sales],
    CALCULATE([Total Sales], ALL(Products[Category]))
)
```

**DAX Best Practices**:
- Gebruik DIVIDE() niet `/` (voorkomt divide-by-zero errors)
- Format measures met Currency/Percentage (niet manual "€ " toevoegen)
- Groupeer measures in Display Folders (Model view → properties)

**Output**:
- Measures lijst met formules (screenshot)
- Data model diagram (export als image)

---

### Fase 5: Visualization (Report View)

**Stappen**:

1. **Visual Selectie per Finding**:

| **Finding Type** | **Best Visual** | **Wanneer Gebruiken** |
|------------------|-----------------|----------------------|
| Vergelijking (A vs B) | Bar chart | Vergelijk categorieën (bijv. sales per product) |
| Trend over tijd | Line chart | Toon ontwikkeling (bijv. monthly revenue) |
| Compositie (parts of whole) | Pie/Donut chart | Aandelen (bijv. market share) |
| Distributie | Histogram | Spreiding data (bijv. order values) |
| Correlatie | Scatter plot | Relatie 2 variabelen (bijv. price vs. sales) |
| KPI tracking | Card/Gauge | Enkele metric (bijv. "Total Revenue: €1.2M") |
| Geographical | Map | Locatie data (bijv. sales per region) |
| Ranking | Table met bars | Top 10 products, customers, etc. |

2. **Dashboard Layout Principes**:

```
Page Layout Best Practices:

Top:
- Filters (slicers): Date range, Category, Region
- KPI Cards: 3-5 key metrics (Total Sales, Avg Order, Growth %)

Middle:
- Main Insight: Grootste/belangrijkste chart (50% van ruimte)
  Voorbeeld: Monthly sales trend line chart

Bottom:
- Supporting Insights: 2-3 kleinere charts
  Voorbeeld: Top 10 products (bar), Sales by region (map)

Sidebar (rechts):
- Actions: Drill-through buttons, bookmarks
```

**Foundation Level Dashboard** (max 7.0):
- 3-5 visuals
- Basis chart types (bar, line, pie)
- Duidelijke labels en títels
- 1 page

**Analytical Level Dashboard** (max 8.5):
- 5-8 visuals
- Drill-down functionaliteit
- Cross-filtering tussen visuals
- Tooltips met extra context
- 2-3 pages (overview + deep dives)

**Advanced Level Dashboard** (max 10):
- 8+ visuals
- Bookmarks voor scenarios
- Custom visuals (R/Python integration)
- Mobile layout
- Dynamic titles (DAX in title)

3. **Visual Formatting Tips**:

```
Elke visual MOET hebben:
□ Title: "Wat is de conclusie?" (niet "Chart 1")
□ Axis labels: Duidelijk wat X en Y betekenen
□ Data labels: Toon waarden (indien niet te druk)
□ Colors: Consistent (bijv. rood = negatief, groen = positief)
□ Tooltips: Extra context bij hover
```

**Output**:
- Power BI .pbix file
- Export als PDF (File → Export → PDF) voor presentatie

---

### Fase 6: Deployment & Iteration

**Stappen**:

1. **Performance Optimization**:
```
Query Editor → Advanced Editor
Check:
- Zijn er onnodige stappen? (Remove via X)
- Kan ik queries combineren? (merge ipv 2 aparte imports)
- Gebruik ik alleen nodige kolommen? (Remove Columns voor rest)
```

2. **Documentatie**:
```
In Power BI:
- Measure beschrijvingen: Right-click measure → Properties → Description
- Table descriptions: Model view → Properties panel

Extern (Word/Markdown):
- Data sources gebruikt
- Cleaning decisions rationale
- Key assumptions
- Known limitations
```

3. **Presentatie Prep**:
```
Reading View (niet Edit mode tijdens presentatie!)
Presentatie Tips:
- Start met Page 1 (Overview)
- Gebruik slicers live (toon interactiviteit)
- Drill-down in charts (right-click → Drill down)
- Highlight specifieke data point (ctrl+click)
```

**Output**:
- Final .pbix file
- Exported PDF
- Documentatie document

---

## 2. Python Workflow (Pandas + Matplotlib)

### Setup (Eenmalig, ~45 min)

**Install Anaconda** (recommended):
- Download: https://www.anaconda.com/download
- Includes: Python, Jupyter, Pandas, NumPy, Matplotlib, Scikit-learn

**Alternative: Python + pip**:
```bash
# Install Python 3.11+ from python.org
# Then install packages:
pip install pandas matplotlib seaborn jupyter scikit-learn
```

**IDE Keuze**:
- **Jupyter Notebook**: Best voor exploratie & documentatie (aanbevolen voor ECONAN)
- **VS Code**: Best voor scripts & automation
- **PyCharm**: Best voor advanced development

---

### Fase 1-2: Business & Data Understanding (Python)

**Create Jupyter Notebook**: `econan_analysis.ipynb`

```python
# Cell 1: Imports & Setup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuratie
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")
%matplotlib inline

# Cell 2: Business Context (Markdown cell!)
"""
# ECONAN Analyse: [Sector] - [Strategische Vraag]

**Stakeholder**: [Rol - CEO/CFO/etc.]

**Strategische Vraag**:
> [Quote van Senior stakeholder]

**Sub-vragen**:
1. [Sub-vraag 1]
2. [Sub-vraag 2]
3. [Sub-vraag 3]

**Success Criteria**:
- [Wat moet ik aantonen?]
"""

# Cell 3: Data Import
# Voor CSV:
df = pd.read_csv('data/sales_data.csv', parse_dates=['Order_Date'])

# Voor Excel:
df = pd.read_excel('data/sales_data.xlsx', sheet_name='Sales')

# Voor meerdere files:
import glob
files = glob.glob('data/*.csv')
df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

# Cell 4: Initial Exploration
print("Dataset Shape:", df.shape)
print("\nColumn Types:\n", df.dtypes)
print("\nFirst 5 rows:\n", df.head())
print("\nBasic Stats:\n", df.describe())
print("\nMissing Values:\n", df.isnull().sum())
```

**Output**:
- Jupyter notebook met business context
- Data profiling summary

---

### Fase 3: Data Preparation (Pandas)

```python
# Cell 5: Data Cleaning

# a) Handle Missing Values
# Option 1: Drop rows with any missing
df_clean = df.dropna()

# Option 2: Drop rows with missing in specific columns
df_clean = df.dropna(subset=['Sales', 'Product_ID'])

# Option 3: Impute missing values
df['Sales'].fillna(df['Sales'].median(), inplace=True)

# DOCUMENTEER je keuze:
"""
**Cleaning Decision**: Dropped rows with missing Sales (234 rows, 2.3% of data)
**Rationale**: Sales is critical for analysis; imputation would introduce bias
**Impact**: Sample size reduced from 10,000 to 9,766
"""

# b) Data Type Conversion
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Product_ID'] = df['Product_ID'].astype(str)
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')

# c) Remove Duplicates
df_clean = df.drop_duplicates(subset=['Transaction_ID'], keep='first')

# d) Outlier Detection & Treatment
# Method 1: IQR method
Q1 = df['Sales'].quantile(0.25)
Q3 = df['Sales'].quantile(0.75)
IQR = Q3 - Q1
outliers = (df['Sales'] < Q1 - 1.5*IQR) | (df['Sales'] > Q3 + 1.5*IQR)
print(f"Outliers detected: {outliers.sum()} ({outliers.sum()/len(df)*100:.1f}%)")

# Treatment options:
# Option A: Remove
df_clean = df[~outliers]
# Option B: Cap (winsorize)
df.loc[df['Sales'] > Q3 + 1.5*IQR, 'Sales'] = Q3 + 1.5*IQR

# Cell 6: Feature Engineering

# Foundation Level Features
df['Gross_Margin'] = df['Revenue'] - df['Cost']
df['Margin_Percent'] = (df['Gross_Margin'] / df['Revenue']) * 100
df['Year'] = df['Order_Date'].dt.year
df['Month'] = df['Order_Date'].dt.month
df['Quarter'] = df['Order_Date'].dt.quarter

# Analytical Level Features
# YoY Growth
df_yearly = df.groupby('Year')['Sales'].sum().reset_index()
df_yearly['YoY_Growth'] = df_yearly['Sales'].pct_change() * 100

# Moving Average (3-month)
df['Sales_MA3'] = df.groupby('Product_ID')['Sales'].transform(
    lambda x: x.rolling(window=3, min_periods=1).mean()
)

# Advanced Level Features
# Customer Lifetime Value (CLV)
customer_clv = df.groupby('Customer_ID').agg({
    'Sales': 'sum',
    'Order_Date': lambda x: (x.max() - x.min()).days,
    'Transaction_ID': 'count'
}).rename(columns={'Transaction_ID': 'Frequency'})
customer_clv['CLV'] = customer_clv['Sales'] / (customer_clv['Order_Date'] / 365)

# Cell 7: Data Quality Report
"""
## Data Quality Summary

**Original Dataset**: {df.shape[0]} rows, {df.shape[1]} columns
**After Cleaning**: {df_clean.shape[0]} rows ({(df_clean.shape[0]/df.shape[0])*100:.1f}% retained)

**Key Transformations**:
1. Dropped {outliers.sum()} outliers in Sales (beyond 1.5 IQR)
2. Filled {df['Sales'].isnull().sum()} missing Sales values with median
3. Converted Order_Date to datetime format
4. Created 5 new features: [list]
"""
```

**Output**:
- Clean dataset: `df_clean`
- Feature engineering code met documentatie
- Quality report (markdown cell)

---

### Fase 4: Modeling & Analysis (Pandas + Scikit-learn)

```python
# Cell 8: Descriptive Analysis (Foundation Level)

# Aggregations
summary_stats = df.groupby('Product_Category').agg({
    'Sales': ['sum', 'mean', 'count'],
    'Gross_Margin': 'mean'
}).round(2)

print("Summary by Category:\n", summary_stats)

# Pivot tables
pivot = df.pivot_table(
    values='Sales',
    index='Product_Category',
    columns='Year',
    aggfunc='sum',
    fill_value=0
)
print("\nSales by Category & Year:\n", pivot)

# Cell 9: Correlation Analysis (Analytical Level)

# Correlation matrix
corr_matrix = df[['Sales', 'Price', 'Quantity', 'Discount']].corr()
print("Correlation Matrix:\n", corr_matrix)

# Visualize correlation
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Between Variables')
plt.show()

# Cell 10: Regression Analysis (Analytical/Advanced Level)

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error

# Prepare data
X = df[['Price', 'Discount', 'Marketing_Spend']]
y = df['Sales']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"Model Performance:")
print(f"R² Score: {r2:.3f}")
print(f"Mean Absolute Error: €{mae:.2f}")
print(f"\nCoefficients:")
for feature, coef in zip(X.columns, model.coef_):
    print(f"{feature}: {coef:.2f}")

# Cell 11: Scenario Analysis (Advanced Level)

# Define scenarios
scenarios = {
    'Base Case': {'Price': 100, 'Discount': 0.10, 'Marketing_Spend': 5000},
    'Scenario A - Premium': {'Price': 120, 'Discount': 0.05, 'Marketing_Spend': 7000},
    'Scenario B - Volume': {'Price': 80, 'Discount': 0.20, 'Marketing_Spend': 3000}
}

results = {}
for name, params in scenarios.items():
    X_scenario = pd.DataFrame([params])
    predicted_sales = model.predict(X_scenario)[0]
    results[name] = predicted_sales

scenario_df = pd.DataFrame(list(results.items()), columns=['Scenario', 'Predicted_Sales'])
print("\nScenario Analysis:\n", scenario_df)
```

**Output**:
- Statistical analysis results
- Model performance metrics
- Scenario predictions

---

### Fase 5: Visualization (Matplotlib + Seaborn)

```python
# Cell 12: Visualizations for Stakeholder

# 1. Time Series (Trend)
plt.figure(figsize=(12, 6))
monthly_sales = df.groupby(df['Order_Date'].dt.to_period('M'))['Sales'].sum()
monthly_sales.plot(linewidth=2, marker='o')
plt.title('Monthly Sales Trend', fontsize=16, fontweight='bold')
plt.xlabel('Month')
plt.ylabel('Sales (€)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('outputs/monthly_trend.png', dpi=300)
plt.show()

# 2. Category Comparison (Bar Chart)
plt.figure(figsize=(10, 6))
category_sales = df.groupby('Product_Category')['Sales'].sum().sort_values(ascending=False)
category_sales.plot(kind='barh', color='steelblue')
plt.title('Sales by Product Category', fontsize=16, fontweight='bold')
plt.xlabel('Total Sales (€)')
plt.ylabel('Category')
for i, v in enumerate(category_sales):
    plt.text(v, i, f' €{v:,.0f}', va='center')
plt.tight_layout()
plt.savefig('outputs/category_sales.png', dpi=300)
plt.show()

# 3. Distribution (Histogram)
plt.figure(figsize=(10, 6))
plt.hist(df['Sales'], bins=50, edgecolor='black', alpha=0.7)
plt.axvline(df['Sales'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: €{df["Sales"].mean():.0f}')
plt.axvline(df['Sales'].median(), color='green', linestyle='--', linewidth=2, label=f'Median: €{df["Sales"].median():.0f}')
plt.title('Distribution of Order Values', fontsize=16, fontweight='bold')
plt.xlabel('Sales (€)')
plt.ylabel('Frequency')
plt.legend()
plt.tight_layout()
plt.savefig('outputs/sales_distribution.png', dpi=300)
plt.show()

# 4. Scatter Plot (Correlation)
plt.figure(figsize=(10, 6))
plt.scatter(df['Price'], df['Sales'], alpha=0.5)
plt.title('Price vs. Sales', fontsize=16, fontweight='bold')
plt.xlabel('Price (€)')
plt.ylabel('Sales (units)')
# Add trendline
z = np.polyfit(df['Price'], df['Sales'], 1)
p = np.poly1d(z)
plt.plot(df['Price'], p(df['Price']), "r--", linewidth=2, label='Trendline')
plt.legend()
plt.tight_layout()
plt.savefig('outputs/price_vs_sales.png', dpi=300)
plt.show()

# 5. Heatmap (for correlation or pivot)
plt.figure(figsize=(10, 6))
pivot_data = df.pivot_table(values='Sales', index='Month', columns='Year', aggfunc='sum')
sns.heatmap(pivot_data, annot=True, fmt='.0f', cmap='YlGnBu')
plt.title('Monthly Sales Heatmap by Year', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('outputs/sales_heatmap.png', dpi=300)
plt.show()
```

**Output**:
- High-quality PNG exports (300 DPI)
- Saved in `/outputs/` folder
- Ready for presentation slides

---

### Fase 6: Deployment & Reporting

```python
# Cell 13: Generate Executive Summary

summary_report = f"""
# Executive Summary: {strategic_question}

**Analyst**: [Your Name]
**Date**: {pd.Timestamp.now().strftime('%Y-%m-%d')}
**Stakeholder**: [Role]

## Key Findings

1. **[Finding 1]**: [Insight with number]
   - Supporting data: [Metric]
   - Business impact: [What does this mean?]

2. **[Finding 2]**: [Insight with number]
   - Supporting data: [Metric]
   - Business impact: [What does this mean?]

3. **[Finding 3]**: [Insight with number]
   - Supporting data: [Metric]
   - Business impact: [What does this mean?]

## Recommendation

Based on the analysis, I recommend **[Option A/B]** because:
- [Reason 1 with data support]
- [Reason 2 with data support]
- [Reason 3 with data support]

## Risks & Mitigation

- **Risk 1**: [Description] → **Mitigation**: [How to reduce]
- **Risk 2**: [Description] → **Mitigation**: [How to reduce]

## Next Steps

1. [Action 1] - Owner: [Who] - Timeline: [When]
2. [Action 2] - Owner: [Who] - Timeline: [When]

---
*Analysis conducted using Python (Pandas, Scikit-learn) following CRISP-DM methodology*
"""

with open('outputs/executive_summary.md', 'w') as f:
    f.write(summary_report)

print("Executive summary saved to outputs/executive_summary.md")

# Cell 14: Export Results

# Export cleaned data
df_clean.to_csv('outputs/cleaned_data.csv', index=False)

# Export key tables
summary_stats.to_excel('outputs/summary_tables.xlsx', sheet_name='Category Stats')

# Export model artifacts (if using ML)
import joblib
joblib.dump(model, 'outputs/sales_model.pkl')

print("All artifacts exported to /outputs/")
```

**Final Deliverables**:
- Jupyter Notebook (`econan_analysis.ipynb`)
- Exported visualizations (PNG files)
- Executive summary (Markdown/PDF)
- Clean dataset (CSV)
- Model artifacts (if applicable)

---

## 3. Quick Reference: Tool Comparison

### When to Use Which Tool

| **Task** | **Power BI** | **Python** | **R** | **Excel** |
|----------|-------------|-----------|-------|----------|
| Interactive dashboard | ✅ Best | ❌ No | ❌ No | ⚠️ Limited |
| Statistical modeling | ⚠️ Basic | ✅ Best | ✅ Best | ❌ No |
| Large datasets (>1M rows) | ✅ Yes | ✅ Yes | ⚠️ Slower | ❌ No |
| Reproducibility | ✅ Good | ✅ Excellent | ✅ Excellent | ⚠️ Manual |
| Learning curve | ⚠️ Medium | ❌ High | ❌ High | ✅ Low |
| Presentation-ready | ✅ Yes | ⚠️ Needs export | ⚠️ Needs export | ✅ Yes |
| Automation | ✅ Yes (scheduled refresh) | ✅ Yes (scripts) | ✅ Yes (Rmd) | ⚠️ Macros |

---

## Common Pitfalls & Solutions

### ❌ Pitfall 1: "Tool Overcomplication"
**Probleem**: Gebruik van advanced features die je niet begrijpt
**Oplossing**: Start simple - Foundation features zijn vaak voldoende

### ❌ Pitfall 2: "Black Box Syndrome"
**Probleem**: Weet niet wat tool achter de schermen doet
**Oplossing**: Valideer output met manual calculation (sample check)

### ❌ Pitfall 3: "Visualization Overload"
**Probleem**: Te veel charts zonder duidelijke conclusie
**Oplossing**: 1 chart = 1 insight. Elke visual moet vraag beantwoorden

### ❌ Pitfall 4: "Undocumented Assumptions"
**Probleem**: Cleaning/transformation keuzes niet gedocumenteerd
**Oplossing**: Elke beslissing = comment in code / note in Power Query

### ❌ Pitfall 5: "Ignoring Data Quality"
**Probleem**: Direct modelleren zonder data understanding
**Oplossing**: Spend 30% tijd op data profiling en cleaning

---

## Resources

### Learning Resources

**Power BI**:
- Microsoft Learn: https://learn.microsoft.com/training/powerbi/
- Guy in a Cube (YouTube): https://youtube.com/@GuyInACube
- SQLBI (advanced DAX): https://www.sqlbi.com

**Python**:
- Pandas documentation: https://pandas.pydata.org/docs/
- Kaggle Learn: https://www.kaggle.com/learn
- Real Python: https://realpython.com

**R**:
- R for Data Science: https://r4ds.hadley.nz
- Tidyverse: https://www.tidyverse.org
- RStudio Primers: https://posit.cloud/learn/primers

### ECONAN Specific
- AI Path comparison: `/docs/materiaal/ai-pad.html`
- Assessment rubric: `/docs/assessment/rubric.html`
- Sector datasets: [TBD - per sector page]

### Office Hours
- Power BI Clinic: [Week 2, 5 - zie weekplanning]
- Python Help: [Week 3, 6 - zie weekplanning]

---

## Assessment Tips

**Voor Criterium B-C-D (Technical Execution)**:
- ✅ Document je cleaning rationale (niet alleen "wat" maar "waarom")
- ✅ Validate je results (manual check op sample data)
- ✅ Comment je code / annotate Power Query steps
- ✅ Export intermediate artifacts (cleaned data, model metrics)

**Voor Criterium F (Autonomy & Onderbouwing)**:
- ✅ Explain tool choice: "Ik koos Python omdat [rationale]"
- ✅ Alternative considered: "Ik overwoog Tableau maar koos Python omdat [trade-off]"
- ✅ Complexity level match: "Ik target Analytical → dus ik gebruik regression, niet alleen descriptive stats"

**Voor Criterium G (Mastery & Groei)**:
- ✅ Show progression: v1 (basic chart) → v2 (refined chart) → v3 (final)
- ✅ Reflect on learning: "Eerste keer was ik [X], nu kan ik [Y]"
- ✅ Transfer potential: "Deze skill is toepasbaar in [future context]"

---

**Volgende Stap**:
1. Kies je tool (Power BI aanbevolen voor beginners)
2. Install & setup (30-45 min)
3. Start met Fase 1-2 (Business & Data Understanding)

**Need Help?**: Office hours & peer buddy system (zie weekplanning)

---

**Einde Document**
