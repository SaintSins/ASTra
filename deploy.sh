#!/bin/bash
# Builds the site for GitHub Pages and pushes it live
python3 -m src.main "/ASTra/"

git add docs/
git commit -m "build: Update site content"
git push origin main

echo "Deployed to GitHub Pages!"