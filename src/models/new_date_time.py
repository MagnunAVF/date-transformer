from src.exceptions.new_date_time_exceptions import *

class NewDateTime:
    def __init__(self, day, month, year, hour, minute):
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour
        self.minute = minute

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
        message = "Month can only be an instance of integer."
        self._validate_integer(value, message)
        self._month = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        message = "Year can only be an instance of integer."
        self._validate_integer(value, message)
        self._year = value

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, value):
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
