import time

from project import Project


class Clock:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.exit = False

    def tick(self, display=None, project: Project = None, string_time=None, use_loop=True):  # type: ignore
        while not self.exit:
            self.seconds += 1
            if self.seconds == 60:
                self.seconds = 0
                self.minutes += 1
                if self.minutes == 60:
                    self.minutes = 0
                    self.hours += 1
            if project is not None:
                prev_time = create_clock_from_str(project.project_time)
                project.project_time = add_time(prev_time, Clock(0, 0, 1)).get_time()
                project.get_project_time().setText(project.project_time[:5])
            if string_time is not None:
                string_time.project_idol_time = self.get_time()
            if display is not None:
                display.setText(self.get_time())
            if not use_loop:
                break
            time.sleep(1)

    def get_time(self):
        return f'{"{:02d}".format(self.hours)}:{"{:02d}".format(self.minutes)}:{"{:02d}".format(self.seconds)}'

    def get_total_seconds(self):
        return self.hours * 60 * 60 + self.minutes * 60 + self.seconds

    def remove_listener(self):
        self.exit = True

    def reset(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.exit = False


def subtract_time(time_1: Clock, time_2: Clock):
    time_1_seconds = time_1.get_total_seconds()
    time_2_seconds = time_2.get_total_seconds()
    seconds_difference = abs(time_1_seconds - time_2_seconds)
    return seconds_to_clock(seconds_difference)


def seconds_to_clock(seconds: int):
    hours = seconds / 3600
    minutes = (hours % 1) * 60
    seconds = round((minutes % 1) * 60)
    if seconds >= 60:
        seconds = 0
        minutes += 1
        if minutes >= 60:
            minutes = 0
            hours += 1
    return Clock(hours=int(hours), minutes=int(minutes), seconds=seconds)


def add_time(time_1: Clock, time_2: Clock):
    time_1_seconds = time_1.get_total_seconds()
    time_2_seconds = time_2.get_total_seconds()
    seconds_difference = time_1_seconds + time_2_seconds
    return seconds_to_clock(seconds_difference)


def create_clock_from_str(time_str: str):
    separates = time_str.split(':')
    hours = int(separates[0])
    minutes = int(separates[1]) % 60
    seconds = int(separates[2]) % 60
    return Clock(hours=hours, minutes=minutes, seconds=seconds)
