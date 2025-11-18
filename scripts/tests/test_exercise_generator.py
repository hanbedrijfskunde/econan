"""
Unit tests for exercise_generator module

Tests exercise generation, template rendering, and distractor creation.
Run with: pytest tests/test_exercise_generator.py
"""

import pytest
from pathlib import Path
import sys

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from lib.exercise_generator import (
    generate_exercise,
    generate_exercises_for_company,
    generate_exercises_by_category,
    calculate_ratio_value,
    extract_numeric_value,
    prepare_template_variables
)
from lib.config_loader import load_companies, load_exercise_templates
from lib.data_models import Exercise


class TestGenerateExercise:
    """Test single exercise generation"""

    def test_generate_v3_exercise(self):
        """Should generate V3 (Liquidity) exercise"""
        companies = load_companies()
        company = companies[0]  # Ahold Delhaize

        exercise = generate_exercise("V3_A1", company)

        assert isinstance(exercise, Exercise)
        assert exercise.exercise_id == "V3_A1"
        assert exercise.category == "V3"
        assert exercise.company.name == "Ahold Delhaize"
        assert exercise.difficulty == "basic"

    def test_generate_v4_exercise(self):
        """Should generate V4 (Valuation) exercise"""
        companies = load_companies()
        company = companies[0]

        exercise = generate_exercise("V4_A1", company)

        assert exercise.exercise_id == "V4_A1"
        assert exercise.category == "V4"
        assert "ROE" in exercise.verification_identity

    def test_generate_v5_exercise(self):
        """Should generate V5 (Cash Flow) exercise"""
        companies = load_companies()
        company = companies[0]

        exercise = generate_exercise("V5_A1", company)

        assert exercise.exercise_id == "V5_A1"
        assert exercise.category == "V5"
        assert "Free Cash Flow" in exercise.verification_identity

    def test_exercise_has_question(self):
        """Exercise should have rendered question"""
        companies = load_companies()
        company = companies[0]

        exercise = generate_exercise("V3_A1", company)

        assert exercise.question_nl
        assert company.name in exercise.question_nl
        assert str(company.year) in exercise.question_nl
        # Should not have template variables
        assert "{{" not in exercise.question_nl
        assert "}}" not in exercise.question_nl

    def test_exercise_has_solution_steps(self):
        """Exercise should have rendered solution steps"""
        companies = load_companies()
        company = companies[0]

        exercise = generate_exercise("V3_A1", company)

        assert isinstance(exercise.solution_steps, list)
        assert len(exercise.solution_steps) > 0
        # Solution steps should be rendered (no template variables)
        for step in exercise.solution_steps:
            assert "{{" not in step
            assert "}}" not in step

    def test_exercise_has_correct_answer(self):
        """Exercise should have correct answer"""
        companies = load_companies()
        company = companies[0]

        exercise = generate_exercise("V3_A1", company)

        assert exercise.correct_answer
        assert isinstance(exercise.correct_answer, str)
        # Current ratio answer should be numeric
        assert len(exercise.correct_answer) > 0

    def test_exercise_has_distractors(self):
        """Exercise should have 3 distractor answers"""
        companies = load_companies()
        company = companies[0]

        exercise = generate_exercise("V3_A1", company)

        assert isinstance(exercise.distractor_answers, list)
        assert len(exercise.distractor_answers) == 3
        # All distractors should be different from correct answer
        for distractor in exercise.distractor_answers:
            assert distractor != exercise.correct_answer


class TestCalculateRatioValue:
    """Test ratio calculation"""

    def test_calculate_current_ratio(self):
        """Should calculate current ratio"""
        companies = load_companies()
        company = companies[0]

        ratio = calculate_ratio_value(company, 'current_ratio')
        expected = company.current_assets / company.current_liabilities

        assert abs(ratio - expected) < 0.01

    def test_calculate_roe_pct(self):
        """Should calculate ROE percentage"""
        companies = load_companies()
        company = companies[0]

        ratio = calculate_ratio_value(company, 'roe_pct')
        expected = (company.net_income / company.total_equity) * 100

        assert abs(ratio - expected) < 0.1

    def test_calculate_fcf(self):
        """Should calculate Free Cash Flow"""
        companies = load_companies()
        company = companies[0]

        ratio = calculate_ratio_value(company, 'fcf_m')
        expected = company.operating_cash_flow - company.investing_cash_flow

        assert abs(ratio - expected) < 1.0

    def test_calculate_working_capital(self):
        """Should calculate working capital"""
        companies = load_companies()
        company = companies[0]

        ratio = calculate_ratio_value(company, 'working_capital_m')
        expected = company.current_assets - company.current_liabilities

        assert abs(ratio - expected) < 1.0

    def test_invalid_ratio_name(self):
        """Should raise ValueError for invalid ratio name"""
        companies = load_companies()
        company = companies[0]

        with pytest.raises(ValueError):
            calculate_ratio_value(company, 'invalid_ratio_name')


class TestPrepareTemplateVariables:
    """Test template variable preparation"""

    def test_variables_include_company_info(self):
        """Variables should include basic company info"""
        companies = load_companies()
        company = companies[0]
        template = {"id": "V3_A1"}

        variables = prepare_template_variables(company, template)

        assert variables['company_name'] == company.name
        assert variables['ticker'] == company.ticker
        assert variables['sector'] == company.sector
        assert variables['year'] == company.year

    def test_variables_include_financial_data(self):
        """Variables should include financial statement data"""
        companies = load_companies()
        company = companies[0]
        template = {"id": "V3_A1"}

        variables = prepare_template_variables(company, template)

        assert 'current_assets_m' in variables
        assert 'total_equity_m' in variables
        assert 'revenue_m' in variables
        assert 'operating_cf_m' in variables

    def test_variables_include_calculated_ratios(self):
        """Variables should include calculated ratios"""
        companies = load_companies()
        company = companies[0]
        template = {"id": "V3_A1"}

        variables = prepare_template_variables(company, template)

        assert 'current_ratio' in variables
        assert 'de_ratio' in variables
        assert 'roe' in variables
        assert 'pe_ratio' in variables

    def test_numbers_are_formatted(self):
        """Numbers should be formatted as strings"""
        companies = load_companies()
        company = companies[0]
        template = {"id": "V3_A1"}

        variables = prepare_template_variables(company, template)

        # All values should be strings
        assert isinstance(variables['current_assets_m'], str)
        assert isinstance(variables['current_ratio'], str)
        assert isinstance(variables['roe_pct'], str)


class TestExtractNumericValue:
    """Test numeric value extraction"""

    def test_extract_from_plain_number(self):
        """Should extract from plain number string"""
        assert extract_numeric_value("0.78") == 0.78
        assert extract_numeric_value("123.45") == 123.45

    def test_extract_from_percentage(self):
        """Should extract from percentage"""
        assert extract_numeric_value("24.5%") == 24.5
        assert extract_numeric_value("3.7%") == 3.7

    def test_extract_from_currency(self):
        """Should extract from currency"""
        assert extract_numeric_value("€1234 miljoen") == 1234
        assert extract_numeric_value("€5678 miljoen") == 5678

    def test_extract_with_thousand_separator(self):
        """Should handle thousand separators"""
        assert extract_numeric_value("€1,234 miljoen") == 1234
        assert extract_numeric_value("12,345.67") == 12345.67


class TestGenerateExercisesForCompany:
    """Test batch generation for single company"""

    def test_generate_all_exercises(self):
        """Should generate all exercises for a company"""
        companies = load_companies()
        company = companies[0]

        exercises = generate_exercises_for_company(company)

        # Should have 4 V3 + 5 V4 + 4 V5 = 13 exercises
        assert len(exercises) == 13
        assert all(isinstance(ex, Exercise) for ex in exercises)

    def test_generate_v3_only(self):
        """Should generate only V3 exercises when filtered"""
        companies = load_companies()
        company = companies[0]

        exercises = generate_exercises_for_company(company, category="V3")

        assert len(exercises) == 4
        assert all(ex.category == "V3" for ex in exercises)

    def test_generate_v4_only(self):
        """Should generate only V4 exercises when filtered"""
        companies = load_companies()
        company = companies[0]

        exercises = generate_exercises_for_company(company, category="V4")

        assert len(exercises) == 5
        assert all(ex.category == "V4" for ex in exercises)

    def test_all_exercises_unique(self):
        """All generated exercises should have unique IDs"""
        companies = load_companies()
        company = companies[0]

        exercises = generate_exercises_for_company(company)
        exercise_ids = [ex.exercise_id for ex in exercises]

        assert len(exercise_ids) == len(set(exercise_ids))


class TestGenerateExercisesByCategory:
    """Test batch generation by category"""

    def test_generate_v3_all_companies(self):
        """Should generate V3 exercises for all companies"""
        exercises = generate_exercises_by_category("V3")

        # 4 V3 templates × 16 companies = 64 exercises
        assert len(exercises) == 64
        assert all(ex.category == "V3" for ex in exercises)

    def test_generate_v4_all_companies(self):
        """Should generate V4 exercises for all companies"""
        exercises = generate_exercises_by_category("V4")

        # 5 V4 templates × 16 companies = 80 exercises
        assert len(exercises) == 80
        assert all(ex.category == "V4" for ex in exercises)

    def test_exercises_cover_all_sectors(self):
        """Generated exercises should cover all 8 sectors"""
        exercises = generate_exercises_by_category("V3")
        sectors = set(ex.company.sector for ex in exercises)

        assert len(sectors) == 8
        expected_sectors = {
            "Retail", "Energy", "Financial Services", "Healthcare",
            "Manufacturing", "Food & Beverage", "Technology", "Real Estate"
        }
        assert sectors == expected_sectors


class TestExerciseQuality:
    """Test quality of generated exercises"""

    def test_distractors_are_plausible(self):
        """Distractor answers should be plausible (close to correct answer)"""
        companies = load_companies()
        company = companies[0]

        exercise = generate_exercise("V3_A1", company)
        correct_value = extract_numeric_value(exercise.correct_answer)

        for distractor in exercise.distractor_answers:
            distractor_value = extract_numeric_value(distractor)
            # Distractors should be within 3x of correct answer
            assert distractor_value < correct_value * 3
            assert distractor_value > correct_value * 0.3

    def test_answer_format_consistency(self):
        """Correct answer and distractors should have same format"""
        companies = load_companies()
        company = companies[0]

        # Test percentage answer
        exercise = generate_exercise("V4_A1", company)
        if "%" in exercise.correct_answer:
            for distractor in exercise.distractor_answers:
                assert "%" in distractor

        # Test currency answer
        exercise = generate_exercise("V5_A1", company)
        if "€" in exercise.correct_answer:
            for distractor in exercise.distractor_answers:
                assert "€" in distractor


if __name__ == "__main__":
    # Run tests with verbose output
    pytest.main([__file__, "-v"])
