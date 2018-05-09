import unittest

from faker import Faker

from src.date_transformer import DateTransformer
from src.models.new_date_time import NewDateTime
from src.exceptions.new_date_time_exceptions import MinuteOutOfRange
from src.exceptions.new_date_time_exceptions import HourOutOfRange
from src.exceptions.new_date_time_exceptions import NegativeYear
from src.exceptions.new_date_time_exceptions import MonthOutOfRange
from src.exceptions.new_date_time_exceptions import DayOutOfRange
from src.exceptions.date_transformer_exceptions import InvalidOperatorException


class TestDateTransformer(unittest.TestCase):
    """ Test TestDateTransformer Entity."""

    def setUp(self):
        self.date_transformer = DateTransformer()
        self.fake = Faker()

    def test_change_date(self):
        """It should transform the dates respecting the rules of the domain."""

        result = self.date_transformer.change_date(
                                                "30/05/1991 13:17", '+', 10)

        self.assertEqual(result, "30/05/1991 13:27")

    def test_change_date_with_invalid_value_arg(self):
        """It should raise an Exception when input minutes value is invalid."""

        with self.assertRaises(TypeError):
            self.date_transformer.change_date("01/03/2010 23:00", '-', "teste")

    def test_change_date_with_invalid_op_arg(self):
        """It should raise an Exception when input op is invalid"""

        with self.assertRaises(InvalidOperatorException):
            self.date_transformer.change_date("01/03/2010 23:00", '?', 4000)

    def test_add_to_date_from_minutes_to_hours_transition(self):
        """It should sum input minutes to datetime and correctly execute the
        transition from minutes to hours"""

        datetime = NewDateTime(1, 1, 2001, 3, 34)

        result_datetime = self.date_transformer._add_to_datetime(datetime, 10)
        self.assertEqual(result_datetime.minute, 44)
        self.assertEqual(result_datetime.hour, 3)

        _3_hours = 180
        result_datetime = self.date_transformer._add_to_datetime(
                                                    datetime, _3_hours + 21)
        self.assertEqual(result_datetime.minute, 55)
        self.assertEqual(result_datetime.hour, 6)

    def test_add_to_date_from_hours_to_days_transition(self):
        """It should sum input minutes to datetime and correctly execute the
        transition from hours to days"""

        datetime = NewDateTime(4, 2, 2012, 5, 10)

        _3_hours = 180
        result_datetime = self.date_transformer._add_to_datetime(
                                                            datetime, _3_hours)
        self.assertEqual(result_datetime.hour, 8)
        self.assertEqual(result_datetime.day, 4)

        _2_days = 2880
        result_datetime = self.date_transformer._add_to_datetime(
                                                            datetime, _2_days)
        self.assertEqual(result_datetime.hour, 5)
        self.assertEqual(result_datetime.day, 6)

    def test_add_to_date_from_days_to_years_transition(self):
        """It should sum input minutes to datetime and correctly execute the
        transition from days to years"""

        datetime = NewDateTime(10, 5, 2101, 12, 13)

        _3_days = 4320
        result_datetime = self.date_transformer._add_to_datetime(
                                                            datetime, _3_days)
        self.assertEqual(result_datetime.day, 13)
        self.assertEqual(result_datetime.year, 2101)

        _5_years = 2628000
        result_datetime = self.date_transformer._add_to_datetime(
                                                            datetime, _5_years)
        self.assertEqual(result_datetime.day, 10)
        self.assertEqual(result_datetime.year, 2106)

    def test_add_to_date_from_days_to_month_transition(self):
        """It should sum input minutes to datetime and correctly execute the
        transition from days to month"""

        datetime_31_days_month = NewDateTime(7, 5, 2101, 12, 13)

        _3_days = 4320
        result_datetime = self.date_transformer._add_to_datetime(
                                            datetime_31_days_month, _3_days)
        self.assertEqual(result_datetime.day, 10)
        self.assertEqual(result_datetime.month, 5)

        _37_days = 53280
        result_datetime = self.date_transformer._add_to_datetime(
                                            datetime_31_days_month, _37_days)
        self.assertEqual(result_datetime.day, 13)
        self.assertEqual(result_datetime.month, 6)

        datetime_30_days_month = NewDateTime(27, 4, 1970, 12, 13)

        _2_days = 2880
        result_datetime = self.date_transformer._add_to_datetime(
                                            datetime_30_days_month, _2_days)
        self.assertEqual(result_datetime.day, 29)
        self.assertEqual(result_datetime.month, 4)

        _6_days = 8640
        result_datetime = self.date_transformer._add_to_datetime(
                                            datetime_30_days_month, _6_days)
        self.assertEqual(result_datetime.day, 3)
        self.assertEqual(result_datetime.month, 5)

        datetime_28_days_month = NewDateTime(25, 2, 1989, 12, 13)

        result_datetime = self.date_transformer._add_to_datetime(
                                            datetime_28_days_month, _2_days)
        self.assertEqual(result_datetime.day, 27)
        self.assertEqual(result_datetime.month, 2)

        result_datetime = self.date_transformer._add_to_datetime(
                                            datetime_28_days_month, _6_days)
        self.assertEqual(result_datetime.day, 3)
        self.assertEqual(result_datetime.month, 3)

    def test_add_to_date_from_days_to_month_sequential_transition(self):
        """It should sum input minutes to datetime and correctly execute the
        transition from days to month (with more than one month transaction)"""

        datetime_31_days_month = NewDateTime(7, 5, 2101, 12, 13)

        _62_days = 89280
        result_datetime = self.date_transformer._add_to_datetime(
                                            datetime_31_days_month, _62_days)
        self.assertEqual(result_datetime.day, 8)
        self.assertEqual(result_datetime.month, 7)

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

    def test_extract_years(self):
        """It should return the years and the remainder days."""

        years_and_remainder_days = 740
        only_days = 200
        exactly_one_year = 365

        self.assertTupleEqual(self.date_transformer._extract_years(
                                only_days), (0, 200))

        self.assertTupleEqual(self.date_transformer._extract_years(
                                years_and_remainder_days), (2, 10))

        self.assertTupleEqual(self.date_transformer._extract_years(
                                exactly_one_year), (1, 0))
