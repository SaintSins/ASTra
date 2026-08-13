#!/bin/bash
# Builds the site for local preview
python3 -m src.main "/"
echo "Build complete. Run 'python3 -m http.server 8888 --directory docs' to preview."