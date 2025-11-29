# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains the ECONAN (Economic Analysis) module learning environment for the C-cluster curriculum at HAN Bedrijfskunde. The project is a static GitHub Pages website that serves educational content to students who analyze business sectors using CRISP-DM methodology.

### BEDROM → ECONAN Context

**CRITICAL CONTEXT**: ECONAN is the second module in a two-part sequence:

1. **BEDROM** (precedes ECONAN): Students performed conceptual analysis of 8 business sectors (Retail, Energy, Financial Services, Healthcare, Manufacturing, Food & Beverage, Technology, Real Estate)
   - Focus: Qualitative understanding (SWOT, stakeholder maps, ESG analysis)

2. **ECONAN** (this module): Students perform quantitative analysis using Euronext company data
   - Focus: CRISP-DM methodology, KPI analysis, financial modeling, NPV/ROI calculations
   - **The Bridge**: From "ESG is important" (BEDROM) to "30% price premium = 8% higher margin, NPV = €2.3M" (ECONAN)

### Hybrid Learning Model

ECONAN uses a **role-based team structure** with **methodology choice**:
- **Roles**: Senior stakeholders (CEO/CFO/RvC) + Junior Analysts
- **Methodology paths**: AI-augmented OR Conventional tools (Power BI, Python, Tableau, R)
- **Assessment**: CRISP-DM criteria (A-D) + PAM framework (Purpose-Autonomy-Mastery scores E-F-G)

## Repository Structure

```
econan/
├── docs/                           # GitHub Pages website root
│   ├── index.html                 # Homepage
│   ├── css/                       # Design system + component styles
│   ├── sectoren/                  # 8 sector pages with strategic questions
│   ├── rollen/                    # Role descriptions (CEO, CFO, RvC, Analyst)
│   ├── weekplanning/              # 7-week planning pages
│   ├── materiaal/                 # Learning materials (AI + Conventional paths)
│   ├── assessment/                # Assessment rubrics and complexity levels
│   ├── draaiboeken/               # Session scripts (Markdown + HTML)
│   ├── handouts/                  # Student guides (data extraction, templates)
│   ├── templates/                 # Forms (self-assessment, feedback)
│   ├── oefeningen/                # Exercises (e.g., spot-de-fout.html)
│   └── examples/                  # Tutorial examples (financial analysis)
├── ai-prompt-templates.md         # AI-augmented path: CRISP-DM prompts
├── conventional-tools-guide.md    # Conventional path: tool selection + workflows
├── bedrom-econan-sector-mapping.md # 8 sectors × 2 strategic questions mapping
├── LRD-ECONAN-Herontwerp-2025.md  # Learning Requirements Document (v3.0)
├── IMPLEMENTATION-SUMMARY.md      # Implementation status + key decisions
├── fix_sections.py                # Utility: renumber LRD sections
└── .claude/skills/                # Agent skills (curriculum-architect, etc.)
```

## Technology Stack

- **Static site**: Plain HTML5 + CSS3 (no build process)
- **Framework**: Bootstrap 5.3 via CDN (responsive design)
- **Fonts**: Inter (UI) + JetBrains Mono (code) via Google Fonts
- **Hosting**: GitHub Pages (`/docs` folder)
- **Language**: Professional business Dutch (Nederlands) for all student-facing content

## Key Documents

### Source of Truth Documents
1. [LRD-ECONAN-Herontwerp-2025.md](LRD-ECONAN-Herontwerp-2025.md) - Learning Requirements Document (v3.0 - Hybrid Model)
   - Section 1: Context & Foundation (student profile, BEDROM connection)
   - Section 2: Functional Requirements (Purpose/Autonomy/Mastery + Hybrid Methodology + Role Structure)
   - Sections 3-13: Non-functional, Assessment, Support, Content, Measurement, Iteration, Risk, Success, Implementation, Roles, Appendices

2. [IMPLEMENTATION-SUMMARY.md](IMPLEMENTATION-SUMMARY.md) - What's been built and why
   - Hybrid model rationale (role-based teams + dual methodology)
   - PAM framework optimization strategy
   - Week-by-week structure updates
   - Assessment differentiation (role-based weighting)

3. [bedrom-econan-sector-mapping.md](bedrom-econan-sector-mapping.md) - Strategic question bank
   - 8 sectors × 2 strategic questions (rendement vs. risico/groei focus)
   - Euronext company examples per sector
   - BEDROM → ECONAN knowledge bridge per question

### Methodology-Specific Documents
4. [ai-prompt-templates.md](ai-prompt-templates.md) - AI-augmented path
   - CRISP-DM phase-specific prompt templates
   - Validation principles (AI as tool, not replacement)
   - Documentation requirements (prompt logging)

5. [conventional-tools-guide.md](conventional-tools-guide.md) - Conventional tools path
   - Tool selection matrix (Power BI, Tableau, Python, R, Excel)
   - Use case guidance (when to use which tool)
   - CRISP-DM phase workflows per tool

## Common Tasks

### Viewing the Website Locally
```bash
# Option 1: Python simple server (recommended)
cd docs && python3 -m http.server 8000
# Visit http://localhost:8000

# Option 2: VS Code Live Server extension
# Right-click docs/index.html → "Open with Live Server"
```

### Creating New Content

#### Adding a New HTML Page
1. Create HTML file in appropriate `docs/` subdirectory
2. Use existing pages as template (keep navigation structure)
3. Ensure professional Dutch language
4. Link from parent index.html or navigation

#### Converting Markdown to HTML
```bash
# No automated build process - convert manually or use:
# Pandoc (if installed): pandoc file.md -o file.html --standalone
# Or copy-paste Markdown into HTML template and style manually
```

#### Adding Draaiboek (Session Script)
```bash
# Create both .md and .html versions in docs/draaiboeken/
# Naming: week-N-sessie.md and week-N-sessie.html
# Include: Learning goals, time breakdown, activities, materials needed
```

### Fixing Section Numbers
```bash
# If LRD section numbering gets out of sync:
python3 fix_sections.py
# This script renumbers sections in LRD-ECONAN-Herontwerp-2025.md
```

## Design Principles

### K.I.S.S. Principle (Keep It Simple Stupid)
- No complex JavaScript frameworks
- Plain HTML/CSS for maintainability
- Avoid over-engineering learning experiences

### PBBK Design Criteria
1. Deliver right content at right moment in most effective way
2. Account for student diversity (not "average" students)
3. Test every design and monitor every implementation
4. Automate or outsource operational tasks
5. Respect privacy and manage personal data correctly

### PAM Framework (Purpose-Autonomy-Mastery)
Every session and design decision optimizes for:
- **Purpose** (5/5): Why does this learning matter? Real strategic decisions
- **Autonomy** (5/5): Triple choice (sector + role + methodology)
- **Mastery** (5/5): Complexity levels (Foundation/Analytical/Advanced) + role-specific growth
- Measurement: https://hanbedrijfskunde.github.io/retrospective/?workshop=ECONAN%20WK1

## Agent Skills Available

Specialized agent skills in [.claude/skills/](.claude/skills/):

### curriculum-architect
Use when designing courses, sessions, or learning activities for ECONAN.
**Trigger**: "course design", "curriculum", "learning design", "educational planning"

### tech-lead
Use when creating Technical Design Documents (TDD).

### product-manager
Use when creating Product Requirements Documents (PRD).

## Content Guidelines

### Language
- **All student-facing content**: Professional business Dutch (Nederlands)
- **Technical documentation**: English acceptable for code/config
- Tone: Empowering ("Jij kiest"), practical, supportive

### Visual Hierarchy
- Use semantic HTML headings (H1-H6)
- Cards for grouped content
- Badges for labels (AI/Conventional, complexity levels)
- PAM-aligned colors:
  - Blue (`--color-primary-*`): Purpose
  - Green (`--color-success-*`): Autonomy
  - Yellow/Orange (`--color-warning-*`): Mastery

### File Naming Conventions
- HTML pages: lowercase with hyphens (`senior-ceo.html`)
- Markdown docs: same as HTML or descriptive (`data-extraction-guide.md`)
- Draaiboeken: `week-N-sessie.md` pattern
- No spaces in filenames

## GitHub Pages Deployment

### Current Setup
- **Branch**: `main`
- **Source folder**: `/docs`
- **URL**: https://[username].github.io/econan/ (or custom domain)
- **Auto-deploy**: Any push to `main` triggers rebuild (1-2 min delay)

### Testing Before Push
Always test locally before pushing:
```bash
cd docs && python3 -m http.server 8000
# Check navigation, responsive design, Dutch language correctness
```

## Assessment Structure

ECONAN uses **dual assessment criteria**:
1. **CRISP-DM criteria (A-D)**: Technical execution (Business Understanding, Data Understanding, Data Preparation, Modeling/Evaluation)
2. **PAM criteria (E-F-G)**: Student experience (Purpose, Autonomy, Mastery scores)

**Role-based weighting**:
- Seniors: 60% Criterium A, 20% B-C (strategic focus)
- Analysts: 40% Criterium A, 80% B-C (technical focus)
- Both: 50% Criterium D (joint responsibility)

**Methodology-agnostic**: AI path and Conventional path assessed on same CRISP-DM rigor, different artifacts.
