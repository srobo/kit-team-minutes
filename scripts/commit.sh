#!/bin/bash
set -o errexit -o nounset -o pipefail
filename="$(date '+%Y/%Y-%m-%d.md')"
curl https://hackmd.io/@racc/kit-team-agenda/download  | sed '/^---$/Q' > "$filename"
git add "$filename"
git commit -m "Add minutes for $(date '+%Y-%m-%d')"
git push
