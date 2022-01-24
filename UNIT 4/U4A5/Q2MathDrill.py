# NAME OF AUTHOR: Ryan Swanson
# NAME OF THE PROGRAM: Math Drill Program - Q2MathDrill
# DATE OF CREATION:  01/24/22
# PURPOSE OF PROGRAM: provide the user with a chance to complete an addition or multiplcation program with feedback, aswell as a chance to exit the program at any time 

# VARIABLE DEFINITION 
import random
import math

multiplcation = 1
addition = 2
multNum1 = 0
multNum2 = 0 #assigning variables to the numbers that will be a part of the problem 

addNum1 = 0
addNum2 = 0

userMultAnswer = 0
userAddAnswer = 0

randomProbGen = random.randint(1,2) #generates number 1 or 2 whihc determines if the problem is addition or multiplcation

exitKey = '0'

# INPUT/PROCESSING/OUTPUT 

if randomProbGen == 1: #multiplcation
  multNum1 = random.randint(1,12) #gets number from 1 to 12 
  multNum2 = random.randint(1,12) #gets number from 1 to 12
  print(multNum1, 'x', multNum2) #prints question
  multAnswer = (multNum1 * multNum2) #calculates the real answer
  userMultAnswer = input('Press 0 to exit or Please enter the answer:') #gets user's answer to the multiple choice question
  
  if int(userMultAnswer) == multAnswer:
    print("Correct!") #checks if the answer is correct and prints a statement based on the outcome 

  if int(userMultAnswer) != multAnswer and int(userMultAnswer) != 0:
    print("Incorrect, the answer was:", multAnswer)
    
  if userMultAnswer == '0':
     print ("Exiting...") #exits the program if the user types 0



if randomProbGen == 2: #addition
  addNum1 = random.randint(1,100) #gets number from 1 to 100 to use in the question
  addNum2 = random.randint(1,100)
  print(addNum1, "+", addNum2) #prints the question
  addAnswer = (addNum1 + addNum2) #calculates the real answer
  userAddAnswer = input('Press 0 to exit or Please enter the answer:') #gets user inputted answer
  
  if int(userAddAnswer) == addAnswer:
    print("Correct!") #checks if users answer matches the correct answer and prints statement based on that result

  if int(userAddAnswer) != addAnswer and int(userAddAnswer) != 0:
    print("Incorrect, the answer was:", addAnswer)
    
  if userAddAnswer == '0':
   print ("Exiting...") #exits the program if 0 is entered
    
