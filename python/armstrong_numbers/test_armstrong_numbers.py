"""Test suite for Armstrong Numbers."""

import pytest

from python.armstrong_numbers.armstrong_numbers import is_armstrong_number


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        pytest.param(0, True, id="zero_is_an_armstrong_number"),
        pytest.param(5, True, id="single_digit_numbers_are_armstrong_numbers"),
        pytest.param(10, False, id="there_are_no_two_digit_armstrong_numbers"),
        pytest.param(153, True, id="three_digit_number_that_is_an_armstrong_number"),
        pytest.param(
            100,
            False,
            id="three_digit_number_that_is_not_an_armstrong_number",
        ),
        pytest.param(9_474, True, id="four_digit_number_that_is_an_armstrong_number"),
        pytest.param(
            9_475,
            False,
            id="four_digit_number_that_is_not_an_armstrong_number",
        ),
        pytest.param(
            9_926_315,
            True,
            id="seven_digit_number_that_is_an_armstrong_number",
        ),
        pytest.param(
            9_926_314,
            False,
            id="seven_digit_number_that_is_not_an_armstrong_number",
        ),
    ],
)
def test_is_armstrong_number(number: int, *, expected: bool) -> None:
    """Verify that `is_armstrong_number` returns correctly."""
    assert is_armstrong_number(number) == expected


if __name__ == "__main__":
    pytest.main()
