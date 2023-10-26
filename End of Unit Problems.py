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


#################################################
###
### Define a simple nextDay procedure, that assumes
### every month has 30 days********!!!!!.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):
    if 12 < month < 1 or 30 < day < 1:
        return "Error. Input correct date."
    elif day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


##############################################################
# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will **NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
#



def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    if month1 == month2:
        numDays = (day2 - day1) + (year2 - year1)*360
        return numDays
    else:
        numDays = (30 - day1 + day2) + (month2 - month1 - 1)*30 + (year2 -year1)*360
        return numDays


def test():
    test_cases = [((2012, 9, 30, 2012, 10, 30), 30),
                  ((2012, 1, 1, 2013, 1, 1), 360),
                  ((2012, 9, 1, 2012, 9, 4), 3)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")


test()

##############################################
# Given the variable,

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# define a procedure, how_many_days,
# that takes as input a number
# representing a month, and returns
# the number of days in that month.

def how_many_days(month_number):
    return days_in_month[month_number-1]


##############################################
# Given the variable countries defined as:

#             Name    Capital  Populations (millions)
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

# Write code to print out the capital of India
# by accessing the list

print(countries[1][1])

# What multiple of Romania's population is the population
# of China? Calculate this by accessing the list and
# dividing the population of China (1350)
# by the population of Romania (21).
# Please print your result.

print((countries[0][2])/countries[2][2])

##############################################
# We defined:

stooges = ['Moe','Larry','Curly']

# but in some Stooges films, Curly was
# replaced by Shemp.

# Write one line of code that changes
# the value of stooges to be:

['Moe','Larry','Shemp']

# but does not create a new List
# object.

stooges[2] = 'Shemp'
print(stooges)

##############################################

# Define a procedure, replace_spy,
# that takes as its input a list of
# three numbers, and modifies the
# value of the third element in the
# input list to be one more than its
# previous value.

spy = [0,0,7]

def replace_spy(input):
    input[2] = input[2]+1
    return input


# In the test below, the first line calls your
# procedure which will change spy, and the
# second checks you have changed it.
# Uncomment the top two lines below.

#replace_spy(spy)
#print spy
#>>> [0,0,8]


##############################################
# Define a procedure, sum_list,
# that takes as its input a
# list of numbers, and returns
# the sum of all the elements in
# the input list.

def sum_list(input):
    answer = 0
    for i in input:
        answer += i
    return answer


print(sum_list([1, 7, 4]))
#>>> 12

print(sum_list([9, 4, 10]))
#>>> 23

print(sum_list([44, 14, 76]))
#>>> 134

##############################################

# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase
# letter 'U'.

def measure_udacity(input):
    count = 0
    for i in input:
        for a in i:
            if a == "U":
                count += 1
    return count



print(measure_udacity(['Dave','Sebastian','Katy']))
#>>> 0

print(measure_udacity(['Umika','Umberto']))
#>>> 2

##############################################
# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element(p, value):
    for i in range(len(p)):
        if p[i] == value:
            return i
    return -1


print()
print(find_element(['Job', 'Andy', 'Peter', 'Sean', 'Michael', 'Gundega', 'Sarah'], 'Kathleen'))


print(find_element([1,2,3],3))
#>>> 2

print(find_element(['alpha','beta'],'gamma'))
#>>> -1

##Using built in index method to solve the same problem.
def find_element_2(p, value):
    try:
        answer = p.index(value)
        return answer
    except:
        return -1

print(find_element_2([1,2,3],3))
print(find_element_2(['alpha','beta'],'gamma'))


##############################################
# Define a procedure, union,
# that takes as inputs two lists.
# It should modify the first input
# list to be the set union of the two
# lists. You may assume the first list
# is a set, that is, it contains no
# repeated elements.

def union(a,b):
    for i in b:
        if i not in a:
            a.append(i)




# To test, uncomment all lines
# below except those beginning with >>>.
#
a = [1,2,3]
b = [2,4,6]

# union(a,b)
print(a)
# # >>> [1,2,3,4,6]
print(b)
# # >>> [2,4,6]


##############################################
# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list_of_numbers):
    if len(list_of_numbers) == 0:
        return 0
    else:
        return max(list_of_numbers)




print(greatest([4,23,1]))
#>>> 23
print(greatest([]))
#>>> 0

##############################################
# Define a procedure, total_enrollment,
# that takes as an input a list of elements,
# where each element is a list containing
# three elements: a university name,
# the total number of students enrolled,
# and the annual tuition fees.

# The procedure should return two numbers,
# not a string,
# giving the total number of students
# enrolled at all of the universities
# in the list, and the total tuition fees
# (which is the sum of the number
# of students enrolled times the
# tuition fees for each university).

udacious_univs = [['Udacity', 90000, 0]]

usa_univs = [['California Institute of Technology', 2175, 37704],
             ['Harvard', 19627, 39849],
             ['Massachusetts Institute of Technology', 10566, 40732],
             ['Princeton', 7802, 37000],
             ['Rice', 5879, 35551],
             ['Stanford', 19535, 40569],
             ['Yale', 11701, 40500]]


def total_enrollment(input_list):
    total_students=0
    total_tuition =0
    if len(input_list) == 0:
        return (0,0)
    else:
        for items in input_list:
            total_students += items[1]
            total_tuition += items[1] * items[2]
        return (total_students,total_tuition)





print(total_enrollment(udacious_univs))
# >>> (90000,0)

# The L is automatically added by Python to indicate a long
# number. If you are trying the question in an outside
# interpreter you might not see it.

print(total_enrollment(usa_univs))
# >>> (77285,3058581079)


##############################################

# The mean of a set of numbers is the sum of the numbers divided by the
# number of numbers. Write a procedure, list_mean, which takes a list of numbers
# as its input and return the mean of the numbers in the list.

# Hint: You will need to work out how to make your division into decimal
# division instead of integer division. You get decimal division if any of
# the numbers involved are decimals.

def list_mean(input_list):
    answer = 0
    total_num = 0
    if len(input_list) == 0:
        return 0
    else:
        for items in input_list:
            total_num += items
        answer = total_num/len(input_list)
        return answer


print(list_mean([1,2,3,4]))
#>>> 2.5
print(list_mean([1,3,4,5,2]))
#>>> 3.0
print(list_mean([]))
#>>> ??? You decide. If you decide it should give an error, comment
# out the print line above to prevent your code from being graded as
# incorrect.
print(list_mean([2]))
#>>> 2.0

##############################################


# Crypto Analysis: Frequency Analysis
#
# To analyze encrypted messages, to find out information about the possible
# algorithm or even language of the clear text message, one could perform
# frequency analysis. This process could be described as simply counting
# the number of times a certain symbol occurs in the given text.
# For example:
# For the text "test" the frequency of 'e' is 1, 's' is 1 and 't' is 2.
#
# The input to the function will be an encrypted body of text that only contains
# the lowercase letters a-z.
# As output you should return a list of the normalized frequency
# for each of the letters a-z.
# The normalized frequency is simply the number of occurrences, i,
# divided by the total number of characters in the message, n.




def freq_analysis(message):
    dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
            'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    answer = []
    for letter in message:
        if letter in dict:
            dict[letter] += 1
    for key, value in dict.items():
            answer.append(value/len(message))
    return answer

#Tests

print(freq_analysis("abcd"))
#>>> [0.25, 0.25, 0.25, 0.25, 0.0, ..., 0.0]

print(freq_analysis("adca"))
#>>> [0.5, 0.0, 0.25, 0.25, 0.0, ..., 0.0]

print(freq_analysis('bewarethebunnies'))
#>>> [0.0625, 0.125, 0.0, 0.0, ..., 0.0]

##############################################


# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

index = []



def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return index
    index.append([keyword, [url]])
    return index





#
add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
print(index)

#>>> [['udacity', ['http://udacity.com', 'http://npr.org']],
#>>> ['computing', ['http://acm.org']]]


