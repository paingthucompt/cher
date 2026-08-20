#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT_DIR="$ROOT_DIR/BUILD/output"
OUTPUT_FILE="$OUTPUT_DIR/SocialAutoUpload_Master_Bible_v1.0.1.pdf"
FILE_LIST="$ROOT_DIR/BUILD/master_bible_files.txt"

cd "$ROOT_DIR"
python3 BUILD/validate_repository.py

if ! command -v pandoc >/dev/null 2>&1; then
  echo "Pandoc is not installed. Install pandoc to build PDF output."
  echo "Validation completed; no PDF was generated."
  exit 0
fi

mkdir -p "$OUTPUT_DIR"
pandoc \
  --from markdown \
  --to pdf \
  --toc \
  --toc-depth=2 \
  --number-sections \
  --resource-path="$ROOT_DIR" \
  -V "title:SocialAutoUpload Universe - Master Bible" \
  -o "$OUTPUT_FILE" \
  $(grep -v '^#' "$FILE_LIST" | sed '/^$/d')

echo "Built: $OUTPUT_FILE"
