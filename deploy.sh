#!/bin/bash
# Builds the site for GitHub Pages and pushes it live
python3 -m src.main "/Static-Site-Generator/"

git add docs/
git commit -m "Deploy: Update site content $(date +'%Y-%m-%d %H:%M')"
git push origin nested-inline-parser

echo "Deployed to GitHub Pages!"