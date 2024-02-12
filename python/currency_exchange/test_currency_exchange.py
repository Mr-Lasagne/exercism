"""Test suite for Currency Exchange."""

import pytest

from python.currency_exchange.currency_exchange import (
    exchange_money,
    exchangeable_value,
    get_change,
    get_leftover_of_bills,
    get_number_of_bills,
    get_value_of_bills,
)


@pytest.mark.parametrize(
    ("budget", "exchange_rate", "expected"),
    [(100000, 0.8, 125000), (700000, 10.0, 70000)],
)
def test_exchange_money(budget: float, exchange_rate: float, expected: float) -> None:
    """Verify that `exchange_money` returns correctly."""
    assert exchange_money(budget, exchange_rate) == expected


@pytest.mark.parametrize(
    ("budget", "exchange_rate", "expected"),
    [(463000, 5000, 458000), (1250, 120, 1130), (15000, 1380, 13620)],
)
def test_get_change(budget: float, exchange_rate: float, expected: float) -> None:
    """Verify that `get_change` returns correctly."""
    assert get_change(budget, exchange_rate) == expected


@pytest.mark.parametrize(
    ("denomination", "number_of_bills", "expected"),
    [(10000, 128, 1280000), (50, 360, 18000), (200, 200, 40000)],
)
def test_get_value_of_bills(
    denomination: int,
    number_of_bills: int,
    expected: int,
) -> None:
    """Verify that `get_value_of_bills` returns correctly."""
    assert get_value_of_bills(denomination, number_of_bills) == expected


@pytest.mark.parametrize(
    ("amount", "denomination", "expected"),
    [(163270, 50000, 3), (54361, 1000, 54)],
)
def test_get_number_of_bills(amount: float, denomination: int, expected: int) -> None:
    """Verify that `get_number_of_bills` returns correctly."""
    assert get_number_of_bills(amount, denomination) == expected


@pytest.mark.parametrize(
    ("amount", "denomination", "expected"),
    [(10.1, 10, 0.1), (654321.0, 5, 1.0), (3.14, 2, 1.14)],
)
def test_get_leftover_of_bills(
    amount: float,
    denomination: int,
    expected: float,
) -> None:
    """Verify that `get_leftover_of_bills` returns correctly."""
    assert pytest.approx(get_leftover_of_bills(amount, denomination)) == expected


@pytest.mark.parametrize(
    ("budget", "exchange_rate", "spread", "denomination", "expected"),
    [
        (100000, 10.61, 10, 1, 8568),
        (1500, 0.84, 25, 40, 1400),
        (470000, 1050, 30, 10000000000, 0),
        (470000, 0.00000009, 30, 700, 4017094016600),
        (425.33, 0.0009, 30, 700, 363300),
    ],
)
def test_exchangeable_value(
    budget: float,
    exchange_rate: float,
    spread: int,
    denomination: int,
    expected: int,
) -> None:
    """Verify that `exchangeable_value` returns correctly."""
    assert exchangeable_value(budget, exchange_rate, spread, denomination) == expected


if __name__ == "__main__":
    pytest.main()
