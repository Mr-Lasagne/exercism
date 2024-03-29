"""Test suite for Making the Grade."""

from __future__ import annotations

import pytest

from python.making_the_grade.making_the_grade import (
    above_threshold,
    count_failed_students,
    letter_grades,
    perfect_score,
    round_scores,
    student_ranking,
)


@pytest.mark.parametrize(
    ("student_scores", "expected"),
    [
        ([], []),
        ([0.5], [0]),
        ([1.5], [2]),
        (
            [90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3],
            [90, 40, 55, 70, 31, 25, 80, 95, 39, 40],
        ),
        (
            [50, 36.03, 76.92, 40.7, 43, 78.29, 63.58, 91, 28.6, 88.0],
            [50, 36, 77, 41, 43, 78, 64, 91, 29, 88],
        ),
    ],
)
def test_round_scores(student_scores: list[float], expected: list[int]) -> None:
    """Verify `round_scores` returns correctly."""
    assert round_scores(student_scores) == expected


@pytest.mark.parametrize(
    ("student_scores", "expected"),
    [([89, 85, 42, 57, 90, 100, 95, 48, 70, 96], 0), ([40, 40, 35, 70, 30, 41, 90], 4)],
)
def test_count_failed_students(student_scores: list[int], expected: int) -> None:
    """Verify `count_failed_students` returns correctly."""
    assert count_failed_students(student_scores) == expected


@pytest.mark.parametrize(
    ("student_scores", "threshold", "expected"),
    [
        ([40, 39, 95, 80, 25, 31, 70, 55, 40, 90], 98, []),
        ([88, 29, 91, 64, 78, 43, 41, 77, 36, 50], 80, [88, 91]),
        ([100, 89], 100, [100]),
        ([88, 29, 91, 64, 78, 43, 41, 77, 36, 50], 78, [88, 91, 78]),
        ([], 80, []),
    ],
)
def test_above_threshold(
    student_scores: list[int],
    threshold: int,
    expected: list[int],
) -> None:
    """Verify `above_threshold` returns correctly."""
    assert above_threshold(student_scores, threshold) == expected


@pytest.mark.parametrize(
    ("highest", "expected"),
    [
        (100, [41, 56, 71, 86]),
        (97, [41, 55, 69, 83]),
        (85, [41, 52, 63, 74]),
        (92, [41, 54, 67, 80]),
        (81, [41, 51, 61, 71]),
    ],
)
def test_letter_grades(highest: int, expected: list[int]) -> None:
    """Verify `letter_grades` returns correctly."""
    assert letter_grades(highest) == expected


@pytest.mark.parametrize(
    ("student_scores", "student_names", "expected"),
    [
        ([82], ["Betty"], ["1. Betty: 82"]),
        ([88, 73], ["Paul", "Ernest"], ["1. Paul: 88", "2. Ernest: 73"]),
        (
            [100, 98, 92, 86, 70, 68, 67, 60],
            ["Rui", "Betty", "Joci", "Yoshi", "Kora", "Bern", "Jan", "Rose"],
            [
                "1. Rui: 100",
                "2. Betty: 98",
                "3. Joci: 92",
                "4. Yoshi: 86",
                "5. Kora: 70",
                "6. Bern: 68",
                "7. Jan: 67",
                "8. Rose: 60",
            ],
        ),
    ],
)
def test_student_ranking(
    student_scores: list[int],
    student_names: list[str],
    expected: list[str],
) -> None:
    """Verify `student_ranking` returns correctly."""
    assert student_ranking(student_scores, student_names) == expected


@pytest.mark.parametrize(
    ("student_info", "expected"),
    [
        (
            [["Joci", 100], ["Vlad", 100], ["Raiana", 100], ["Alessandro", 100]],
            ["Joci", 100],
        ),
        ([["Jill", 30], ["Paul", 73]], []),
        ([], []),
        (
            [
                ["Rui", 60],
                ["Joci", 58],
                ["Sara", 91],
                ["Kora", 93],
                ["Alex", 42],
                ["Jan", 81],
                ["Lilliana", 40],
                ["John", 60],
                ["Bern", 28],
                ["Vlad", 55],
            ],
            [],
        ),
        (
            [
                ["Yoshi", 52],
                ["Jan", 86],
                ["Raiana", 100],
                ["Betty", 60],
                ["Joci", 100],
                ["Kora", 81],
                ["Bern", 41],
                ["Rose", 94],
            ],
            ["Raiana", 100],
        ),
    ],
)
def test_perfect_score(
    student_info: list[list[str | int]],
    expected: list[str | int],
) -> None:
    """Verify `perfect_score` returns correctly."""
    assert perfect_score(student_info) == expected


if __name__ == "__main__":
    pytest.main()
