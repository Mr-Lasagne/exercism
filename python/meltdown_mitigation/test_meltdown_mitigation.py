"""Test suite for Meltdown Mitigation."""

import pytest

from python.meltdown_mitigation.meltdown_mitigation import (
    fail_safe,
    is_criticality_balanced,
    reactor_efficiency,
)


def test_is_criticality_balanced() -> None:
    """Verify `is_criticality_balanced` returns correctly."""
    assert is_criticality_balanced(750, 600) is True


@pytest.mark.parametrize(
    ("voltage", "current", "theoretical_max_power", "expected"),
    [
        pytest.param(10, 1000, 10000, "green", id="efficiency_green"),
        pytest.param(10, 799, 10000, "orange", id="efficiency_orange"),
        pytest.param(10, 599, 10000, "red", id="efficiency_red"),
        pytest.param(10, 299, 10000, "black", id="efficiency_black"),
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
        pytest.param(10, 399, 10000, "LOW", id="status_low"),
        pytest.param(10, 901, 10000, "NORMAL", id="status_normal"),
        pytest.param(10, 1101, 10000, "DANGER", id="status_danger"),
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
