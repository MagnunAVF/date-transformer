from re import split

from src.models.new_date_time import NewDateTime
from src.exceptions.new_date_time_exceptions import *
from src.exceptions.date_transformer_exceptions import *

class DateTransformer:
    def change_date(self, date, op, value):
        if not isinstance(value, int):
            raise TypeError("Invalid minutes value. Minutes must be integer.")

        minutes_value = abs(value)

        try:
            datetime = self._date_extractor_from_str(date)
        except(Exception) as e:
            raise e

        if op == "+":
            result_datetime = self._add_to_datetime(datetime, minutes_value)
        elif op == "-":
            raise NotImplementedError
        else:
            raise InvalidOperatorException

        return str(result_datetime)

    def _add_to_datetime(self, datetime, minutes_value):
        tuple_from_minutes = self._extract_hours(minutes_value + datetime.minute)
        minute = tuple_from_minutes[1]
        hours_to_sum = tuple_from_minutes[0]

        tuple_from_hours = self._extract_days(hours_to_sum + datetime.hour)
        hour = tuple_from_hours[1]
        days_to_sum = tuple_from_hours[0]

        if(days_to_sum == 0):
            new_datetime = NewDateTime( datetime.day,
                                        datetime.month,
                                        datetime.year,
                                        hour,
                                        minute)
            return new_datetime

        tuple_from_days = self._extract_years(days_to_sum)
        year_to_sum = tuple_from_days[0]
        days_to_sum = tuple_from_days[1]

        if(days_to_sum == 0):
            new_datetime = NewDateTime( datetime.day,
                                        datetime.month,
                                        datetime.year+year_to_sum,
                                        hour,
                                        minute)
            return new_datetime

        initial_day = datetime.day
        current_day = datetime.day
        current_month = datetime.month
        month_change = False

        while days_to_sum > datetime.DAYS_OF_A_MONTH[current_month]['days']:
            month_change = True
            limit_day = datetime.DAYS_OF_A_MONTH[current_month]['days']
            missing_days = limit_day - current_day
            days_to_sum = days_to_sum - missing_days
            current_month += 1
            current_day = 0

        month = current_month
        year = datetime.year + year_to_sum

        if month_change:
            day = days_to_sum
        else:
            day = days_to_sum + initial_day

        limit_day = datetime.DAYS_OF_A_MONTH[month]['days']
        if day > limit_day:
            day = limit_day - current_day
            month += 1

        new_datetime = NewDateTime(day, month, year, hour, minute)

        return new_datetime

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

    def _extract_years(self, days):
        if days > 364:
            remainder = days % 365
            result = (days - remainder)/365
            return (int(result), remainder)
        return (0, days)
