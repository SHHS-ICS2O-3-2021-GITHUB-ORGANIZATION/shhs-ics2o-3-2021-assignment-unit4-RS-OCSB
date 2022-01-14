# NAME OF AUTHOR: Ryan Swanson
# NAME OF THE PROGRAM: Random Addition Problem Generator
# DATE OF CREATION: 1/14/22
# PURPOSE OF PROGRAM: Generate 2 random numbers and create an addition problem that the user can answer

import random #importing modules
import math

# VARIABLE DEFINITION 
var1 = 0
var2 = 0
userAnswer = 0
additionQuestion = 0


(var1) = (random.randint(1,100))  #generating the random values and assigning them
(var2) = (random.randint(1,100))


additionQuestion = (var1 + var2) #creating the final value of the quesiton


# INPUT 
print("The Question is:")
print(var1, "+", var2)
print("Enter your answer below:")
userAnswer = input() #getting user input as the answer 


# PROCESSING and OUTPUT
if int(userAnswer) == (additionQuestion):   #if statements for the final process and output that tell the user if they were correct or not
  print ("Correct!")
  
else: print("Incorrect, The answer was", additionQuestion)


