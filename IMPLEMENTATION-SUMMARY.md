# ECONAN Module Herontwerp: Implementation Summary

**Versie**: 1.0 (LRD v3.0 - Hybrid Model)
**Datum**: 9 November 2025
**Status**: Klaar voor review en pilot implementatie

---

## Executive Summary

Het ECONAN module herontwerp is succesvol afgerond met de implementatie van een **hybride model** dat studenten maximale autonomie geeft terwijl Purpose en Mastery behouden blijven. De kern innovatie: **role-based team structure** (Senior stakeholders vs. Analists) gecombineerd met **methodology autonomy** (AI-augmented vs. Conventional tools).

### Key Deliverables Created

✅ **LRD v3.0** - Updated met Sections 2.4 & 2.5, volledige weekplanning, revised assessment
✅ **Sector Mapping** - 8 sectoren met 16 strategische vraagstukken (BEDROM → ECONAN)
✅ **Website Structure** - GitHub Pages ready met index.html + directory structuur
✅ **AI Path Materials** - Comprehensive prompt templates voor alle CRISP-DM fasen
✅ **Conventional Path Materials** - Power BI & Python workflows met voorbeelden

---

## 1. Core Concept: Hybrid Model

### What Changed from Original Plan

**Original LRD v2.0 Concept** (niet haalbaar):
- ❌ Echte externe opdrachtgevers (8 organisaties) → Logistiek complex, niet beschikbaar short-term
- ❌ Nieuwe assessment criteria E-F-G → Curriculum commissie goedkeuring vereist
- ❌ Homogene teams (iedereen zelfde rol) → Beperkte autonomy differentiation

**New LRD v3.0 Concept** (hybride model):
- ✅ **Simulatie met strategische vraagstukken** uit BEDROM sectoren
- ✅ **Role-based teams**: 1-2 Seniors (CEO/CFO/RvC) + 2-3 Analists (Analysts)
- ✅ **Dual methodology**: AI-augmented OF Conventional tools (keuze voor Analists)
- ✅ **Work within existing A-D criteria** maar prepare E-F-G als optionele extensie
- ✅ **BEDROM integration**: Leverage student prior knowledge from previous module

### PAM Framework Optimization

| **Dimension** | **How Achieved** | **Target Score** |
|---------------|------------------|------------------|
| **Purpose** | Real strategic decisions (rendement/risico/groei) from BEDROM sectors students already know | 5/5 |
| **Autonomy** | Triple choice: Sector + Role (Senior/Junior) + Methodology (AI/Conventional) | 5/5 |
| **Mastery** | Complexity levels (Foundation/Analytical/Advanced) + Role-specific growth | 5/5 |

---

## 2. LRD v3.0 Key Changes

### Section 2.4: Hybrid Methodology Requirements (NEW)

**LR-H1 through LR-H6** define:
- Dual methodology paths (AI vs Conventional) with equal rigor
- Different artifacts, same CRISP-DM assessment
- Guidance voor tool choice based on learning goals
- Cross-path learning opportunities (Week 4 methodology sharing)
- No methodology lock-in until Week 3
- Future-proof mindset: tools change, systematiek blijft

**Impact**: Junior analisten kunnen kiezen wat past bij hun leerdoel without penalty in grading.

---

### Section 2.5: Role-Based Team Structure Requirements (NEW)

**LR-R1 through LR-R8** define:
- Team composition: 4-5 studenten, 1-2 Seniors + 2-3 Analists
- Role responsibilities:
  - **Seniors**: Strategic question formulation, steer analysts, make decisions, lead presentation
  - **Analists**: CRISP-DM execution, methodology choice (AI/Conventional), analysis delivery
- Role-based assessment differentiation:
  - Seniors: zwaarder op Criterium A (Business Understanding) & E (Purpose)
  - Analists: zwaarder op Criteria B-C-D (technical execution) & G (Mastery)
- Real-world simulation fidelity (CEO/CFO/RvC roles uit rollen.md)

**Impact**: Studenten kunnen kiezen: "Wil ik strategisch leren (Senior) of technisch leren (Junior)?"

---

### Week 1-7 Structure Updates

All weekly plans updated to include:
- **Week 1**: +30 min Hybrid Methodology Intro, +20 min Role Structure uitleg, +25 min rol toewijzing
- **Week 2-3**: Parallel workshops (AI path vs Conventional path), role-specific activities
- **Week 4**: Cross-methodology learning (AI teams ↔ Conventional teams delen aanpak)
- **Week 5-6**: Methodology-specific office hours (AI prompting vs tool troubleshooting)
- **Week 7**: Methodology reflection panel + role-specific reflectie

**Total time**: Week 1 now ~4.5 uur (was 3.5) due to methodology and role introductions.

---

### Assessment Updates (Section 4)

**LR-AC1**: CRISP-DM criteria now **methodology-agnostic** and **role-differentiated**
- Criterium A: 60% weging Seniors, 40% Analists
- Criteria B-C: 80% weging Analists, 20% Seniors
- Criterium D: Equal weging (joint responsibility)

**LR-AC2**: PAM criteria E-F-G updated with role and methodology differentiation
- Note added: "Indien curriculum commissie niet akkoord, integreer in A-D"

**Key principle**: Process (CRISP-DM) > Tool (AI vs Conventional) in assessment

---

### Learning Materials (Section 6.2)

**LR-CM4** completely rewritten as **Dual-Path Learning Materials**:
- **AI-Augmented Path**:
  - Prompt Template Library (per CRISP-DM fase)
  - AI Tool Guides (ChatGPT, Claude)
  - Critical Evaluation Guide (validation techniques)
  - Example Prompt Logs
  - Video: "From business question to AI-driven insights"
- **Conventional Tools Path**:
  - Power BI guide (primary recommendation)
  - Alternative tools (Tableau, Python, R, Excel) quickstarts
  - CRISP-DM workflow per tool
- **Cross-Path Materials** (both):
  - Tool-agnostic CRISP-DM guide
  - Data interpretation guide
  - Stakeholder communication guide

---

## 3. BEDROM → ECONAN Sector Mapping

### Document Created: `bedrom-econan-sector-mapping.md`

**8 Sectors Mapped** with 2 strategische vraagstukken each (16 total):

1. **Retail (Fashion)**: Sustainable pricing, omnichannel expansion
2. **Energy (Renewable)**: Portfolio allocation, fossil fuel phase-out
3. **Financial Services**: Digital banking, loan portfolio risk
4. **Healthcare (Pharma)**: Drug portfolio prioritization, emerging market expansion
5. **Manufacturing (Automotive)**: EV portfolio shift, supply chain regionalization
6. **Food & Beverage**: Plant-based launch, private label competition
7. **Technology (SaaS)**: Freemium vs premium, geographic expansion
8. **Real Estate**: Office repositioning, green building investment

### Vraagstuk Structure

Each includes:
- **Rol context**: Which Senior stakeholder roles (CEO/CFO/RvC)
- **Strategische vraag**: Clear decision between Optie A vs B
- **Beslissing type**: Rendement/Risico/Groei classification
- **Data sources**: Realistic data types described
- **Analyse niveaus**: Foundation/Analytical/Advanced breakdown
- **BEDROM connectie**: Explicit link to prior module learnings

### Implementation Notes

For pilot (Semester 1):
- Select **5 sectoren** most popular from BEDROM
- Ensure real/realistic data available (partnerships or simulated)
- Create 1-pager per sector for Week 1 presentation (60 min activity)

---

## 4. GitHub Pages Website

### Structure Created: `/docs/`

**Core Pages**:
- ✅ `index.html` - Homepage met volledige overzicht (PAM, hybrid model, sectoren preview)
- ✅ `css/style.css` - Professional styling (Bootstrap 5.3 + custom)
- ✅ `README.md` - Website structure documentation + implementation plan

**Directory Structure**:
```
/docs/
├── rollen/          (Senior vs Junior rol details)
├── sectoren/        (8 sector pages met vraagstukken)
├── weekplanning/    (Week 1-7 detailed plans)
├── materiaal/       (AI + Conventional path materials)
└── assessment/      (Rubric, complexity levels)
```

### Design Principles

- **K.I.S.S.**: Plain HTML/CSS, no complex build process
- **Responsive**: Mobile-first, Bootstrap grid
- **Accessible**: Semantic HTML, ARIA labels
- **Professional Dutch**: All student-facing content

### Deployment Ready

- GitHub Pages compatible (static site)
- URL: `https://[username].github.io/econan/` or custom domain
- Auto-deploy on push to `main` branch

### Priority Pages for Week 1

**Must create before pilot**:
1. `rollen/index.html` - Rol overzicht (Senior vs Junior)
2. `sectoren/index.html` - Alle 8 sectoren listing
3. `weekplanning/index.html` - 7-weken structuur
4. `materiaal/index.html` - Materiaal hub

---

## 5. AI Path Materials

### Document Created: `ai-prompt-templates.md` (21,000+ words)

**Comprehensive templates for each CRISP-DM phase**:

1. **Business Understanding** (Templates 1.1-1.2):
   - Strategische vraag decompositie
   - Success criteria definitie

2. **Data Understanding** (Templates 2.1-2.2):
   - Data source exploratie
   - Data quality assessment

3. **Data Preparation** (Templates 3.1-3.2):
   - Data cleaning strategy
   - Feature engineering suggesties

4. **Modeling** (Templates 4.1-4.3):
   - Analysis method selectie
   - Results interpretation
   - Scenario analysis

5. **Evaluation** (Templates 5.1-5.2):
   - Model/analysis validatie
   - Alternative explanations (Devil's Advocate)

6. **Deployment** (Templates 6.1-6.2):
   - Strategische aanbeveling formulatie
   - Visualization advisory

**Meta-Prompts** (M.1-M.3):
- Iterative refinement techniques
- Assumption challenge prompts
- Expertise request framing

**Validation Checklist**:
- ✅ Relevantie, Correctheid, Compleetheid, Communicatie
- ⚠️ Red Flags: Hallucination, Overconfidence, Generic advice, Jargon overload

**Documentation Template**:
- Prompt log structure for assessment artifacts
- "What to log" guidelines (effective prompts, AI outputs, validation notes, refinements)

**Advanced Techniques**:
- Chain-of-Thought prompting
- Few-Shot learning
- Socratic prompting

**Common Pitfalls & Solutions**:
- 5 major pitfalls met concrete oplossingen

---

## 6. Conventional Tools Path Materials

### Document Created: `conventional-tools-guide.md` (18,000+ words)

**Tool Selection Matrix**:
- 5 tools compared: Power BI, Tableau, Python, R, Excel
- Rating per dimension (Visualisatie, Modeling, Automation, Cost)
- "Kies X als..." decision flowchart

**Detailed Workflows**:

### Power BI Workflow
- Setup & configuration (30 min)
- Full CRISP-DM implementation:
  - Business Understanding: Data model design
  - Data Understanding: Power Query profiling
  - Data Preparation: Cleaning + feature engineering in M/DAX
  - Modeling: Relationships + DAX measures (Foundation/Analytical/Advanced examples)
  - Visualization: Dashboard layout best practices, visual selection per finding type
  - Deployment: Performance optimization + documentation

**Foundation/Analytical/Advanced differentiation** voor elke fase.

### Python Workflow (Pandas + Matplotlib)
- Setup via Anaconda (45 min)
- Jupyter Notebook structure
- Full CRISP-DM code templates:
  - Imports & business context markdown
  - Data import (CSV/Excel/multiple files)
  - Data profiling (describe, dtypes, missing values)
  - Cleaning (dropna, fillna, outlier treatment with IQR)
  - Feature engineering (Foundation/Analytical/Advanced examples)
  - Modeling (descriptive, correlation, regression, scenarios)
  - Visualization (Matplotlib/Seaborn templates)
  - Executive summary generation + export

**Every code snippet documented** met business rationale.

### Tool Comparison Table
- "When to Use Which Tool" per task type

**Common Pitfalls & Solutions**:
- 5 major pitfalls specific to conventional tools

**Resources**:
- Learning links per tool (Microsoft Learn, Kaggle, R4DS)
- Office hours schedule (Power BI Clinic, Python Help)

**Assessment Tips**:
- Specific voor Criteria B-C-D, F, G
- Documentatie best practices
- Progression showcasing (v1 → v2 → v3)

---

## 7. Implementation Roadmap

### Phase 1: Pre-Pilot Preparation (4-6 weken voor start)

**Week 1-2: Content Finalization**
- [ ] Select 5 sectoren for pilot (based on BEDROM popularity)
- [ ] Source/simulate data for each sector (realistic datasets)
- [ ] Create sector 1-pagers for Week 1 presentation
- [ ] Finalize assessment rubric (A-D confirmed, E-F-G optional)
- [ ] Get curriculum commissie feedback on changes

**Week 3-4: Website Development**
- [ ] Build Priority 1 pages (rollen, sectoren, weekplanning, materiaal)
- [ ] Add detailed sector pages (8 pages)
- [ ] Create AI path materials page met prompt templates
- [ ] Create Conventional path materials page met tool guides
- [ ] Test website on mobile + desktop

**Week 5-6: Docent Training & Materials**
- [ ] Docent training (4 uur): Coaching, PAM framework, dual-path facilitation
- [ ] Create Week 1 presentation deck (4.5 uur materiaal)
- [ ] Create assessment templates (rubric Excel/Word files)
- [ ] Setup retrospective tool link (https://hanbedrijfskunde.github.io/retrospective/?workshop=ECONAN%20WK1)
- [ ] Create pulse check surveys (Week 2, Week 6)

---

### Phase 2: Pilot Execution (Semester 1, 7 weken)

**Pilot Scope**:
- **1 klas** (max 40 studenten, 8 teams)
- **5 sectoren** (uit de 8 beschikbare)
- **Both paths supported**: AI + Conventional

**Success Criteria**:
- ≥70% studenten score ≥4/5 op alle 3 PAM dimensies
- Docent werkdruk ≤120% van huidige situatie
- Beide methodologies (AI + Conventional) equally represented (geen bias)
- Role distribution: ~40% Seniors, ~60% Analists

**Data Collection**:
- Pulse checks (Week 2, 6)
- Retrospective (Week 7)
- Student interviews (sample van 10)
- Docent logboek (tijdsregistratie, wat werkte/niet werkte)

---

### Phase 3: Post-Pilot Review & Iteration (2-3 weken na pilot)

**Review Meeting** (binnen 3 weken):
- Deelnemers: Docenten, curriculum architect, student vertegenwoordigers
- Analyse: PAM scores, methodology preference, role distribution, werkdruk

**Refinement**:
- Adjust weekplanning op basis van timing issues
- Update materials op basis van student feedback
- Address methodology balance (if too many choose one path)
- Refine assessment rubric based on first grading experience

**Prepare for Scale**:
- Semester 2: 2-3 klassen (max 100 studenten)
- Add remaining sectoren if needed
- Build case library (geanonimiseerde student work examples)

---

## 8. Risk Analysis & Mitigation

### Risk 1: Assessment Criteria E-F-G Not Approved

**Probability**: Medium
**Impact**: Medium

**Mitigation**:
- LRD already includes fallback: "Note: Indien PAM criteria niet toegevoegd kunnen worden, integreer deze aspecten in bestaande criteria A-D via assessment rubric"
- Prepare alternative rubric where Purpose/Autonomy/Mastery are sub-criteria within A-D

---

### Risk 2: Methodology Imbalance (Everyone Chooses AI Path)

**Probability**: Medium-High (AI hype)
**Impact**: Low-Medium (not problematic per se, but limits cross-learning)

**Mitigation**:
- Week 1: Emphasize that BOTH paths are equally valuable
- Show success stories van conventional path (if available from pilot)
- Geen limit opleggen (respect autonomy), maar encourage diversity
- Week 4 checkpoint: Cross-path learning explicitly scheduled

---

### Risk 3: Role Distribution Skewed (Too Many Seniors)

**Probability**: Medium (everyone wants to be CEO)
**Impact**: High (teams met 4 Seniors, 1 Junior = onwerkbaar)

**Mitigation**:
- Week 1: Clear guidance on aanbevolen verdeling (40% Seniors, 60% Analists)
- Assessment: Make clear that role-mismatch (bijv. Senior student die geen strategic thinking toont) = lagere cijfer
- Docent review van team charters (Week 2) met feedback op onrealistische rolverdeling

---

### Risk 4: Data Availability Issues

**Probability**: Medium-High (real data partnerships take time)
**Impact**: Medium (can use simulated data, but less authentic)

**Mitigation**:
- Pilot: Accept simulated data for some sectoren (prioritize 2-3 real datasets)
- Partner with HAN bedrijfsleven contacten voor data access (anonymized)
- Build data library over time (each semester adds 1-2 new datasets)

---

### Risk 5: Docent Werkdruk Overschrijding

**Probability**: Medium (nieuwe systematiek = learning curve)
**Impact**: High (unsustainable if >120%)

**Mitigation**:
- Pilot: Extra uren gealloceerd (expect 120%, not sustainable but acceptable for pilot)
- Automation: Pulse checks, scheduling tools, FAQ document reduce repetitive work
- Peer support: Buddy system offloads first-line questions van docent naar studenten
- Monitor closely: Docent logboek met tijdsregistratie per activiteit

---

## 9. Expected Outcomes

### Student Experience (PAM)

**Purpose** (Target: 5/5):
- Strategische vraagstukken zijn real business dilemma's (rendement/risico/groei)
- BEDROM connectie maakt it personally relevant ("Ik ken deze sector al")
- Senior rollen geven ownership over strategic decision

**Autonomy** (Target: 5/5):
- Triple choice: Sector + Rol + Methodologie = unprecedented autonomy
- Guided choice (niet overwhelming): clear recommendations + rationale
- Flexibility: Switch methodology tot Week 3, role rotation optioneel na Week 4

**Mastery** (Target: 5/5):
- Complexity levels (Foundation/Analytical/Advanced) accommoderen diverse startniveaus
- Role-based differentiation: Seniors grow in strategic thinking, Analists in technical skills
- Methodology differentiation: AI path = prompt engineering mastery, Conventional = tool mastery
- Visible progress: v1 → v2 → v3 iterations documented

---

### Learning Outcomes

**Seniors** (CEO/CFO/RvC roles) will learn:
- ✅ Strategic question formulation (from conceptual BEDROM to data-driven ECONAN)
- ✅ Analyst steering (hoe stuur je Analist om juiste analyses te krijgen?)
- ✅ Data-driven decision making (balancing data insights met business judgment)
- ✅ Stakeholder communication (presenting to opdrachtgever = real skill)

**Analists - AI Path** will learn:
- ✅ Prompt engineering voor CRISP-DM (systematic methodology)
- ✅ Critical evaluation of AI output (validation, limitation recognition)
- ✅ AI augmentation mindset (AI as tool, not oracle)
- ✅ Meta-learning: "Wanneer AI vs conventional?"

**Analists - Conventional Path** will learn:
- ✅ Technical tool mastery (Power BI/Python/Tableau/R)
- ✅ Hands-on data manipulation (cleaning, feature engineering, modeling)
- ✅ Reproducible workflows (code/scripts gedocumenteerd)
- ✅ Statistical rigor (p-values, confidence intervals, assumptions)

**All Students** will learn:
- ✅ CRISP-DM systematiek (tool-agnostic, transferable)
- ✅ Business context first (data is middel, not doel)
- ✅ Stakeholder communication (technical → business language)
- ✅ Ethical judgment & limitations (awareness van wat je NIET kunt concluderen)

---

### Assessment Innovation

**Strengths van hybrid model**:
- ✅ Role-based assessment = differentiated grading based on learning goals
- ✅ Methodology-agnostic = process > tool (future-proof)
- ✅ Equal rigor both paths = no "easy way out"
- ✅ Work within existing criteria (A-D) = curriculum commissie approval niet strictly vereist
- ✅ PAM criteria (E-F-G) as optional extension = shows ambition without dependency

---

## 10. Files Created & Locations

| **File** | **Location** | **Purpose** | **Status** |
|----------|--------------|-------------|------------|
| LRD-ECONAN-Herontwerp-2025.md | `/workspaces/econan/` | Main learning requirements document (updated to v3.0) | ✅ Complete |
| bedrom-econan-sector-mapping.md | `/workspaces/econan/` | 8 sectoren met 16 strategische vraagstukken | ✅ Complete |
| ai-prompt-templates.md | `/workspaces/econan/` | AI-Augmented Path prompt templates (all CRISP-DM phases) | ✅ Complete |
| conventional-tools-guide.md | `/workspaces/econan/` | Conventional Tools Path workflows (Power BI, Python) | ✅ Complete |
| docs/index.html | `/workspaces/econan/docs/` | Website homepage | ✅ Complete |
| docs/css/style.css | `/workspaces/econan/docs/css/` | Website styling | ✅ Complete |
| docs/README.md | `/workspaces/econan/docs/` | Website structure documentation | ✅ Complete |
| IMPLEMENTATION-SUMMARY.md | `/workspaces/econan/` | This document - comprehensive overview | ✅ Complete |

---

## 11. Next Steps for User

### Immediate (This Week)

1. **Review LRD v3.0**:
   - Read Sections 2.4, 2.5 (nieuwe hybrid model sections)
   - Check updated Week 1-7 planning
   - Validate assessment criteria updates

2. **Review Sector Mapping**:
   - Select 5 sectoren for pilot uit de 8
   - Identify data sources per selected sector
   - Create/refine strategische vraagstuk descriptions

3. **Website Decision**:
   - Confirm GitHub Pages as hosting platform
   - Setup repository if not done
   - Assign who will build Priority 1 pages

---

### Short Term (Next 2-4 Weeks)

4. **Curriculum Commissie**:
   - Present hybrid model concept
   - Request feedback on assessment criteria E-F-G (or confirm working within A-D)
   - Get approval for pilot (if required)

5. **Data Sourcing**:
   - Contact HAN bedrijfsleven relations voor data partnerships
   - Fallback: Create simulated but realistic datasets
   - Test data quality and size (minimum ~500 rows, ideally 5K+)

6. **Docent Prep**:
   - Schedule docent training (4 uur)
   - Prep Week 1 materials (presentation deck voor 4.5 uur sessie)
   - Create assessment templates (rubric files)

---

### Medium Term (4-6 Weeks Before Pilot)

7. **Website Development**:
   - Build Priority 1 pages (rollen, sectoren, weekplanning, materiaal)
   - Test on different devices
   - Soft launch for docent review

8. **Materials Finalization**:
   - Convert `ai-prompt-templates.md` to website HTML page
   - Convert `conventional-tools-guide.md` to website HTML page
   - Create downloadable PDFs (team charter template, etc.)

9. **Student Communication**:
   - Create Week 1 pre-read (sent 1 week before): module overview, PAM explanation, hybrid model intro
   - Setup retrospective tool link met correct workshop ID

---

### Long Term (Continuous)

10. **Pilot Execution** (7 weken)
11. **Data Collection** (pulse checks, retrospective, interviews)
12. **Post-Pilot Review** (binnen 3 weken na afloop)
13. **Iteration** (prepare for Semester 2 scale-up)

---

## 12. Key Contacts & Resources

### ECONAN Team
- **Curriculum Architect**: [Naam] - Responsible for LRD updates, assessment design
- **Lead Docent**: [Naam] - Pilot execution, student coaching
- **Bedrijfsleven Relations**: [Naam] - Data partnerships, opdrachtgever network

### External Resources
- **BEDROM Program**: https://github.com/hanbedrijfskunde/bedrom/blob/main/course-docs/onderwijsprogramma.md
- **Retrospective Tool**: https://hanbedrijfskunde.github.io/retrospective/?workshop=ECONAN%20WK1
- **PM-CA Discussion**: Background context for PAM framework application

---

## 13. Conclusion

Het ECONAN herontwerp naar LRD v3.0 Hybrid Model is een **innovatieve, realistische, en schaalbare** oplossing die:

✅ **Maximaliseert autonomy** via triple choice (sector, rol, methodologie)
✅ **Behoudt purpose** via BEDROM-connected strategische vraagstukken
✅ **Differentieert mastery** via complexity levels + role-based growth
✅ **Werkt binnen constraints** (geen externe opdrachtgevers, existing assessment criteria)
✅ **Future-proofs studenten** via tool-agnostic CRISP-DM + AI literacy
✅ **Schaalbaar is** (simulatie > real clients = geen logistical limit)

De volgende stap is **curriculum commissie approval** + **data sourcing** + **website development** om klaar te zijn voor pilot in [SEMESTER/JAAR].

**Target pilot start**: [DD-MM-YYYY]
**Target PAM scores**: 5/5, 5/5, 5/5 (Purpose, Autonomy, Mastery)
**Target student satisfaction**: ≥80% score ≥4/5 op alle dimensies

---

**Questions?** Contact [Curriculum Architect Naam] of open GitHub issue in https://github.com/[username]/econan

**Ready to build!** 🚀

---

**Einde Document**
