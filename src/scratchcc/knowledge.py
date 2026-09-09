"""Human-curated knowledge storage for Scratch Cloud Checker."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


class KnowledgeBase:
    """Store facts that are intentionally taught to SCC."""

    def __init__(self) -> None:
        self._items: list[dict[str, Any]] = []
        self._next_id = 1

    def learn(
        self,
        text: str,
        *,
        category: str = "general",
        source: str | None = None,
    ) -> dict[str, Any]:
        """Add a fact to the knowledge base."""
        if not isinstance(text, str) or not text.strip():
            raise ValueError("text must be a non-empty string")
        if not isinstance(category, str) or not category.strip():
            raise ValueError("category must be a non-empty string")
        if source is not None and not isinstance(source, str):
            raise TypeError("source must be a string or None")

        item = {
            "id": self._next_id,
            "text": text.strip(),
            "category": category.strip(),
            "source": source.strip() if source else None,
            "learned_at": datetime.now(timezone.utc).isoformat(),
        }
        self._items.append(item)
        self._next_id += 1
        return dict(item)

    def search(self, query: str) -> list[dict[str, Any]]:
        """Return knowledge entries containing all query words."""
        if not isinstance(query, str) or not query.strip():
            return []

        terms = query.casefold().split()
        matches = []
        for item in self._items:
            haystack = " ".join(
                str(item.get(key, ""))
                for key in ("text", "category", "source")
            ).casefold()
            if all(term in haystack for term in terms):
                matches.append(dict(item))
        return matches

    def all(self) -> list[dict[str, Any]]:
        """Return all stored knowledge."""
        return [dict(item) for item in self._items]

    def forget(self, item_id: int) -> bool:
        """Remove knowledge by ID. Returns True when something was removed."""
        for index, item in enumerate(self._items):
            if item["id"] == item_id:
                del self._items[index]
                return True
        return False

    def clear(self) -> None:
        """Remove all knowledge entries."""
        self._items.clear()


__all__ = ["KnowledgeBase"]
