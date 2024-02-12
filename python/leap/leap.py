"""Solution to Leap."""


def is_leap_year(year: int) -> bool:
    """Determine whether the year is a leap year.

    :param year: The year being evaluated.
    :type year: int
    :return: True if the year is a leap year, False otherwise.
    :rtype: bool
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
