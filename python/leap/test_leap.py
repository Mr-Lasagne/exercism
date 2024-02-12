"""Test suite for Leap."""

import pytest

from python.leap.leap import is_leap_year


@pytest.mark.parametrize(
    ("year", "expected"),
    [
        pytest.param(2015, False, id="year_not_divisible_by_4_is_common_year"),
        pytest.param(1970, False, id="year_divisible_by_2_and_not_by_4_is_common_year"),
        pytest.param(1996, True, id="year_divisible_by_4_and not_by_100_is_leap_year"),
        pytest.param(1960, True, id="year_divisible_by_4_and_5_is_leap_year"),
        pytest.param(
            2100,
            False,
            id="year_divisible_by_100_and_not_by_400_is_common_year",
        ),
        pytest.param(
            1900,
            False,
            id="year_divisible_by_100_and_not_by_3_is_common_year",
        ),
        pytest.param(2000, True, id="year_divisible_by_400_is_leap_year"),
        pytest.param(
            2400,
            True,
            id="year_divisible_by_400_and_not_by_125_is_leap_year",
        ),
        pytest.param(
            1800,
            False,
            id="year_divisible_by_200_and_not_by_400_is_common_year",
        ),
    ],
)
def test_is_leap_year(year: int, *, expected: bool) -> None:
    """Verify `is_leap_year` returns correctly."""
    assert is_leap_year(year) == expected


if __name__ == "__main__":
    pytest.main()
