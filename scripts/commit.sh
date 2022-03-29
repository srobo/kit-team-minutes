#!/bin/bash
filename="$(date '+%Y/%Y-%m-%d.md')"
curl https://hackmd.io/@racc/kit-team-agenda/download  | ruby -pe 'return if $_ =~ /^---$/' > "$filename"
git add "$filename"
git commit -m "Add minutes for $(date '+%Y-%m-%d')"
git push

