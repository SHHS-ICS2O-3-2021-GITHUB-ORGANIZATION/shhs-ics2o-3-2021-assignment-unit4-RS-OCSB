# NAME OF AUTHOR: Ryan Swanson
# NAME OF THE PROGRAM: Random Number Generator
# DATE OF CREATION: 1/14/2022
# PURPOSE OF PROGRAM: Take two numbers to define the range and then print a random value between the two

# VARIABLE DEFINITION 

var1 = 0
var2 = 0
randomNum = 0


# INPUT 
var1 = int(input('Please select your first number: ')) #assigns the inputs to variables
var2 = int(input('Please select your second number: '))

# PROCESSING 
import random

randomNum = (random.randint(var1,var2)) #generates a random int from input number 1 to number 2

# OUTPUT 
print(randomNum)
