# Blueprint

A [Copier](https://copier.readthedocs.io/) template for Python data science and machine learning projects.

## Requirements

- **uv** - [Installation guide](https://docs.astral.sh/uv/getting-started/installation/)
- **Copier** - Install with: `pipx install copier` or `uv tool install copier`
- **git** - For version control

Projects support Python 3.10 through 3.14. uv will automatically download and install your chosen Python version if needed.

## Usage

Create a new project:

```bash
copier copy gh:markbugden/blueprint my-project-name
```

The template will prompt you to customize:
- Python version (3.10-3.14)
- Data science packages (pandas, numpy, matplotlib, seaborn)
- PyTorch support (CPU/GPU)
- Gradio app template
- Linter (Ruff)
- Dev tools (tqdm, ipykernel for Jupyter)

## Project Structure

Generated projects include:
- Standard data science layout (data/, models/, notebooks/, reports/, scripts/, src/)
- Optional app/ directory for Gradio web applications
- Git repository with initial commit
- Virtual environment with pinned Python version
- uv.lock for reproducible dependencies

## Updating Projects

Update an existing project when the template changes:

```bash
cd my-project
copier update
```
