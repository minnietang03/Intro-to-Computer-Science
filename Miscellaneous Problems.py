# Given the variables s and t defined as:
s = 'udacity'
t = 'bodacious'
# write Python code that prints out udacious
# without using any quote characters in
# your code.


print(s[:3]+t[4:])


# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the first occurrence of 'hoo'
# in the value of text, or -1 if
# it does not occur at all.

text = "first hoo"

# ENTER CODE BELOW HERE

print(text.find('hoo'))

# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the second occurrence of 'zip'
# in text, or -1 if it does not occur
# at least twice.

# The Python code should be general enough
# to pass every possible case where 'zip'
# can occur in a string

# Here are two example test cases:
# text = 'all zip files are zipped'
# >>> 18
# text = 'all zip files are compressed'
# >>> -1

text = "all zip files are zipped"


# ENTER CODE BELOW HERE
def find_second_occurrence(word, text):
    first_occurrence = text.find(word)
    if first_occurrence == -1:
        return -1  # Word not found in the text
    second_occurrence = text.find(word, first_occurrence + 1)
    return second_occurrence


print(find_second_occurrence('zip', text))

# IMPORTANT BEFORE SUBMITTING:
# You should only have one print command in your function

########################################################

def weekends(x):
    return x=="Saturday" or x == 'Sunday'


print(weekends("Monday"))
print(weekends("Saturday"))
print(weekends("July"))
print(weekends("Sunday"))

########################################################
# Define a procedure, stamps, which takes as its input a positive integer in
# pence and returns the number of 5p, 2p and 1p stamps (p is pence) required
# to make up that value. The return value should be a tuple of three numbers
# (that is, your return statement should be followed by the number of 5p,
# the number of 2p, and the nuber of 1p stamps).
#
# Your answer should use as few total stamps as possible by first using as
# many 5p stamps as possible, then 2 pence stamps and finally 1p stamps as
# needed to make up the total.
#
# (No fair for USians to just say use a "Forever" stamp and be done with it!)
#

# def stamps():
#     # Your code here
#
#
# print stamps(8)
# #>>> (1, 1, 1)  # one 5p stamp, one 2p stamp and one 1p stamp
# print stamps(5)
# #>>> (1, 0, 0)  # one 5p stamp, no 2p stamps and no 1p stamps
# print stamps(29)
# #>>> (5, 2, 0)  # five 5p stamps, two 2p stamps and no 1p stamps
# print stamps(0)
# #>>> (0, 0, 0) # no 5p stamps, no 2p stamps and no 1p stamps




###############################################################

# The range of a set of values is the maximum value minus the minimum
# value. Define a procedure, set_range, which returns the range of three input
# values.

# Hint: the procedure, biggest which you coded in this unit
# might help you with this question. You might also like to find a way to
# code it using some built-in functions.

def set_range(x,y,z):
    return max(x,y,z) - min(x,y,z)



print(set_range(10, 4, 7))
#>>> 6  # since 10 - 4 = 6

print(set_range(1.1, 7.4, 18.7))
#>>> 17.6 # since 18.7 - 1.1 = 17.6

############################################################

# By Sam the Great from forums
# That freaking superhero has been frequenting Udacity
# as his favorite boss battle fight stage. The 'Udacity'
# banner keeps breaking, and money is being wasted on
# repairs. This time, we need you to proceduralize the
# fixing process by building a machine to automatically
# search through debris and return the 'Udacity' banner
# to the company, and be able to similarly fix other goods.

# Write a Python procedure fix_machine to take 2 string inputs
# and returns the 2nd input string as the output if all of its
# characters can be found in the 1st input string and "Give me
# something that's not useless next time." if it's impossible.
# Letters that are present in the 1st input string may be used
# as many times as necessary to create the 2nd string (you
# don't need to keep track of repeat usage).

# NOTE: # If you are experiencing difficulties taking
        # this problem seriously, please refer back to
        # "Superhero flyby", the prequel, in Problem Set 11.

# TOOLS: # if statement
         # while loop
         # string operations
         # Unit 1 Basics

# BONUS: #
# 5***** #  If you've graduated from CS101,
#  Gold  #  try solving this in one line.
# Stars! #


def fix_machine(x, y):
    if all(letter in x for letter in y):
        return y
    else:
       return "Give me something that's not useless next time."

# solution in one line for bonus
# def fix_machine(input_string, output_string):
#     return output_string if all(char in input_string for char in output_string) else "Give me something that's not useless next time."


print(fix_machine("UdaciousUdacitee",'Udacity'))
print(fix_machine("buy me dat Unicorn",'Udacity'))
print(fix_machine('AEIOU and sometimes y... c', 'Udacity'))
print(fix_machine("bwsx0-=mttrhix",'t-shirt'))


### TEST CASES ###
# print("Test case 1: ", fix_machine('UdaciousUdacitee', 'Udacity')) #"Give me something that's not useless next time."
# print("Test case 2: ", fix_machine('buy me dat Unicorn', 'Udacity')) #== 'Udacity'
# print "Test case 3: ", fix_machine('AEIOU and sometimes y... c', 'Udacity') == 'Udacity'
# print "Test case 4: ", fix_machine('wsx0-=mttrhix', 't-shirt') == 't-shirt'


############################################################
# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
#

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days_in_months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    days_in_months_2 = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    (month2 * days_in_months.get(month2) - day2) - (month1 * days_in_months.get(month1) - day1)
    (year2 - year1)*365

# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()