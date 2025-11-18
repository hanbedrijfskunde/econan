"""
Data models for ECONAN Exercise Generator

This module defines the core data structures used for generating verification exercises:
- Company: Represents financial data for a single company
- Exercise: Represents a generated verification exercise with question and solution

Design principles:
- Immutable data structures using dataclasses
- Type hints for all attributes
- Validation logic for financial relationships
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Literal


@dataclass(frozen=True)
class Company:
    """
    Represents financial statement data for a single company.

    Attributes:
        name: Company name (e.g., "Ahold Delhaize")
        ticker: Stock ticker symbol (e.g., "AD.AS")
        sector: Business sector (e.g., "Retail")
        year: Financial year for the data

        # Balance Sheet (in millions EUR)
        total_assets: Total assets
        current_assets: Current assets (within 1 year)
        current_liabilities: Current liabilities (within 1 year)
        total_equity: Total shareholders' equity
        total_debt: Total debt (short-term + long-term)

        # Income Statement (in millions EUR)
        revenue: Total revenue
        operating_income: Operating income (EBIT)
        net_income: Net income after tax
        interest_expense: Interest expense

        # Cash Flow Statement (in millions EUR)
        operating_cash_flow: Cash from operations
        investing_cash_flow: Cash from investing activities
        financing_cash_flow: Cash from financing activities

        # Market data
        market_cap: Market capitalization (in millions EUR)
        share_price: Current share price (in EUR)
        shares_outstanding: Number of shares outstanding (in millions)
    """

    # Identification
    name: str
    ticker: str
    sector: str
    year: int

    # Balance Sheet
    total_assets: float
    current_assets: float
    current_liabilities: float
    total_equity: float
    total_debt: float

    # Income Statement
    revenue: float
    operating_income: float
    net_income: float
    interest_expense: float

    # Cash Flow Statement
    operating_cash_flow: float
    investing_cash_flow: float
    financing_cash_flow: float

    # Market data
    market_cap: float
    share_price: float
    shares_outstanding: float

    def __post_init__(self):
        """Validate financial data relationships."""
        # Basic sanity checks
        if self.total_assets <= 0:
            raise ValueError(f"{self.name}: Total assets must be positive")
        if self.total_equity <= 0:
            raise ValueError(f"{self.name}: Total equity must be positive")
        if self.revenue <= 0:
            raise ValueError(f"{self.name}: Revenue must be positive")

    @property
    def total_liabilities(self) -> float:
        """Calculate total liabilities from balance sheet identity."""
        return self.total_assets - self.total_equity

    @property
    def debt_to_equity(self) -> float:
        """Calculate Debt/Equity ratio."""
        return self.total_debt / self.total_equity if self.total_equity > 0 else float('inf')

    @property
    def current_ratio(self) -> float:
        """Calculate Current Ratio (liquidity measure)."""
        return self.current_assets / self.current_liabilities if self.current_liabilities > 0 else float('inf')

    @property
    def roe(self) -> float:
        """Calculate Return on Equity."""
        return self.net_income / self.total_equity if self.total_equity > 0 else 0.0

    @property
    def operating_margin(self) -> float:
        """Calculate Operating Margin."""
        return self.operating_income / self.revenue if self.revenue > 0 else 0.0

    @property
    def asset_turnover(self) -> float:
        """Calculate Asset Turnover."""
        return self.revenue / self.total_assets if self.total_assets > 0 else 0.0

    @property
    def earnings_yield(self) -> float:
        """Calculate Earnings Yield (inverse of P/E ratio)."""
        return self.net_income / self.market_cap if self.market_cap > 0 else 0.0

    @property
    def pe_ratio(self) -> float:
        """Calculate Price/Earnings ratio."""
        return self.market_cap / self.net_income if self.net_income > 0 else float('inf')


@dataclass
class Exercise:
    """
    Represents a generated verification exercise.

    Attributes:
        exercise_id: Unique identifier (e.g., "V3_A1")
        category: Exercise category (V3=Liquidity, V4=Valuation, V5=Cash Flow)
        difficulty: Difficulty level (basic, intermediate, advanced)
        company: Company data for the exercise
        question_nl: Exercise question in Dutch
        solution_steps: List of solution steps with explanations
        correct_answer: Final correct answer
        distractor_answers: List of plausible incorrect answers
        verification_identity: Mathematical identity to verify (e.g., "ROE = Net Margin × Asset Turnover × Leverage")
        learning_objective: Learning objective code (e.g., "LR-FSA-3")
    """

    exercise_id: str
    category: Literal["V3", "V4", "V5"]
    difficulty: Literal["basic", "intermediate", "advanced"]
    company: Company
    question_nl: str
    solution_steps: List[str]
    correct_answer: str
    distractor_answers: List[str]
    verification_identity: str
    learning_objective: str

    def to_dict(self) -> Dict:
        """Convert exercise to dictionary for template rendering."""
        return {
            "id": self.exercise_id,
            "category": self.category,
            "difficulty": self.difficulty,
            "company_name": self.company.name,
            "company_ticker": self.company.ticker,
            "company_sector": self.company.sector,
            "question": self.question_nl,
            "steps": self.solution_steps,
            "answer": self.correct_answer,
            "distractors": self.distractor_answers,
            "identity": self.verification_identity,
            "learning_objective": self.learning_objective
        }

    def __str__(self) -> str:
        """Human-readable representation."""
        return f"Exercise {self.exercise_id} ({self.category}) - {self.company.name} [{self.difficulty}]"
