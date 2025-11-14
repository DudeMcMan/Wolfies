"""Small CLI prototype for species split-time lookup.

Usage:
    python -m src.app species1 species2

This is intentionally minimal and uses the mock data in `data/species_split_times.json`.
"""
import argparse
from pathlib import Path
from src.database import SpeciesDatabase


def parse_args():
    p = argparse.ArgumentParser(description="Estimate split time for two taxa (prototype)")
    p.add_argument("species1", help="First species name (e.g. wolf)")
    p.add_argument("species2", help="Second species name (e.g. direwolf)")
    return p.parse_args()


def main():
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    data_path = repo_root / "data" / "species_split_times.json"
    db = SpeciesDatabase(str(data_path))

    result = db.get_split_time(args.species1, args.species2)
    if result is None:
        print(f"No data found for '{args.species1}' and '{args.species2}'.")
        print("Try different names or expand the database at 'data/species_split_times.json'.")
        return

    min_mya = result.get("min_mya")
    max_mya = result.get("max_mya")
    note = result.get("note", "")

    print(f"Estimated split: {min_mya} - {max_mya} million years ago")
    if note:
        print(f"Note: {note}")


if __name__ == "__main__":
    main()
