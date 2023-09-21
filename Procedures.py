# Define a procedure, square, that takes one number
# as its input, and returns the square of that
# number (result of multiplying
# the number by itself).
# To help you out, the code for sum(a,b) is below.

def square(a):
    a *= a
    return a
print(square(4))




# To test your procedure, uncomment the print
# statement below, by removing the hash mark (#)
# at the beginning of the line.

# Do not remove the # from in front of the line
# with the arrows (>>>). Lines which begin like
# this (#>>>) are included to show the results
# you should see when run your procedure.

#print square(5)
#>>> 25


# Define a procedure, sum3, that takes three
# inputs, and returns the sum of the three
# input numbers.
# To help you out, the code for sum(a,b) is below.

def sum3(a,b,c):
    answer = a + b + c
    return answer




print(sum3(1,2,3))
print(sum3(93,53,70))


#print sum3(1,2,3)
#>>> 6

#print sum3(93,53,70)
#>>> 216

###########################
# Define a procedure, abbaize, that takes
# two strings as its inputs, and returns
# a string that is the first input,
# followed by two repetitions of the second input,
# followed by the first input.


def abbaize(a,b):
    answer = a+b+b+a
    return answer


print(abbaize('a','b'))
print(abbaize('dog','cat'))



#print abbaize('a','b')
#>>> 'abba'

#print abbaize('dog','cat')
#>>> 'dogcatcatdog'

##################
# Define a procedure, find_second, that takes
# two strings as its inputs: a search string
# and a target string. It should return a
# number that is the position of the second
# occurrence of the target string in the
# search string.

danton = "De l'audace, encore de l'audace, toujours de l'audace"
twister = "she sells seashells by the seashore"

def find_second(text, word):
    first_occurrence = text.find(word)
    if first_occurrence == -1:
        return 'Not Found'
    second_occurrence = text.find(word, first_occurrence+1)
    return second_occurrence

print(find_second(danton,'audace'))
print(find_second(twister,'she'))




#print find_second(danton, 'audace')
#>>> 25


#print find_second(twister,'she')
#>>> 13