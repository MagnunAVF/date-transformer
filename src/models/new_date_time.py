from src.exceptions.new_date_time_exceptions import *

class NewDateTime:
    def __init__(self, day, month, year, hour, minute):
        self.DAYS_OF_A_MONTH = {
            1: {'name': 'January', 'days': 31},
            2: {'name': 'February', 'days': 28},
            3: {'name': 'March', 'days': 31},
            4: {'name': 'April', 'days': 30},
            5: {'name': 'May', 'days': 31},
            6: {'name': 'July', 'days': 30},
            7: {'name': 'June', 'days': 31},
            8: {'name': 'August', 'days': 31},
            9: {'name': 'September', 'days': 30},
            10: {'name': 'October', 'days': 31},
            11: {'name': 'November', 'days': 30},
            12: {'name': 'Dezember', 'days': 31},
        }

        self.day = day
        self.month = month
        self.year = year
        self.hour = hour
        self.minute = minute

        self._validate_day_range(day, month)

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        message = "Day can only be an instance of integer."
        self._validate_integer(value, message)
        self._day = value

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        if value < 1 or value > 12:
            raise MonthOutOfRange("Month must be in the range of 1 to 12")

        message = "Month can only be an instance of integer."
        self._validate_integer(value, message)
        self._month = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if value < 0:
            raise NegativeYear("Year can NOT be negative")

        message = "Year can only be an instance of integer."
        self._validate_integer(value, message)
        self._year = value

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, value):
        if value < 0 or value > 23:
            raise HourOutOfRange("Hour must be in the range of 0 to 23")

        message = "Hour can only be an instance of integer."
        self._validate_integer(value, message)
        self._hour = value

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, value):
        if value < 0 or value > 59:
            raise MinuteOutOfRange("Minute must be in the range of 0 to 59")

        message = "Minute can only be an instance of integer."
        self._validate_integer(value, message)

        self._minute = value

    def _validate_integer(self, value, message):
        if not isinstance(value, int):
            raise TypeError(message)

    def _validate_day_range(self, day, month):
        reference_month = int(month)

        if day < 1 or day > self.DAYS_OF_A_MONTH[reference_month]['days']:
            raise DayOutOfRange("Day must respect the month days range")
