"""Solution to Armstrong Numbers."""


def is_armstrong_number(number: int) -> bool:
    """Determine whether or not a given number is an Armstrong number.

    :param number: A given integer.
    :type number: int
    :return: True if the number is an Armstrong number, False otherwise.
    :rtype: bool
    """
    return number == sum(int(digit) ** len(str(number)) for digit in str(number))
