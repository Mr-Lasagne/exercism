"""Test suite for Little Sister's Essay."""

import pytest

from python.little_sisters_essay.little_sisters_essay import (
    capitalize_title,
    check_sentence_ending,
    clean_up_spacing,
    replace_word_choice,
)


@pytest.mark.parametrize(
    ("title", "expected"),
    [
        pytest.param("canopy", "Canopy", id="capitalize_single_word"),
        pytest.param(
            "fish are cold blooded",
            "Fish Are Cold Blooded",
            id="capitalize_multiple_words",
        ),
    ],
)
def test_capitalize_title(title: str, expected: str) -> None:
    """Verify `capitalize_word` returns correctly."""
    assert capitalize_title(title) == expected


@pytest.mark.parametrize(
    ("sentence", "expected"),
    [
        pytest.param(
            "Snails can sleep for 3 years.",
            True,
            id="sentence_ending_with_period",
        ),
        pytest.param("Fittonia are nice", False, id="sentence_ending_without_period"),
    ],
)
def test_check_sentence_ending(sentence: str, *, expected: bool) -> None:
    """Verify `sentence_ending` returns correctly."""
    assert check_sentence_ending(sentence) == expected


@pytest.mark.parametrize(
    ("sentence", "expected"),
    [
        pytest.param(
            "  A rolling stone gathers no moss",
            "A rolling stone gathers no moss",
            id="remove_leading_whitespace",
        ),
        pytest.param(
            "  Elephants can't jump.  ",
            "Elephants can't jump.",
            id="remove_leading_and_trailing_whitespace",
        ),
    ],
)
def test_clean_up_spacing(sentence: str, expected: str) -> None:
    """Verify `remove_extra_spaces` returns correctly."""
    assert clean_up_spacing(sentence) == expected


@pytest.mark.parametrize(
    ("sentence", "old_word", "new_word", "expected"),
    [
        pytest.param(
            "Animals are cool.",
            "cool",
            "awesome",
            "Animals are awesome.",
            id="replace_word_in_phrase",
        ),
        pytest.param(
            "Animals are cool.",
            "small",
            "tiny",
            "Animals are cool.",
            id="fail_to_replace_word_not_in_phrase",
        ),
    ],
)
def test_replace_word_choice(
    sentence: str,
    old_word: str,
    new_word: str,
    expected: str,
) -> None:
    """Verify `replace_word_choice` returns correctly."""
    assert replace_word_choice(sentence, old_word, new_word) == expected


if __name__ == "__main__":
    pytest.main()
