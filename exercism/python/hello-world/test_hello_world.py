"""Test suite for Exercism's Python exercise: Hello World."""

import pytest
from hello_world import hello


def test_say_hello_world() -> None:
    """Test case for the function to say hello."""
    assert hello() == "Hello, World!"


if __name__ == "__main__":
    pytest.main()
