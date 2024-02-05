import unittest

import pytest
from zebra_puzzle import drinks_water, owns_zebra


class TestZebraPuzzle(unittest.TestCase):
    def test_resident_who_drinks_water(self):
        self.assertEqual(drinks_water(), "Norwegian")

    def test_resident_who_owns_zebra(self):
        self.assertEqual(owns_zebra(), "Japanese")


if __name__ == "__main__":
    pytest.main()
