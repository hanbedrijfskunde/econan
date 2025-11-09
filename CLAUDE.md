# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository is a learning environment for Economic Analysis (C-cluster - ECONAN). The project focuses on creating high-quality learning experiences that maximize student intrinsic motivation through Purpose, Autonomy, and Mastery.

### BEDROM → ECONAN Context

**CRITICAL CONTEXT FOR AI TOOLS**: ECONAN is the second module in a two-part sequence:

1. **BEDROM** (Business Economics & Dynamics Research and Organizational Management)
   - **Precedes** ECONAN in the curriculum
   - Students performed **conceptual analysis** of 8 business sectors:
     - Retail (Fashion & Consumer Goods)
     - Energy (Oil & Gas, Renewable)
     - Financial Services (Banking, Insurance)
     - Healthcare (Pharmaceuticals, Biotech)
     - Manufacturing (Automotive)
     - Food & Beverage (Consumer Goods)
     - Technology (SaaS, Cloud)
     - Real Estate (Commercial REITs)
   - Focus: Qualitative understanding of business dynamics, stakeholders, strategic challenges
   - Output: Conceptual frameworks, SWOT analyses, stakeholder maps

2. **ECONAN** (Economic Analysis - this module)
   - **Builds on** BEDROM sector knowledge
   - Students perform **quantitative analysis** using data from Euronext-listed companies
   - Same 8 sectors, but now with data-driven decision making
   - Focus: CRISP-DM methodology, KPI analysis, financial modeling, benchmark comparisons
   - Output: Strategic recommendations backed by hard numbers (NPV, ROI, margins, etc.)

**The Bridge**: Students transition from "ESG is important for consumer sentiment" (BEDROM) to "30% higher sustainable fashion prices lead to 12% lower volume but 8% higher margin, NPV = €2.3M positive" (ECONAN).

**When students reference BEDROM**: They are referring to their prior conceptual knowledge of a sector. ECONAN asks them to quantify and validate those concepts with real company data.

## Agent Skills Available

This repository includes specialized agent skills in [.claude/skills/](.claude/skills/):

### curriculum-architect
Expert higher education learning designer specializing in creating courses optimized for student experience. Use this skill when designing courses, sessions, or learning activities for ECONAN.

**Trigger phrases**: "course design", "curriculum", "learning design", "educational planning"

**Key principles**:
- Design for 5/5 scores on Purpose, Autonomy, and Mastery
- Follow PBBK design criteria (K.I.S.S. principle)
- Apply Daniel Pink's Drive framework (intrinsic motivation)
- Student retrospective tool: https://hanbedrijfskunde.github.io/retrospective/?workshop=ECONAN%20WK1
- **All student-facing content must be in professional business Dutch (Nederlands)**

### Other Skills
- **tech-lead**: Creates Technical Design Documents (TDD)
- **product-manager**: Generates Product Requirements Documents (PRD)

## Learning Design Principles

### Student Experience Measurement
Every session should be measured using the three dimensions:
- **Purpose**: Why does this learning matter? (Target: 5/5)
- **Autonomy**: Do students have meaningful control? (Target: 5/5)
- **Mastery**: Are students experiencing optimal challenge and growth? (Target: 5/5)

### PBBK Design Criteria
1. Deliver the right content at the right moment in the most effective way
2. Account for student diversity (not "average" students)
3. Test every design and monitor every implementation
4. Automate or outsource operational tasks
5. Respect privacy and manage personal data correctly

### K.I.S.S. Principle
Keep It Simple Stupid - avoid over-engineering learning experiences.

## Current State

The repository is in its initial setup phase with agent skills configured for curriculum development. When adding code or content, follow the PBBK design criteria and optimize for student intrinsic motivation.
