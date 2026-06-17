#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_ROOT"

die()  { echo "Error: $*" >&2; exit 1; }
info() { echo "$*" >&2; }

if [[ $# -eq 0 || -z "${1:-}" ]]; then
    info "=== Full test suite ==="
    pytest tests/unit/test_dto tests/unit/test_openapi tests/unit/test_signature -x -q
else
    IFS=',' read -ra TEST_FILES <<< "$1"
    info "=== Targeted tests: ${TEST_FILES[*]} ==="
    pytest "${TEST_FILES[@]}" -x -q
fi
