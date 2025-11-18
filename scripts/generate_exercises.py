#!/usr/bin/env python3
"""
ECONAN Exercise Generator - Command Line Interface

Generate verification exercises for ECONAN financial analysis education.

Usage:
    # Generate all exercises for all companies
    python generate_exercises.py --output-dir output/

    # Generate only V3 (Liquidity) exercises
    python generate_exercises.py --category V3 --output-dir output/

    # Generate exercises for specific company
    python generate_exercises.py --ticker AD.AS --output-dir output/

    # Generate in specific format (markdown, html, or json)
    python generate_exercises.py --format html --output-dir output/

    # Generate without solutions (student version)
    python generate_exercises.py --no-solutions --output-dir output/

Examples:
    # All exercises in Markdown format
    python generate_exercises.py --format markdown --output output/

    # V4 exercises in HTML format with solutions
    python generate_exercises.py --category V4 --format html --output output/

    # Single company, all exercises, JSON format
    python generate_exercises.py --ticker SHELL.AS --format json --output output/
"""

import argparse
import sys
from pathlib import Path
from typing import Optional, List

# Add lib directory to path
sys.path.insert(0, str(Path(__file__).parent))

from lib import (
    load_companies,
    get_company_by_ticker,
    get_companies_by_sector,
    generate_exercise,
    generate_exercises_for_company,
    generate_exercises_by_category,
    format_exercises_batch,
    format_exercise_markdown,
    format_exercise_html,
    format_exercise_json
)
from lib.data_models import Exercise


def create_output_directory(output_dir: Path) -> None:
    """Create output directory if it doesn't exist."""
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"✓ Output directory: {output_dir}")


def save_exercise_file(
    content: str,
    filename: str,
    output_dir: Path,
    format_type: str
) -> None:
    """Save exercise content to file."""
    extension_map = {
        "markdown": ".md",
        "html": ".html",
        "json": ".json"
    }

    extension = extension_map.get(format_type, ".txt")
    filepath = output_dir / f"{filename}{extension}"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  ✓ {filepath.name}")


def generate_all_exercises(
    output_dir: Path,
    format_type: str = "markdown",
    include_solutions: bool = True
) -> None:
    """Generate all exercises for all companies."""
    print("\n📊 Generating all exercises for all companies...")

    companies = load_companies()
    print(f"  Companies: {len(companies)}")

    all_exercises = []
    for company in companies:
        exercises = generate_exercises_for_company(company)
        all_exercises.extend(exercises)

    print(f"  Total exercises: {len(all_exercises)}")

    # Save batch file
    content = format_exercises_batch(all_exercises, format_type, include_solutions)
    filename = "all_exercises"
    save_exercise_file(content, filename, output_dir, format_type)

    print(f"\n✓ Generated {len(all_exercises)} exercises")


def generate_by_category(
    category: str,
    output_dir: Path,
    format_type: str = "markdown",
    include_solutions: bool = True
) -> None:
    """Generate all exercises for a specific category."""
    category_names = {
        "V3": "Liquiditeitsanalyse",
        "V4": "Waardering & Winstgevendheid",
        "V5": "Cashflow Analyse"
    }

    print(f"\n📊 Generating {category} ({category_names.get(category, '')}) exercises...")

    exercises = generate_exercises_by_category(category)
    print(f"  Total exercises: {len(exercises)}")

    # Save batch file
    content = format_exercises_batch(exercises, format_type, include_solutions)
    filename = f"{category.lower()}_exercises"
    save_exercise_file(content, filename, output_dir, format_type)

    print(f"\n✓ Generated {len(exercises)} {category} exercises")


def generate_by_company(
    ticker: str,
    output_dir: Path,
    format_type: str = "markdown",
    include_solutions: bool = True,
    category: Optional[str] = None
) -> None:
    """Generate exercises for a specific company."""
    print(f"\n📊 Generating exercises for {ticker}...")

    company = get_company_by_ticker(ticker)
    print(f"  Company: {company.name}")
    print(f"  Sector: {company.sector}")

    exercises = generate_exercises_for_company(company, category=category)
    print(f"  Total exercises: {len(exercises)}")

    # Save batch file
    content = format_exercises_batch(exercises, format_type, include_solutions)
    filename = f"{company.ticker.replace('.', '_').lower()}_exercises"
    save_exercise_file(content, filename, output_dir, format_type)

    print(f"\n✓ Generated {len(exercises)} exercises for {company.name}")


def generate_by_sector(
    sector: str,
    output_dir: Path,
    format_type: str = "markdown",
    include_solutions: bool = True,
    category: Optional[str] = None
) -> None:
    """Generate exercises for all companies in a sector."""
    print(f"\n📊 Generating exercises for {sector} sector...")

    companies = get_companies_by_sector(sector)
    print(f"  Companies: {len(companies)}")
    for company in companies:
        print(f"    - {company.name} ({company.ticker})")

    all_exercises = []
    for company in companies:
        exercises = generate_exercises_for_company(company, category=category)
        all_exercises.extend(exercises)

    print(f"  Total exercises: {len(all_exercises)}")

    # Save batch file
    content = format_exercises_batch(all_exercises, format_type, include_solutions)
    filename = f"{sector.lower().replace(' ', '_')}_exercises"
    save_exercise_file(content, filename, output_dir, format_type)

    print(f"\n✓ Generated {len(all_exercises)} exercises for {sector} sector")


def generate_individual_files(
    output_dir: Path,
    format_type: str = "markdown",
    include_solutions: bool = True,
    category: Optional[str] = None,
    ticker: Optional[str] = None
) -> None:
    """Generate individual files for each exercise."""
    print("\n📊 Generating individual exercise files...")

    if ticker:
        company = get_company_by_ticker(ticker)
        exercises = generate_exercises_for_company(company, category=category)
    elif category:
        exercises = generate_exercises_by_category(category)
    else:
        companies = load_companies()
        exercises = []
        for company in companies:
            exercises.extend(generate_exercises_for_company(company))

    print(f"  Total exercises: {len(exercises)}")

    # Create subdirectory for individual files
    individual_dir = output_dir / "individual"
    individual_dir.mkdir(exist_ok=True)

    for exercise in exercises:
        # Format exercise
        if format_type == "markdown":
            content = format_exercise_markdown(exercise, include_solutions)
        elif format_type == "html":
            content = format_exercise_html(exercise, include_solutions)
        elif format_type == "json":
            import json
            content = json.dumps(format_exercise_json(exercise), indent=2, ensure_ascii=False)
        else:
            raise ValueError(f"Unsupported format: {format_type}")

        # Save file
        filename = f"{exercise.exercise_id}_{exercise.company.ticker.replace('.', '_').lower()}"
        save_exercise_file(content, filename, individual_dir, format_type)

    print(f"\n✓ Generated {len(exercises)} individual files in {individual_dir}")


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="ECONAN Exercise Generator - Generate verification exercises for financial analysis",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate all exercises in Markdown
  python generate_exercises.py --output output/

  # Generate V3 exercises in HTML
  python generate_exercises.py --category V3 --format html --output output/

  # Generate exercises for Ahold Delhaize
  python generate_exercises.py --ticker AD.AS --output output/

  # Generate exercises for Retail sector
  python generate_exercises.py --sector Retail --output output/

  # Generate without solutions (student version)
  python generate_exercises.py --no-solutions --output output/

  # Generate individual files for each exercise
  python generate_exercises.py --individual --output output/
        """
    )

    # Output options
    parser.add_argument(
        "--output", "-o",
        type=str,
        required=True,
        help="Output directory for generated exercises"
    )

    parser.add_argument(
        "--format", "-f",
        type=str,
        choices=["markdown", "html", "json"],
        default="markdown",
        help="Output format (default: markdown)"
    )

    # Filtering options
    parser.add_argument(
        "--category", "-c",
        type=str,
        choices=["V3", "V4", "V5"],
        help="Filter by exercise category (V3=Liquidity, V4=Valuation, V5=Cash Flow)"
    )

    parser.add_argument(
        "--ticker", "-t",
        type=str,
        help="Generate exercises for specific company ticker (e.g., AD.AS, SHELL.AS)"
    )

    parser.add_argument(
        "--sector", "-s",
        type=str,
        help="Generate exercises for specific sector (e.g., Retail, Energy)"
    )

    # Content options
    parser.add_argument(
        "--no-solutions",
        action="store_true",
        help="Exclude solution steps (student version)"
    )

    parser.add_argument(
        "--individual",
        action="store_true",
        help="Generate individual files for each exercise (instead of batch)"
    )

    args = parser.parse_args()

    # Validate arguments
    if args.ticker and args.sector:
        print("Error: Cannot specify both --ticker and --sector")
        sys.exit(1)

    # Setup
    output_dir = Path(args.output)
    create_output_directory(output_dir)
    include_solutions = not args.no_solutions

    print("=" * 80)
    print("ECONAN Exercise Generator")
    print("=" * 80)
    print(f"Format: {args.format}")
    print(f"Solutions: {'Included' if include_solutions else 'Excluded'}")
    if args.category:
        print(f"Category: {args.category}")
    if args.ticker:
        print(f"Company: {args.ticker}")
    if args.sector:
        print(f"Sector: {args.sector}")

    # Generate exercises
    try:
        if args.individual:
            generate_individual_files(
                output_dir,
                args.format,
                include_solutions,
                args.category,
                args.ticker
            )
        elif args.ticker:
            generate_by_company(
                args.ticker,
                output_dir,
                args.format,
                include_solutions,
                args.category
            )
        elif args.sector:
            generate_by_sector(
                args.sector,
                output_dir,
                args.format,
                include_solutions,
                args.category
            )
        elif args.category:
            generate_by_category(
                args.category,
                output_dir,
                args.format,
                include_solutions
            )
        else:
            generate_all_exercises(
                output_dir,
                args.format,
                include_solutions
            )

        print("\n" + "=" * 80)
        print("✓ Generation complete!")
        print("=" * 80)

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
