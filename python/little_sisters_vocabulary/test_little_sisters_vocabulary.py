"""Test suite for Little Sister's Vocabulary."""

import pytest

from python.little_sisters_vocabulary.little_sisters_vocabulary import (
    add_prefix_un,
    adjective_to_verb,
    make_word_groups,
    remove_suffix_ness,
)


def test_add_prefix_un() -> None:
    """Verify `add_prefix_un` returns correctly."""
    assert add_prefix_un("happy") == "unhappy"


def test_make_word_groups() -> None:
    """Verify `make_word_groups` returns correctly."""
    assert (
        make_word_groups(["en", "circle", "fold", "close", "lighten"])
        == "en :: encircle :: enfold :: enclose :: enlighten"
    )


@pytest.mark.parametrize(
    ("word", "expected"),
    [
        pytest.param("heaviness", "heavy", id="ending_with_iness"),
        pytest.param("sadness", "sad", id="ending_with_ness"),
    ],
)
def test_remove_suffix_ness(word: str, expected: str) -> None:
    """Verify `remove_suffix_ness` returns correctly."""
    assert remove_suffix_ness(word) == expected


def test_adjective_to_verb() -> None:
    """Verify `adjective_to_verb` returns correctly."""
    assert adjective_to_verb("His expression went dark.", -1) == "darken"


if __name__ == "__main__":
    pytest.main()
