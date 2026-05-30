"""
Md Heading Operations Module.

Provides functions for processing heading text into
Markdown, HTML, Title Case and hyperlink IDs.
"""

__author__ = "UTHSAB CHANDRA PAUL SAJIB"


def get_markdown(words: list[str], level: int) -> str:
    """
    Generates a Markdown string.

    Args:
        words: list[str]  # List of words in the heading.
        level: int  # Heading level (1-6)

    Returns:
           str: Markdown formatted heading string.
    """
    # Pre-declare Variable
    text: str  # Stores the full heading as a single string

    text = " ".join(words)
    return "#" * level + " " + text


def make_title_case(words: list[str]):
    """
    Converts list of words to Title Case.

    Args:
        words: list[str]  # List of heading words

    Returns: None
    """
    # Pre-declare Variables:
    i: int  # Loop counter for list index
    word: str  # Stores current word being processed

    for i in range(len(words)):
        word = words[i]
        words[i] = word[0].upper() + word[1:].lower()


def get_id(words: list[str], level: int) -> str:
    """
    Creates a hyperlink ID for the heading

    Args:
        words: list[str]  # List of words in the heading
        level: int  # Heading level

    Returns:
           str: Hyperlink ID string.
    """
    # Pre-declare VAriable:
    text: str  # Stores hyphen-joined lowercase heading

    text = "-".join(words).lower()
    return f"#{level}-{text}"


def get_html(words: list[str], level: int) -> str:
    """
    Generates HTML Heading

    Args:
        words: list[str]  # List of heading words
        level: int  # Heading level

    Returns: 
           str: HTML formatted heading string
    """
    # Pre-declare Variables:
    text: str  # Stores full heading text

    text = " ".join(words)
    return f"<h{level}>{text}</h{level}>"

