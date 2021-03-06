import unittest

from faker import Faker
from random import randint
from random import choice

from src.models.new_date_time import NewDateTime
from src.exceptions.new_date_time_exceptions import MinuteOutOfRange
from src.exceptions.new_date_time_exceptions import HourOutOfRange
from src.exceptions.new_date_time_exceptions import NegativeYear
from src.exceptions.new_date_time_exceptions import MonthOutOfRange
from src.exceptions.new_date_time_exceptions import DayOutOfRange


class TestNewDateTime(unittest.TestCase):
    """ Test NewDateTime model."""

    def setUp(self):
        self.fake = Faker()
        self.valid_new_date_time = NewDateTime(
                                        randint(1, 25),
                                        randint(1, 12),
                                        randint(0, 10000),
                                        randint(0, 23),
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

    def test_day_range(self):
        """It is NOT valid with day out of the range.
        Ranges by month:
        - January, March, May, July, August, October, December => 01 to 31
        - April, June, September, November => 01 to 30
        - February => 01 to 28"""

        self.assertRaises(
            DayOutOfRange,
            NewDateTime,
            randint(-10000, 0), 1, 1999, 13, 33)

        months_with_31 = [1, 3, 5, 7, 8, 10, 12]
        self.assertRaises(
            DayOutOfRange,
            NewDateTime,
            randint(32, 1000), choice(months_with_31), 1999, 13, 33)

        months_with_30 = [4, 6, 9, 11]
        self.assertRaises(
            DayOutOfRange,
            NewDateTime,
            randint(31, 1000), choice(months_with_30), 1999, 13, 33)

        self.assertRaises(
            DayOutOfRange,
            NewDateTime,
            randint(29, 1000), 2, 1999, 13, 33)

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

    def test_month_range(self):
        """It is NOT valid with month out of the range (01 to 12)."""

        self.assertRaises(
            MonthOutOfRange,
            NewDateTime,
            12, randint(-10000, 0), 1999, 13, 33)

        self.assertRaises(
            MonthOutOfRange,
            NewDateTime,
            12, randint(13, 10000), 1999, 13, 33)

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

    def test_negative_year(self):
        """It is NOT valid with a negative year."""

        self.assertRaises(
            NegativeYear,
            NewDateTime,
            12, 4, randint(-10000, 0), 13, 33)

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

    def test_hour_range(self):
        """It is NOT valid with hour out of the range (00 to 23)."""

        self.assertRaises(
            HourOutOfRange,
            NewDateTime,
            12, 4, 1999, randint(-10000, 0), 33)

        self.assertRaises(
            HourOutOfRange,
            NewDateTime,
            12, 4, 1999, randint(24, 10000), 33)

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

    def test__str__(self):
        date_time = NewDateTime(30, 5, 1991, 13, 27)

        str_result = str(date_time)

        self.assertEqual(str_result, "30/05/1991 13:27")
