"""Test suite for Little Sister's Essay."""

import pytest

from python.little_sisters_essay.little_sisters_essay import (
    capitalize_title,
    check_sentence_ending,
    clean_up_spacing,
    replace_word_choice,
)


def test_capitalize_word() -> None:
    """Verify `capitalize_word` returns correctly."""
    assert capitalize_title("canopy") == "Canopy"


def test_sentence_ending() -> None:
    """Verify `sentence_ending` returns correctly."""
    assert check_sentence_ending("Snails can sleep for 3 years.") is True


def test_remove_extra_spaces() -> None:
    """Verify `remove_extra_spaces` returns correctly."""
    assert clean_up_spacing("  Elephants can't jump.  ") == "Elephants can't jump."


def test_replace_word_choice() -> None:
    """Verify `replace_word_choice` returns correctly."""
    assert (
        replace_word_choice("Animals are cool.", "cool", "awesome")
        == "Animals are awesome."
    )


if __name__ == "__main__":
    pytest.main()
