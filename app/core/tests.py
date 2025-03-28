"""
Sample tests
"""

from django.test import SimpleTestCase
from . import calc


class CalcTests(SimpleTestCase):
    """Test adding numbers together."""

    def test_add_numbers(self):
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        res = calc.subtract(10, 15)
        self.assertEqual(res, 5)
