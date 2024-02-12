"""Test suite for Little Sister's Vocabulary."""

from __future__ import annotations

import pytest

from python.little_sisters_vocabulary.little_sisters_vocabulary import (
    add_prefix_un,
    adjective_to_verb,
    make_word_groups,
    remove_suffix_ness,
)


@pytest.mark.parametrize(
    ("word", "expected"),
    [
        ("happy", "unhappy"),
        ("manageable", "unmanageable"),
        ("fold", "unfold"),
        ("eaten", "uneaten"),
        ("avoidable", "unavoidable"),
        ("usual", "unusual"),
    ],
)
def test_add_prefix_un(word: str, expected: str) -> None:
    """Verify `add_prefix_un` returns correctly."""
    assert add_prefix_un(word) == expected


@pytest.mark.parametrize(
    ("vocabulary_words", "expected"),
    [
        pytest.param(
            [
                "en",
                "circle",
                "fold",
                "close",
                "joy",
                "lighten",
                "tangle",
                "able",
                "code",
                "culture",
            ],
            "en :: encircle :: enfold :: enclose :: enjoy :: enlighten :: entangle :: "
            "enable :: encode :: enculture",
            id="make_word_groups_en",
        ),
        pytest.param(
            [
                "pre",
                "serve",
                "dispose",
                "position",
                "requisite",
                "digest",
                "natal",
                "addressed",
                "adolescent",
                "assumption",
                "mature",
                "compute",
            ],
            "pre :: preserve :: predispose :: preposition :: prerequisite :: predigest "
            ":: prenatal :: preaddressed :: preadolescent :: preassumption :: premature"
            " :: precompute",
            id="make_word_groups_pre",
        ),
        pytest.param(
            [
                "auto",
                "didactic",
                "graph",
                "mate",
                "chrome",
                "centric",
                "complete",
                "echolalia",
                "encoder",
                "biography",
            ],
            "auto :: autodidactic :: autograph :: automate :: autochrome :: autocentric"
            " :: autocomplete :: autoecholalia :: autoencoder :: autobiography",
            id="make_word_groups_auto",
        ),
        pytest.param(
            [
                "inter",
                "twine",
                "connected",
                "dependent",
                "galactic",
                "action",
                "stellar",
                "cellular",
                "continental",
                "axial",
                "operative",
                "disciplinary",
            ],
            "inter :: intertwine :: interconnected :: interdependent :: intergalactic "
            ":: interaction :: interstellar :: intercellular :: intercontinental :: "
            "interaxial :: interoperative :: interdisciplinary",
            id="make_word_groups_inter",
        ),
    ],
)
def test_make_word_groups(vocabulary_words: list[str], expected: str) -> None:
    """Verify `make_word_groups` returns correctly."""
    assert make_word_groups(vocabulary_words) == expected


@pytest.mark.parametrize(
    ("word", "expected"),
    [
        ("heaviness", "heavy"),
        ("sadness", "sad"),
        ("softness", "soft"),
        ("crabbiness", "crabby"),
        ("lightness", "light"),
        ("artiness", "arty"),
        ("edginess", "edgy"),
    ],
)
def test_remove_suffix_ness(word: str, expected: str) -> None:
    """Verify `remove_suffix_ness` returns correctly."""
    assert remove_suffix_ness(word) == expected


@pytest.mark.parametrize(
    ("sentence", "index", "expected"),
    [
        ("Look at the bright sky.", -2, "brighten"),
        ("His expression went dark.", -1, "darken"),
        ("The bread got hard after sitting out.", 3, "harden"),
        ("The butter got soft in the sun.", 3, "soften"),
        ("Her eyes were light blue.", -2, "lighten"),
        ("The morning fog made everything damp with mist.", -3, "dampen"),
        ("He cut the fence pickets short by mistake.", 5, "shorten"),
        ("Charles made weak crying noises.", 2, "weaken"),
        ("The black oil got on the white dog.", 1, "blacken"),
    ],
)
def test_adjective_to_verb(sentence: str, index: int, expected: str) -> None:
    """Verify `adjective_to_verb` returns correctly."""
    assert adjective_to_verb(sentence, index) == expected


if __name__ == "__main__":
    pytest.main()
