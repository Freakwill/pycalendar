#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import calendar
from datetime import date

today = date.today()

class MyCalendar(calendar.Calendar):

    def __init__(self, firstweekday=6):
        super(MyCalendar, self).__init__(firstweekday)

    def monthdayscalendar(self, year=today.year, month=today.month):
        days = super(MyCalendar, self).monthdayscalendar(year, month)
        if days[0][0] == 0:
            if today.month >= 2:
                last = super(MyCalendar, self).monthdayscalendar(year=today.year, month=today.month-1)
            else:
                last = super(MyCalendar, self).monthdayscalendar(year=today.year-1, month=12)
            days[0] = [a+b for a, b in zip(last[-1], days[0])]
        if days[-1][-1] == 0:
            # if today.month <= 11:
            #     next_ = super(MyCalendar, self).monthdayscalendar(year=today.year, month=today.month+1)
            # else:
            #     next_ = super(MyCalendar, self).monthdayscalendar(year=today.year+1, month=1)
            # days[-1] = [a + b for a, b in zip(next_[0], days[-1])]
            l = 1
            for k, day in enumerate(days[-1]):
                if day == 0:
                    days[-1][k] = l
                    l += 1
        return days


class MyHTMLCalendar(MyCalendar, calendar.HTMLCalendar):
    cssclasses = ['mo', 'tu', 'we', 'th', 'fr', 'sa', 'su']

    def __init__(self, firstweekday=6):
        super(MyCalendar, self).__init__(firstweekday)

    def formatmonth(self, theyear=today.year, themonth=today.month):
        formatdays = super(MyHTMLCalendar, self).formatmonth(theyear, themonth)
        days = super(MyHTMLCalendar, self).monthdayscalendar(year=today.year, month=today.month)
        if days[0][0] == 0:
            if today.month >= 2:
                last = super(MyHTMLCalendar, self).monthdayscalendar(year=today.year, month=today.month-1)
            else:
                last = super(MyHTMLCalendar, self).monthdayscalendar(year=today.year-1, month=12)
            days[0] = [a+b for a, b in zip(last[-1], days[0])]
        if days[-1][-1] == 0:
            # if today.month <= 11:
            #     next_ = super(MyCalendar, self).monthdayscalendar(year=today.year, month=today.month+1)
            # else:
            #     next_ = super(MyCalendar, self).monthdayscalendar(year=today.year+1, month=1)
            # days[-1] = [a + b for a, b in zip(next_[0], days[-1])]
            l = 1
            for k, day in enumerate(days[-1]):
                if day == 0:
                    days[-1][k] = l
                    l += 1
        return formatdays

    def __str__(self):
        return ';'.join((str(today), c.formatmonth(theyear=today.year, themonth=today.month)))


c = MyHTMLCalendar()
print(c)