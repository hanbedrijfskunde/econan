# ECONAN Exercise Generator

Automated verification exercise generator for ECONAN financial analysis education.

## Overview

This tool generates verification exercises by combining:
- **Company financial data** from 16 Euronext-listed companies across 8 sectors
- **Exercise templates** for V3 (Liquidity), V4 (Valuation), and V5 (Cash Flow)
- **Jinja2 template rendering** for variable substitution
- **Distractor generation** for multiple-choice questions

## Features

- **208 total exercises**: 13 templates × 16 companies
  - V3 (Liquidity): 64 exercises
  - V4 (Valuation): 80 exercises
  - V5 (Cash Flow): 64 exercises
- **Multiple output formats**: Markdown, HTML, JSON
- **Flexible filtering**: By category, company, or sector
- **Solution control**: Include/exclude solutions for instructor vs student versions
- **Batch or individual**: Generate combined files or individual exercise files

## Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Verify installation
python generate_exercises.py --help
```

## Quick Start

### Generate All Exercises

```bash
# All exercises in Markdown format
python generate_exercises.py --output output/

# All exercises in HTML format
python generate_exercises.py --format html --output output/
```

### Generate by Category

```bash
# V3 (Liquidity) exercises
python generate_exercises.py --category V3 --output output/

# V4 (Valuation) exercises in HTML
python generate_exercises.py --category V4 --format html --output output/

# V5 (Cash Flow) exercises in JSON
python generate_exercises.py --category V5 --format json --output output/
```

### Generate by Company

```bash
# Ahold Delhaize (AD.AS)
python generate_exercises.py --ticker AD.AS --output output/

# Shell (SHELL.AS) - V3 exercises only
python generate_exercises.py --ticker SHELL.AS --category V3 --output output/

# ASML (ASML.AS) in HTML format
python generate_exercises.py --ticker ASML.AS --format html --output output/
```

### Generate by Sector

```bash
# All Retail sector companies
python generate_exercises.py --sector Retail --output output/

# Energy sector - V4 exercises
python generate_exercises.py --sector Energy --category V4 --output output/
```

### Student vs Instructor Versions

```bash
# Student version (no solutions)
python generate_exercises.py --no-solutions --output output/student/

# Instructor version (with solutions)
python generate_exercises.py --output output/instructor/
```

### Individual Files

```bash
# Generate individual file for each exercise
python generate_exercises.py --individual --output output/

# V3 exercises as individual HTML files
python generate_exercises.py --category V3 --format html --individual --output output/
```

## Command Reference

### Options

| Option | Short | Description | Values |
|--------|-------|-------------|--------|
| `--output` | `-o` | Output directory (required) | Path |
| `--format` | `-f` | Output format | `markdown`, `html`, `json` |
| `--category` | `-c` | Exercise category | `V3`, `V4`, `V5` |
| `--ticker` | `-t` | Company ticker symbol | e.g., `AD.AS`, `SHELL.AS` |
| `--sector` | `-s` | Business sector | e.g., `Retail`, `Energy` |
| `--no-solutions` | - | Exclude solutions (student version) | Flag |
| `--individual` | - | Generate individual files | Flag |

### Categories

- **V3**: Liquiditeitsanalyse (Liquidity Analysis)
  - Current Ratio, Working Capital, D/E Ratio, Leverage
- **V4**: Waardering & Winstgevendheid (Valuation & Profitability)
  - ROE, DuPont Analysis, P/E Ratio, Earnings Yield, Operating Margin
- **V5**: Cashflow Analyse (Cash Flow Analysis)
  - Free Cash Flow, Net Cash Change, OCF Margin, Cash Conversion

### Available Companies

| Ticker | Company | Sector |
|--------|---------|--------|
| AD.AS | Ahold Delhaize | Retail |
| MC.PA | LVMH | Retail |
| SHELL.AS | Shell | Energy |
| TTE.PA | TotalEnergies | Energy |
| INGA.AS | ING Group | Financial Services |
| CS.PA | AXA | Financial Services |
| SAN.PA | Sanofi | Healthcare |
| PHIA.AS | Koninklijke Philips | Healthcare |
| STLAM.MI | Stellantis | Manufacturing |
| RNO.PA | Renault | Manufacturing |
| UNA.AS | Unilever | Food & Beverage |
| HEIA.AS | Heineken | Food & Beverage |
| ASML.AS | ASML | Technology |
| CAP.PA | Capgemini | Technology |
| URW.AS | Unibail-Rodamco-Westfield | Real Estate |
| LI.PA | Klepierre | Real Estate |

## Output Formats

### Markdown (`.md`)
- Human-readable format
- Easy to version control
- Can be converted to PDF/HTML
- Best for: Documentation, GitHub

### HTML (`.html`)
- Web-ready format
- Includes ECONAN design system classes
- Interactive elements (radio buttons for answers)
- Best for: Online platforms, LMS integration

### JSON (`.json`)
- Machine-readable format
- Includes all metadata
- API-ready structure
- Best for: Data processing, automated grading

## Project Structure

```
scripts/
├── generate_exercises.py      # CLI tool (main entry point)
├── requirements.txt            # Python dependencies
├── lib/                        # Core library
│   ├── __init__.py            # Package initialization
│   ├── data_models.py         # Company and Exercise classes
│   ├── config_loader.py       # YAML configuration loading
│   ├── exercise_generator.py  # Exercise generation engine
│   └── formatter.py           # Output formatters (MD/HTML/JSON)
├── config/                     # Configuration files
│   ├── company_data.yaml      # 16 companies with financial data
│   └── exercise_templates.yaml # 13 exercise templates
└── tests/                      # Test suite
    ├── test_config_loader.py  # Config loading tests (25 tests)
    └── test_exercise_generator.py # Generator tests (29 tests)
```

## Examples

### Example 1: Complete Course Material

Generate all exercises in multiple formats for a complete course:

```bash
# Instructor version (with solutions) in Markdown
python generate_exercises.py --output output/instructor/markdown/

# Student version (no solutions) in HTML
python generate_exercises.py --no-solutions --format html --output output/student/html/

# Data export in JSON for analytics
python generate_exercises.py --format json --output output/data/
```

### Example 2: Week-by-Week Assignments

Generate exercises by category for weekly assignments:

```bash
# Week 3: Liquidity Analysis
python generate_exercises.py --category V3 --no-solutions --format html --output output/week3/

# Week 4: Valuation & Profitability
python generate_exercises.py --category V4 --no-solutions --format html --output output/week4/

# Week 5: Cash Flow Analysis
python generate_exercises.py --category V5 --no-solutions --format html --output output/week5/
```

### Example 3: Sector-Specific Practice

Generate sector-specific exercises for BEDROM→ECONAN transition:

```bash
# Retail sector (Ahold, LVMH)
python generate_exercises.py --sector Retail --output output/sectors/retail/

# Technology sector (ASML, Capgemini)
python generate_exercises.py --sector Technology --output output/sectors/tech/

# Energy sector (Shell, TotalEnergies)
python generate_exercises.py --sector Energy --output output/sectors/energy/
```

## Development

### Running Tests

```bash
# All tests
pytest

# Config loader tests
pytest tests/test_config_loader.py -v

# Generator tests
pytest tests/test_exercise_generator.py -v

# Test coverage
pytest --cov=lib --cov-report=html
```

### Adding New Companies

1. Edit `config/company_data.yaml`
2. Add company data with all required fields
3. Run tests to validate: `pytest tests/test_config_loader.py`

### Adding New Exercise Templates

1. Edit `config/exercise_templates.yaml`
2. Add template with Jinja2 syntax (`{{ variable }}`)
3. Update answer mapping in `lib/exercise_generator.py`
4. Run tests: `pytest tests/test_exercise_generator.py`

## Technical Details

### Financial Calculations

The generator calculates 20+ financial ratios:
- **Liquidity**: Current Ratio, Working Capital
- **Leverage**: D/E Ratio, Leverage Multiplicator
- **Profitability**: ROE, DuPont Components, Operating Margin
- **Valuation**: P/E Ratio, Earnings Yield, EPS
- **Cash Flow**: FCF, OCF Margin, Cash Conversion

### Distractor Generation

Distractors (incorrect answers) are generated using:
- **±10-20% variance**: Plausible calculation errors
- **±30-40% variance**: Conceptual misunderstandings
- **Inverse/reciprocal errors**: Common mistakes (e.g., 1/x instead of x)
- Format preservation (€, %, plain numbers)

### Mathematical Verification

All exercises include verification identities:
- Balance sheet: Assets = Liabilities + Equity
- DuPont: ROE = Net Margin × Asset Turnover × Leverage
- P/E: Market Cap / Net Income = Share Price / EPS
- Cash Flow: Δ Cash = Operating CF + Investing CF + Financing CF

## Support

For issues, questions, or contributions:
- **Issue Tracker**: GitHub Issues
- **Documentation**: This README
- **Tests**: `pytest tests/ -v`

## License

ECONAN Development Team - Educational Use
