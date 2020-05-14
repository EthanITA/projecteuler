""" You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)? """

import datetime
import calendar

from util import count_matching


def get_first_month_days(year):
    days = []
    for month in range(12):
        days.append(calendar.weekday(year, month+1, 1))
    return days


def first_month_sundays(start_date, end_date):
    sundays = 0
    for year in range(start_date, end_date+1):
        days = get_first_month_days(year)
        sundays += count_matching(calendar.SUNDAY, days)
    return sundays


if __name__ == "__main__":

    print(first_month_sundays(1901, 2000))
