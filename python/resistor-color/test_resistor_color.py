import unittest

import pytest
from resistor_color import color_code, colors


class TestResistorColor(unittest.TestCase):
    def test_black(self):
        self.assertEqual(color_code("black"), 0)

    def test_white(self):
        self.assertEqual(color_code("white"), 9)

    def test_orange(self):
        self.assertEqual(color_code("orange"), 3)

    def test_colors(self):
        expected = [
            "black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white",
        ]
        self.assertEqual(colors(), expected)


if __name__ == "__main__":
    pytest.main()
