# NAME OF AUTHOR: Ryan Swanson
# NAME OF THE PROGRAM: The Number Guess Game - U4 Final A
# DATE OF CREATION: 01/24/22
# PURPOSE OF PROGRAM: To create a fun game that the user can determine the parameters of in the forms of min and max values. The user is given feedback based on the amount of tries it took them aswell as if the answer was correct or incorrect. 

# VARIABLE DEFINITION 
import math
import random #allows random generation functions to work
from colorama import init #imports colored text functions
from termcolor import colored
 

generatedAnswer = 0 #setting variables that will be used to store data such as the user's guesses or the counter function

userGuess = 0

counter = 0

(user_first_input) = 0

(user_second_input) = 0

init() #starts the colored text functions


# INPUT 
 
print(colored("Welcome to the Number Game!", "cyan"))
user_first_input = input("\nFirst, please enter the lowest value to guess from:") #gets users min input value

user_second_input = input("\nEnter the highest value to guess to:") #gets users max input value 

generatedAnswer = random.randint(int(user_first_input), int(user_second_input)) #picks a random number from inbetween the numbers given by the user

print(colored("\n\nNow, try and guess the number chosen by the computer from the range you input!", 'green'))



#PROCESSING and OUTPUT


#Loop determines if the users answer matches the generated number 
while userGuess != generatedAnswer:
  counter = counter + 1 #everytime the loop is passed through 1 value is added to counter to output the amount of attempts later
  userGuess = int(input("Enter your guess here:"))

  if userGuess == generatedAnswer: #if the user's guess is correct, correct is outputted along with teh amount fo attempts 
    print("\nCorrect, the answer was", generatedAnswer)
    print("You guessed the number in", counter, "attempt!")

  else: #outputs to teh user that their selection was incorrect
    print(colored("\nIncorrect, Please try again", 'red'))
