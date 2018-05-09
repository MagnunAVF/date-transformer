import unittest

from faker import Faker
from random import randint

from src.models.new_date_time import NewDateTime
from src.exceptions.new_date_time_exceptions import MinuteOutOfRange


class TestNewDateTime(unittest.TestCase):
    """ Test NewDateTime model."""

    def setUp(self):
        self.fake = Faker()
        self.valid_new_date_time = NewDateTime(
                                        randint(0, 100),
                                        randint(0, 100),
                                        randint(0, 100),
                                        randint(0, 100),
                                        randint(0, 59))

    def test_day_integer_validation(self):
        """It is NOT valid with the day being of a different type of integer
        when creating or changing the variable."""

        self.assertRaises(TypeError, NewDateTime, "12", 4, 1999, 3, 34)

        with self.assertRaises(TypeError):
            self.valid_new_date_time.day = self.fake.name()

    def test_day_getter(self):
        """It returns the correct day value."""

        self.valid_new_date_time.day = 12

        self.assertEqual(self.valid_new_date_time.day, 12)

    def test_month_integer_validation(self):
        """It is NOT valid with the month being of a different type of integer
        when creating or changing the variable."""

        self.assertRaises(TypeError, NewDateTime, 12, "4", 1999, 3, 34)

        with self.assertRaises(TypeError):
            self.valid_new_date_time.month = self.fake.name()

    def test_month_getter(self):
        """It returns the correct month value."""

        self.valid_new_date_time.month = 4

        self.assertEqual(self.valid_new_date_time.month, 4)

    def test_year_integer_validation(self):
        """It is NOT valid with the year being of a different type of integer
        when creating or changing the variable."""

        self.assertRaises(TypeError, NewDateTime, 12, 4, "1999", 3, 34)

        with self.assertRaises(TypeError):
            self.valid_new_date_time.year = self.fake.name()

    def test_year_getter(self):
        """It returns the correct year value."""

        self.valid_new_date_time.year = 1991

        self.assertEqual(self.valid_new_date_time.year, 1991)

    def test_hour_integer_validation(self):
        """It is NOT valid with the hour being of a different type of integer
        when creating or changing the variable."""

        self.assertRaises(TypeError, NewDateTime, 12, 4, 1999, "3", 34)

        with self.assertRaises(TypeError):
            self.valid_new_date_time.hour = self.fake.name()

    def test_hour_getter(self):
        """It returns the correct hour value."""

        self.valid_new_date_time.hour = 22

        self.assertEqual(self.valid_new_date_time.hour, 22)

    def test_minute_integer_validation(self):
        """It is NOT valid with the minute being of a different type of integer
        when creating or changing the variable."""

        self.assertRaises(TypeError, NewDateTime, 12, 4, 1999, 3, "34")

        with self.assertRaises(TypeError):
            self.valid_new_date_time.minute = "foo"

    def test_minute_getter(self):
        """It returns the correct minute value."""

        self.valid_new_date_time.minute = 44

        self.assertEqual(self.valid_new_date_time.minute, 44)

    def test_minute_range(self):
        """It is NOT valid with minute out of the range (00 to 59)."""

        self.assertRaises(
            MinuteOutOfRange,
            NewDateTime,
            12, 4, 1999, 3, randint(-10000, 0))

        self.assertRaises(
            MinuteOutOfRange,
            NewDateTime,
            12, 4, 1999, 3, randint(60, 10000))
