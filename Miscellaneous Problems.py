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
#

def stamps(x):
    return (int(x / 5), int((x % 5) / 2), int(((x % 5) % 2)))
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












