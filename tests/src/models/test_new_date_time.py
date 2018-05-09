import unittest

from src.models.new_date_time import NewDateTime


class TestNewDateTime(unittest.TestCase):
    """ Test NewDateTime model."""

    def setUp(self):
        self.valid_new_date_time = NewDateTime(12, 4, 1999, 3, 34)

    def test_day_validation(self):
        """It is NOT valid with the day being of a different type of integer
        when creating or changing the variable"""

        self.assertRaises(TypeError, NewDateTime, "12", 4, 1999, 3, 34)

        with self.assertRaises(TypeError):
            self.valid_new_date_time.day = "foo"

        self.assertEqual(self.valid_new_date_time.day, 12)

    def test_month_validation(self):
        """It is NOT valid with the month being of a different type of integer
        when creating or changing the variable"""

        self.assertRaises(TypeError, NewDateTime, 12, "4", 1999, 3, 34)

        with self.assertRaises(TypeError):
            self.valid_new_date_time.month = "foo"

        self.assertEqual(self.valid_new_date_time.month, 4)

    def test_year_validation(self):
        """It is NOT valid with the year being of a different type of integer
        when creating or changing the variable"""

        self.assertRaises(TypeError, NewDateTime, 12, 4, "1999", 3, 34)

        with self.assertRaises(TypeError):
            self.valid_new_date_time.year = "foo"

        self.assertEqual(self.valid_new_date_time.year, 1999)

    def test_hour_validation(self):
        """It is NOT valid with the hour being of a different type of integer
        when creating or changing the variable"""

        self.assertRaises(TypeError, NewDateTime, 12, 4, 1999, "3", 34)

        with self.assertRaises(TypeError):
            self.valid_new_date_time.hour = "foo"

        self.assertEqual(self.valid_new_date_time.hour, 3)

    def test_minute_validation(self):
        """It is NOT valid with the minute being of a different type of integer
        when creating or changing the variable"""

        self.assertRaises(TypeError, NewDateTime, 12, 4, 1999, 3, "34")

        with self.assertRaises(TypeError):
            self.valid_new_date_time.minute = "foo"

        self.assertEqual(self.valid_new_date_time.minute, 34)
