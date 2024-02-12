"""Solution to Making the Grade."""

from __future__ import annotations

PASS_MARK = 40
PERFECT_SCORE = 100


def round_scores(student_scores: list[float]) -> list[int]:
    """Round all provided student scores to the nearest integer.

    :param student_scores: The list of student exam scores.
    :type student_scores: list[float]
    :return: The student scores rounded to nearest integer value.
    :rtype: list[int]
    """
    return [round(score) for score in student_scores]


def count_failed_students(student_scores: list[int]) -> int:
    """Count the number of failing students out of the group provided.

    :param student_scores: The list containing student scores.
    :type student_scores: list[int]
    :return: The number of student scores at or below 40.
    :rtype: int
    """
    return sum(score <= PASS_MARK for score in student_scores)


def above_threshold(student_scores: list[int], threshold: int) -> list[int]:
    """Determine the list of student scores above the provided threshold.

    :param student_scores: The list of scores.
    :type student_scores: list[int]
    :param threshold: The threshold to cross to be the "best" score.
    :type threshold: int
    :return: The list of scores that are at or above the "best" threshold.
    :rtype: list[int]
    """
    return [score for score in student_scores if score >= threshold]


def letter_grades(highest: int) -> list[int]:
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: The value of highest exam score.
    :type highest: int
    :return: The of lower threshold scores for each D-A letter grade interval.
    :rtype: list[int]
    """
    grade_difference = round((highest - 40) / 4)
    return list(range(41, highest, grade_difference))


def student_ranking(student_scores: list[int], student_names: list[str]) -> list[str]:
    """Organize the student's rank, name, and grade information in ascending order.

    :param student_scores: The list of scores in descending order.
    :type student_scores: list[int]
    :param student_names: The list of names by exam score in descending order.
    :type student_names: list[str]
    :return: The list of the student ranks, names, and grades in ascending
        order.
    :rtype: list[str]
    """
    student_ranks = []

    for index, (name, score) in enumerate(zip(student_names, student_scores)):
        student_ranks.append(f"{index + 1}. {name}: {score}")

    return student_ranks


def perfect_score(student_info: list[list[str | int]]) -> list[str | int]:
    """List the name and grade of the first student to make a perfect score.

    :param student_info: The list of lists of student names and scores.
    :type student_info: list[list[str, int]]
    :return: The first student name and score who achieved 100.
    :rtype: list[str, int]
    """
    return next(
        ([name, score] for name, score in student_info if score == PERFECT_SCORE),
        [],
    )
