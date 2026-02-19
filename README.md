# {{project_name}}

## Motivation and Goals

[Describe the motivation behind this project and what goals it aims to achieve]

## Table of Contents

- [Motivation and Goals](#motivation-and-goals)
- [Links](#links)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Data](#data)

## Links

- [Related Resource 1](#)
- [Related Resource 2](#)

## Repository Structure

```
.
├── data/           # Data files (raw, processed, external)
├── notebooks/      # Jupyter notebooks for exploration and analysis
├── reports/        # Generated reports, figures, and documents
├── scripts/        # Standalone scripts for specific tasks
└── src/            # Source code for the project
```

## Getting Started

### Prerequisites

- Python 3.8+
- uv (for environment management)

### Installation

[Add installation instructions here]

### Usage

[Add usage instructions here]

## Development

### Linting and formatting
This project uses [ruff](https://docs.astral.sh/ruff/) for linting and formatting. 

```bash
uv run ruff check
```

```bash
uv run ruff format
```

### Git conventions
TO maintain a clean and navigable history, please follow these conventions:

- Branching: Use descriptive prefixes. E.g. `feature/`, `fix`, `bug/`, `refactor/`.
- Commits: Use [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/). E.g. `fix: handle empty csv`, `feat: add data loader`. 
- Pull requests: Ensure all code is formatted and linted before submission. 

## Data

[Describe the data sources, format, and any preprocessing steps]
