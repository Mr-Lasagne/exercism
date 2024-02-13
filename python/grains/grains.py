"""Solution to Grains."""

TOTAL = 2**64 - 1
NUMBER_OF_SQUARES = 64


def square(number: int) -> int:
    """Calculate the number of grains on a given square.

    :param number: The given square number.
    :type number: int
    :raise ValueError: If square number is outside the range.
    :return: The number of grains on the given square number.
    :rtype: int
    """
    if not 1 <= number <= NUMBER_OF_SQUARES:
        msg = "Number must be between 1 and 64."
        raise ValueError(msg)

    return 2 ** (number - 1)


def total() -> int:
    """Calculate the total number of grains on the chessboard.

    :return: The total number of grains on the chessboard.
    :rtype: int
    """
    return TOTAL
