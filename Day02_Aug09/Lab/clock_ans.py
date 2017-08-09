class Clock(object):
    def __init__(self, hour, minutes):
        self.minutes = minutes
        self.hour = hour

    @classmethod
    def at(cls, hour, minutes=0):
        return cls(hour, minutes)

    def __str__(self):
        if self.hour in range(0, 10):
            if self.minutes in range(0, 10):
                return "0"+str(self.hour)+":""0"+str(self.minutes)
            else:
                return "0"+str(self.hour)+":"+str(self.minutes)
        else:
            if self.minutes in range(0, 10):
                return str(self.hour)+":""0"+str(self.minutes)
            else:
                return str(self.hour)+":"+str(self.minutes)


    def __add__(self, minutes):
        total_min = minutes + self.minutes
        if total_min <= 59:
            return Clock(abs(self.hour), total_min)
        else:
            addHours = total_min / 60
            new_hour = self.hour + addHours
            hour_times = new_hour / 24
            if hour_times == 1:
                return Clock(abs(new_hour - 24), (total_min % 60))
            else:
                new_hour = new_hour - (hour_times * 24)
                return Clock(abs(new_hour), (total_min % 60))

    def __sub__(self, minutes):
        total_min = self.minutes - minutes
        if total_min > 0:
            return Clock(abs(self.hour), total_min)
        else:
            subHours = total_min / 60
            new_hour = self.hour + subHours
            hour_times = abs(new_hour / 24)
            if hour_times == 1:
                new_hour = hour_times - 24
                return Clock(abs(new_hour), (total_min % 60))
            else:
                new_hour = new_hour - (hour_times * 24)
                return Clock(abs(new_hour), (total_min % 60))

    def __eq__(self, other):
        return True if (self.hour == other.hour) \
        and (self.minutes == other.minutes) else False

    def __ne__(self, other):
        return False if (self.hour == other.hour) \
        and (self.minutes == other.minutes) else True
