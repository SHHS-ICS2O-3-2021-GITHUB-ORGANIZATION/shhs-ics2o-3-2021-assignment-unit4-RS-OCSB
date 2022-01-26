# NAME OF AUTHOR: Ryan Swanson
# NAME OF THE PROGRAM: Word length Calculator - U5A1 (q1 length)
# DATE OF CREATION: 01/25/22
# PURPOSE OF PROGRAM: Get an inputted word from the user and display the length of said word back to teh user. Program loops until user types exit

# VARIABLE DEFINITION 
userWord = 0

# INPUT 
userWord = input("Please enter the word you would like to find the length of or type exit to exit the program:") #gets the users input word for the first time

# PROCESSING 
while userWord != ('exit'): #if the user doesnt type exit 
  print("Your word is",(len(userWord)), "letter(s) long!") #calculates the length of the inputed word

  userWord = input("\n\nPlease enter the word you would like to find the length of or type exit to exit the program:") #loops back to get another word

# OUTPUT 
if userWord == ('exit'):
  print("exiting!") #exits the program if it detects the word exit being typed
