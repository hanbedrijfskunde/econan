"""
Unit tests for config_loader module

Tests configuration loading, data validation, and utility functions.
Run with: pytest tests/test_config_loader.py
"""

import pytest
from pathlib import Path
import sys

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from lib.config_loader import (
    load_companies,
    load_exercise_templates,
    get_company_by_ticker,
    get_companies_by_sector,
    get_all_sectors,
    get_template_by_id
)
from lib.data_models import Company


class TestLoadCompanies:
    """Test company data loading"""

    def test_load_companies_returns_list(self):
        """Should return a list of Company objects"""
        companies = load_companies()
        assert isinstance(companies, list)
        assert len(companies) > 0
        assert all(isinstance(c, Company) for c in companies)

    def test_load_companies_expected_count(self):
        """Should load 16 companies (2 per sector × 8 sectors)"""
        companies = load_companies()
        assert len(companies) == 16

    def test_company_has_required_fields(self):
        """Each company should have all required financial data"""
        companies = load_companies()
        company = companies[0]  # Test first company

        # Check string fields
        assert isinstance(company.name, str) and company.name
        assert isinstance(company.ticker, str) and company.ticker
        assert isinstance(company.sector, str) and company.sector

        # Check numeric fields
        assert isinstance(company.year, int) and company.year > 2000
        assert company.total_assets > 0
        assert company.current_assets > 0
        assert company.total_equity > 0
        assert company.revenue > 0
        assert company.net_income > 0

    def test_company_calculated_properties(self):
        """Company should calculate financial ratios correctly"""
        companies = load_companies()
        company = companies[0]

        # Test ROE calculation
        expected_roe = company.net_income / company.total_equity
        assert abs(company.roe - expected_roe) < 0.0001

        # Test D/E calculation
        expected_de = company.total_debt / company.total_equity
        assert abs(company.debt_to_equity - expected_de) < 0.0001

        # Test Current Ratio
        expected_cr = company.current_assets / company.current_liabilities
        assert abs(company.current_ratio - expected_cr) < 0.0001

    def test_balance_sheet_identity(self):
        """Total Assets should equal Total Liabilities + Total Equity"""
        companies = load_companies()
        for company in companies:
            total_liabilities = company.total_liabilities
            balance_check = total_liabilities + company.total_equity
            # Allow 1% tolerance for rounding
            assert abs(company.total_assets - balance_check) / company.total_assets < 0.01, \
                f"{company.name}: Balance sheet doesn't balance"


class TestLoadExerciseTemplates:
    """Test exercise template loading"""

    def test_load_all_templates(self):
        """Should load all exercise templates"""
        templates = load_exercise_templates()
        assert 'v3_exercises' in templates
        assert 'v4_exercises' in templates
        assert 'v5_exercises' in templates
        assert 'metadata' in templates

    def test_load_templates_by_category(self):
        """Should filter templates by category"""
        v3_templates = load_exercise_templates(category="v3")
        assert 'v3_exercises' in v3_templates
        assert 'v4_exercises' not in v3_templates

    def test_v3_template_structure(self):
        """V3 templates should have required fields"""
        templates = load_exercise_templates()
        v3 = templates['v3_exercises'][0]

        assert 'id' in v3
        assert 'difficulty' in v3
        assert 'learning_objective' in v3
        assert 'verification_identity' in v3
        assert 'question_template' in v3
        assert 'solution_steps' in v3

    def test_template_count(self):
        """Should have expected number of templates per category"""
        templates = load_exercise_templates()
        # V3: 4 templates (A1, A2, B1, B2)
        assert len(templates['v3_exercises']) == 4
        # V4: 5 templates (A1, A2, B1, B2, C1)
        assert len(templates['v4_exercises']) == 5
        # V5: 4 templates (A1, A2, B1, B2)
        assert len(templates['v5_exercises']) == 4


class TestGetCompanyByTicker:
    """Test company retrieval by ticker"""

    def test_get_existing_company(self):
        """Should retrieve company by valid ticker"""
        company = get_company_by_ticker("AD.AS")
        assert company.ticker == "AD.AS"
        assert company.name == "Ahold Delhaize"
        assert company.sector == "Retail"

    def test_get_company_case_insensitive(self):
        """Should work with different ticker cases"""
        company1 = get_company_by_ticker("AD.AS")
        company2 = get_company_by_ticker("ad.as")
        assert company1.ticker == company2.ticker

    def test_get_nonexistent_company(self):
        """Should raise ValueError for invalid ticker"""
        with pytest.raises(ValueError, match="not found"):
            get_company_by_ticker("INVALID.TICKER")


class TestGetCompaniesBySector:
    """Test company retrieval by sector"""

    def test_get_retail_companies(self):
        """Should retrieve all Retail sector companies"""
        companies = get_companies_by_sector("Retail")
        assert len(companies) == 2
        assert all(c.sector == "Retail" for c in companies)

    def test_get_energy_companies(self):
        """Should retrieve all Energy sector companies"""
        companies = get_companies_by_sector("Energy")
        assert len(companies) == 2
        assert all(c.sector == "Energy" for c in companies)

    def test_sector_case_insensitive(self):
        """Should work with different sector cases"""
        companies1 = get_companies_by_sector("Retail")
        companies2 = get_companies_by_sector("retail")
        assert len(companies1) == len(companies2)

    def test_invalid_sector(self):
        """Should raise ValueError for invalid sector"""
        with pytest.raises(ValueError, match="No companies found"):
            get_companies_by_sector("InvalidSector")


class TestGetAllSectors:
    """Test sector enumeration"""

    def test_get_all_sectors(self):
        """Should return all 8 unique sectors"""
        sectors = get_all_sectors()
        assert len(sectors) == 8
        expected_sectors = [
            "Energy",
            "Financial Services",
            "Food & Beverage",
            "Healthcare",
            "Manufacturing",
            "Real Estate",
            "Retail",
            "Technology"
        ]
        assert sorted(sectors) == sorted(expected_sectors)


class TestGetTemplateById:
    """Test template retrieval by ID"""

    def test_get_v3_template(self):
        """Should retrieve V3 template by ID"""
        template = get_template_by_id("V3_A1")
        assert template['id'] == "V3_A1"
        assert template['difficulty'] == "basic"
        assert 'Current Ratio' in template['verification_identity']

    def test_get_v4_template(self):
        """Should retrieve V4 template by ID"""
        template = get_template_by_id("V4_A2")
        assert template['id'] == "V4_A2"
        assert 'DuPont' in template['verification_identity']

    def test_get_v5_template(self):
        """Should retrieve V5 template by ID"""
        template = get_template_by_id("V5_A1")
        assert template['id'] == "V5_A1"
        assert 'Free Cash Flow' in template['verification_identity']

    def test_invalid_template_id(self):
        """Should raise ValueError for invalid template ID"""
        with pytest.raises(ValueError):
            get_template_by_id("V999_Z99")


class TestDataQuality:
    """Test data quality and consistency"""

    def test_all_companies_have_unique_tickers(self):
        """Each company should have a unique ticker"""
        companies = load_companies()
        tickers = [c.ticker for c in companies]
        assert len(tickers) == len(set(tickers))

    def test_all_sectors_have_two_companies(self):
        """Each sector should have exactly 2 companies"""
        companies = load_companies()
        sectors = {}
        for company in companies:
            if company.sector not in sectors:
                sectors[company.sector] = 0
            sectors[company.sector] += 1

        for sector, count in sectors.items():
            assert count == 2, f"Sector {sector} has {count} companies, expected 2"

    def test_market_cap_calculation(self):
        """Market cap should approximately equal share price × shares outstanding"""
        companies = load_companies()
        for company in companies:
            calculated_market_cap = company.share_price * company.shares_outstanding
            # Allow 1% tolerance
            tolerance = 0.01 * company.market_cap
            assert abs(company.market_cap - calculated_market_cap) < tolerance, \
                f"{company.name}: Market cap mismatch"

    def test_pe_ratio_consistency(self):
        """P/E ratio should be consistent with market cap and net income"""
        companies = load_companies()
        for company in companies:
            if company.net_income > 0:
                expected_pe = company.market_cap / company.net_income
                # Allow small rounding differences
                assert abs(company.pe_ratio - expected_pe) < 0.01, \
                    f"{company.name}: P/E ratio inconsistent"


if __name__ == "__main__":
    # Run tests with verbose output
    pytest.main([__file__, "-v"])
