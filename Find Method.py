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












