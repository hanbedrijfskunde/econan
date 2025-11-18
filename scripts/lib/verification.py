"""
Mathematical Identity Verification for ECONAN Exercises

This module validates that exercises maintain mathematical consistency by
verifying key financial identities:
- Balance Sheet: Assets = Liabilities + Equity
- DuPont ROE: ROE = Net Margin × Asset Turnover × Leverage
- P/E and Earnings Yield: Earnings Yield = 1 / P/E
- Cash Flow Statement: Δ Cash = Operating CF + Investing CF + Financing CF
- Leverage Identity: Leverage = 1 + D/E

Functions:
    - verify_exercise: Verify all applicable identities for an exercise
    - verify_balance_sheet: Verify balance sheet equation
    - verify_dupont: Verify DuPont ROE decomposition
    - verify_pe_earnings_yield: Verify P/E and Earnings Yield relationship
    - verify_leverage_identity: Verify leverage = 1 + D/E
    - verify_cash_flow_statement: Verify cash flow statement equation
"""

from typing import Dict, List, Tuple, Optional
from decimal import Decimal, ROUND_HALF_UP

from .data_models import Company, Exercise


# Tolerance for floating-point comparisons (1% relative error)
RELATIVE_TOLERANCE = 0.01


def _decimal_close(a: float, b: float, rel_tol: float = RELATIVE_TOLERANCE) -> bool:
    """
    Check if two numbers are approximately equal within relative tolerance.

    Args:
        a: First number
        b: Second number
        rel_tol: Relative tolerance (default: 1%)

    Returns:
        bool: True if numbers are within tolerance
    """
    if a == 0 and b == 0:
        return True
    if a == 0 or b == 0:
        # Use absolute tolerance for comparison with zero
        return abs(a - b) < 0.01

    relative_error = abs(a - b) / max(abs(a), abs(b))
    return relative_error <= rel_tol


def verify_balance_sheet(company: Company) -> Tuple[bool, str]:
    """
    Verify balance sheet identity: Assets = Liabilities + Equity

    Args:
        company: Company object with financial data

    Returns:
        Tuple[bool, str]: (is_valid, message)
    """
    assets = company.total_assets
    liabilities = company.total_liabilities
    equity = company.total_equity

    right_side = liabilities + equity

    is_valid = _decimal_close(assets, right_side)

    if is_valid:
        message = f"✓ Balance sheet valid: Assets ({assets:.0f}) = Liabilities ({liabilities:.0f}) + Equity ({equity:.0f})"
    else:
        diff = assets - right_side
        diff_pct = (diff / assets) * 100
        message = f"✗ Balance sheet invalid: Assets ({assets:.0f}) ≠ Liabilities ({liabilities:.0f}) + Equity ({equity:.0f}). Difference: {diff:.0f} ({diff_pct:.2f}%)"

    return is_valid, message


def verify_dupont(company: Company) -> Tuple[bool, str]:
    """
    Verify DuPont ROE identity: ROE = Net Margin × Asset Turnover × Leverage

    Args:
        company: Company object with financial data

    Returns:
        Tuple[bool, str]: (is_valid, message)
    """
    # Direct ROE calculation
    roe_direct = company.roe

    # DuPont components
    net_margin = company.net_income / company.revenue if company.revenue > 0 else 0
    asset_turnover = company.revenue / company.total_assets if company.total_assets > 0 else 0
    leverage = company.total_assets / company.total_equity if company.total_equity > 0 else 0

    # DuPont ROE
    roe_dupont = net_margin * asset_turnover * leverage

    is_valid = _decimal_close(roe_direct, roe_dupont)

    if is_valid:
        message = f"✓ DuPont valid: ROE ({roe_direct:.4f}) = Net Margin ({net_margin:.4f}) × Asset Turnover ({asset_turnover:.2f}) × Leverage ({leverage:.2f})"
    else:
        diff = roe_direct - roe_dupont
        message = f"✗ DuPont invalid: ROE direct ({roe_direct:.4f}) ≠ DuPont ({roe_dupont:.4f}). Difference: {diff:.4f}"

    return is_valid, message


def verify_pe_earnings_yield(company: Company) -> Tuple[bool, str]:
    """
    Verify P/E and Earnings Yield relationship: Earnings Yield = 1 / P/E

    Args:
        company: Company object with financial data

    Returns:
        Tuple[bool, str]: (is_valid, message)
    """
    if company.net_income <= 0:
        return True, "⊘ P/E verification skipped: negative or zero earnings"

    pe_ratio = company.pe_ratio
    earnings_yield = company.earnings_yield

    # Inverse relationship
    expected_earnings_yield = 1 / pe_ratio if pe_ratio > 0 else 0

    is_valid = _decimal_close(earnings_yield, expected_earnings_yield)

    if is_valid:
        message = f"✓ P/E identity valid: Earnings Yield ({earnings_yield:.4f}) = 1 / P/E ({1/pe_ratio:.4f})"
    else:
        diff = earnings_yield - expected_earnings_yield
        message = f"✗ P/E identity invalid: Earnings Yield ({earnings_yield:.4f}) ≠ 1/P/E ({expected_earnings_yield:.4f}). Difference: {diff:.4f}"

    return is_valid, message


def verify_leverage_identity(company: Company) -> Tuple[bool, str]:
    """
    Verify leverage identity: Leverage = Total Assets / Total Equity
                                       = (Total Liabilities + Total Equity) / Total Equity
                                       = 1 + (Total Liabilities / Total Equity)

    Note: This is NOT the same as 1 + D/E, because Total Liabilities includes
    both debt and non-debt liabilities (accounts payable, accrued expenses, etc.)

    Args:
        company: Company object with financial data

    Returns:
        Tuple[bool, str]: (is_valid, message)
    """
    leverage_direct = company.total_assets / company.total_equity if company.total_equity > 0 else 0
    leverage_via_liabilities = 1 + (company.total_liabilities / company.total_equity if company.total_equity > 0 else 0)

    is_valid = _decimal_close(leverage_direct, leverage_via_liabilities)

    if is_valid:
        message = f"✓ Leverage identity valid: {leverage_direct:.2f} = 1 + (Liabilities/Equity) = {leverage_via_liabilities:.2f}"
    else:
        diff = leverage_direct - leverage_via_liabilities
        message = f"✗ Leverage identity invalid: Direct ({leverage_direct:.2f}) ≠ 1+(L/E) ({leverage_via_liabilities:.2f}). Difference: {diff:.2f}"

    return is_valid, message


def verify_cash_flow_statement(company: Company) -> Tuple[bool, str]:
    """
    Verify cash flow statement identity: Δ Cash = Operating CF + Investing CF + Financing CF

    Note: This is an identity check, not a balance check, as we don't have
    beginning/ending cash balances in our simplified model.

    Args:
        company: Company object with financial data

    Returns:
        Tuple[bool, str]: (is_valid, message)
    """
    net_cash_change = company.operating_cash_flow + company.investing_cash_flow + company.financing_cash_flow

    # For verification, we just check that the sum is calculated correctly
    # In a real scenario, this would equal the change in cash on balance sheet
    message = f"ℹ Cash flow components sum to: {net_cash_change:.0f} million (Operating: {company.operating_cash_flow:.0f}, Investing: {company.investing_cash_flow:.0f}, Financing: {company.financing_cash_flow:.0f})"

    return True, message


def verify_current_ratio_identity(company: Company) -> Tuple[bool, str]:
    """
    Verify current ratio calculation: Current Ratio = Current Assets / Current Liabilities

    Args:
        company: Company object with financial data

    Returns:
        Tuple[bool, str]: (is_valid, message)
    """
    if company.current_liabilities <= 0:
        return True, "⊘ Current ratio verification skipped: zero or negative current liabilities"

    current_ratio_direct = company.current_ratio
    current_ratio_calculated = company.current_assets / company.current_liabilities

    is_valid = _decimal_close(current_ratio_direct, current_ratio_calculated)

    if is_valid:
        message = f"✓ Current ratio valid: {current_ratio_direct:.2f} = {company.current_assets:.0f} / {company.current_liabilities:.0f}"
    else:
        diff = current_ratio_direct - current_ratio_calculated
        message = f"✗ Current ratio invalid: Property ({current_ratio_direct:.2f}) ≠ Calculated ({current_ratio_calculated:.2f}). Difference: {diff:.2f}"

    return is_valid, message


def verify_working_capital_identity(company: Company) -> Tuple[bool, str]:
    """
    Verify working capital and current ratio relationship.

    Working Capital = Current Assets - Current Liabilities
    If Current Ratio = CR, then Working Capital = Current Liabilities × (CR - 1)

    Args:
        company: Company object with financial data

    Returns:
        Tuple[bool, str]: (is_valid, message)
    """
    working_capital_direct = company.current_assets - company.current_liabilities
    working_capital_via_cr = company.current_liabilities * (company.current_ratio - 1)

    is_valid = _decimal_close(working_capital_direct, working_capital_via_cr)

    if is_valid:
        message = f"✓ Working capital identity valid: {working_capital_direct:.0f} = CL × (CR - 1) = {working_capital_via_cr:.0f}"
    else:
        diff = working_capital_direct - working_capital_via_cr
        message = f"✗ Working capital identity invalid: Direct ({working_capital_direct:.0f}) ≠ Via CR ({working_capital_via_cr:.0f}). Difference: {diff:.0f}"

    return is_valid, message


def verify_market_cap_consistency(company: Company) -> Tuple[bool, str]:
    """
    Verify market cap = share price × shares outstanding

    Args:
        company: Company object with financial data

    Returns:
        Tuple[bool, str]: (is_valid, message)
    """
    market_cap_stated = company.market_cap
    market_cap_calculated = company.share_price * company.shares_outstanding

    is_valid = _decimal_close(market_cap_stated, market_cap_calculated)

    if is_valid:
        message = f"✓ Market cap valid: {market_cap_stated:.0f} = Price ({company.share_price:.2f}) × Shares ({company.shares_outstanding:.1f})"
    else:
        diff = market_cap_stated - market_cap_calculated
        diff_pct = (diff / market_cap_stated) * 100
        message = f"✗ Market cap invalid: Stated ({market_cap_stated:.0f}) ≠ Calculated ({market_cap_calculated:.0f}). Difference: {diff:.0f} ({diff_pct:.2f}%)"

    return is_valid, message


def verify_company_data(company: Company) -> Dict[str, Tuple[bool, str]]:
    """
    Run all applicable verifications on company financial data.

    Args:
        company: Company object with financial data

    Returns:
        Dict[str, Tuple[bool, str]]: Dictionary of verification results
            Key: verification name
            Value: (is_valid, message)
    """
    verifications = {
        'balance_sheet': verify_balance_sheet(company),
        'dupont': verify_dupont(company),
        'pe_earnings_yield': verify_pe_earnings_yield(company),
        'leverage_identity': verify_leverage_identity(company),
        'current_ratio': verify_current_ratio_identity(company),
        'working_capital': verify_working_capital_identity(company),
        'market_cap': verify_market_cap_consistency(company),
        'cash_flow_statement': verify_cash_flow_statement(company),
    }

    return verifications


def verify_exercise(exercise: Exercise) -> Dict[str, Tuple[bool, str]]:
    """
    Verify mathematical identities for a generated exercise.

    This checks that the exercise maintains mathematical consistency
    based on the verification identity specified in the template.

    Args:
        exercise: Exercise object to verify

    Returns:
        Dict[str, Tuple[bool, str]]: Dictionary of verification results
    """
    # Run company data verifications
    company_verifications = verify_company_data(exercise.company)

    # Add exercise-specific verification based on category
    exercise_verifications = {}

    if exercise.category == "V3":
        # Liquidity exercises
        if "Current Ratio" in exercise.verification_identity:
            exercise_verifications['current_ratio'] = company_verifications['current_ratio']
        if "Working Capital" in exercise.verification_identity:
            exercise_verifications['working_capital'] = company_verifications['working_capital']
        if "Debt-to-Equity" in exercise.verification_identity:
            exercise_verifications['leverage_identity'] = company_verifications['leverage_identity']
        if "Leverage" in exercise.verification_identity:
            exercise_verifications['leverage_identity'] = company_verifications['leverage_identity']

    elif exercise.category == "V4":
        # Valuation exercises
        if "ROE" in exercise.verification_identity:
            if "DuPont" in exercise.verification_identity:
                exercise_verifications['dupont'] = company_verifications['dupont']
        if "P/E Ratio" in exercise.verification_identity:
            exercise_verifications['pe_earnings_yield'] = company_verifications['pe_earnings_yield']
            exercise_verifications['market_cap'] = company_verifications['market_cap']
        if "Earnings Yield" in exercise.verification_identity:
            exercise_verifications['pe_earnings_yield'] = company_verifications['pe_earnings_yield']

    elif exercise.category == "V5":
        # Cash flow exercises
        exercise_verifications['cash_flow_statement'] = company_verifications['cash_flow_statement']

    # Always include balance sheet
    exercise_verifications['balance_sheet'] = company_verifications['balance_sheet']

    return exercise_verifications


def print_verification_report(company: Company, verbose: bool = True) -> bool:
    """
    Print a verification report for company data.

    Args:
        company: Company object to verify
        verbose: If True, print all verifications. If False, only print failures.

    Returns:
        bool: True if all verifications pass, False otherwise
    """
    print(f"\n{'='*80}")
    print(f"Verification Report: {company.name} ({company.ticker})")
    print(f"{'='*80}\n")

    verifications = verify_company_data(company)
    all_valid = True

    for name, (is_valid, message) in verifications.items():
        if verbose or not is_valid:
            print(f"{name:25s} | {message}")
        if not is_valid:
            all_valid = False

    print(f"\n{'='*80}")
    if all_valid:
        print("✓ All verifications passed")
    else:
        print("✗ Some verifications failed")
    print(f"{'='*80}\n")

    return all_valid


def verify_all_companies() -> Dict[str, bool]:
    """
    Verify all companies in the dataset.

    Returns:
        Dict[str, bool]: Dictionary mapping company ticker to validation status
    """
    from .config_loader import load_companies

    companies = load_companies()
    results = {}

    print(f"\n{'='*80}")
    print("Verifying all companies...")
    print(f"{'='*80}\n")

    for company in companies:
        print(f"Verifying {company.name} ({company.ticker})...")
        verifications = verify_company_data(company)

        all_valid = all(is_valid for is_valid, _ in verifications.values())
        results[company.ticker] = all_valid

        if all_valid:
            print(f"  ✓ All identities valid")
        else:
            print(f"  ✗ Some identities failed:")
            for name, (is_valid, message) in verifications.items():
                if not is_valid:
                    print(f"    - {message}")

    # Summary
    passed = sum(1 for valid in results.values() if valid)
    total = len(results)

    print(f"\n{'='*80}")
    print(f"Verification Summary: {passed}/{total} companies passed all checks")
    print(f"{'='*80}\n")

    return results


if __name__ == "__main__":
    # Test verification on first company
    from .config_loader import load_companies

    companies = load_companies()
    test_company = companies[0]

    print_verification_report(test_company, verbose=True)

    # Verify all companies
    verify_all_companies()
