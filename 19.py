"""
Project Euler
Problem 19

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


Solution
Initialize a counter.
Start counting from day 2 on a 7 day cycle.
Keep track of day date, month and year.
Increment counter when detecting a Sunday falling on day 1.



NOTES
1900 is not a leap year
2000 is a leap year

No need to check for century divisible by 400 since it doesn't occur.

author:  Adam Shechter
"""
MONTH_A = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
MONTH_B = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def main():
    print(counting_sundays({"day": 1, "mon": 1, "yr": 1901}, 3, 2000))


def counting_sundays(start_date, start_day, end_year):
    # day of the week
    day_runner = start_day
    # counter
    sun_count = 0
    while start_date['yr'] <= end_year:
        print("Day {}     Date {}   Month {}    Year {}".format(day_runner, start_date['day'], start_date['mon'], start_date['yr']))
        # Run check
        if day_runner == 1 and start_date['day'] == 1:
            sun_count += 1
            print("******* FOUND ********")
        # increment date
        day_runner = day_runner + 1 if day_runner < 7 else 1
        # leap year check
        leap_year = True if start_date['yr'] % 4 == 0 else False
        if leap_year:
            if start_date['yr'] % 100 == 0 and start_date['yr'] % 400 != 0:
                leap_year = False
        if leap_year:
            if start_date['day'] < MONTH_B[start_date['mon']-1]:
                start_date['day'] += 1
            else:
                if start_date['mon'] < 12:
                    start_date['mon'] += 1
                    start_date['day'] = 1
                else:
                    start_date['yr'] += 1
                    start_date['day'] = 1
                    start_date['mon'] = 1
        else:
            if start_date['day'] < MONTH_A[start_date['mon']-1]:
                start_date['day'] += 1
            else:
                if start_date['mon'] < 12:
                    start_date['mon'] += 1
                    start_date['day'] = 1
                else:
                    start_date['yr'] += 1
                    start_date['day'] = 1
                    start_date['mon'] = 1
    return sun_count

if __name__ == '__main__':
    main()
