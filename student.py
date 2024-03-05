from datetime import date, timedelta

class Student:
    """A Student class as base for method testing"""

    def __init__(self, first_name, last_name):
        self._first_name = first_name # read only field with the underscore
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    @property # the property method is for read-only
    def full_name(self):
        return f"{self._first_name} {self._last_name}"
    
    
    @property # the property method is for read-only
    def email(self):
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"

    
    # apply_extension
    def apply_extension(self, days):
        self.end_date = self.end_date + timedelta(days=days)

    
    def alert_santa(self):
        self.naughty_list = True
