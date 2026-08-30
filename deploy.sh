#!/bin/bash
# Builds the site for GitHub Pages and pushes it live
python3 -m src.main "/ASTra/"

git add docs/ content/
git commit -m "docs: update site content"
git push origin main

echo "Deployed to GitHub Pages!"