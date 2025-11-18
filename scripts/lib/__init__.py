"""
ECONAN Exercise Generator Library

This package provides data models and utilities for generating automated
verification exercises for financial analysis education.

Modules:
    - data_models: Core data structures (Company, Exercise)
    - config_loader: YAML configuration loading utilities
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

__all__ = [
    "Company",
    "Exercise",
    "load_companies",
    "load_exercise_templates",
    "get_company_by_ticker",
    "get_companies_by_sector",
    "get_all_sectors",
    "get_template_by_id"
]
