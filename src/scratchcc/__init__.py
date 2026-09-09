"""Scratch Cloud Checker (SCC)."""

__version__ = "0.0.1"


class SCC:
    """Main Scratch Cloud Checker interface."""

    def info(self) -> dict[str, str]:
        return {
            "name": "Scratch Cloud Checker",
            "package": "scratchcc",
            "version": __version__,
            "status": "development",
        }


__all__ = ["SCC", "__version__"]
