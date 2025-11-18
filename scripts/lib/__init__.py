"""
ECONAN Exercise Generator Library

This package provides data models and utilities for generating automated
verification exercises for financial analysis education.

Modules:
    - data_models: Core data structures (Company, Exercise)
    - config_loader: YAML configuration loading utilities
    - exercise_generator: Exercise generation with template rendering
    - formatter: Output formatting (Markdown, HTML, JSON)
    - verification: Mathematical identity verification
"""

__version__ = "0.1.0"
__author__ = "ECONAN Development Team"

from .data_models import Company, Exercise
from .config_loader import (
    load_companies,
    load_exercise_templates,
    get_company_by_ticker,
    get_companies_by_sector,
    get_all_sectors,
    get_template_by_id
)
from .exercise_generator import (
    generate_exercise,
    generate_exercises_for_company,
    generate_exercises_by_category
)
from .formatter import (
    format_exercise_markdown,
    format_exercise_html,
    format_exercise_json,
    format_exercises_batch
)
from .verification import (
    verify_company_data,
    verify_exercise,
    verify_all_companies,
    print_verification_report
)

__all__ = [
    # Data models
    "Company",
    "Exercise",
    # Config loaders
    "load_companies",
    "load_exercise_templates",
    "get_company_by_ticker",
    "get_companies_by_sector",
    "get_all_sectors",
    "get_template_by_id",
    # Exercise generation
    "generate_exercise",
    "generate_exercises_for_company",
    "generate_exercises_by_category",
    # Formatters
    "format_exercise_markdown",
    "format_exercise_html",
    "format_exercise_json",
    "format_exercises_batch",
    # Verification
    "verify_company_data",
    "verify_exercise",
    "verify_all_companies",
    "print_verification_report"
]
