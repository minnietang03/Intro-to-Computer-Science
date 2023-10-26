# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number x in the string is less than or equal
# to the preceding number y, the number x should be inserted
# into a sublist. Continue adding the following numbers to the
# sublist until reaching a number z that
# is greater than the number y.
# Then add this number z to the normal list and continue.

#Hint - "int()" turns a string's element into a number

# def numbers_in_lists(string):
    # YOUR CODE

#testcases
# string = '543987'
# result = [5,[4,3],9,[8,7]]
# print repr(string), numbers_in_lists(string) == result
# string= '987654321'
# result = [9,[8,7,6,5,4,3,2,1]]
# print repr(string), numbers_in_lists(string) == result
# string = '455532123266'
# result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
# print repr(string), numbers_in_lists(string) == result
# string = '123456789'
# result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print repr(string), numbers_in_lists(string) == result


def number_in_list(string):
    result = []
    sublist = []
    prev_number = None
    for i in string:
        number = int(i)
        if number not in range(1,10):
            return "Error. Numbers 1-9 only."
        if prev_number is None or number > prev_number:
            if sublist:
                result.append(sublist)
                sublist = []
            result.append(number)
        else:
            sublist.append(number)
        prev_number = number
    if sublist:
        result.append(sublist)
    return result


print(number_in_list('543987'))
print(number_in_list('987654321'))
print(number_in_list('455532123266'))
print(number_in_list('123456789'))

