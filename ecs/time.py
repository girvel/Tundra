class Time:
    def __init__(self, years=0, months=0, days=0, hours=0, minutes=0, seconds=0):
        self.years = years
        self.months = months
        self.days = days
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __int__(self):
        result = 0
        for p in (
                (self.years, 12),
                (self.months, 30),
                (self.days, 24),
                (self.hours, 60),
                (self.minutes, 60),
                (self.seconds, 1),
        ):
            result += p[0]
            result *= p[1]

        return result

    def __truediv__(self, other):
        return int(self) / int(other)

    def __floordiv__(self, other):
        return int(self) // int(other)
