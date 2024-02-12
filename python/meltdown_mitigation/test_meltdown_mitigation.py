"""Test suite for Meltdown Mitigation."""

import pytest

from python.meltdown_mitigation.meltdown_mitigation import (
    fail_safe,
    is_criticality_balanced,
    reactor_efficiency,
)


@pytest.mark.parametrize(
    ("temperature", "neutrons_emitted", "expected"),
    [
        (750, 650, True),
        (799, 501, True),
        (500, 600, True),
        (1000, 800, False),
        (800, 500, False),
        (800, 500.01, False),
        (799.99, 500, False),
        (500.01, 999.99, False),
        (625, 800, False),
        (625.99, 800, False),
        (625.01, 799.99, False),
        (799.99, 500.01, True),
        (624.99, 799.99, True),
        (500, 1000, False),
        (500.01, 1000, False),
        (499.99, 1000, True),
    ],
)
def test_is_criticality_balanced(
    temperature: float,
    neutrons_emitted: float,
    *,
    expected: bool,
) -> None:
    """Verify `is_criticality_balanced` returns correctly."""
    assert is_criticality_balanced(temperature, neutrons_emitted) == expected


@pytest.mark.parametrize(
    ("voltage", "current", "theoretical_max_power", "expected"),
    [
        (10, 1_000, 10_000, "green"),
        (10, 999, 10_000, "green"),
        (10, 800, 10_000, "green"),
        (10, 799, 10_000, "orange"),
        (10, 700, 10_000, "orange"),
        (10, 600, 10_000, "orange"),
        (10, 599, 10_000, "red"),
        (10, 560, 10_000, "red"),
        (10, 400, 10_000, "red"),
        (10, 300, 10_000, "red"),
        (10, 299, 10_000, "black"),
        (10, 200, 10_000, "black"),
        (10, 0, 10_000, "black"),
    ],
)
def test_reactor_efficiency(
    voltage: float,
    current: float,
    theoretical_max_power: float,
    expected: str,
) -> None:
    """Verify `reactor_efficiency` returns correctly."""
    assert reactor_efficiency(voltage, current, theoretical_max_power) == expected


@pytest.mark.parametrize(
    ("temperature", "neutrons_produced_per_second", "threshold", "expected"),
    [
        (10, 399, 10_000, "LOW"),
        (10, 300, 10_000, "LOW"),
        (10, 1, 10_000, "LOW"),
        (10, 0, 10_000, "LOW"),
        (10, 901, 10_000, "NORMAL"),
        (10, 1_000, 10_000, "NORMAL"),
        (10, 1_099, 10_000, "NORMAL"),
        (10, 899, 10_000, "LOW"),
        (10, 700, 10_000, "LOW"),
        (10, 400, 10_000, "LOW"),
        (10, 1_101, 10_000, "DANGER"),
        (10, 1_200, 10_000, "DANGER"),
    ],
)
def test_fail_safe(
    temperature: float,
    neutrons_produced_per_second: float,
    threshold: float,
    expected: str,
) -> None:
    """Verify `fail_safe` returns correctly."""
    assert fail_safe(temperature, neutrons_produced_per_second, threshold) == expected


if __name__ == "__main__":
    pytest.main()
