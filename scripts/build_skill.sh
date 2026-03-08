#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT_DIR="$ROOT_DIR/dist"
OUT_FILE="$OUT_DIR/strategy-skills.skill"

mkdir -p "$OUT_DIR"

# Package repo as .skill (zip). Exclude git + dist.
# Note: OpenClaw can install with: openclaw skills install <path>.skill
cd "$ROOT_DIR"
rm -f "$OUT_FILE"
zip -r "$OUT_FILE" . -x ".git/*" "dist/*" >/dev/null

echo "Built: $OUT_FILE"
