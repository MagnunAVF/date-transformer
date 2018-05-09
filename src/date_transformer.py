from re import split

from src.models.new_date_time import NewDateTime
from src.exceptions.new_date_time_exceptions import *
from src.exceptions.date_transformer_exceptions import *

class DateTransformer:
    def change_date(self, date, op, value):
        if not isinstance(value, int):
            raise TypeError("Invalid minutes value. Minutes must be integer.")

        minutes_value = abs(value)

        if op == "+":
            return True
        elif op == "-":
            return True
        else:
            raise InvalidOperatorException

    def _date_extractor_from_str(self, date_str):
        try:
            str_array = split('\s+', date_str)

            date_str = str_array[0]
            time_str = str_array[1]

            date_array = split('/', date_str)
            time_array = split(':', time_str)

            day = int(date_array[0])
            month = int(date_array[1])
            year = int(date_array[2])
            hour = int(time_array[0])
            minute = int(time_array[1])
        except (TypeError, ValueError) as e:
            raise e("Invalid DateTime Input.Correct format: 'dd/MM/yyyy HH:mm'")

        try:
            result_datetime = NewDateTime(day, month, year, hour, minute)
        except (MinuteOutOfRange, HourOutOfRange, NegativeYear, MonthOutOfRange,
                DayOutOfRange) as e:
            raise e

        return result_datetime

    def _extract_hours(self, minutes):
        if minutes > 59:
            remainder = minutes % 60
            result = (minutes - remainder)/60
            return (int(result), remainder)
        return (0, minutes)

    def _extract_days(self, hours):
        if hours > 23:
            remainder = hours % 24
            result = (hours - remainder)/24
            return (int(result), remainder)
        return (0, hours)
