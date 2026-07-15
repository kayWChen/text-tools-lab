"""text_tools — small string utilities."""


def word_count(text: str) -> int:
    """Return the number of whitespace-separated words in text."""
    if not text:
        return 0
    return len(text.split())


def reverse_words(text: str) -> str:
    """Reverse the order of words in a sentence."""
    return " ".join(reversed(text.split()))


def capitalize_each(text: str) -> str:
    """Capitalize the first letter of every word."""
    return " ".join(word.capitalize() for word in text.split())

def char_count(text: str, include_spaces: bool = True) -> int:
    """Count characters, optionally excluding whitespace."""
    if include_spaces:
        return len(text)
    return len(text.replace(" ", ""))