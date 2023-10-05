days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
days_in_month_2 = [31,29,31,30,31,30,31,31,30,31,30,31]

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
        if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
            count_of_days += 366
        else:
            count_of_days += 365
    return count_of_days

def both_NonLeapYearcalc(year1, month1, day1, year2, month2, day2):
    total_of_year1 = (days_in_month[month1-1]-day1)+ sum(days_in_month[month1:])
    total_of_year2 = sum(days_in_month[:month2-1])+day2
    total_days = (total_of_year2 + total_of_year1)+ years_in_days(year1, year2)
    return total_days

def both_leapYearCalc(year1, month1, day1, year2, month2, day2):
    total_of_year1 = (days_in_month_2[month1-1]-day1)+ sum(days_in_month_2[month1:])
    total_of_year2 = sum(days_in_month_2[:month2-1])+day2
    total_days = (total_of_year2 + total_of_year1)+ years_in_days(year1, year2)
    return total_days

def only_Year1LeapYearcalc(year1, month1, day1, year2, month2, day2):
    total_of_year1 = (days_in_month_2[month1-1]-day1)+ sum(days_in_month_2[month1:])
    total_of_year2 = sum(days_in_month[:month2-1])+day2
    total_days = (total_of_year2 + total_of_year1)+ years_in_days(year1, year2)
    return total_days

def only_Year2LeapYearcalc(year1, month1, day1, year2, month2, day2):
    total_of_year1 = (days_in_month[month1-1]-day1)+ sum(days_in_month[month1:])
    total_of_year2 = sum(days_in_month_2[:month2-1])+day2
    total_days = (total_of_year2 + total_of_year1)+ years_in_days(year1, year2)
    return total_days



def sameYear_nonLeapYear(year1,month1,day1,year2,month2,day2):
    total_days = day2 + sum(days_in_month[month1-1:month2-1]) - day1
    return total_days

def sameYear_LeapYear(year1,month1,day1,year2,month2,day2):
    total_days = day2 + sum(days_in_month_2[month1-1:month2-1]) - day1
    return total_days

def is_YearLeap(x):
    return (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0)


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    if year1 > year2:
        return "Input Error: Year1 cannot exceed Year2."
    elif (year2 == year1) and (year2 % 4 !=0):
        return sameYear_nonLeapYear(year1, month1, day1, year2, month2, day2)
    elif (year2 == year1) and is_YearLeap(year2):
        return sameYear_LeapYear(year1, month1, day1, year2, month2, day2)
    elif is_YearLeap(year1):
        if is_YearLeap(year2):
            return both_leapYearCalc(year1, month1, day1, year2, month2, day2)
        else:
            return only_Year1LeapYearcalc(year1, month1, day1, year2, month2, day2)
    elif is_YearLeap(year2):
        return only_Year2LeapYearcalc(year1, month1, day1, year2, month2, day2)
    else:
        return both_NonLeapYearcalc(year1, month1, day1, year2, month2, day2)






print(daysBetweenDates(2012,1,1,2012,2,28))
print(daysBetweenDates(2012,1,1,2012,3,1))
print(daysBetweenDates(2011,6,30,2012,6,30))
print(daysBetweenDates(2011,1,1,2012,8,8))
print(daysBetweenDates(1900,1,1,1999,12,31))


# def test():
#     test_cases = [((2012,1,1,2012,2,28), 58),
#                   ((2012,1,1,2012,3,1), 60),
#                   ((2011,6,30,2012,6,30), 366),
#                   ((2011,1,1,2012,8,8), 585 ),
#                   ((1900,1,1,1999,12,31), 36523)]
#     for (args, answer) in test_cases:
#         result = daysBetweenDates(*args)
#         if result != answer:
#             print("Test with data:", args, "failed")
#         else:
#             print("Test case passed!")
#
# test()



