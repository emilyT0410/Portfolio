#Create a simple application in Python that identifies prime numbers within a specified range
#The application should allow users to input two numbers, representing the start and end of a range, and then output all the prime numbers within that range

import math

#Create a function to identify prime numbers
def is_prime(n):
    # check for even numbers
    if n % 2 == 0 and n > 2: 
        return False

    # loop through odd numbers
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        # check if it has a remainder
        if n % i == 0:
            return False
        
    return True

#Create a function to get and validate input
def get_number():
    while True:
        try:
            num = int(input("Please enter a number: "))
            return num
        except ValueError:
            print("Input must be an integer")

    
#Ask the user to input start range number and validate input
start_number = get_number()

#Ask the user to input the end range number and validate input
end_number = get_number()

#For values in range of inputted numbers, calculate those that are prime
for n in range(start_number, end_number):
    if is_prime(n):
        print(f"{n} is a prime number")
    


