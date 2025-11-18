"""
Unit tests for verification module

Tests mathematical identity verification for financial data.
Run with: pytest tests/test_verification.py
"""

import pytest
from pathlib import Path
import sys

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from lib.verification import (
    verify_balance_sheet,
    verify_dupont,
    verify_pe_earnings_yield,
    verify_leverage_identity,
    verify_current_ratio_identity,
    verify_working_capital_identity,
    verify_market_cap_consistency,
    verify_company_data,
    verify_exercise
)
from lib.config_loader import load_companies
from lib.exercise_generator import generate_exercise


class TestBalanceSheetVerification:
    """Test balance sheet identity verification"""

    def test_balance_sheet_valid(self):
        """All companies should have valid balance sheets"""
        companies = load_companies()

        for company in companies:
            is_valid, message = verify_balance_sheet(company)
            assert is_valid, f"{company.name}: {message}"

    def test_balance_sheet_formula(self):
        """Balance sheet formula should be Assets = Liabilities + Equity"""
        companies = load_companies()
        company = companies[0]

        calculated_assets = company.total_liabilities + company.total_equity
        assert abs(company.total_assets - calculated_assets) / company.total_assets < 0.01


class TestDuPontVerification:
    """Test DuPont ROE identity verification"""

    def test_dupont_valid(self):
        """All companies should satisfy DuPont identity"""
        companies = load_companies()

        for company in companies:
            is_valid, message = verify_dupont(company)
            assert is_valid, f"{company.name}: {message}"

    def test_dupont_formula(self):
        """DuPont: ROE = Net Margin × Asset Turnover × Leverage"""
        companies = load_companies()
        company = companies[0]

        roe_direct = company.roe
        net_margin = company.net_income / company.revenue
        asset_turnover = company.revenue / company.total_assets
        leverage = company.total_assets / company.total_equity
        roe_dupont = net_margin * asset_turnover * leverage

        assert abs(roe_direct - roe_dupont) / roe_direct < 0.01


class TestPERatioVerification:
    """Test P/E ratio and Earnings Yield relationship"""

    def test_pe_earnings_yield_valid(self):
        """All companies should satisfy P/E and Earnings Yield relationship"""
        companies = load_companies()

        for company in companies:
            if company.net_income > 0:
                is_valid, message = verify_pe_earnings_yield(company)
                assert is_valid, f"{company.name}: {message}"

    def test_pe_earnings_yield_formula(self):
        """Earnings Yield = 1 / P/E Ratio"""
        companies = load_companies()
        company = companies[0]

        earnings_yield = company.earnings_yield
        pe_ratio = company.pe_ratio
        expected_earnings_yield = 1 / pe_ratio

        assert abs(earnings_yield - expected_earnings_yield) / earnings_yield < 0.01


class TestLeverageIdentity:
    """Test leverage identity verification"""

    def test_leverage_identity_valid(self):
        """All companies should satisfy leverage identity"""
        companies = load_companies()

        for company in companies:
            is_valid, message = verify_leverage_identity(company)
            assert is_valid, f"{company.name}: {message}"

    def test_leverage_formula(self):
        """Leverage = 1 + (Total Liabilities / Total Equity)"""
        companies = load_companies()
        company = companies[0]

        leverage_direct = company.total_assets / company.total_equity
        leverage_via_liabilities = 1 + (company.total_liabilities / company.total_equity)

        assert abs(leverage_direct - leverage_via_liabilities) / leverage_direct < 0.01


class TestCurrentRatioVerification:
    """Test current ratio calculation"""

    def test_current_ratio_valid(self):
        """All companies should have valid current ratio"""
        companies = load_companies()

        for company in companies:
            is_valid, message = verify_current_ratio_identity(company)
            assert is_valid, f"{company.name}: {message}"

    def test_current_ratio_formula(self):
        """Current Ratio = Current Assets / Current Liabilities"""
        companies = load_companies()
        company = companies[0]

        current_ratio_property = company.current_ratio
        current_ratio_calculated = company.current_assets / company.current_liabilities

        assert abs(current_ratio_property - current_ratio_calculated) < 0.01


class TestWorkingCapitalVerification:
    """Test working capital identity"""

    def test_working_capital_valid(self):
        """All companies should satisfy working capital identity"""
        companies = load_companies()

        for company in companies:
            is_valid, message = verify_working_capital_identity(company)
            assert is_valid, f"{company.name}: {message}"

    def test_working_capital_formula(self):
        """Working Capital = Current Assets - Current Liabilities"""
        companies = load_companies()
        company = companies[0]

        working_capital_direct = company.current_assets - company.current_liabilities
        working_capital_via_cr = company.current_liabilities * (company.current_ratio - 1)

        assert abs(working_capital_direct - working_capital_via_cr) < 1.0


class TestMarketCapVerification:
    """Test market cap consistency"""

    def test_market_cap_valid(self):
        """All companies should have consistent market cap"""
        companies = load_companies()

        for company in companies:
            is_valid, message = verify_market_cap_consistency(company)
            assert is_valid, f"{company.name}: {message}"

    def test_market_cap_formula(self):
        """Market Cap = Share Price × Shares Outstanding"""
        companies = load_companies()
        company = companies[0]

        market_cap_stated = company.market_cap
        market_cap_calculated = company.share_price * company.shares_outstanding

        assert abs(market_cap_stated - market_cap_calculated) / market_cap_stated < 0.01


class TestCompanyDataVerification:
    """Test complete company data verification"""

    def test_all_companies_pass_verification(self):
        """All 16 companies should pass all verifications"""
        companies = load_companies()

        for company in companies:
            verifications = verify_company_data(company)
            failed = [(name, msg) for name, (valid, msg) in verifications.items() if not valid]

            assert len(failed) == 0, f"{company.name} failed: {failed}"

    def test_verification_includes_all_identities(self):
        """Verification should check all key identities"""
        companies = load_companies()
        company = companies[0]

        verifications = verify_company_data(company)
        expected_verifications = {
            'balance_sheet',
            'dupont',
            'pe_earnings_yield',
            'leverage_identity',
            'current_ratio',
            'working_capital',
            'market_cap',
            'cash_flow_statement'
        }

        assert set(verifications.keys()) == expected_verifications


class TestExerciseVerification:
    """Test exercise-specific verification"""

    def test_v3_exercise_verification(self):
        """V3 exercises should verify liquidity identities"""
        companies = load_companies()
        company = companies[0]

        exercise = generate_exercise("V3_A1", company)
        verifications = verify_exercise(exercise)

        assert 'balance_sheet' in verifications
        assert 'current_ratio' in verifications

    def test_v4_exercise_verification(self):
        """V4 exercises should verify valuation identities"""
        companies = load_companies()
        company = companies[0]

        exercise = generate_exercise("V4_A2", company)
        verifications = verify_exercise(exercise)

        assert 'balance_sheet' in verifications
        assert 'dupont' in verifications

    def test_v5_exercise_verification(self):
        """V5 exercises should verify cash flow identities"""
        companies = load_companies()
        company = companies[0]

        exercise = generate_exercise("V5_A1", company)
        verifications = verify_exercise(exercise)

        assert 'balance_sheet' in verifications
        assert 'cash_flow_statement' in verifications

    def test_all_exercises_verify(self):
        """All generated exercises should pass verification"""
        from lib.exercise_generator import generate_exercises_for_company

        companies = load_companies()
        # Test first 2 companies to save time
        for company in companies[:2]:
            exercises = generate_exercises_for_company(company)

            for exercise in exercises:
                verifications = verify_exercise(exercise)
                failed = [(name, msg) for name, (valid, msg) in verifications.items() if not valid]

                assert len(failed) == 0, f"Exercise {exercise.exercise_id} for {company.name} failed: {failed}"


if __name__ == "__main__":
    # Run tests with verbose output
    pytest.main([__file__, "-v"])
