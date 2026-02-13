#!/usr/bin/env bash
# full_setup.sh — Master setup script for the Organic Social Poster skill.
#
# Run this AFTER you've set up your API credentials (Meta, TikTok, GitHub).
# It will: verify credentials, restructure the repo, and confirm everything's ready.
#
# Usage:
#   bash scripts/full_setup.sh              # Full setup
#   bash scripts/full_setup.sh --check-only # Just verify credentials

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(dirname "$SCRIPT_DIR")"

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  ORGANIC SOCIAL POSTER — SETUP"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Step 1: Check Python deps
echo "Step 1: Installing Python dependencies..."
pip install python-docx --break-system-packages -q 2>/dev/null && echo "  ✅ python-docx installed" || echo "  ⚠️  python-docx install failed (non-critical)"
echo ""

# Step 2: Verify API credentials
echo "Step 2: Verifying API credentials..."
python3 "${SCRIPT_DIR}/verify_setup.py"
VERIFY_STATUS=$?
echo ""

if [ "$1" = "--check-only" ] 2>/dev/null; then
  echo "Check-only mode. Exiting."
  exit $VERIFY_STATUS
fi

if [ $VERIFY_STATUS -ne 0 ]; then
  echo "⚠️  Some APIs aren't set up yet."
  echo "   See references/api-setup-guide.md for instructions."
  echo "   You can still restructure the repo — continue? (y/n)"
  read -r CONTINUE
  if [ "$CONTINUE" != "y" ]; then
    exit 1
  fi
fi

# Step 3: Restructure repo (dry run first)
echo ""
echo "Step 3: Restructuring GitHub repo..."
echo "  Running dry run first..."
python3 "${SCRIPT_DIR}/restructure_repo.py" --dry-run
echo ""
echo "  This will reorganize Business Research/ → Brands/ in your GitHub repo."
echo "  Proceed with the restructure? (y/n)"
read -r PROCEED
if [ "$PROCEED" = "y" ]; then
  python3 "${SCRIPT_DIR}/restructure_repo.py"
else
  echo "  Skipped repo restructure. You can run it later:"
  echo "    python3 scripts/restructure_repo.py"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  SETUP COMPLETE"
echo ""
echo "  Next steps:"
echo "  1. Add images to Brands/{BrandName}/organic-images/ on GitHub"
echo "  2. Tell Claude: 'post for TableClay' (or any brand)"
echo "  3. Review the caption draft and approve"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
