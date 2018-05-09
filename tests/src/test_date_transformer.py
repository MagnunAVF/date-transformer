import unittest

from faker import Faker

from src.date_transformer import DateTransformer
from src.models.new_date_time import NewDateTime
from src.exceptions.new_date_time_exceptions import MinuteOutOfRange
from src.exceptions.new_date_time_exceptions import HourOutOfRange
from src.exceptions.new_date_time_exceptions import NegativeYear
from src.exceptions.new_date_time_exceptions import MonthOutOfRange
from src.exceptions.new_date_time_exceptions import DayOutOfRange


class TestDateTransformer(unittest.TestCase):
    """ Test TestDateTransformer Entity."""

    def setUp(self):
        self.date_transformer = DateTransformer()
        self.fake = Faker()

    def test_change_date(self):
        """It should transform the dates respecting the rules of the domain."""

        result = self.date_transformer.change_date(
                                                "01/03/2010 23:00", '+', 4000)

        self.assertEqual(result, "01/03/2010 23:00")

    def test_date_extractor_from_str_with_invalid_str(self):
        """It should raise an exception when input string is invalid."""

        invalid_datetime_str = self.fake.job

        with self.assertRaises(Exception):
            self.date_transformer._date_extractor_from_str(
                                                        invalid_datetime_str)

    def test_date_extractor_from_str_with_valid_args(self):
        """It should create an NewDateTime object when input string is
        valid."""

        valid_datetime_str = "01/03/2010 23:00"

        valid_datetime_obj = self.date_transformer._date_extractor_from_str(
                                valid_datetime_str)
        self.assertIsInstance(valid_datetime_obj, NewDateTime)

    def test_date_extractor_from_str_with_invalid_args(self):
        """It should raise an specific exception when input string is
        invalid."""

        invalid_datetime_day_str = "33/03/2010 23:00"
        invalid_datetime_month_str = "33/15/2010 23:00"
        invalid_datetime_year_str = "33/03/-1 23:00"
        invalid_datetime_hour_str = "33/03/2010 25:00"
        invalid_datetime_min_str = "33/03/2010 23:66"

        with self.assertRaises(DayOutOfRange):
            self.date_transformer._date_extractor_from_str(
                                            invalid_datetime_day_str)

        with self.assertRaises(MonthOutOfRange):
            self.date_transformer._date_extractor_from_str(
                                            invalid_datetime_month_str)

        with self.assertRaises(NegativeYear):
            self.date_transformer._date_extractor_from_str(
                                            invalid_datetime_year_str)

        with self.assertRaises(HourOutOfRange):
            self.date_transformer._date_extractor_from_str(
                                            invalid_datetime_hour_str)

        with self.assertRaises(MinuteOutOfRange):
            self.date_transformer._date_extractor_from_str(
                                            invalid_datetime_min_str)

    def test_extract_hours(self):
        """It should return the hours and the remainder minutes."""

        hours_and_remainder_minutes = 253
        only_minutes = 45
        exactly_one_hour = 60

        self.assertTupleEqual(self.date_transformer._extract_hours(
                                only_minutes), (0, 45))

        self.assertTupleEqual(self.date_transformer._extract_hours(
                                hours_and_remainder_minutes), (4, 13))

        self.assertTupleEqual(self.date_transformer._extract_hours(
                                exactly_one_hour), (1, 0))

    def test_extract_days(self):
        """It should return the days and the remainder hours."""

        days_and_remainder_hours = 27
        only_hours = 23
        exactly_one_day = 24

        self.assertTupleEqual(self.date_transformer._extract_days(
                                only_hours), (0, 23))

        self.assertTupleEqual(self.date_transformer._extract_days(
                                days_and_remainder_hours), (1, 3))

        self.assertTupleEqual(self.date_transformer._extract_days(
                                exactly_one_day), (1, 0))
