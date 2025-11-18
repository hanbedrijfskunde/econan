"""
Configuration Loader for ECONAN Exercise Generator

This module provides utilities to load and parse YAML configuration files:
- company_data.yaml: Financial statement data for Euronext companies
- exercise_templates.yaml: Exercise templates for V3/V4/V5 categories

Functions:
    - load_companies: Load all company financial data
    - load_exercise_templates: Load exercise templates by category
    - get_company_by_ticker: Retrieve specific company data
    - get_companies_by_sector: Retrieve all companies in a sector
"""

import yaml
from pathlib import Path
from typing import List, Dict, Optional
from .data_models import Company, Exercise


# Configuration file paths
CONFIG_DIR = Path(__file__).parent.parent / "config"
COMPANY_DATA_PATH = CONFIG_DIR / "company_data.yaml"
EXERCISE_TEMPLATES_PATH = CONFIG_DIR / "exercise_templates.yaml"


def load_companies() -> List[Company]:
    """
    Load all company financial data from company_data.yaml.

    Returns:
        List[Company]: List of Company objects with complete financial data

    Raises:
        FileNotFoundError: If company_data.yaml is not found
        yaml.YAMLError: If YAML file is malformed
        ValueError: If company data is invalid
    """
    if not COMPANY_DATA_PATH.exists():
        raise FileNotFoundError(f"Company data file not found: {COMPANY_DATA_PATH}")

    with open(COMPANY_DATA_PATH, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    companies = []
    for company_dict in data.get('companies', []):
        try:
            company = Company(
                name=company_dict['name'],
                ticker=company_dict['ticker'],
                sector=company_dict['sector'],
                year=company_dict['year'],
                total_assets=float(company_dict['total_assets']),
                current_assets=float(company_dict['current_assets']),
                current_liabilities=float(company_dict['current_liabilities']),
                total_equity=float(company_dict['total_equity']),
                total_debt=float(company_dict['total_debt']),
                revenue=float(company_dict['revenue']),
                operating_income=float(company_dict['operating_income']),
                net_income=float(company_dict['net_income']),
                interest_expense=float(company_dict['interest_expense']),
                operating_cash_flow=float(company_dict['operating_cash_flow']),
                investing_cash_flow=float(company_dict['investing_cash_flow']),
                financing_cash_flow=float(company_dict['financing_cash_flow']),
                market_cap=float(company_dict['market_cap']),
                share_price=float(company_dict['share_price']),
                shares_outstanding=float(company_dict['shares_outstanding'])
            )
            companies.append(company)
        except KeyError as e:
            raise ValueError(f"Missing required field in company data: {e}")
        except (TypeError, ValueError) as e:
            raise ValueError(f"Invalid financial data for {company_dict.get('name', 'unknown')}: {e}")

    return companies


def load_exercise_templates(category: Optional[str] = None) -> Dict:
    """
    Load exercise templates from exercise_templates.yaml.

    Args:
        category: Optional category filter ("v3", "v4", "v5")
                 If None, returns all templates

    Returns:
        Dict: Dictionary with template data
              Format: {
                  "v3_exercises": [...],
                  "v4_exercises": [...],
                  "v5_exercises": [...],
                  "metadata": {...}
              }

    Raises:
        FileNotFoundError: If exercise_templates.yaml is not found
        yaml.YAMLError: If YAML file is malformed
    """
    if not EXERCISE_TEMPLATES_PATH.exists():
        raise FileNotFoundError(f"Exercise templates file not found: {EXERCISE_TEMPLATES_PATH}")

    with open(EXERCISE_TEMPLATES_PATH, 'r', encoding='utf-8') as f:
        templates = yaml.safe_load(f)

    if category:
        category_key = f"{category.lower()}_exercises"
        if category_key not in templates:
            raise ValueError(f"Invalid category: {category}. Must be one of: v3, v4, v5")
        return {
            category_key: templates[category_key],
            "metadata": templates.get("metadata", {})
        }

    return templates


def get_company_by_ticker(ticker: str, companies: Optional[List[Company]] = None) -> Company:
    """
    Retrieve a specific company by its ticker symbol.

    Args:
        ticker: Stock ticker symbol (e.g., "AD.AS", "SHELL.AS")
        companies: Optional pre-loaded list of companies
                  If None, will load from file

    Returns:
        Company: Company object matching the ticker

    Raises:
        ValueError: If ticker is not found
    """
    if companies is None:
        companies = load_companies()

    ticker_upper = ticker.upper()
    for company in companies:
        if company.ticker.upper() == ticker_upper:
            return company

    raise ValueError(f"Company with ticker '{ticker}' not found")


def get_companies_by_sector(sector: str, companies: Optional[List[Company]] = None) -> List[Company]:
    """
    Retrieve all companies in a specific sector.

    Args:
        sector: Business sector (e.g., "Retail", "Energy", "Technology")
        companies: Optional pre-loaded list of companies
                  If None, will load from file

    Returns:
        List[Company]: List of companies in the specified sector

    Raises:
        ValueError: If no companies found in sector
    """
    if companies is None:
        companies = load_companies()

    sector_companies = [c for c in companies if c.sector.lower() == sector.lower()]

    if not sector_companies:
        available_sectors = sorted(set(c.sector for c in companies))
        raise ValueError(
            f"No companies found in sector '{sector}'. "
            f"Available sectors: {', '.join(available_sectors)}"
        )

    return sector_companies


def get_all_sectors(companies: Optional[List[Company]] = None) -> List[str]:
    """
    Get a list of all unique sectors in the dataset.

    Args:
        companies: Optional pre-loaded list of companies
                  If None, will load from file

    Returns:
        List[str]: Sorted list of unique sector names
    """
    if companies is None:
        companies = load_companies()

    return sorted(set(c.sector for c in companies))


def get_template_by_id(template_id: str, templates: Optional[Dict] = None) -> Dict:
    """
    Retrieve a specific exercise template by its ID.

    Args:
        template_id: Exercise template ID (e.g., "V3_A1", "V4_B2")
        templates: Optional pre-loaded templates dictionary
                  If None, will load from file

    Returns:
        Dict: Template data including question, steps, identity, etc.

    Raises:
        ValueError: If template_id is not found
    """
    if templates is None:
        templates = load_exercise_templates()

    # Determine category from ID prefix
    category_prefix = template_id.split('_')[0].lower()
    category_key = f"{category_prefix}_exercises"

    if category_key not in templates:
        raise ValueError(f"Invalid template ID format: {template_id}")

    # Search for template
    for template in templates[category_key]:
        if template['id'] == template_id:
            return template

    raise ValueError(f"Template with ID '{template_id}' not found")


# Utility function for debugging
def print_data_summary():
    """
    Print a summary of available companies and exercise templates.
    Useful for debugging and data exploration.
    """
    print("=" * 80)
    print("ECONAN Exercise Generator - Data Summary")
    print("=" * 80)

    # Load companies
    companies = load_companies()
    print(f"\n📊 Companies loaded: {len(companies)}")

    # Group by sector
    sectors = {}
    for company in companies:
        if company.sector not in sectors:
            sectors[company.sector] = []
        sectors[company.sector].append(company.ticker)

    print("\nCompanies by sector:")
    for sector in sorted(sectors.keys()):
        tickers = ', '.join(sectors[sector])
        print(f"  {sector}: {tickers}")

    # Load templates
    templates = load_exercise_templates()
    print(f"\n📝 Exercise templates:")
    print(f"  V3 (Liquidity): {len(templates.get('v3_exercises', []))} templates")
    print(f"  V4 (Valuation): {len(templates.get('v4_exercises', []))} templates")
    print(f"  V5 (Cash Flow): {len(templates.get('v5_exercises', []))} templates")

    print("\n" + "=" * 80)


if __name__ == "__main__":
    # Run data summary when module is executed directly
    print_data_summary()
