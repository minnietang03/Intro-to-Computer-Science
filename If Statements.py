# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.

def bigger(x,y):
    if x > y:
        return x
    elif x==y:
        return x
    else:
        return y

print(bigger(2,7))
#>>> 7

print(bigger(3,2))
#>>> 3

print(bigger(3,3))
#>>> 3

###############################################################
# Define a procedure, is_friend, that
# takes a string as its input, and
# returns a Boolean indicating if
# the input string is the name of
# a friend. Assume I am friends with
# everyone whose name starts with D
# and no one else. You do not need to
# check for the lower case 'd'


def is_friend(x):
    return x.startswith("D")

print(is_friend('Diane'))
#>>> True

print(is_friend('Fred'))
#>>> False

###############################################################
# Define a procedure, is_friend_2, that takes
# a string as its input, and returns a
# Boolean indicating if the input string
# is the name of a friend. Assume
# I am friends with everyone whose name
# starts with either 'D' or 'N', but no one
# else. You do not need to check for
# lower case 'd' or 'n'

# testing use case to see if code works before writing fun
# name = "Minnie"
#
# print(name.startswith("D") or name.startswith("N"))


def is_friend_2(x):
    return x.startswith('D') or x.startswith('N')

print(is_friend_2('Diane'))
# >>> True

print(is_friend_2('Ned'))
# >>> True

print(is_friend_2('Moe'))
# >>> False


###############################################################
# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

def biggest(x,y,z):
    return max(x,y,z)


print(biggest(3, 6, 9))
#>>> 9

print(biggest(6, 9, 3))
#>>> 9

print(biggest(9, 3, 6))
#>>> 9

print(biggest(3, 3, 9))
#>>> 9

print(biggest(9, 3, 9))
#>>> 9

##############################################

# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(x,y,z):
    numbers = [x,y,z]
    numbers.sort()
    return numbers[1]


print(median(1,2,3))
#>>> 2

print(median(9,3,6))

##############################################

# Define a procedure weekend which takes a string as its input, and
# returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.

def weekend(day):
   if day == 'Saturday':
       return "True"
   if day == 'Sunday':
       return "True"
   else:
       return "False"

# your code here

print(weekend('Monday'))
# >>> False

print(weekend('Saturday'))
# >>> True

print(weekend('July'))
# >>> False







