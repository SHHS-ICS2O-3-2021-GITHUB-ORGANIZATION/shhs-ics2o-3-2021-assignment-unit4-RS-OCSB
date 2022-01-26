# NAME OF AUTHOR: Ryan Swanson
# NAME OF THE PROGRAM: Word Reverser - U5A1 - Acitvity2 - q2reverse
# DATE OF CREATION: 01/25/22
# PURPOSE OF PROGRAM: Take a users inputted word and output it reversed and letter by letter

# VARIABLE DEFINITION 
userWord = 0
reversedWord = 0 #defining variables


# INPUT 
userWord = input("Please input the word you would like to be reversed:") #getting users input and assigning to a variable


# PROCESSING and OUTPUT
reversedWord = (userWord[::-1]) #reverses the word 

for i in range(0,18): #prints the letters in reverse order
  print(reversedWord[i:i+1])
