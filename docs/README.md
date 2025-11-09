# ECONAN Website Structure

This directory contains the GitHub Pages website for the ECONAN module.

## Directory Structure

```
docs/
├── index.html                  # Homepage
├── css/
│   └── style.css              # Custom styles
├── js/
│   └── (future JavaScript)
├── rollen/
│   ├── index.html             # Rollen overzicht
│   ├── senior-ceo.html        # CEO rol details
│   ├── senior-cfo.html        # CFO rol details
│   ├── senior-rvc.html        # RvC rol details
│   └── junior-analyst.html    # Analist rol details
├── sectoren/
│   ├── index.html             # Sectoren overzicht
│   ├── retail.html            # Retail strategische vraagstukken
│   ├── energy.html            # Energy strategische vraagstukken
│   ├── finance.html           # Finance strategische vraagstukken
│   ├── healthcare.html        # Healthcare strategische vraagstukken
│   ├── manufacturing.html     # Manufacturing strategische vraagstukken
│   ├── food.html              # Food & Beverage strategische vraagstukken
│   ├── technology.html        # Technology (SaaS) strategische vraagstukken
│   └── realestate.html        # Real Estate strategische vraagstukken
├── weekplanning/
│   ├── index.html             # 7-weken overzicht
│   ├── week1.html             # Week 1: Identity & Mission
│   ├── week2-3.html           # Week 2-3: Discovery
│   ├── week4.html             # Week 4: Checkpoint
│   ├── week5-6.html           # Week 5-6: Analysis
│   └── week7.html             # Week 7: Delivery
├── materiaal/
│   ├── index.html             # Materiaal overzicht
│   ├── ai-pad.html            # AI-Augmented Path materiaal
│   │   ├── prompt-templates/  # CRISP-DM prompt templates
│   │   ├── ai-tools-guide.html
│   │   └── validation-guide.html
│   ├── conventional-pad.html  # Conventional Tools Path materiaal
│   │   ├── powerbi-guide.html
│   │   ├── python-guide.html
│   │   └── tableau-guide.html
│   ├── crisp-dm-guide.html    # Tool-agnostic CRISP-DM guide
│   └── bedrom-bridge.html     # BEDROM → ECONAN connectie materialen
└── assessment/
    ├── index.html             # Assessment overzicht
    ├── rubric.html            # CRISP-DM A-D + PAM E-F-G rubric
    ├── role-based.html        # Role-based assessment uitleg
    └── complexity-levels.html # Foundation/Analytical/Advanced uitleg
```

## Technology Stack

- **HTML5**: Semantic markup
- **CSS3**: Custom styles + Bootstrap 5.3
- **Bootstrap 5.3**: Responsive framework (via CDN)
- **GitHub Pages**: Static site hosting
- **No build process**: Plain HTML/CSS for simplicity (KISS principle)

## Design Principles

1. **K.I.S.S. (Keep It Simple Stupid)**
   - No complex JavaScript frameworks
   - Plain HTML/CSS with Bootstrap
   - Easy to maintain and update

2. **Responsive Design**
   - Mobile-first approach
   - Bootstrap grid system
   - Accessible on all devices

3. **Accessibility**
   - Semantic HTML
   - ARIA labels where needed
   - Keyboard navigation support
   - High contrast text

4. **Content-First**
   - Clear navigation
   - Scannable content
   - Professional Dutch language
   - Focus on student needs

## Key Pages to Create

### Priority 1 (Must Have for Week 1)
- [x] index.html - Homepage with overzicht
- [ ] rollen/index.html - Rollen overzicht (Senior vs Junior)
- [ ] sectoren/index.html - Alle 8 sectoren met strategische vraagstukken
- [ ] weekplanning/index.html - 7-weken structuur
- [ ] materiaal/index.html - Materiaal hub voor beide paden

### Priority 2 (Must Have for Week 2)
- [ ] materiaal/ai-pad.html - AI path materiaal en prompt templates
- [ ] materiaal/conventional-pad.html - Conventional tools materiaal
- [ ] assessment/rubric.html - Volledige assessment rubric
- [ ] Individual sector pages (8 pages: retail, energy, finance, etc.)

### Priority 3 (Should Have)
- [ ] Detailed rol pages (CEO, CFO, RvC, Analist)
- [ ] Week-by-week detailed pages
- [ ] FAQ page
- [ ] Resources/links page

## Content Strategy

### Language
- **Professional Business Dutch (Nederlands)** for all student-facing content
- Clear, concise, action-oriented language
- Avoid jargon unless explained

### Tone
- **Empowering**: "Jij kiest...", "Jouw analyse..."
- **Practical**: Focus on actionable information
- **Supportive**: "We helpen je met...", "Je krijgt..."

### Visual Hierarchy
- Use headings (H1-H6) semantically
- Cards for grouped content
- Badges for labels (AI/Conventional, Foundation/Analytical/Advanced)
- Colors aligned with PAM framework:
  - Blue: Purpose
  - Green: Autonomy
  - Yellow/Orange: Mastery

## Deployment

### GitHub Pages Setup
1. Repository settings → Pages
2. Source: Deploy from branch `main`
3. Folder: `/docs`
4. Custom domain (optional): econan.hanbedrijfskunde.nl

### URL Structure
- Production: `https://[username].github.io/econan/`
- Or custom: `https://econan.hanbedrijfskunde.nl/`

## Maintenance

### Content Updates
- Edit HTML files directly in `/docs/`
- Commit changes to `main` branch
- GitHub Pages auto-deploys (1-2 min delay)

### Version Control
- Use semantic commit messages
- Tag releases for each semester (v1.0-2025S1, etc.)
- Keep backup of previous versions

## Future Enhancements (Optional)

- Search functionality
- Interactive role/sector selector tool
- Student testimonials section
- Data visualization examples gallery
- Integration with retrospective tool
- Downloadable PDFs (team charter template, etc.)

## Contact

For questions or contributions:
- Repository: https://github.com/[username]/econan
- Issues: Use GitHub Issues for bug reports/feature requests

---

**Last Updated**: 9 November 2025
**Status**: Initial Structure Created
**Next Steps**: Create priority 1 pages for Week 1 launch
