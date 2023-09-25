# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.

def print_numbers(x):
    a = 1
    while a <= x:
        print(a)
        a += 1



print(print_numbers(3))
# >>> 1
# >>> 2
# >>> 3

###############################################
# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
    count = 1
    answer = 1
    while count <= n:
        answer *= count
        count += 1
    return answer



print(factorial(4))
#>>> 24
print(factorial(5))
#>>> 120
print(factorial(6))
#>>> 720


############################################

# Define a procedure, countdown, that takes a
# positive whole number as its input, and prints
# out a countdown from that number to 1,
# followed by Blastoff!
# The procedure should not return anything.
# For this question, you just need to call
# the procedure using the line
# countdown(3)
# instead of print countdown(3).


def countdown(x):
    for x in reversed(range(1,x+1)):
        print(x)
    print("Blastoff!")




countdown(3)
#>>> 3
#>>> 2
#>>> 1
#>>> Blastoff!

###########################################

# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurrences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

def find_last(search,target):
    last = -1
    while True:
        pos = search.find(target, last +1)
        if pos == -1:
            return last
        last = pos







print(find_last('aaaa', 'a'))
#>>> 3

print(find_last('aaaaa', 'aa'))
#>>> 3

print(find_last('aaaa', 'b'))
#>>> -1

#print find_last("111111111", "1")
#>>> 8

#print find_last("222222222", "")
#>>> 9

#print find_last("", "3")
#>>> -1

#print find_last("", "")
#>>> 0

###########################################
