"""Very small mock database layer for species split-time lookups.

This module loads `data/species_split_times.json` and provides a simple
lookup API. It's intentionally forgiving with name matching (lowercase,
whitespace-trimmed) and will attempt to match either order of the pair.
"""
from __future__ import annotations

import json
import os
from typing import Optional, Dict, Any


def _normalize(name: str) -> str:
    return name.strip().lower()


class SpeciesDatabase:
    def __init__(self, json_path: str):
        self.path = json_path
        self._data: Dict[str, Dict[str, Any]] = {}
        if os.path.exists(self.path):
            with open(self.path, "r", encoding="utf-8") as fh:
                self._data = json.load(fh)

    def get_split_time(self, a: str, b: str) -> Optional[Dict[str, Any]]:
        """Return a dict with keys `min_mya`, `max_mya`, and optional `note`.

        Matching strategy (prototype):
        - Exact pair key `a:b` or `b:a` (normalized)
        - If no exact key, search keys containing both names as substrings.
        - Otherwise return None.
        """
        na = _normalize(a)
        nb = _normalize(b)

        # exact keys
        key1 = f"{na}:{nb}"
        key2 = f"{nb}:{na}"
        if key1 in self._data:
            return self._data[key1]
        if key2 in self._data:
            return self._data[key2]

        # substring match
        for key, val in self._data.items():
            kparts = [p.strip() for p in key.split(":")]
            if na in kparts and nb in kparts:
                return val

        # last attempt: keys where both names appear anywhere
        for key, val in self._data.items():
            kn = key.lower()
            if na in kn and nb in kn:
                return val

        return None
