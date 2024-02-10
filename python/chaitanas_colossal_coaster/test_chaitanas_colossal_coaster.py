"""Test suite for Chaitana's Colossal Coaster."""

from __future__ import annotations

import pytest

from python.chaitanas_colossal_coaster.chaitanas_colossal_coaster import (
    add_me_to_the_queue,
    add_me_with_my_friends,
    find_my_friend,
    how_many_namefellows,
    remove_the_last_person,
    remove_the_mean_person,
    sorted_names,
)


@pytest.mark.parametrize(
    ("express_queue", "normal_queue", "ticket_type", "person_name", "expected"),
    [
        (
            ["Tony", "Bruce"],
            ["RobotGuy", "WW"],
            0,
            "HawkEye",
            ["RobotGuy", "WW", "HawkEye"],
        ),
        (
            ["Tony", "Bruce"],
            ["RobotGuy", "WW"],
            1,
            "RichieRich",
            ["Tony", "Bruce", "RichieRich"],
        ),
    ],
)
def test_add_me_to_the_queue(
    express_queue: list[str],
    normal_queue: list[str],
    ticket_type: int,
    person_name: str,
    expected: list[str],
) -> None:
    """Verify `add_me_to_the_queue` returns correctly."""
    assert (
        add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name)
        == expected
    )


@pytest.mark.parametrize(
    ("queue", "friend_name", "expected"),
    [
        (["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], "Natasha", 0),
        (["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], "Steve", 1),
        (["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], "Rocket", 4),
    ],
)
def test_find_my_friend(queue: list[str], friend_name: str, expected: int) -> None:
    """Verify `find_my_friend` returns correctly."""
    assert find_my_friend(queue, friend_name) == expected


@pytest.mark.parametrize(
    ("queue", "index", "person_name", "expected"),
    [
        (
            ["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"],
            0,
            "Bucky",
            ["Bucky", "Natasha", "Steve", "Tchalla", "Wanda", "Rocket"],
        ),
        (
            ["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"],
            1,
            "Bucky",
            ["Natasha", "Bucky", "Steve", "Tchalla", "Wanda", "Rocket"],
        ),
        (
            ["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"],
            5,
            "Bucky",
            ["Natasha", "Steve", "Tchalla", "Wanda", "Rocket", "Bucky"],
        ),
    ],
)
def test_add_me_with_my_friends(
    queue: list[str],
    index: int,
    person_name: str,
    expected: list[str],
) -> None:
    """Verify `add_me_with_my_friends` returns correctly."""
    assert add_me_with_my_friends(queue, index, person_name) == expected


@pytest.mark.parametrize(
    ("queue", "person_name", "expected"),
    [
        (
            ["Natasha", "Steve", "Ultron", "Wanda", "Rocket"],
            "Ultron",
            ["Natasha", "Steve", "Wanda", "Rocket"],
        ),
        (
            ["Natasha", "Steve", "Wanda", "Rocket", "Ultron"],
            "Ultron",
            ["Natasha", "Steve", "Wanda", "Rocket"],
        ),
        (
            ["Ultron", "Natasha", "Steve", "Wanda", "Rocket"],
            "Ultron",
            ["Natasha", "Steve", "Wanda", "Rocket"],
        ),
    ],
)
def test_remove_the_mean_person(
    queue: list[str],
    person_name: str,
    expected: list[str],
) -> None:
    """Verify `remove_the_mean_person` returns correctly."""
    assert remove_the_mean_person(queue, person_name) == expected


@pytest.mark.parametrize(
    ("queue", "person_name", "expected"),
    [
        (["Natasha", "Steve", "Ultron", "Natasha", "Rocket"], "Bucky", 0),
        (["Natasha", "Steve", "Ultron", "Rocket"], "Natasha", 1),
        (["Natasha", "Steve", "Ultron", "Natasha", "Rocket"], "Natasha", 2),
    ],
)
def test_how_many_namefellows(
    queue: list[str],
    person_name: str,
    expected: int,
) -> None:
    """Verify `how_many_namefellows` returns correctly."""
    assert how_many_namefellows(queue, person_name) == expected


def test_remove_the_last_person() -> None:
    """Verify `remove_the_last_person` returns correctly."""
    assert (
        remove_the_last_person(["Natasha", "Steve", "Ultron", "Natasha", "Rocket"])
        == "Rocket"
    )


def test_sorted_names() -> None:
    """Verify `sorted_names` returns correctly."""
    assert sorted_names(["Steve", "Ultron", "Natasha", "Rocket"]) == [
        "Natasha",
        "Rocket",
        "Steve",
        "Ultron",
    ]


if __name__ == "__main__":
    pytest.main()
