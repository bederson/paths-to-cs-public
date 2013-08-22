class Clock():
    def __init__(self, time):
        self.time = time

    def get_time(self):
        return self.time

    def __str__(self):
        return "Time: " + self.time


class AlarmClock(Clock):
    def __init__(self, time, alarm):
        self.time = time
        self.alarm = alarm

    def get_alarm(self):
        return self.alarm

    def __str__(self):
        return "Time: " + self.time + " (Alarm: " + self.alarm + ")"


c1 = Clock("9am")
c2 = Clock("11am")
a1 = AlarmClock("1pm", "5pm")
a2 = AlarmClock("1pm", "7pm")
clocks = [c1, c2, a1, a2]

for clock in clocks:
    print clock