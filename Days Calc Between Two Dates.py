days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
days_in_month_leap = [31,29,31,30,31,30,31,31,30,31,30,31]

#
year2 = 2015
month2 = 1
day2 = 2


year1 = 2013
month1= 12
day1= 28


def years_in_days(year1, year2):
    count_of_days = 0
    for x in range(year1, year2-1):
        if is_leap_year(x):
            count_of_days += 366
        else:
            count_of_days += 365
    return count_of_days


def days_in_months_with_leap(year):
    if is_leap_year(year):
        return days_in_month_leap
    else:
        return days_in_month
def days_between(year, month1, day1, month2, day2):
    months = days_in_months_with_leap(year)
    return day2 + sum(months[month1 - 1:month2 - 1]) - day1

def days_left_in_year(year, month, day):
    months = days_in_months_with_leap(year)
    return months[month-1]-day + sum(months[month:])

def days_in_year_to_date(year, month, day):
    months = days_in_months_with_leap(year)
    return sum(months[:month-1]) + day

def is_leap_year(x):
    return (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0)


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    if year1 > year2:
        return "Input Error: Year1 cannot exceed Year2."
    elif (year2 == year1):
        return days_between(year1, month1, day1, month2, day2)
    else:
        start_days = days_left_in_year(year1, month1, day1)
        end_days = days_in_year_to_date(year2, month2, day2)
        days_in_years_between = years_in_days(year1, year2)
        return start_days+end_days+days_in_years_between









def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")

test()







