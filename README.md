# Static Site Generator

# ⚠️ LEGACY BRANCH: Flat-List Parser

> **Note:** This branch is deprecated. It contains initial version of the static site generator, which utilized a linear, flat-list parsing architecture. It has been archived for historical context. While functional for basic Markdown, the linear parsing approach struggled with deeply nested formatting. This limitation inspired the complete rewrite of the parsing engine using an Abstract Syntax Tree (AST), which can now be found on the main branch.
> 
> Active development has moved to the `main` branch, which features a completely rewritten recursive Abstract Syntax Tree (AST) engine and automated CI/CD pipelines.

A custom, recursive Static Site Generator built in Python. This engine reads a directory tree of Markdown files, translates them into HTML, injects them into a base template, and outputs a complete, deploy-ready website. 

This project specifically includes dynamic basepath routing to support seamless deployment to GitHub Pages.

## Features

* **Markdown to HTML Parsing:** Converts Markdown text, headers, and images into raw HTML nodes.
* **Recursive Generation:** Automatically traverses nested directories in the `content/` folder and mirrors the exact file structure in the output directory.
* **Template Injection:** Extracts the main `h1` header from the Markdown to use as the page title, and injects the generated HTML into a customizable `template.html`.
* **Static Asset Management:** Safely wipes and recreates the output directory, cleanly copying all images, CSS, and static assets before generating pages.
* **Production Basepath Routing:** Accepts a CLI argument to dynamically rewrite absolute paths (`href="/...` and `src="/...`) to support GitHub Pages sub-directory hosting.

## Project Structure

```text
.
├── content/               # Source Markdown files (mirrored to output)
├── docs/                  # Generated production site (for GitHub Pages)
├── static/                # Images, CSS, and other static assets
├── src/                   # Python source code
├── main.py                # Entry point and CLI argument handling
│   ├── gencontent.py      # Recursive page generation logic
│   ├── copystatic.py      # Asset management logic
│   ├── textnode.py        # TextNode inline element class and conversions
│   ├── htmlnode.py        # Base HTMLNode, LeafNode, and ParentNode classes
│   ├── inline_markdown.py # Splits, extractors, and parsers for inline text
│   └── markdown_blocks.py # Block parsing, block-typing, and full document conversion
├── tests/                 # Unit tests covering all files in the src directory
├── template.html          # Base HTML template
├── main.sh                # Script for local testing 
└── build.sh               # Script for production build (GitHub Pages)
```

## How to Use

### Local Testing
To generate the site for local testing (defaults to `/` basepath) and serve it on a local Python server:
```bash
./main.sh
```

### Production Build (GitHub Pages)
To generate the site into the docs/ folder with the correct GitHub repository basepath:
```bash
./build.sh
```
(Ensure `build.sh` is configured with `python3 -m src.main "/YOUR_REPO_NAME/"`)

### Deployment
This site is configured to deploy to **GitHub Pages**.

1. Run `./build.sh` to generate the production files in the `docs` folder.

2. Commit and push the `docs` folder to the `main` branch.

3. In your GitHub repository settings, navigate to Pages, set the source to `Deploy from a branch`, choose `main`, and select the `docs` folder.

### Technologies Used
* **Python 3** (Standard Library only: `os`, `shutil`, `sys`)

* **Shell Scripting**

* **Git & GitHub Pages**
