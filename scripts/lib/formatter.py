"""
Output Formatters for ECONAN Exercises

This module provides formatters to output exercises in various formats:
- Markdown (.md): Human-readable format for documentation
- HTML: Web-ready format for online platforms
- JSON: Machine-readable format for APIs and data processing

Functions:
    - format_exercise_markdown: Single exercise to Markdown
    - format_exercise_html: Single exercise to HTML
    - format_exercise_json: Single exercise to JSON
    - format_exercises_batch: Multiple exercises to any format
"""

import json
from typing import List, Dict, Literal
from datetime import datetime

from .data_models import Exercise


def format_exercise_markdown(exercise: Exercise, include_solution: bool = True) -> str:
    """
    Format a single exercise as Markdown.

    Args:
        exercise: Exercise object to format
        include_solution: Whether to include solution steps (default: True)

    Returns:
        str: Markdown formatted exercise
    """
    md = []

    # Header
    md.append(f"# {exercise.exercise_id}: {exercise.company.name}")
    md.append(f"")
    md.append(f"**Categorie:** {exercise.category} - {_get_category_name(exercise.category)}")
    md.append(f"**Moeilijkheidsgraad:** {_get_difficulty_dutch(exercise.difficulty)}")
    md.append(f"**Leerdoel:** {exercise.learning_objective}")
    md.append(f"**Sector:** {exercise.company.sector}")
    md.append(f"")

    # Question
    md.append(f"## Vraag")
    md.append(f"")
    md.append(exercise.question_nl)
    md.append(f"")

    # Answer choices (correct + distractors shuffled)
    md.append(f"### Antwoordopties")
    md.append(f"")
    all_answers = [exercise.correct_answer] + exercise.distractor_answers
    # Don't shuffle in markdown for clarity, but mark correct answer
    for i, answer in enumerate(all_answers, 1):
        marker = " ✓" if answer == exercise.correct_answer else ""
        md.append(f"{chr(64+i)}. {answer}{marker}")
    md.append(f"")

    # Solution (optional)
    if include_solution:
        md.append(f"## Oplossing")
        md.append(f"")
        md.append(f"**Correct antwoord:** {exercise.correct_answer}")
        md.append(f"")
        md.append(f"### Stappenplan")
        md.append(f"")
        for i, step in enumerate(exercise.solution_steps, 1):
            md.append(f"{i}. {step}")
        md.append(f"")
        md.append(f"### Verificatie")
        md.append(f"")
        md.append(f"**Identiteit:** {exercise.verification_identity}")
        md.append(f"")

    # Metadata
    md.append(f"---")
    md.append(f"*Gegenereerd voor {exercise.company.name} ({exercise.company.ticker}) - {exercise.company.year}*")
    md.append(f"")

    return "\n".join(md)


def format_exercise_html(exercise: Exercise, include_solution: bool = True) -> str:
    """
    Format a single exercise as HTML.

    Args:
        exercise: Exercise object to format
        include_solution: Whether to include solution steps (default: True)

    Returns:
        str: HTML formatted exercise
    """
    html = []

    # Start container
    html.append(f'<div class="econan-exercise" data-id="{exercise.exercise_id}" data-category="{exercise.category}">')

    # Header
    html.append(f'  <div class="exercise-header">')
    html.append(f'    <h2>{exercise.exercise_id}: {exercise.company.name}</h2>')
    html.append(f'    <div class="exercise-metadata">')
    html.append(f'      <span class="badge badge-category">{exercise.category}</span>')
    html.append(f'      <span class="badge badge-difficulty">{_get_difficulty_dutch(exercise.difficulty)}</span>')
    html.append(f'      <span class="badge badge-sector">{exercise.company.sector}</span>')
    html.append(f'    </div>')
    html.append(f'  </div>')

    # Question
    html.append(f'  <div class="exercise-question">')
    html.append(f'    <h3>Vraag</h3>')
    # Convert newlines to paragraphs
    question_paragraphs = exercise.question_nl.split('\n')
    for para in question_paragraphs:
        if para.strip():
            html.append(f'    <p>{para.strip()}</p>')
    html.append(f'  </div>')

    # Answer choices
    html.append(f'  <div class="exercise-answers">')
    html.append(f'    <h4>Antwoordopties</h4>')
    html.append(f'    <ul class="answer-choices">')
    all_answers = [exercise.correct_answer] + exercise.distractor_answers
    for i, answer in enumerate(all_answers, 1):
        is_correct = 'data-correct="true"' if answer == exercise.correct_answer else ''
        html.append(f'      <li class="answer-choice" {is_correct}>')
        html.append(f'        <label>')
        html.append(f'          <input type="radio" name="answer-{exercise.exercise_id}" value="{chr(64+i)}">')
        html.append(f'          <span class="answer-label">{chr(64+i)}.</span>')
        html.append(f'          <span class="answer-text">{answer}</span>')
        html.append(f'        </label>')
        html.append(f'      </li>')
    html.append(f'    </ul>')
    html.append(f'  </div>')

    # Solution (optional, hidden by default)
    if include_solution:
        html.append(f'  <div class="exercise-solution" style="display: none;">')
        html.append(f'    <h3>Oplossing</h3>')
        html.append(f'    <p class="correct-answer"><strong>Correct antwoord:</strong> {exercise.correct_answer}</p>')
        html.append(f'    <h4>Stappenplan</h4>')
        html.append(f'    <ol class="solution-steps">')
        for step in exercise.solution_steps:
            html.append(f'      <li>{step}</li>')
        html.append(f'    </ol>')
        html.append(f'    <div class="verification">')
        html.append(f'      <h4>Verificatie</h4>')
        html.append(f'      <p><strong>Identiteit:</strong> <code>{exercise.verification_identity}</code></p>')
        html.append(f'    </div>')
        html.append(f'  </div>')

    # Footer
    html.append(f'  <div class="exercise-footer">')
    html.append(f'    <small>Gegenereerd voor {exercise.company.name} ({exercise.company.ticker}) - {exercise.company.year}</small>')
    html.append(f'  </div>')

    # Close container
    html.append(f'</div>')

    return "\n".join(html)


def format_exercise_json(exercise: Exercise) -> Dict:
    """
    Format a single exercise as JSON-serializable dictionary.

    Args:
        exercise: Exercise object to format

    Returns:
        Dict: JSON-serializable dictionary
    """
    return {
        "id": exercise.exercise_id,
        "category": exercise.category,
        "category_name": _get_category_name(exercise.category),
        "difficulty": exercise.difficulty,
        "difficulty_dutch": _get_difficulty_dutch(exercise.difficulty),
        "learning_objective": exercise.learning_objective,
        "company": {
            "name": exercise.company.name,
            "ticker": exercise.company.ticker,
            "sector": exercise.company.sector,
            "year": exercise.company.year
        },
        "question": exercise.question_nl,
        "answers": {
            "correct": exercise.correct_answer,
            "distractors": exercise.distractor_answers,
            "all_shuffled": _shuffle_answers(exercise.correct_answer, exercise.distractor_answers)
        },
        "solution": {
            "steps": exercise.solution_steps,
            "verification_identity": exercise.verification_identity
        },
        "metadata": {
            "generated_at": datetime.now().isoformat()
        }
    }


def format_exercises_batch(
    exercises: List[Exercise],
    output_format: Literal["markdown", "html", "json"],
    include_solutions: bool = True
) -> str:
    """
    Format multiple exercises in specified format.

    Args:
        exercises: List of Exercise objects
        output_format: Output format ("markdown", "html", or "json")
        include_solutions: Whether to include solutions (default: True)

    Returns:
        str: Formatted exercises as a single string

    Raises:
        ValueError: If output_format is invalid
    """
    if output_format == "markdown":
        return _format_batch_markdown(exercises, include_solutions)
    elif output_format == "html":
        return _format_batch_html(exercises, include_solutions)
    elif output_format == "json":
        return _format_batch_json(exercises)
    else:
        raise ValueError(f"Invalid output format: {output_format}. Must be 'markdown', 'html', or 'json'")


def _format_batch_markdown(exercises: List[Exercise], include_solutions: bool) -> str:
    """Format multiple exercises as Markdown."""
    md = []

    # Header
    md.append(f"# ECONAN Verificatie Oefeningen")
    md.append(f"")
    md.append(f"Gegenereerd op: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    md.append(f"Aantal oefeningen: {len(exercises)}")
    md.append(f"")
    md.append(f"---")
    md.append(f"")

    # Individual exercises
    for exercise in exercises:
        md.append(format_exercise_markdown(exercise, include_solutions))
        md.append(f"\n---\n")

    return "\n".join(md)


def _format_batch_html(exercises: List[Exercise], include_solutions: bool) -> str:
    """Format multiple exercises as complete HTML page."""
    html = []

    # HTML header
    html.append('<!DOCTYPE html>')
    html.append('<html lang="nl">')
    html.append('<head>')
    html.append('  <meta charset="UTF-8">')
    html.append('  <meta name="viewport" content="width=device-width, initial-scale=1.0">')
    html.append('  <title>ECONAN Verificatie Oefeningen</title>')
    html.append('  <link rel="stylesheet" href="../../design-system.css">')
    html.append('  <link rel="stylesheet" href="../../components.css">')
    html.append('  <style>')
    html.append('    .econan-exercise { margin-bottom: 2rem; padding: 1.5rem; border: 1px solid #ddd; border-radius: 8px; }')
    html.append('    .exercise-header h2 { margin-top: 0; }')
    html.append('    .exercise-metadata { margin: 0.5rem 0; }')
    html.append('    .badge { display: inline-block; padding: 0.25rem 0.75rem; margin-right: 0.5rem; ')
    html.append('             background: #e0e0e0; border-radius: 4px; font-size: 0.875rem; }')
    html.append('    .answer-choices { list-style: none; padding: 0; }')
    html.append('    .answer-choice { margin: 0.5rem 0; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; }')
    html.append('    .answer-choice:hover { background: #f5f5f5; }')
    html.append('    .exercise-solution { margin-top: 1.5rem; padding: 1rem; background: #f9f9f9; border-radius: 4px; }')
    html.append('    .solution-steps { padding-left: 1.5rem; }')
    html.append('    .verification code { background: #e0e0e0; padding: 0.25rem 0.5rem; border-radius: 3px; }')
    html.append('  </style>')
    html.append('</head>')
    html.append('<body>')
    html.append('  <header class="econan-header">')
    html.append('    <h1>ECONAN Verificatie Oefeningen</h1>')
    html.append(f'    <p>Gegenereerd op: {datetime.now().strftime("%Y-%m-%d %H:%M")} | ')
    html.append(f'       Aantal oefeningen: {len(exercises)}</p>')
    html.append('  </header>')
    html.append('  <main class="exercises-container">')

    # Individual exercises
    for exercise in exercises:
        html.append(format_exercise_html(exercise, include_solutions))

    # HTML footer
    html.append('  </main>')
    html.append('  <footer>')
    html.append('    <p><small>ECONAN Exercise Generator - Automated Verification Exercises</small></p>')
    html.append('  </footer>')
    html.append('</body>')
    html.append('</html>')

    return "\n".join(html)


def _format_batch_json(exercises: List[Exercise]) -> str:
    """Format multiple exercises as JSON."""
    data = {
        "metadata": {
            "generated_at": datetime.now().isoformat(),
            "count": len(exercises),
            "version": "1.0"
        },
        "exercises": [format_exercise_json(ex) for ex in exercises]
    }
    return json.dumps(data, indent=2, ensure_ascii=False)


def _get_category_name(category: str) -> str:
    """Get Dutch name for category."""
    names = {
        "V3": "Liquiditeitsanalyse",
        "V4": "Waardering & Winstgevendheid",
        "V5": "Cashflow Analyse"
    }
    return names.get(category, category)


def _get_difficulty_dutch(difficulty: str) -> str:
    """Get Dutch translation for difficulty."""
    translations = {
        "basic": "Basis",
        "intermediate": "Gemiddeld",
        "advanced": "Gevorderd"
    }
    return translations.get(difficulty, difficulty)


def _shuffle_answers(correct: str, distractors: List[str]) -> List[Dict[str, str]]:
    """Shuffle answers for JSON output."""
    import random
    all_answers = [{"text": correct, "is_correct": True}]
    all_answers.extend([{"text": d, "is_correct": False} for d in distractors])
    random.shuffle(all_answers)
    return all_answers


if __name__ == "__main__":
    # Test formatting
    from .exercise_generator import generate_exercise
    from .config_loader import load_companies

    print("Testing exercise formatters...")

    # Generate test exercise
    companies = load_companies()
    test_company = companies[0]
    exercise = generate_exercise("V3_A1", test_company)

    # Test Markdown
    print("\n=== MARKDOWN FORMAT ===\n")
    print(format_exercise_markdown(exercise))

    # Test JSON
    print("\n=== JSON FORMAT ===\n")
    print(json.dumps(format_exercise_json(exercise), indent=2, ensure_ascii=False))
