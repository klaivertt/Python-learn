#!/usr/bin/env bash

set -euo pipefail

search_root="${1:-.}"
output_file="${2:-py_lines_report.txt}"

total_lines=0

{
  echo "Rapport de lignes des fichiers Python"
  echo "Racine : ${search_root}"
  echo

  while IFS= read -r -d '' file; do
    line_count=$(wc -l < "$file")
    total_lines=$((total_lines + line_count))
    printf '%s : %s\n' "$file" "$line_count"
  done < <(find "$search_root" -type f -name '*.py' -print0)

  echo
  printf 'Total : %s\n' "$total_lines"
} > "$output_file"

echo "Rapport écrit dans : $output_file"