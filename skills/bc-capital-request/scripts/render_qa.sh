#!/usr/bin/env bash
# Render a pptx to one jpeg per slide, so the result can actually be looked at.
# Usage: render_qa.sh deck.pptx [dpi]
# Requires: soffice (LibreOffice) and pdftoppm (poppler-utils) on PATH. Exit 1 if one is missing.
set -euo pipefail
case "${1:-}" in -h|--help) echo "Usage: render_qa.sh deck.pptx [dpi]"; exit 0;; esac
for tool in soffice pdftoppm; do
  command -v "$tool" >/dev/null 2>&1 || { echo "render_qa.sh: $tool not found on PATH" >&2; exit 1; }
done
f="${1:?usage: render_qa.sh deck.pptx [dpi]}"
dpi="${2:-100}"
base="$(basename "${f%.pptx}")"
dir="$(cd "$(dirname "$f")" && pwd)"
cd "$dir"
rm -f "$base.pdf" "$base"-[0-9]*.jpg
soffice --headless --convert-to pdf "$(basename "$f")" >/dev/null 2>&1 || \
  soffice.py --headless --convert-to pdf "$(basename "$f")" >/dev/null 2>&1
pdftoppm -jpeg -r "$dpi" "$base.pdf" "$base"
ls -1 "$base"-*.jpg
echo
echo "Now open each image and check:"
echo "  1 nothing clipped, nothing past x=12.83in"
echo "  2 no white text on 8793CA / 1EB68A / F8AF99 / 48C2CA / EDC0DA"
echo "  3 every title on one line"
echo "  4 no Lorem ipsum, no 'Mintacim', no old-brand leftovers"
echo "  5 all four footer fields filled on every slide"
