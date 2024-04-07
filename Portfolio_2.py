#Create a matrix calculator that performs basic operations on user-inputted matrices

#Ask the user to enter two lists
#Create matrix from list 1
#Create matrix from list 2
#Multiple list 1 by list 2
#Subtract list 1 from list 2
#Add list 1 and list 2

#Import numpy
import numpy as np

#Function to get user input and add to empty list_1 and list_2
def get_user_matrix():
    list_1 = []
    list_2 = []
    for list in [list_1, list_2]:
#Apend 2 user imputted integers to each list 
        for x in range(0,2):
            user_item = int(input("Enter a number: "))
            list.append(user_item)
#Create matrix from the two lists
    return np.array([list_1, list_2])

#Create 2 matrix, x and y, using the function above
x = get_user_matrix()
print(x)
y = get_user_matrix()
print(y)

#Matrix multiplication
matrix_multiply = np.dot(x, y)
print(matrix_multiply)

#Matrix subtraction
matrix_subtraction = y - x
print(matrix_subtraction)

#Matrix addition 
matrix_addition = x + y
print(matrix_addition)