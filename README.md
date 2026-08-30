# ASTra: A Zero-Dependency Markdown Compiler & AST Engine

A robust, Python-based text parsing engine that compiles raw Markdown into production-ready HTML. 

Originally built to understand file systems and text parsing fundamentals, the core parsing engine was entirely rewritten to utilize a custom recursive **Abstract Syntax Tree (AST)** architecture. This project demonstrates modular software design, custom regex tokenization, and automated deployment workflows without relying on external libraries.

## Features

* **Recursive AST Engine:** Parses Markdown by building a hierarchical Abstract Syntax Tree (AST), enabling infinite nesting of HTML elements (e.g., italicized text inside blockquotes inside nested lists).
* **Hybrid Regex Bridge:** Safely extracts and tokenizes inline formatting (bold, italic, links, images) using custom regex rules before feeding them into the node generation pipeline.
* **Recursive Page Generation:** Automatically traverses nested directories in the `content/` folder and mirrors the exact file structure in the output directory.
* **Dynamic Template Injection:** Extracts the main `h1` header from the Markdown to use as the page title, injecting the generated HTML into a customizable `template.html` skeleton.
* **Static Asset Management:** Safely wipes and recreates the output directory on every build, cleanly copying all images, CSS, and static assets to guarantee a fresh build state.
* **Environment-Aware Path Routing:** Dynamically rewrites absolute paths (`href` and `src`) based on CLI arguments to support both local web servers and GitHub Pages sub-directory hosting. 
* **Automated Deployment Workflows:** Includes custom `build.sh` and `deploy.sh` scripts for sandbox testing and one-click production deployments to GitHub.
* **Modular Tailwind Theming:** Built with easily editable semantic variables and typography overrides for quick design adjustments.

## Differences: Legacy vs. AST Engine

The defining engineering milestone of this project is the transition from a linear, flat-list parsing model (v1.0) to a hierarchical Abstract Syntax Tree structure (v2.0).

### Legacy Engine
The original parser used a sequential loop to split text into a flat list of text nodes. While functional for basic paragraphs, it became brittle when handling nested formatting (e.g., bold text inside an italicized quote block) and relied on fragile string-splitting logic that was difficult to scale or extend.

### AST Engine
The current engine processes Markdown by building a node-based tree structure before generating any HTML. 
* **Hierarchical Nesting:** HTML nodes can now act as parents to other HTML nodes infinitely, allowing for complex, deeply nested document structures.
* **The Hybrid Bridge:** Inline markdown elements are safely extracted using a custom regex tokenization layer. This isolates the formatting rules from the core parsing logic, feeding clean tokens directly into the AST generation pipeline.

| Feature | Legacy Engine | AST Engine |
|---|---|---|
| **Data Structure** | Flat Array/List | Tree (Parent/Child Nodes) |
| **Nesting Support** | Breaks on deep nesting | Infinite recursion |
| **Parsing Logic** | Sequential string slicing | Regex tokenization & node mapping |
| **Maintainability** | High friction for new rules | Plug-and-play node classes |

## Project Structure

```text
.
├── content/                    # Raw Markdown content (directories dictate file routing)
├── docs/                       # Compiled HTML output (served by GitHub Pages)
├── static/                     # Global assets (CSS, images)
├── src/                        # Core Engine Source Code
│   ├── main.py                 # Application entry point
│   ├── copystatic.py           # Asset management and directory synchronization
│   ├── gencontent.py           # Recursive HTML page generation logic
│   ├── markdown_blocks.py      # AST Engine: Block-level markdown parsing
│   ├── inline_markdown.py      # Hybrid Bridge: Regex tokenization for inline formatting
│   ├── textnode.py             # Intermediate text representations
│   ├── htmlnode.py             # AST data structures (ParentNode, LeafNode)
│   └── escape_handlers.py      # Markdown character escape logic
├── tests/                      # Unit tests for AST generation and regex parsing
├── template.html               # Base HTML skeleton for all generated pages
├── build.sh                    # Shell script for local sandbox testing
├── deploy.sh                   # Shell script for automated GitHub Pages deployment
└── test.sh                     # Automated test runner script

```

## Adding Content

To create or update pages on your website, add or modify Markdown (`.md`) files inside the `content/` directory. The AST engine automatically handles the rest.

### 1. Folder Routing
The recursive generation engine perfectly mirrors your `content/` directory structure into the `docs/` output directory. 

Because of this, you can structure your site using standard folders and `index.md` files to create clean URLs:
* `content/index.md` compiles to `docs/index.html` (Homepage)
* `content/contact/index.md` compiles to `docs/contact/index.html`
* `content/blog/automation/index.md` compiles to `docs/blog/automation/index.html`

### 2. Required Headings
Every Markdown file must include exactly one top-level heading (e.g., `# My Page Title`). 

The engine actively parses the AST to locate this `h1` block, extracts its text, and dynamically injects it into the `<title>` tag of the `template.html` skeleton before rendering the final page.

### 3. Static Assets
If you need to include images in your Markdown (e.g., `![Alt text](/images/pic.png)`), place the image files directly into the `static/images/` directory. The build script automatically copies the entire `static/` folder into the root of your `docs/` folder on every build.

## Local Testing and Deployment

This project utilizes custom shell scripts to separate the local development environment from the production build, preventing unfinished drafts or broken paths from being pushed live.

*(Note: Ensure your shell scripts are executable by running `chmod +x build.sh deploy.sh test.sh` before your first use).*

### 1. Running Unit Tests
Before building, you can verify the integrity of the AST engine and regex bridge by running the test suite:
```bash
./test.sh
```

### 2. Local Sandbox Testing
To build and preview your markdown changes locally without affecting the live site, run:
```bash
./build.sh
```
This script generates the HTML into the `docs/` folder using absolute root paths ("/"). Because it uses local routing, your CSS and images will load correctly on your own machine.

To preview the generated site, start a local Python web server:
```bash
python3 -m http.server 8888 --directory docs
```
You can then view your site in the browser at `http://localhost:8888`.

### 3. Live Production Deployment
When your local draft is ready to be published to GitHub Pages, run:
```bash
./deploy.sh
```
This script automates the entire CI/CD deployment pipeline:

1. Rebuilds the HTML using your specific repository basepath (`"/ASTra/"`) so all assets and links route correctly in the production environment.

2. Stages the freshly generated `docs/` directory.

3. Commits the changes to Git with an automated timestamp.

4. Pushes the build to the active main branch, triggering the live GitHub Pages update.
