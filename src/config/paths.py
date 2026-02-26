"""Centralized path definitions for the project."""

from pathlib import Path


def repo_root() -> Path:
    """Defines the root of the repository directory."""
    return Path(__file__).resolve().parents[2]


ROOT_DIR = repo_root()
DATA_DIR = ROOT_DIR / "data"


if __name__ == "__main__":
    print(f"Project Root: {ROOT_DIR}")
    print(f"Data Dir: {DATA_DIR}")
