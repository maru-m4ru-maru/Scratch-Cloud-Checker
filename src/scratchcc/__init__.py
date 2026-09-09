"""Scratch Cloud Checker (SCC)."""

from .knowledge import KnowledgeBase
from .memory import Memory

__version__ = "0.0.3"


class SCC:
    """Main Scratch Cloud Checker interface."""

    def __init__(
        self,
        memory: Memory | None = None,
        knowledge: KnowledgeBase | None = None,
    ) -> None:
        self.memory = memory or Memory()
        self.knowledge = knowledge or KnowledgeBase()

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

    def learn(
        self,
        text: str,
        *,
        category: str = "general",
        source: str | None = None,
    ) -> dict:
        """Teach SCC a curated fact for its knowledge base."""
        return self.knowledge.learn(text, category=category, source=source)

    def search_knowledge(self, query: str) -> list[dict]:
        """Find curated knowledge related to a query."""
        return self.knowledge.search(query)

    def knowledge_all(self) -> list[dict]:
        """Return all curated knowledge entries."""
        return self.knowledge.all()

    def forget_knowledge(self, item_id: int) -> bool:
        """Remove one curated knowledge entry."""
        return self.knowledge.forget(item_id)


__all__ = ["SCC", "Memory", "KnowledgeBase", "__version__"]
