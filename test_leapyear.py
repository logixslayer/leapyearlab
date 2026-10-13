import unittest
from leap_year import isLeapYear

class TestLeapYear(unittest.TestCase):

    def test_leap_year(self):
        self.assertTrue(isLeapYear(2024))

    def test_non_leap_year(self):
        self.assertFalse(isLeapYear(2023))

    def test_century_non_leap_year(self):
        self.assertFalse(isLeapYear(1900))

    def test_century_leap_year(self):
        self.assertTrue(isLeapYear(2000))

if __name__ == "__main__":
    unittest.main()