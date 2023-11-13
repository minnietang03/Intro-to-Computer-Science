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

##############################################


# Define a procedure, lookup,
# that takes two inputs:

# - an index
# - keyword

# The procedure should return a list
# of the urls associated
# with the keyword. If the keyword
# is not in the index, the procedure
# should return an empty list.

index = [['udacity', ['http://udacity.com', 'http://npr.org']],
         ['computing', ['http://acm.org']]]


def lookup(index,keyword):
    for items in index:
        if keyword == items[0]:
            return items[1]
    return []

print(lookup(index,'udacity'))
print(lookup(index,'computing'))
print(lookup(index,'uda'))



#print lookup(index,'udacity')
#>>> ['http://udacity.com','http://npr.org']

##############################################

# Define a procedure, add_page_to_index,
# that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

# It should update the index to include
# all of the word occurences found in the
# page content by adding the url to the
# word's associated url list.

index = []

#
# def add_to_index(index,keyword,url):
#     for entry in index:
#         if entry[0] == keyword:
#             entry[1].append(url)
#             return
#     index.append([keyword,[url]])

def add_page_to_index(index,url,content):
    content = content.split()
    for items in content:
        index.append([items, [url]])
    return index



add_page_to_index(index,'fake.text',"This is a test")
print(index)


#>>> [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']],
#>>> ['test',['fake.text']]]


##############################################
# 1 Gold Star

# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.



def split_string(source, splitlist):
    result = [source]
    for item in splitlist:
        new_result = []
        for words in result:
            new_result.extend(words.split(item))
        result = new_result
    return [words for words in result if words]







out = split_string("This is a test-of the,string separation-code!"," ,!-")
print(out)
# # #>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']
# #
out = split_string("After  the flood   ...  all the colors came out.", " .")
print(out)
# #>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']
#
out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print(out)
# #>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']

##############################################

# Write a procedure, count_words, which takes as input a string
# and returns the number of words in the string. You may consider words
# as strings of characters separated by spaces.

def count_words(passage):
    new_passage = passage.split()
    return len(new_passage)


passage =("The number of orderings of the 52 cards in a deck of cards "
"is so great that if every one of the almost 7 billion people alive "
"today dealt one ordering of the cards per second, it would take "
"2.5 * 10**40 times the age of the universe to order the cards in every "
"possible way.")
print(count_words(passage))
#>>>56

##############################################

# Write a procedure, speed_fraction, which takes as its inputs the result of
# a traceroute (in ms) and distance (in km) between two points. It should
# return the speed the data travels as a decimal fraction of the speed of
# light.

speed_of_light = 300000 # km per second

def speed_fraction(traceroute, distance):
    traceroute_in_seconds  = traceroute /1000
    time = (distance*2 ) / (traceroute_in_seconds)
    answer = time/speed_of_light
    return answer






print(speed_fraction(50,5000))
# answer =  0.666666666667

print(speed_fraction(50,10000))
# answer =  1.33333333333  # Any thoughts about this answer, or these inputs?




##############################################

# Write a procedure, convert_seconds, which takes as input a non-negative
# number of seconds and returns a string of the form
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes,
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#


def is_plural_hour(number):
    if number == 1:
        return 'hour'
    return 'hours'


def is_plural_minute(number):
    if number == 1:
        return 'minute'
    return 'minutes'


def is_plural_second(number):
    if number == 1:
        return 'second'
    return 'seconds'


def convert_seconds(number):
    if number % 3600 != 0:
        hour = int(number / 3600)
        hour_plural = is_plural_hour(hour)
        if ((number % 3600) % 60) != 0:
            minute = int((number % 3600) / 60)
            minute_plural = is_plural_minute(minute)
            if isinstance(number, float):
                second = round(((number % 3600) % 60), 1)
            else:
                second = int(((number % 3600) % 60))
            second_plural = is_plural_second(second)
            return f'{hour} {hour_plural}, {minute} {minute_plural}, {second} {second_plural}'

        else:
            minute = int((number % 3600) / 60)
            minute_plural = is_plural_minute(minute)
            return f'{hour} {hour_plural}, {minute} {minute_plural}'
    hour = int(number / 3600)
    hour_plural = is_plural_hour(hour)
    return f'{hour} {hour_plural}'


print(convert_seconds(60))

print(convert_seconds(3600))


print(convert_seconds(3661))
# #>>> 1 hour, 1 minute, 1 second
#
print(convert_seconds(7325))
# #>>> 2 hours, 2 minutes, 5 seconds
#
print(convert_seconds(7261.7))
# #>>> 2 hours, 1 minute, 1.7 seconds

##############################################
# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).


# print(2 ** 10)     # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

# print(2 ** 20)      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

# print(2 ** 30)     # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

# print(2 ** 40)     # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size
# is given in megabytes (MB).


def convert_bits(size, unit):
    if unit == 'kb':
        size /= 1024
    elif unit == 'Gb':
        size *= 1024
    elif unit == 'Tb':
        size *= (1.024 ** 6)
    elif unit == 'kB':
        size /= (1024 / 8)
    elif unit == 'GB':
        size *= (1024 * 8)
    elif unit == 'TB':
        size *= ((1.024 ** 6) * 8)
    elif unit == 'MB':
        size *= 8
    return size

# print(convert_bits(1024,'kB'))
# print(convert_bits(13,'GB'))
# print(convert_bits(5.6,'MB'))
# print(convert_bits(5.6,'Mb'))
# print(convert_bits(10,'MB'))
# print(convert_bits(2,'kB'))
# print(convert_bits(2,'kb'))



def download_time(file_size, file_unit, bandwidth, bandwidth_unit):
    speed_of_download = convert_bits(file_size, file_unit) / convert_bits(bandwidth, bandwidth_unit)
    return speed_of_download










def is_plural_hour(number):
        if number == 1:
            return 'hour'
        return 'hours'


def is_plural_minute(number):
    if number == 1:
        return 'minute'
    return 'minutes'


def is_plural_second(number):
    if number == 1:
        return 'second'
    return 'seconds'


def convert_seconds(number):
    if number % 3600 != 0:
        hour = int(number / 3600)
        hour_plural = is_plural_hour(hour)
        if ((number % 3600) % 60) != 0:
            minute = int((number % 3600) / 60)
            minute_plural = is_plural_minute(minute)
            if isinstance(number, float):
                second = round(((number % 3600) % 60), 1)
            else:
                second = int(((number % 3600) % 60))
            second_plural = is_plural_second(second)
            return f'{hour} {hour_plural}, {minute} {minute_plural}, {second} {second_plural}'

        else:
            minute = int((number % 3600) / 60)
            minute_plural = is_plural_minute(minute)
            return f'{hour} {hour_plural}, {minute} {minute_plural}'
    hour = int(number / 3600)
    hour_plural = is_plural_hour(hour)
    return f'{hour} {hour_plural}'

number = download_time(1024,'kB', 1, 'MB')
# print(f'{number} seconds')
print(convert_seconds(number))

# print(download_time(1024,'kB', 1, 'MB'))
# #>>> 0 hours, 0 minutes, 1 second


number = download_time(1024,'kB', 1, 'Mb')
# print(convert_bits(1024,'kB'))
# print(convert_bits(1, 'Mb'))
# print(f'{number} seconds')
print(convert_seconds(number))

# print(download_time(1024,'kB', 1, 'Mb'))
# #>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable
#
# #
number = download_time(13,'GB', 5.6, 'MB')
# print(convert_bits(13,'GB'))
# print(convert_bits(5, 'MB'))
# print(f'{number} seconds')
print(convert_seconds(number))
#
# # print(download_time(13,'GB', 5.6, 'MB'))
# # #>>> 0 hours, 39 minutes, 37.1428571429 seconds
#
#
number = download_time(13,'GB', 5.6, 'Mb')
# print(f'{number} seconds')
print(convert_seconds(number))
#
# # print(download_time(13,'GB', 5.6, 'Mb'))
# # #>>> 5 hours, 16 minutes, 57.1428571429 seconds
#
#
number = download_time(10,'MB', 2, 'kB')
# print(f'{number} seconds')
print(convert_seconds(number))
#
# # print(download_time(10,'MB', 2, 'kB'))
# # #>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable
#
#
number = download_time(10,'MB', 2, 'kb')
# print(f'{number} seconds')
print(convert_seconds(number))
#
# # print(download_time(10,'MB', 2, 'kb'))
# #>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable
#




##############################################

# Define a function, hash_string,
# that takes as inputs a keyword
# (string) and a number of buckets,
# and returns a number representing
# the bucket for that keyword.

def hash_string(keyword,buckets):
    total = 0
    if keyword:
        for i in range(len(keyword)):
            total += ord(keyword[i])
        return total % buckets
    else:
        return None





# hash entire string

print(hash_string('a',12))
#>>> 1

print(hash_string('b',12))
#>>> 2

print(hash_string('a',13))
#>>> 6

print(hash_string('au',12))
#>>> 10

print(hash_string('udacity',12))
#>>> 11

print(hash_string('Udacity', 14))
# 14
print(hash_string('CS101', 20))
# 16
print(hash_string('abcdefghijklmnop', 80))
# 72
print(hash_string('searchwithpeter.info', 73))
# 48


##############################################

# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
    hash_table = []
    for i in range(nbuckets):
        hash_table.append([])
    return hash_table

print(make_hashtable(10))


##############################################
# Define a procedure, hashtable_get_bucket,
# that takes two inputs - a hashtable, and
# a keyword, and returns the bucket where the
# keyword could occur.

def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword, len(htable))]

def hash_string(keyword,buckets):
    total = 0
    if keyword:
        for i in range(len(keyword)):
            total += ord(keyword[i])
        return total % buckets
    else:
        return None

def make_hashtable(nbuckets):
    hash_table = []
    for i in range(nbuckets):
        hash_table.append([])
    return hash_table




table = [[['Francis', 13], ['Ellis', 11]], [], [['Bill', 17],
['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]]

# print(hashtable_get_bucket(table, 'Zoe'))
# # print(hashtable_get_bucket(table, "Zoe"))
# #>>> [['Bill', 17], ['Zoe', 14]]
#
# print(hashtable_get_bucket(table, "Brick"))
# #>>> []
#
# print(hashtable_get_bucket(table, "Lilith"))
# #>>> [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]


for i, bucket in enumerate(table):
    print(f'At index {i} the bucket is {bucket}')




##############################################
# Define a procedure,
#
#    hashtable_add(htable,key,value)
#
# that adds the key to the hashtable (in
# the correct bucket), with the correct
# value and returns the new hashtable.
#
# (Note that the video question and answer
#  do not return the hashtable, but your code
#  should do this to pass the test cases.)

def hashtable_add(htable, key, value):
    index = hash_string(key, len(htable))
    htable[index].append([key,value])
    return htable



def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword, len(htable))]

def hash_string(keyword,buckets):
    total = 0
    if keyword:
        for i in range(len(keyword)):
            total += ord(keyword[i])
        return total % buckets
    else:
        return None

def make_hashtable(nbuckets):
    hash_table = []
    for i in range(nbuckets):
        hash_table.append([])
    return hash_table


table = make_hashtable(5)

#
hashtable_add(table,'Bill', 17)
hashtable_add(table,'Coach', 4)
hashtable_add(table,'Ellis', 11)
hashtable_add(table,'Francis', 13)
hashtable_add(table,'Louis', 29)
hashtable_add(table,'Nick', 2)
hashtable_add(table,'Rochelle', 4)
hashtable_add(table,'Zoe', 14)
print(table)
print(len(table))
# >>> [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
# >>> [['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

##############################################
# Define a procedure,

# hashtable_lookup(htable,key)

# that takes two inputs, a hashtable
# and a key (string),
# and returns the value associated
# with that key.

def hashtable_lookup(htable,key):
    index = hash_string(key, len(htable))
    for items in htable[index]:
        if items[0] == key:
            return items[1]





def hashtable_add(htable, key, value):
    index = hash_string(key, len(htable))
    htable[index].append([key,value])
    return htable



def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword, len(htable))]

def hash_string(keyword,buckets):
    total = 0
    if keyword:
        for i in range(len(keyword)):
            total += ord(keyword[i])
        return total % buckets
    else:
        return None

def make_hashtable(nbuckets):
    hash_table = []
    for i in range(nbuckets):
        hash_table.append([])
    return hash_table

table = [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
[['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

print(hashtable_lookup(table, 'Francis'))
#>>> 13

print(hashtable_lookup(table, 'Louis'))
#>>> 29

print(hashtable_lookup(table, 'Zoe'))
#>>> 14
##############################################
# Define a procedure,

# hashtable_update(htable,key,value)

# that updates the value associated with key. If key is already in the
# table, change the value to the new value. Otherwise, add a new entry
# for the key and value.

# Hint: Use hashtable_lookup as a starting point.
# Make sure that you return the new htable

def hashtable_update(htable,key,value):
    index = hash_string(key, len(htable))
    for items in htable[index]:
        if items[0] == key:
            items[1] = value
            return htable
    htable[index].append([key, value])
    return htable



def hashtable_lookup(htable,key):
    index = hash_string(key, len(htable))
    for items in htable[index]:
        if items[0] == key:
            return items[1]



def hashtable_add(htable, key, value):
    index = hash_string(key, len(htable))
    htable[index].append([key,value])
    return htable



def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword, len(htable))]

def hash_string(keyword,buckets):
    total = 0
    if keyword:
        for i in range(len(keyword)):
            total += ord(keyword[i])
        return total % buckets
    else:
        return None

def make_hashtable(nbuckets):
    hash_table = []
    for i in range(nbuckets):
        hash_table.append([])
    return hash_table



table = [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
[['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

# print(hashtable_update(table, 'Bill', 42))

print(hashtable_update(table, 'Rochelle', 94))
# print(hashtable_update(table, 'Luke', 7))
# hashtable_update(table, 'Zed', 68)
print(table)
#>>> [[['Ellis', 11], ['Francis', 13]], [['Zed', 68]], [['Bill', 42],
#>>> ['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Nick', 2],
#>>> ['Rochelle', 94]]]


##############################################


# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5
population_dict = {}
def population(key, value):
    population_dict[key] = value
    return population_dict


print(population('Shanghai', 17.8))
print(population('Istanbul', 13.3))
print(population('Karachi', 13.0))
print(population('Mumbai', 12.5))


##############################################


# Change the lookup procedure
# to now work with dictionaries.

def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    return None

##############################################

# Define a procedure,
#
#    hashtable_add(htable,key,value)
#
# that adds the key to the hashtable (in
# the correct bucket), with the correct
# value and returns the new hashtable.
#
# (Note that the video question and answer
#  do not return the hashtable, but your code
#  should do this to pass the test cases.)




def hashtable_add(htable, key, value):
    index = hash_string(key, len(htable))
    htable[index].append([key, value])
    return htable


def hashtable_get_bucket(htable, keyword):
    return htable[hash_string(keyword, len(htable))]


def hash_string(keyword, buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out


def make_hashtable(nbuckets):
    table = []
    for unused in range(0, nbuckets):
        table.append([])
    return table

# table = make_hashtable(5)
# hashtable_add(table,'Bill', 17)
# hashtable_add(table,'Coach', 4)
# hashtable_add(table,'Ellis', 11)
# hashtable_add(table,'Francis', 13)
# hashtable_add(table,'Louis', 29)
# hashtable_add(table,'Nick', 2)
# hashtable_add(table,'Rochelle', 4)
# hashtable_add(table,'Zoe', 14)
# print table
# >>> [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
# >>> [['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

##############################################

# Dictionaries of Dictionaries (of Dictionaries)

# The next several questions concern the data structure below for keeping
# track of Udacity's courses (where all of the values are strings):

#    { <hexamester>, { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }

# For example,

courses = {
    'feb2012': {'cs101': {'name': 'Building a Search Engine',
                          'teacher': 'Dave',
                          'assistant': 'Peter C.'},
                'cs373': {'name': 'Programming a Robotic Car',
                          'teacher': 'Sebastian',
                          'assistant': 'Andy'}},
    'apr2012': {'cs101': {'name': 'Building a Search Engine',
                          'teacher': 'Dave',
                          'assistant': 'Sarah'},
                'cs212': {'name': 'The Design of Computer Programs',
                          'teacher': 'Peter N.',
                          'assistant': 'Andy',
                          'prereq': 'cs101'},
                'cs253':
                    {'name': 'Web Application Engineering - Building a Blog',
                     'teacher': 'Steve',
                     'prereq': 'cs101'},
                'cs262':
                    {'name': 'Programming Languages - Building a Web Browser',
                     'teacher': 'Wes',
                     'assistant': 'Peter C.',
                     'prereq': 'cs101'},
                'cs373': {'name': 'Programming a Robotic Car',
                          'teacher': 'Sebastian'},
                'cs387': {'name': 'Applied Cryptography',
                          'teacher': 'Dave'}},
    'jan2044': {'cs001': {'name': 'Building a Quantum Holodeck',
                          'teacher': 'Dorina'},
                'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                          'teacher': 'Jasper'},
                }
}


# If you want to loop through the keys in the dictionary,
# you can use the construct below.
#         for <key> in <dictionary>:
#                    <block>
# For example, this procedure returns a list of all the courses offered
# in the given hexamester:

def courses_offered(courses, hexamester):
    res = []
    for c in courses[hexamester]:
        res.append(c)
    return res


# You do not need to use this code if you do not want to and may find another,
# simpler method to answer this question, although later ones may require this.

# Define a procedure, is_offered(courses, course, hexamester), that returns
# True if the input course is offered in the input hexamester, and returns
# False otherwise.  For example,

# print is_offered(courses, 'cs101', 'apr2012')
# >>> True

# print is_offered(courses, 'cs003', 'apr2012')
# >>> False

# (Note: it is okay if your procedure produces an error if the input
# hexamester is not included in courses.
# For example, is_offered(courses, 'cs101', 'dec2011') can produce an error.)
# However, do not leave any uncommented statements in your code which lead
# to an error as your code will be graded as incorrect.

def is_offered(courses, course, hexamester):
    for dicts in courses[hexamester]:
        if course in dicts:
            return True
    return False

print(is_offered(courses, 'cs101', 'apr2012'))
# >>> True

print(is_offered(courses, 'cs003', 'apr2012'))
# >>> False

print(is_offered(courses, 'cs001', 'jan2044'))
# >>> True

print(is_offered(courses, 'cs253', 'feb2012'))
# >>> False
##############################################

# Dictionaries of Dictionaries (of Dictionaries)

# The next several questions concern the data structure below for keeping
# track of Udacity's courses (where all of the values are strings):

#    { <hexamester>, { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }

# For example,

courses = {
    'feb2012': {'cs101': {'name': 'Building a Search Engine',
                          'teacher': 'Dave',
                          'assistant': 'Peter C.'},
                'cs373': {'name': 'Programming a Robotic Car',
                          'teacher': 'Sebastian',
                          'assistant': 'Andy'}},
    'apr2012': {'cs101': {'name': 'Building a Search Engine',
                          'teacher': 'Dave',
                          'assistant': 'Sarah'},
                'cs212': {'name': 'The Design of Computer Programs',
                          'teacher': 'Peter N.',
                          'assistant': 'Andy',
                          'prereq': 'cs101'},
                'cs253':
                    {'name': 'Web Application Engineering - Building a Blog',
                     'teacher': 'Steve',
                     'prereq': 'cs101'},
                'cs262':
                    {'name': 'Programming Languages - Building a Web Browser',
                     'teacher': 'Wes',
                     'assistant': 'Peter C.',
                     'prereq': 'cs101'},
                'cs373': {'name': 'Programming a Robotic Car',
                          'teacher': 'Sebastian'},
                'cs387': {'name': 'Applied Cryptography',
                          'teacher': 'Dave'}},
    'jan2044': {'cs001': {'name': 'Building a Quantum Holodeck',
                          'teacher': 'Dorina'},
                'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                          'teacher': 'Jasper'},
                }
}


# If you want to loop through the keys in the dictionary,
# you can use the construct below.
#         for <key> in <dictionary>:
#                    <block>
# For example, this procedure returns a list of all the courses offered
# in the given hexamester:

def courses_offered(courses, hexamester):
    res = []
    for c in courses[hexamester]:
        res.append(c)
    return res


# You do not need to use this code if you do not want to and may find another,
# simpler method to answer this question, although later ones may require this.

# Define a procedure, is_offered(courses, course, hexamester), that returns
# True if the input course is offered in the input hexamester, and returns
# False otherwise.  For example,

# print is_offered(courses, 'cs101', 'apr2012')
# >>> True

# print is_offered(courses, 'cs003', 'apr2012')
# >>> False

# (Note: it is okay if your procedure produces an error if the input
# hexamester is not included in courses.
# For example, is_offered(courses, 'cs101', 'dec2011') can produce an error.)
# However, do not leave any uncommented statements in your code which lead
# to an error as your code will be graded as incorrect.

def is_offered(courses, course, hexamester):
    for dicts in courses[hexamester]:
        if course in dicts:
            return True
    return False
#
# print(is_offered(courses, 'cs101', 'apr2012'))
# # >>> True
#
# print(is_offered(courses, 'cs003', 'apr2012'))
# # >>> False
#
# print(is_offered(courses, 'cs001', 'jan2044'))
# # >>> True
#
# print(is_offered(courses, 'cs253', 'feb2012'))
# # >>> False
#

# Define a procedure, when_offered(courses, course), that takes a courses data
# structure and a string representing a class, and returns a list of strings
# representing the hexamesters when the input course is offered.

def when_offered(courses,course):
    offer_hexamesters = []
    for key, values in courses.items():
        for value in values:
            if value == course:
                offer_hexamesters.append(key)
    return offer_hexamesters




print(when_offered (courses, 'cs101'))
#>>> ['apr2012', 'feb2012']

print(when_offered(courses, 'bio893'))
#>>> []


##############################################


# Dictionaries of Dictionaries (of Dictionaries)

# The next several questions concern the data structure below for keeping
# track of Udacity's courses (where all of the values are strings):

#    { <hexamester>, { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }

# For example,

courses = {
    'feb2012': {'cs101': {'name': 'Building a Search Engine',
                          'teacher': 'Dave',
                          'assistant': 'Peter C.'},
                'cs373': {'name': 'Programming a Robotic Car',
                          'teacher': 'Sebastian',
                          'assistant': 'Andy'}},
    'apr2012': {'cs101': {'name': 'Building a Search Engine',
                          'teacher': 'Dave',
                          'assistant': 'Sarah'},
                'cs212': {'name': 'The Design of Computer Programs',
                          'teacher': 'Peter N.',
                          'assistant': 'Andy',
                          'prereq': 'cs101'},
                'cs253':
                    {'name': 'Web Application Engineering - Building a Blog',
                     'teacher': 'Steve',
                     'prereq': 'cs101'},
                'cs262':
                    {'name': 'Programming Languages - Building a Web Browser',
                     'teacher': 'Wes',
                     'assistant': 'Peter C.',
                     'prereq': 'cs101'},
                'cs373': {'name': 'Programming a Robotic Car',
                          'teacher': 'Sebastian'},
                'cs387': {'name': 'Applied Cryptography',
                          'teacher': 'Dave'}},
    'jan2044': {'cs001': {'name': 'Building a Quantum Holodeck',
                          'teacher': 'Dorina'},
                'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                          'teacher': 'Jasper'},
                }
}


# If you want to loop through the keys in the dictionary,
# you can use the construct below.
#         for <key> in <dictionary>:
#                    <block>
# For example, this procedure returns a list of all the courses offered
# in the given hexamester:

def courses_offered(courses, hexamester):
    res = []
    for c in courses[hexamester]:
        res.append(c)
    return res


# You do not need to use this code if you do not want to and may find another,
# simpler method to answer this question, although later ones may require this.

# Define a procedure, is_offered(courses, course, hexamester), that returns
# True if the input course is offered in the input hexamester, and returns
# False otherwise.  For example,

# print is_offered(courses, 'cs101', 'apr2012')
# >>> True

# print is_offered(courses, 'cs003', 'apr2012')
# >>> False

# (Note: it is okay if your procedure produces an error if the input
# hexamester is not included in courses.
# For example, is_offered(courses, 'cs101', 'dec2011') can produce an error.)
# However, do not leave any uncommented statements in your code which lead
# to an error as your code will be graded as incorrect.

def is_offered(courses, course, hexamester):
    for dicts in courses[hexamester]:
        if course in dicts:
            return True
    return False
#
# print(is_offered(courses, 'cs101', 'apr2012'))
# # >>> True
#
# print(is_offered(courses, 'cs003', 'apr2012'))
# # >>> False
#
# print(is_offered(courses, 'cs001', 'jan2044'))
# # >>> True
#
# print(is_offered(courses, 'cs253', 'feb2012'))
# # >>> False
#

# Define a procedure, when_offered(courses, course), that takes a courses data
# structure and a string representing a class, and returns a list of strings
# representing the hexamesters when the input course is offered.

def when_offered(courses,course):
    offer_hexamesters = []
    for key, values in courses.items():
        for value in values:
            if value == course:
                offer_hexamesters.append(key)
    return offer_hexamesters




# print(when_offered (courses, 'cs101'))
# #>>> ['apr2012', 'feb2012']
#
# print(when_offered(courses, 'bio893'))
#>>> []/


# Define a procedure, involved(courses, person), that takes
# as input a courses structure and a person and returns a Dictionary that
# describes all the courses the person is involved in.  A person is involved
# in a course if they are a value for any property for the course.  The output
# Dictionary should have hexamesters as its keys, and each value should be a
# list of courses that are offered that hexamester (the courses in the list
# can be in any order).

def involved(courses, person):
    new_dict = {}
    for keys, values in courses.items():
        for keys2, values2 in values.items():
            for keys3, values3 in values2.items():
                if person == values3:
                    if keys in new_dict:
                        new_dict[keys].append(keys2)
                    else:
                        new_dict[keys] = [keys2]
    return new_dict






# For example:

print(involved(courses, 'Dave'))
#>>> {'apr2012': ['cs101', 'cs387'], 'feb2012': ['cs101']}

print(involved(courses, 'Peter C.'))
#>>> {'apr2012': ['cs262'], 'feb2012': ['cs101']}

print(involved(courses, 'Dorina'))
#>>> {'jan2044': ['cs001']}

print(involved(courses,'Peter'))
#>>> {}

print(involved(courses,'Robotic'))
#>>> {}

print(involved(courses, ''))
#>>> {}


##############################################
# 6. In video 28. Update, it was suggested that some of the duplicate code in
# lookup and update could be avoided by a better design.  We can do this by
# defining a procedure that finds the entry     corresponding to a given key, and
# using that in both lookup and update.

# Here are the original procedures:
def hashtable_update(htable, key, value):
    entry = find_entry(hashtable_get_bucket(htable, key), key)
    if entry:
        entry[1] = value
    else:
        hashtable_get_bucket(htable, key).append([key, value])


def hashtable_lookup(htable, key):
    entry = find_entry(hashtable_get_bucket(htable, key), key)
    if entry:
        return entry[1]
    return None


def find_entry(bucket, key):
    for entry in bucket:
        if entry[0] == key:
            return entry
    return None

def make_hashtable(size):
    table = []
    for unused in range(0, size):
        table.append([])
    return table

def hash_string(s, size):
    h = 0
    for c in s:
         h = h + ord(c)
    return h % size

def hashtable_get_bucket(htable, key):
    return htable[hash_string(key, len(htable))]

# Whenever we have duplicate code like the loop that finds the entry in
# hashtable_update and hashtable_lookup, we should think if there is a better way
# to write this that would avoid the duplication. We should be able to rewrite
# these procedures to be shorter by defining a new procedure and rewriting both
# hashtable_update and hashtable_lookup to use that procedure.

# Modify the code for both hashtable_update and hashtable_lookup to have the same
# behavior they have now, but using fewer lines of code in each procedure.  You
# should define a new procedure to help with this. Your new version should have
# approximately the same running time as the original version, but neither
# hashtable_update or hashtable_lookup should include any for or while loop, and
# the block of each procedure should be no more than 6 lines long.

# Your procedures should have the same behavior as the originals.  For example,

table = make_hashtable(10)
hashtable_update(table, 'Python', 'Monty')
hashtable_update(table, 'CLU', 'Barbara Liskov')
hashtable_update(table, 'JavaScript', 'Brendan Eich')
hashtable_update(table, 'Python', 'Guido van Rossum')
print(hashtable_lookup(table, 'Python'))
#>>> Guido van Rossum

##############################################

# [Double Gold Star] Memoization is a way to make code run faster by saving
# previously computed results.  Instead of needing to recompute the value of an
# expression, a memoized computation first looks for the value in a cache of
# pre-computed values.

# Define a procedure, cached_execution(cache, proc, proc_input), that takes in
# three inputs: a cache, which is a Dictionary that maps inputs to proc to
# their previously computed values, a procedure, proc, which can be called by
# just writing proc(proc_input), and proc_input which is the input to proc.
# Your procedure should return the value of the proc with input proc_input,
# but should only evaluate it if it has not been previously called.


cache = {}
def cached_execution(cache, proc, proc_input):
    if proc in cache:
        print('cache is not empty')
        return cache[proc]
    else:
        answer = proc(proc_input)
        cache[proc] = answer
        return answer



# Here is an example showing the desired behavior of cached_execution:

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result = result * i
    print("Running factorial")
    return result

print('First time running.')
print(cached_execution(cache, factorial, 50))

  # start cache as an empty dictionary
### first execution (should print out Running factorial and the result)

print("Second time:")
# ### second execution (should only print out the result)
print(cached_execution(cache, factorial, 50))
#

##############################################
# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a'
# following 'z'.

def shift(letter):
    if letter == 'z':
        return 'a'
    return chr(ord(letter) +1)



print(shift('a'))
#>>> b
print(shift('n'))
#>>> o
print(shift('z'))
#>>> a

##############################################
# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.
#
def shift_n_letters(letter, n):
    return chr(97 + (((ord(letter) + n)-97) % 26))


print(shift_n_letters('s', 1))
#>>> t
print(shift_n_letters('s', 2))
#>>> u
print(shift_n_letters('s', 10))
#>>> c
print(shift_n_letters('s', -10))
#>>> i
print(shift_n_letters('a', -1))
#z
print(shift_n_letters('k', -12))
#y

##############################################
# Dictionaries of Dictionaries (of Dictionaries)

# The next several questions concern the data structure below for keeping
# track of Udacity's courses (where all of the values are strings):

#    { <hexamester>, { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }

# For example,

courses = {
    'feb2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'apr2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262': {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'jan2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
                        'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                     }
    }


# For the following questions, you will find the
#         for <key> in <dictionary>:
#                    <block>
# construct useful. This loops through the key values in the Dictionary.  For
# example, this procedure returns a list of all the courses offered in the given
# hexamester:

def courses_offered(courses, hexamester):
    res = []
    for c in courses[hexamester]:
        res.append(c)
    return res

# Define a procedure, when_offered(courses, course), that takes a courses data
# structure and a string representing a class, and returns a list of strings
# representing the hexamesters when the input course is offered.

def when_offered(courses,course):
    offer_hexamesters = []
    for key, values in courses.items():
        for value in values:
            if value == course:
                offer_hexamesters.append(key)
    return offer_hexamesters





#print when_offered (courses, 'cs101')
#>>> ['apr2012', 'feb2012']

#print when_offered(courses, 'bio893')
#>>> []


##############################################
# Dictionaries of Dictionaries (of Dictionaries)

# The next several questions concern the data structure below for keeping
# track of Udacity's courses (where all of the values are strings):

#    { <hexamester>, { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }

# For example,

courses = {
    'feb2012': {'cs101': {'name': 'Building a Search Engine',
                          'teacher': 'Dave',
                          'assistant': 'Peter C.'},
                'cs373': {'name': 'Programming a Robotic Car',
                          'teacher': 'Sebastian',
                          'assistant': 'Andy'}},
    'apr2012': {'cs101': {'name': 'Building a Search Engine',
                          'teacher': 'Dave',
                          'assistant': 'Sarah'},
                'cs212': {'name': 'The Design of Computer Programs',
                          'teacher': 'Peter N.',
                          'assistant': 'Andy',
                          'prereq': 'cs101'},
                'cs253':
                    {'name': 'Web Application Engineering - Building a Blog',
                     'teacher': 'Steve',
                     'prereq': 'cs101'},
                'cs262':
                    {'name': 'Programming Languages - Building a Web Browser',
                     'teacher': 'Wes',
                     'assistant': 'Peter C.',
                     'prereq': 'cs101'},
                'cs373': {'name': 'Programming a Robotic Car',
                          'teacher': 'Sebastian'},
                'cs387': {'name': 'Applied Cryptography',
                          'teacher': 'Dave'}},
    'jan2044': {'cs001': {'name': 'Building a Quantum Holodeck',
                          'teacher': 'Dorina'},
                'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                          'teacher': 'Jasper'},
                }
}


# If you want to loop through the keys in the dictionary,
# you can use the construct below.
#         for <key> in <dictionary>:
#                    <block>
# For example, this procedure returns a list of all the courses offered
# in the given hexamester:

def courses_offered(courses, hexamester):
    res = []
    for c in courses[hexamester]:
        res.append(c)
    return res


# You do not need to use this code if you do not want to and may find another,
# simpler method to answer this question, although later ones may require this.

# Define a procedure, is_offered(courses, course, hexamester), that returns
# True if the input course is offered in the input hexamester, and returns
# False otherwise.  For example,

# print is_offered(courses, 'cs101', 'apr2012')
# >>> True

# print is_offered(courses, 'cs003', 'apr2012')
# >>> False

# (Note: it is okay if your procedure produces an error if the input
# hexamester is not included in courses.
# For example, is_offered(courses, 'cs101', 'dec2011') can produce an error.)
# However, do not leave any uncommented statements in your code which lead
# to an error as your code will be graded as incorrect.

def is_offered(courses, course, hexamester):
    for dicts in courses[hexamester]:
        if course in dicts:
            return True
    return False

# print is_offered(courses, 'cs101', 'apr2012')
# >>> True

# print is_offered(courses, 'cs003', 'apr2012')
# >>> False

# print is_offered(courses, 'cs001', 'jan2044')
# >>> True

# print is_offered(courses, 'cs253', 'feb2012')
# >>> False


##############################################


# Dictionaries of Dictionaries (of Dictionaries)

# The next several questions concern the data structure below for keeping
# track of Udacity's courses (where all of the values are strings):

#    { <hexamester>, { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }

# For example,

courses = {
    'feb2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'apr2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253':
                {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262':
                {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'jan2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
               'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                     }
    }






# [keys] = key
# For the following questions, you will find the
#         for <key> in <dictionary>:
#                    <block>
# construct useful. This loops through the key values in the Dictionary. For
# example, this procedure returns a list of all the courses offered in the given
# hexamester:

def courses_offered(courses, hexamester):
    res = []
    for c in courses[hexamester]:
        res.append(c)
    return res

# [Double Gold Star] Define a procedure, involved(courses, person), that takes
# as input a courses structure and a person and returns a Dictionary that
# describes all the courses the person is involved in.  A person is involved
# in a course if they are a value for any property for the course.  The output
# Dictionary should have hexamesters as its keys, and each value should be a
# list of courses that are offered that hexamester (the courses in the list
# can be in any order).

def involved(courses, person):
    new_dict = {}
    for keys, values in courses.items():
        for key, value in values.items():
            for key3, value3 in value.items():
                if person == value3:
                    if keys in new_dict:
                        new_dict[keys].append(key)
                    else:
                        new_dict[keys] = [key]
    return new_dict




# For example:

print(involved(courses, 'Dave'))
#>>> {'apr2012': ['cs101', 'cs387'], 'feb2012': ['cs101']}

print(involved(courses, 'Peter C.'))
#>>> {'apr2012': ['cs262'], 'feb2012': ['cs101']}

print(involved(courses, 'Dorina'))
#>>> {'jan2044': ['cs001']}

print(involved(courses,'Peter'))
#>>> {}

print(involved(courses,'Robotic'))
#>>> {}

print(involved(courses, ''))
#>>> {}


##############################################
# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def rotate(string, n):
    new_string = []
    for letter in string:
        if letter == ' ':
            new_string.append(' ')
        else:
            new_string.append(chr(97 + (((ord(letter) + n)-97) % 26)))
    return ''.join(new_string)





print(rotate ('sarah', 13))
#>>> 'fnenu'
print(rotate('fnenu',13))
# #>>> 'sarah'
print(rotate('dave',5))
# #>>>'ifaj'
print(rotate('ifaj',-5))
# #>>>'dave'
print(rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17))
# #>>> ???

##############################################
# Question 1: Pick One

# Define a procedure, pick_one, that takes three inputs: a Boolean
# and two other values. If the first input is True, it should return
# the second input. If the first input is False, it should return the
# third input.

# For example, pick_one(True, 37, 'hello') should return 37, and
# pick_one(False, 37, 'hello') should return 'hello'.

def pick_one(boolean, input1, input2):
    if boolean == True:
        return input1
    else:
        return  input2



print(pick_one(True, 37, 'hello'))
#>>> 37

print(pick_one(False, 37, 'hello'))
#>>> hello

print(pick_one(True, 'red pill', 'blue pill'))
#>>> red pill

print(pick_one(False, 'sunny', 'rainy'))
#>>> rainy

##############################################
# Question 2. Triangular Numbers

# The triangular numbers are the numbers 1, 3, 6, 10, 15, 21, ...
# They are calculated as follows.

# 1
# 1 + 2 = 3
# 1 + 2 + 3 = 6
# 1 + 2 + 3 + 4 = 10
# 1 + 2 + 3 + 4 + 5 = 15

# Write a procedure, triangular, that takes as its input a positive
# integer n and returns the nth triangular number.

def triangular(n):
    answer = 0
    for i in range(1, n +1):
        answer += i
    return answer




print(triangular(1))
#>>>1

print(triangular(3))
#>>> 6

print(triangular(10))
#>>> 55

##############################################
# Question 7: Find and Replace

# For this question you need to define two procedures:
#  make_converter(match, replacement)
#     Takes as input two strings and returns a converter. It doesn't have
#     to make a specific type of thing. It can
#     return anything you would find useful in apply_converter.
#  apply_converter(converter, string)
#     Takes as input a converter (produced by make_converter), and
#     a string, and returns the result of applying the converter to the
#     input string. This replaces all occurrences of the match used to
#     build the converter, with the replacement.  It keeps doing
#     replacements until there are no more opportunities for replacements.


def make_converter(match, replacement):
    return (match, replacement)

def apply_converter(converter, string):
    match, replacement = converter
    while match in string:
        string = string.replace(match, replacement)
    return string



# For example,

c1 = make_converter('aa', 'a')
print apply_converter(c1, 'aaaa')
#>>> a

c = make_converter('aba', 'b')
print apply_converter(c, 'aaaaaabaaaaa')
#>>> ab

# Note that this process is not guaranteed to terminate for all inputs
# (for example, apply_converter(make_converter('a', 'aa'), 'a') would
# run forever).


##############################################
# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a
# list, and returns the element in the list that has the most
# consecutive repetitions. If there are multiple elements that
# have the same number of longest repetitions, the result should
# be the one that appears first. If the input list is empty,
# it should return None.

def longest_repetition(input_list):
    curr_max = None
    curr_max_cnt = 0
    last = None
    last_cnt = 0
    for i in input_list:
        if (i == last) or (i == None):
            last_cnt += 1
        else:
            if last_cnt > curr_max_cnt:
                curr_max_cnt = last_cnt
                curr_max = last
            last_cnt = 1
        last = i
    if last_cnt > curr_max_cnt:
        curr_max = last
    return curr_max


#For example,
#
print(longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1]))
# 3

print(longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd']))
# # b
#
print(longest_repetition([1,2,3,4,5]))
# # 1
#
print(longest_repetition([]))
# None

print(longest_repetition([[1], [2, 2], [2, 2], [2, 2], [3, 3, 3]]))


##############################################

# One Gold Star
# Question 1-star: Stirling and Bell Numbers

# The number of ways of splitting n items in k non-empty sets is called
# the Stirling number, S(n,k), of the second kind. For example, the group
# of people Dave, Sarah, Peter and Andy could be split into two groups in
# the following ways.

# 1.   Dave, Sarah, Peter         Andy
# 2.   Dave, Sarah, Andy          Peter
# 3.   Dave, Andy, Peter          Sarah
# 4.   Sarah, Andy, Peter         Dave
# 5.   Dave, Sarah                Andy, Peter
# 6.   Dave, Andy                 Sarah, Peter
# 7.   Dave, Peter                Andy, Sarah

# so S(4,2) = 7

# If instead we split the group into one group, we have just one way to
# do it.

# 1. Dave, Sarah, Peter, Andy

# so S(4,1) = 1

# or into four groups, there is just one way to do it as well

# 1. Dave        Sarah          Peter         Andy

# so S(4,4) = 1

# If we try to split into more groups than we have people, there are no
# ways to do it.

# The formula for calculating the Stirling numbers is

#  S(n, k) = k*S(n-1, k) + S(n-1, k-1)

# Furthermore, the Bell number B(n) is the number of ways of splitting n
# into any number of parts, that is,

# B(n) is the sum of S(n,k) for k =1,2, ... , n.

# Write two procedures, stirling and bell. The first procedure, stirling
# takes as its inputs two positive integers of which the first is the
# number of items and the second is the number of sets into which those
# items will be split. The second procedure, bell, takes as input a
# positive integer n and returns the Bell number B(n).

def stirling(n, k):
    if n == k == 1:
        return 1
    elif n >= k >= 1:
        return k * stirling(n - 1, k) + stirling(n - 1, k - 1)
    else:
        return 0

def bell(n):
    bell_sum = 0
    for k in range(1, n + 1):
        bell_sum += stirling(n, k)
    return bell_sum


# print stirling(1,1)
# >>> 1
# print stirling(2,1)
# >>> 1
# print stirling(2,2)
# >>> 1
# print stirling(2,3)
# >>>0

# print stirling(3,1)
# >>> 1
# print stirling(3,2)
# >>> 3
# print stirling(3,3)
# >>> 1

# print stirling(4,1)
# >>> 1
# print stirling(4,2)
# >>> 7
# print stirling(4,3)
# >>> 6
# print stirling(4,4)
# >>> 1

# print stirling(5,1)
# >>> 1
# print stirling(5,2)
# >>> 15
# print stirling(5,3)
# >>> 25
# print stirling(5,4)
# >>> 10
# print stirling(5,5)
# >>> 1

# print stirling(20,15)
# >>> 452329200

# print bell(1)
# >>> 1
# print bell(2)
# >>> 2
# print bell(3)
# >>> 5
# print bell(4)
# >>> 15
# print bell(5)
# >>> 52
# print bell(15)
# >>> 1382958545


