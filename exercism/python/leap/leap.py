"""This is the Leap Year Module.

The function in this module calculates whether a given year is a leap year.
"""


def leap_year(year: int) -> bool:
    """Determine whether the year is a leap year.

    :param year: int - The year being evaluated.
    :return: bool - Is the year a leap year?

    This function takes a year as an argument and computes whether or not it is
    a leap year.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
