"""Scratch Cloud Checker (SCC)."""

from .memory import Memory

__version__ = "0.0.2"


class SCC:
    """Main Scratch Cloud Checker interface."""

    def __init__(self, memory: Memory | None = None) -> None:
        self.memory = memory or Memory()

    def info(self) -> dict[str, str]:
        return {
            "name": "Scratch Cloud Checker",
            "package": "scratchcc",
            "version": __version__,
            "status": "development",
        }

    def remember(self, text: str, *, category: str = "general") -> dict:
        """Remember a piece of information for future conversations."""
        return self.memory.remember(text, category=category)

    def recall(self, query: str) -> list[dict]:
        """Find memories related to a query."""
        return self.memory.recall(query)


__all__ = ["SCC", "Memory", "__version__"]
