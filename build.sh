#!/bin/bash
# Builds the site for local preview
if python3 -m src.main "/"; then
    echo "Build complete. Run 'python3 -m http.server 8888 --directory docs' to preview."
else
    echo "Build failed! Check the Python traceback above."
    exit 1
fi