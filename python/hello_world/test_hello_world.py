"""Test suite for Hello World."""

import pytest

from python.hello_world.hello_world import hello


def test_say_hello_world() -> None:
    """Verify that `hello` returns correctly."""
    assert hello() == "Hello, World!"


if __name__ == "__main__":
    pytest.main()
