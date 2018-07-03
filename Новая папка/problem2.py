from collections import defaultdict


def read_line():
    line = input().split()
    command = line[0]
    if command == "APPOINT":
        day, time, duration, members_num, *members = line[1:]
        day = int(day)
        duration = int(duration)
        members_num = int(members_num)
        time = time2num(time)
        return command, day, time, duration, members_num, members

    if command == "PRINT":
        day, member = line[1:]
        day = int(day)
        return command, day, None, None, None, [member]


def time2num(time, sep=":"):
    hour, minute = [int(i) for i in str(time).split(sep)]
    return hour * 60 + minute


def num2time(num):
    time = num % (24 * 60)
    hours = str(time // 60)
    minutes = str(time % 60)

    if int(minutes) < 10:
        minutes = "0" + minutes

    if int(hours) < 10:
        hours = "0" + hours

    return str(hours) + ":" + str(minutes)


class Appointment:
    def __init__(self, day, time, dur, members):
        self.begin = day * 24 * 60 + time
        self.end = self.begin + dur
        self.members = members


class Schedule:
    def __init__(self,):
        self._schedule = defaultdict(list)

    def check(self, A):
        failed = False
        busy_members = []

        # for each member of appointment check if he/she is busy at this time
        for member in A.members:
            member_schedule = self._schedule[member]
            for appointment in member_schedule:
                if not ((A.begin < appointment.begin and A.end <= appointment.begin) or
                        (A.begin >= appointment.end and A.end > appointment.end)):
                    failed = True
                    busy_members.append(member)
                    break
        return failed, busy_members

    def add(self, A):
        failed, busy_members = self.check(A)

        if failed:
            print("FAIL")
            for member in busy_members:
                print(member, end=" ")
            print()
        else:
            for member in A.members:
                self._schedule[member].append(A)
            print("OK")

    def display(self, day, member):
        member_appointments = self._schedule[member]
        member_appointments.sort(key=lambda x: x.begin)
        for appointment in member_appointments:
            if day * 24 * 60 < appointment.begin < (day + 1) * 24 * 60:
                time = num2time(appointment.begin)
                dur = appointment.end - appointment.begin
                members = " ".join(appointment.members)
                print(time, dur, members)


def main():
    commands_num = int(input())
    schedule = Schedule()
    for i in range(commands_num):
        command, day, time, duration, members_num, members = read_line()

        if command == "APPOINT":
            A = Appointment(day, time, duration, members)
            schedule.add(A)
        if command == "PRINT":
            member = members[0]
            schedule.display(day, member)


if __name__ == "__main__":
    main()
