"""
Exercise Generator for ECONAN

This module generates verification exercises by combining:
- Company financial data from company_data.yaml
- Exercise templates from exercise_templates.yaml
- Jinja2 template rendering for variable substitution
- Distractor answer generation for multiple choice

Functions:
    - generate_exercise: Generate a single exercise from template + company
    - generate_exercises_for_company: Generate all exercises for one company
    - generate_exercises_by_category: Generate exercises for a category (V3/V4/V5)
    - calculate_ratio_value: Calculate financial ratio from company data
"""

from typing import List, Dict, Optional, Tuple
from jinja2 import Template
import random
from decimal import Decimal, ROUND_HALF_UP

from .data_models import Company, Exercise
from .config_loader import (
    load_companies,
    load_exercise_templates,
    get_company_by_ticker,
    get_template_by_id
)


def calculate_ratio_value(company: Company, ratio_name: str) -> float:
    """
    Calculate a specific financial ratio for a company.

    Args:
        company: Company object with financial data
        ratio_name: Name of the ratio to calculate
                   Options: current_ratio, de_ratio, leverage, roe, roe_pct,
                           net_margin, asset_turnover, operating_margin,
                           operating_margin_pct, pe_ratio, earnings_yield,
                           earnings_yield_pct, eps, fcf_m, working_capital_m,
                           ocf_margin, ocf_margin_pct, cash_conversion,
                           net_cash_change_m

    Returns:
        float: Calculated ratio value

    Raises:
        ValueError: If ratio_name is not recognized
    """
    # Direct property access
    if hasattr(company, ratio_name):
        return getattr(company, ratio_name)

    # Calculate derived metrics
    calculations = {
        'roe_pct': lambda: company.roe * 100,
        'operating_margin_pct': lambda: company.operating_margin * 100,
        'earnings_yield_pct': lambda: company.earnings_yield * 100,
        'eps': lambda: company.net_income / company.shares_outstanding,
        'fcf_m': lambda: company.operating_cash_flow - company.investing_cash_flow,
        'working_capital_m': lambda: company.current_assets - company.current_liabilities,
        'ocf_margin': lambda: company.operating_cash_flow / company.revenue,
        'ocf_margin_pct': lambda: (company.operating_cash_flow / company.revenue) * 100,
        'cash_conversion': lambda: company.operating_cash_flow / company.net_income if company.net_income > 0 else 0,
        'net_cash_change_m': lambda: company.operating_cash_flow + company.investing_cash_flow + company.financing_cash_flow,
        'leverage_alt': lambda: 1 + company.debt_to_equity,
        'roe_dupont': lambda: company.net_margin * company.asset_turnover * (company.total_assets / company.total_equity)
    }

    if ratio_name in calculations:
        return calculations[ratio_name]()

    raise ValueError(f"Unknown ratio name: {ratio_name}")


def format_number(value: float, decimal_places: int = 2) -> str:
    """
    Format a number with specified decimal places.

    Args:
        value: Number to format
        decimal_places: Number of decimal places (default: 2)

    Returns:
        str: Formatted number string
    """
    decimal_value = Decimal(str(value))
    quantizer = Decimal('0.1') ** decimal_places
    rounded = decimal_value.quantize(quantizer, rounding=ROUND_HALF_UP)
    return str(rounded)


def prepare_template_variables(company: Company, template: Dict) -> Dict:
    """
    Prepare all variables needed for template rendering.

    Args:
        company: Company object with financial data
        template: Exercise template dictionary

    Returns:
        Dict: Dictionary with all template variables populated
    """
    # Start with basic company info
    variables = {
        'company_name': company.name,
        'ticker': company.ticker,
        'sector': company.sector,
        'year': company.year,
    }

    # Add financial statement data (in millions)
    variables.update({
        'current_assets_m': format_number(company.current_assets, 0),
        'current_liabilities_m': format_number(company.current_liabilities, 0),
        'total_assets_m': format_number(company.total_assets, 0),
        'total_equity_m': format_number(company.total_equity, 0),
        'total_debt_m': format_number(company.total_debt, 0),
        'revenue_m': format_number(company.revenue, 0),
        'operating_income_m': format_number(company.operating_income, 0),
        'net_income_m': format_number(company.net_income, 0),
        'operating_cf_m': format_number(company.operating_cash_flow, 0),
        'investing_cf_m': format_number(company.investing_cash_flow, 0),
        'financing_cf_m': format_number(company.financing_cash_flow, 0),
        'market_cap_m': format_number(company.market_cap, 0),
        'share_price': format_number(company.share_price, 2),
        'shares_outstanding_m': format_number(company.shares_outstanding, 1),
    })

    # Add calculated ratios
    variables.update({
        'current_ratio': format_number(company.current_ratio, 2),
        'de_ratio': format_number(company.debt_to_equity, 2),
        'leverage': format_number(company.total_assets / company.total_equity, 2),
        'leverage_alt': format_number(1 + company.debt_to_equity, 2),
        'roe': format_number(company.roe, 3),
        'roe_pct': format_number(company.roe * 100, 1),
        'net_margin': format_number(company.operating_income / company.revenue, 3),
        'asset_turnover': format_number(company.asset_turnover, 2),
        'operating_margin': format_number(company.operating_margin, 3),
        'operating_margin_pct': format_number(company.operating_margin * 100, 1),
        'pe_ratio': format_number(company.pe_ratio, 1),
        'pe_ratio_alt': format_number(company.pe_ratio, 1),
        'earnings_yield': format_number(company.earnings_yield, 3),
        'earnings_yield_alt': format_number(1 / company.pe_ratio if company.pe_ratio > 0 else 0, 3),
        'earnings_yield_pct': format_number(company.earnings_yield * 100, 1),
        'eps': format_number(company.net_income / company.shares_outstanding, 2),
    })

    # Add cash flow metrics
    fcf = company.operating_cash_flow - company.investing_cash_flow
    working_capital = company.current_assets - company.current_liabilities
    ocf_margin = company.operating_cash_flow / company.revenue if company.revenue > 0 else 0
    cash_conversion = company.operating_cash_flow / company.net_income if company.net_income > 0 else 0
    net_cash_change = company.operating_cash_flow + company.investing_cash_flow + company.financing_cash_flow

    variables.update({
        'fcf_m': format_number(fcf, 0),
        'working_capital_m': format_number(working_capital, 0),
        'ocf_margin': format_number(ocf_margin, 3),
        'ocf_margin_pct': format_number(ocf_margin * 100, 1),
        'cash_conversion': format_number(cash_conversion, 2),
        'net_cash_change_m': format_number(net_cash_change, 0),
        'roe_dupont': format_number(company.roe, 3),
        'roe_direct': format_number(company.roe, 3),
    })

    # Add interpretation text based on cash conversion ratio
    if cash_conversion > 1.0:
        interpretation = "Het bedrijf genereert meer cash dan gerapporteerde winst (hoge kwaliteit van winst)"
    elif cash_conversion < 1.0:
        interpretation = "Het bedrijf genereert minder cash dan winst (mogelijk werkkapitaal issues)"
    else:
        interpretation = "Cash generatie komt overeen met gerapporteerde winst"

    variables['interpretation_cash_conversion'] = interpretation

    return variables


def generate_exercise(
    template_id: str,
    company: Company,
    templates: Optional[Dict] = None
) -> Exercise:
    """
    Generate a single exercise from a template and company data.

    Args:
        template_id: Exercise template ID (e.g., "V3_A1", "V4_B2")
        company: Company object with financial data
        templates: Optional pre-loaded templates (if None, will load from file)

    Returns:
        Exercise: Generated exercise with question, solution, and distractors

    Raises:
        ValueError: If template_id is invalid or generation fails
    """
    # Load template
    template = get_template_by_id(template_id, templates)

    # Determine category from template ID
    category = template_id.split('_')[0].upper()

    # Prepare variables for template rendering
    variables = prepare_template_variables(company, template)

    # Render question template
    question_template = Template(template['question_template'])
    question_nl = question_template.render(**variables)

    # Render solution steps
    solution_steps = []
    for step in template['solution_steps']:
        step_template = Template(step)
        rendered_step = step_template.render(**variables)
        solution_steps.append(rendered_step)

    # Determine correct answer based on verification identity
    correct_answer = extract_correct_answer(template, variables)

    # Generate distractor answers
    distractor_answers = generate_distractors(correct_answer, template, company)

    # Create Exercise object
    exercise = Exercise(
        exercise_id=template_id,
        category=category,
        difficulty=template['difficulty'],
        company=company,
        question_nl=question_nl,
        solution_steps=solution_steps,
        correct_answer=correct_answer,
        distractor_answers=distractor_answers,
        verification_identity=template['verification_identity'],
        learning_objective=template['learning_objective']
    )

    return exercise


def extract_correct_answer(template: Dict, variables: Dict) -> str:
    """
    Extract the correct answer from the verification identity and variables.

    Args:
        template: Exercise template dictionary
        variables: Rendered template variables

    Returns:
        str: Correct answer formatted as a string
    """
    # Parse the verification identity to determine which variable is the answer
    identity = template['verification_identity']
    template_id = template['id']

    # Map template IDs to their answer variables
    answer_mappings = {
        'V3_A1': 'current_ratio',
        'V3_A2': 'working_capital_m',
        'V3_B1': 'de_ratio',
        'V3_B2': 'leverage',
        'V4_A1': 'roe_pct',
        'V4_A2': 'roe_pct',
        'V4_B1': 'pe_ratio',
        'V4_B2': 'earnings_yield_pct',
        'V4_C1': 'operating_margin_pct',
        'V5_A1': 'fcf_m',
        'V5_A2': 'net_cash_change_m',
        'V5_B1': 'ocf_margin_pct',
        'V5_B2': 'cash_conversion',
    }

    if template_id not in answer_mappings:
        raise ValueError(f"No answer mapping for template {template_id}")

    answer_key = answer_mappings[template_id]
    answer_value = variables.get(answer_key, "N/A")

    # Format answer with appropriate units
    if template_id in ['V3_A2', 'V5_A1', 'V5_A2']:
        return f"€{answer_value} miljoen"
    elif template_id in ['V4_A1', 'V4_A2', 'V4_B2', 'V4_C1', 'V5_B1']:
        return f"{answer_value}%"
    else:
        return str(answer_value)


def generate_distractors(correct_answer: str, template: Dict, company: Company) -> List[str]:
    """
    Generate plausible distractor answers for multiple choice.

    Args:
        correct_answer: The correct answer string
        template: Exercise template dictionary
        company: Company object (for contextual distractors)

    Returns:
        List[str]: List of 3 distractor answers
    """
    # Extract numeric value from correct answer
    numeric_value = extract_numeric_value(correct_answer)

    # Generate distractors based on common calculation errors
    distractors = []

    # Distractor 1: Off by ±10-20%
    distractor1 = numeric_value * random.choice([0.85, 0.90, 1.10, 1.15])

    # Distractor 2: Off by ±30-40%
    distractor2 = numeric_value * random.choice([0.65, 0.70, 1.30, 1.35])

    # Distractor 3: Inverse or reciprocal error (common mistake)
    if numeric_value > 0:
        distractor3 = 1 / numeric_value if numeric_value < 10 else numeric_value / 2
    else:
        distractor3 = numeric_value * 1.50

    # Format distractors with same units as correct answer
    for distractor_value in [distractor1, distractor2, distractor3]:
        if '€' in correct_answer and 'miljoen' in correct_answer:
            distractors.append(f"€{format_number(distractor_value, 0)} miljoen")
        elif '%' in correct_answer:
            distractors.append(f"{format_number(distractor_value, 1)}%")
        else:
            distractors.append(format_number(distractor_value, 2))

    return distractors


def extract_numeric_value(answer_string: str) -> float:
    """
    Extract numeric value from formatted answer string.

    Args:
        answer_string: Formatted answer (e.g., "€1,234 miljoen", "12.5%", "0.78")

    Returns:
        float: Numeric value
    """
    # Remove currency symbols, percentage signs, and text
    clean_string = answer_string.replace('€', '').replace('%', '').replace('miljoen', '').strip()

    # Remove thousand separators
    clean_string = clean_string.replace(',', '')

    try:
        return float(clean_string)
    except ValueError:
        return 0.0


def generate_exercises_for_company(
    company: Company,
    category: Optional[str] = None,
    templates: Optional[Dict] = None
) -> List[Exercise]:
    """
    Generate all exercises for a single company.

    Args:
        company: Company object with financial data
        category: Optional category filter ("V3", "V4", "V5")
                 If None, generates all exercises
        templates: Optional pre-loaded templates

    Returns:
        List[Exercise]: List of generated exercises
    """
    if templates is None:
        templates = load_exercise_templates()

    exercises = []

    # Determine which template categories to use
    if category:
        template_keys = [f"{category.lower()}_exercises"]
    else:
        template_keys = ['v3_exercises', 'v4_exercises', 'v5_exercises']

    # Generate exercises from each template
    for key in template_keys:
        for template in templates.get(key, []):
            template_id = template['id']
            try:
                exercise = generate_exercise(template_id, company, templates)
                exercises.append(exercise)
            except Exception as e:
                print(f"Warning: Failed to generate {template_id} for {company.name}: {e}")

    return exercises


def generate_exercises_by_category(
    category: str,
    companies: Optional[List[Company]] = None,
    templates: Optional[Dict] = None
) -> List[Exercise]:
    """
    Generate all exercises for a specific category across all companies.

    Args:
        category: Exercise category ("V3", "V4", "V5")
        companies: Optional pre-loaded companies (if None, will load from file)
        templates: Optional pre-loaded templates (if None, will load from file)

    Returns:
        List[Exercise]: List of generated exercises for the category
    """
    if companies is None:
        companies = load_companies()

    if templates is None:
        templates = load_exercise_templates(category=category.lower())

    exercises = []

    for company in companies:
        company_exercises = generate_exercises_for_company(company, category, templates)
        exercises.extend(company_exercises)

    return exercises


if __name__ == "__main__":
    # Test exercise generation
    print("Testing exercise generation...")

    # Load data
    companies = load_companies()
    test_company = companies[0]  # Ahold Delhaize

    # Generate V3_A1 exercise
    exercise = generate_exercise("V3_A1", test_company)

    print(f"\n{'='*80}")
    print(f"Exercise: {exercise.exercise_id}")
    print(f"Company: {exercise.company.name}")
    print(f"Category: {exercise.category}")
    print(f"Difficulty: {exercise.difficulty}")
    print(f"{'='*80}\n")
    print("Question:")
    print(exercise.question_nl)
    print(f"\n{'='*80}\n")
    print("Solution Steps:")
    for i, step in enumerate(exercise.solution_steps, 1):
        print(f"{i}. {step}")
    print(f"\n{'='*80}\n")
    print(f"Correct Answer: {exercise.correct_answer}")
    print(f"Distractors: {', '.join(exercise.distractor_answers)}")
    print(f"\n{'='*80}\n")
