"""Simple persistent memory for Scratch Cloud Checker (SCC)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class Memory:
    """Store and search simple text memories in a local JSON file."""

    def __init__(self, path: str | Path = "scc_memory.json") -> None:
        self.path = Path(path)
        self._items: list[dict[str, Any]] = []
        self._load()

    def _load(self) -> None:
        if not self.path.exists():
            return

        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            self._items = []
            return

        if isinstance(data, list):
            self._items = [item for item in data if isinstance(item, dict)]

    def _save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(
            json.dumps(self._items, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def remember(self, text: str, *, category: str = "general") -> dict[str, Any]:
        """Save a memory and return the saved record."""
        if not isinstance(text, str) or not text.strip():
            raise ValueError("text must be a non-empty string")
        if not isinstance(category, str) or not category.strip():
            raise ValueError("category must be a non-empty string")

        item = {
            "id": len(self._items) + 1,
            "text": text.strip(),
            "category": category.strip(),
        }
        self._items.append(item)
        self._save()
        return item

    def recall(self, query: str) -> list[dict[str, Any]]:
        """Return memories containing all query words, case-insensitively."""
        if not isinstance(query, str) or not query.strip():
            return []

        words = query.casefold().split()
        results = []
        for item in self._items:
            haystack = f"{item.get('text', '')} {item.get('category', '')}".casefold()
            if all(word in haystack for word in words):
                results.append(item.copy())
        return results

    def all(self) -> list[dict[str, Any]]:
        """Return all saved memories."""
        return [item.copy() for item in self._items]

    def forget(self, memory_id: int) -> bool:
        """Delete a memory by ID and return whether it existed."""
        for index, item in enumerate(self._items):
            if item.get("id") == memory_id:
                del self._items[index]
                self._save()
                return True
        return False

    def clear(self) -> None:
        """Delete all memories."""
        self._items = []
        self._save()


__all__ = ["Memory"]
