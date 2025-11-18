#!/bin/bash
# ECONAN Exercise Generator - Batch Generation Script
# Generates all exercises in multiple formats for different audiences

set -e  # Exit on error

echo "================================================================================"
echo "ECONAN Exercise Generator - Batch Generation"
echo "================================================================================"
echo ""

# Configuration
OUTPUT_BASE="output"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# Clean output directory
echo "🧹 Cleaning output directory..."
rm -rf "${OUTPUT_BASE}"
mkdir -p "${OUTPUT_BASE}"

# 1. INSTRUCTOR VERSIONS (with solutions)
echo ""
echo "📚 Generating INSTRUCTOR versions (with solutions)..."
echo "--------------------------------------------------------------------------------"

# All exercises - Markdown
echo "  ✓ All exercises - Markdown"
python generate_exercises.py \
    --output "${OUTPUT_BASE}/instructor/all_markdown/"

# By category - HTML
echo "  ✓ V3 (Liquidity) - HTML"
python generate_exercises.py \
    --category V3 \
    --format html \
    --output "${OUTPUT_BASE}/instructor/v3_html/"

echo "  ✓ V4 (Valuation) - HTML"
python generate_exercises.py \
    --category V4 \
    --format html \
    --output "${OUTPUT_BASE}/instructor/v4_html/"

echo "  ✓ V5 (Cash Flow) - HTML"
python generate_exercises.py \
    --category V5 \
    --format html \
    --output "${OUTPUT_BASE}/instructor/v5_html/"

# 2. STUDENT VERSIONS (without solutions)
echo ""
echo "🎓 Generating STUDENT versions (without solutions)..."
echo "--------------------------------------------------------------------------------"

# All exercises - HTML
echo "  ✓ All exercises - HTML"
python generate_exercises.py \
    --no-solutions \
    --format html \
    --output "${OUTPUT_BASE}/student/all_html/"

# By category - HTML
echo "  ✓ V3 (Liquidity) - HTML"
python generate_exercises.py \
    --no-solutions \
    --category V3 \
    --format html \
    --output "${OUTPUT_BASE}/student/v3_html/"

echo "  ✓ V4 (Valuation) - HTML"
python generate_exercises.py \
    --no-solutions \
    --category V4 \
    --format html \
    --output "${OUTPUT_BASE}/student/v4_html/"

echo "  ✓ V5 (Cash Flow) - HTML"
python generate_exercises.py \
    --no-solutions \
    --category V5 \
    --format html \
    --output "${OUTPUT_BASE}/student/v5_html/"

# 3. DATA EXPORT (JSON)
echo ""
echo "💾 Generating DATA exports (JSON)..."
echo "--------------------------------------------------------------------------------"

echo "  ✓ All exercises - JSON"
python generate_exercises.py \
    --format json \
    --output "${OUTPUT_BASE}/data/all_json/"

echo "  ✓ V3 exercises - JSON"
python generate_exercises.py \
    --category V3 \
    --format json \
    --output "${OUTPUT_BASE}/data/v3_json/"

echo "  ✓ V4 exercises - JSON"
python generate_exercises.py \
    --category V4 \
    --format json \
    --output "${OUTPUT_BASE}/data/v4_json/"

echo "  ✓ V5 exercises - JSON"
python generate_exercises.py \
    --category V5 \
    --format json \
    --output "${OUTPUT_BASE}/data/v5_json/"

# 4. SECTOR-SPECIFIC (for BEDROM→ECONAN transition)
echo ""
echo "🏢 Generating SECTOR-SPECIFIC exercises..."
echo "--------------------------------------------------------------------------------"

for sector in "Retail" "Energy" "Financial Services" "Healthcare" "Manufacturing" "Food & Beverage" "Technology" "Real Estate"; do
    echo "  ✓ ${sector} sector - HTML"
    python generate_exercises.py \
        --sector "${sector}" \
        --no-solutions \
        --format html \
        --output "${OUTPUT_BASE}/sectors/${sector// /_}/html/"
done

# 5. INDIVIDUAL FILES (for exercise bank)
echo ""
echo "📂 Generating INDIVIDUAL exercise files..."
echo "--------------------------------------------------------------------------------"

echo "  ✓ V3 exercises - Individual Markdown files"
python generate_exercises.py \
    --category V3 \
    --individual \
    --output "${OUTPUT_BASE}/individual/v3/"

echo "  ✓ V4 exercises - Individual Markdown files"
python generate_exercises.py \
    --category V4 \
    --individual \
    --output "${OUTPUT_BASE}/individual/v4/"

echo "  ✓ V5 exercises - Individual Markdown files"
python generate_exercises.py \
    --category V5 \
    --individual \
    --output "${OUTPUT_BASE}/individual/v5/"

# Summary
echo ""
echo "================================================================================"
echo "✓ Batch generation complete!"
echo "================================================================================"
echo ""
echo "Generated files:"
echo "  - Instructor versions (with solutions): ${OUTPUT_BASE}/instructor/"
echo "  - Student versions (no solutions):      ${OUTPUT_BASE}/student/"
echo "  - Data exports (JSON):                  ${OUTPUT_BASE}/data/"
echo "  - Sector-specific:                      ${OUTPUT_BASE}/sectors/"
echo "  - Individual files:                     ${OUTPUT_BASE}/individual/"
echo ""
echo "Total output size:"
du -sh "${OUTPUT_BASE}"
echo ""
echo "================================================================================"
