"""
ECONAN Exercise Generator Library

This package provides data models and utilities for generating automated
verification exercises for financial analysis education.

Modules:
    - data_models: Core data structures (Company, Exercise)
"""

__version__ = "0.1.0"
__author__ = "ECONAN Development Team"

from .data_models import Company, Exercise

__all__ = ["Company", "Exercise"]
