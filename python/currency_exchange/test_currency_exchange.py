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


def test_exchange_money() -> None:
    """Verify that `exchange_money` returns correctly."""
    output = 106.25
    assert exchange_money(127.5, 1.2) == output


def test_get_change() -> None:
    """Verify that `get_change` returns correctly."""
    output = 7.5
    assert get_change(127.5, 120) == output


def test_get_value_of_bills() -> None:
    """Verify that `get_value_of_bills` returns correctly."""
    output = 640
    assert get_value_of_bills(5, 128) == output


def test_get_number_of_bills() -> None:
    """Verify that `get_number_of_bills` returns correctly."""
    output = 25
    assert get_number_of_bills(127.5, 5) == output


def test_get_leftover_of_bills() -> None:
    """Verify that `get_leftover_of_bills` returns correctly."""
    output = 7.5
    assert get_leftover_of_bills(127.5, 20) == output


def test_exchangeable_value() -> None:
    """Verify that `exchangeable_value` returns correctly."""
    output = 80
    assert exchangeable_value(127.25, 1.20, 10, 20) == output


if __name__ == "__main__":
    pytest.main()
