class Clock():
    def __init__(self, time):
        self.time = time

    def get_time(self):
        return self.time

    def convert_to_24hour(self, time12hr):
        if self.time[-2:-1] == 'a':
            hour = int(time12hr[0:-2])
        else:
            hour = int(time12hr[0:-2]) + 12
        if hour < 10:
            time_str = "0" + str(hour) + ":00"
        else:
            time_str = str(hour) + ":00"
        return time_str

    def desc(self):
        return "Time: " + self.convert_to_24hour(self.time)

    def __str__(self):
        return self.desc()


class AlarmClock(Clock):
    def __init__(self, time, alarm):
        Clock.__init__(self, time)
        self.alarm = alarm

    def get_alarm(self):
        return self.alarm

    def desc(self):
        return Clock.desc(self) + " (Alarm: " + self.convert_to_24hour(self.alarm) + ")"


c1 = Clock("9am")
c2 = Clock("11am")
a1 = AlarmClock("1pm", "5pm")
a2 = AlarmClock("1pm", "7pm")
clocks = [c1, c2, a1, a2]

for clock in clocks:
    print clock