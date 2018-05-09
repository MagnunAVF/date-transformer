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
        if not isinstance(value, int):
            raise TypeError("Day can only be an instance of integer.")
        self._day = value

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        if not isinstance(value, int):
            raise TypeError("Month can only be an instance of integer.")
        self._month = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise TypeError("Year can only be an instance of integer.")
        self._year = value

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, value):
        if not isinstance(value, int):
            raise TypeError("Hour can only be an instance of integer.")
        self._hour = value

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, value):
        if not isinstance(value, int):
            raise TypeError("Minute can only be an instance of integer.")
        self._minute = value
