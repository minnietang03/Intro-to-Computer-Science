# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.

def symmetric(a):
    index = 0
    column = []
    while index < len(a):
        for rows in a:
            column.append(rows[index])
        if a[index] != column:
            return False
        index += 1
        column = []
    return True

#print symmetric([[1, 2, 3],
#                [2, 3, 4],
#                [3, 4, 1]])
#>>> True

#print symmetric([["cat", "dog", "fish"],
#                ["dog", "dog", "fish"],
#                ["fish", "fish", "cat"]])
#>>> True

#print symmetric([["cat", "dog", "fish"],
#                ["dog", "dog", "dog"],
#                ["fish","fish","cat"]])
#>>> False

#print symmetric([[1, 2],
#                [2, 1]])
#>>> True

#print symmetric([[1, 2, 3, 4],
#                [2, 3, 4, 5],
#                [3, 4, 5, 6]])
#>>> False

#print symmetric([[1,2,3],
#                 [2,3,1]])
#>>> False


###########################################

# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True
# if the given square is antisymmetric and False otherwise.
# An nxn square is called antisymmetric if A[i][j]=-A[j][i]
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.

# def antisymmetric(a):

    #Write your code here

#
# # Test Cases:
#
# print antisymmetric([[0, 1, 2],
#                      [-1, 0, 3],
#                      [-2, -3, 0]])
# #>>> True
#
# print antisymmetric([[0, 0, 0],
#                      [0, 0, 0],
#                      [0, 0, 0]])
# #>>> True
#
# print antisymmetric([[0, 1, 2],
#                      [-1, 0, -2],
#                      [2, 2,  3]])
# #>>> False
#
# print antisymmetric([[1, 2, 5],
#                      [0, 1, -9],
#                      [0, 0, 1]])
#>>> False

# antisymmetric = [[0, 1, 2],
#                 [-1, 0, 3],
#                 [-2, -3, 0]]


# print(antisymmetric[0][0])
# print(antisymmetric[0][1])
# print(antisymmetric[0][2])
# print()
#
# print(antisymmetric[0][0])
# print(antisymmetric[1][0])
# print(antisymmetric[2][0])
# print()

def antisymmetric(a):
    for x in range(len(a)):
        for y in range(len(a[x])):
            if a[x][y] != -a[y][x]:
                return False
    return True

print(antisymmetric([[0, 1, 2],
                [-1, 0, 3],
                [-2, -3, 0]]))
print(antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]))
print(antisymmetric([[0, 1, 2],
                     [-1, 0, -2],
                     [2, 2,  3]]))
print(antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]]))




#############################################

# By Ashwath from forums
# Given a list of lists representing a n * n matrix as input,
# define a  procedure that returns True if the input is an identity matrix
# and False otherwise.

# An IDENTITY matrix is a square matrix in which all the elements
# on the principal/main diagonal are 1 and all the elements outside
# the principal diagonal are 0.
# (A square matrix is a matrix in which the number of rows
# is equal to the number of columns)








# Write your code here


# Test Cases:

matrix1 = [[1, 0, 0, 0],
           [0, 1, 0, 0],
           [0, 0, 1, 0],
           [0, 0, 0, 1]]

matrix2 = [[1, 0, 0],
           [0, 1, 0],
           [0, 0, 0]]

matrix3 = [[2, 0, 0],
           [0, 2, 0],
           [0, 0, 2]]

matrix4 = [[1, 0, 0, 0],
           [0, 1, 1, 0],
           [0, 0, 0, 1]]

matrix5 = [[1, 0, 0, 0, 0, 0, 0, 0, 0]]

matrix6 = [[1, 0, 0, 0],
           [0, 1, 0, 1],
           [0, 0, 1, 0],
           [0, 0, 0, 1]]


matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]

def testing_zeroes(a):
    for rows in range(len(a)):
        for cols in range(len(a[rows])):
            if rows != cols:
                if a[rows][cols] != 0:
                    return False
    return True


# print(testing_zeroes(matrix1))
# print(testing_zeroes(matrix2))
# print(testing_zeroes(matrix3))
# print(testing_zeroes(matrix4))
# print(testing_zeroes(matrix5))
# print(testing_zeroes(matrix6))
# print(testing_zeroes(matrix7))


#what answer to matrix to should spit out
# print(matrix2[0][0])
# print(matrix2[1][1])
# print(matrix2[2][2])

def square_matrix(a):
    for rows in range(len(a)):
        pass
    if range(len(a)) == range(len(a[rows])):
        return True
    else:
        return False


# test square_matrix func
# print(square_matrix(matrix1))
# print(square_matrix(matrix2))
# print(square_matrix(matrix3))
# print(square_matrix(matrix4))
# print(square_matrix(matrix5))
# print(square_matrix(matrix6))
# print(square_matrix(matrix7))



def is_identity_matrix(a):
    if square_matrix(a) and testing_zeroes(a):
        for rows in range(len(a)):
            if a[rows][rows] != 1:
                return False
        return True
    return False


print(is_identity_matrix(matrix1))
print(is_identity_matrix(matrix2))
print(is_identity_matrix(matrix3))
print(is_identity_matrix(matrix4))
print(is_identity_matrix(matrix5))
print(is_identity_matrix(matrix6))
print(is_identity_matrix(matrix7))


#answers to test cases

# print(is_identity_matrix(matrix1))
# >>>True

# print(is_identity_matrix(matrix2))
# >>>False


# print(is_identity_matrix(matrix3))
# >>>False



# print(is_identity_matrix(matrix4))
# >>>False


# print(is_identity_matrix(matrix5))
# >>>False


# print(is_identity_matrix(matrix6))
# >>>False

# print(is_identity_matrix(matrix7))
# >>>False


