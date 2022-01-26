# NAME OF AUTHOR: Ryan Swanson
# NAME OF THE PROGRAM: Word Triangle - U5A1 - q3wordtriangle
# DATE OF CREATION: 01/25/22
# PURPOSE OF PROGRAM: take the user's input as a word and turn it into a 'triangle' and output it

# VARIABLE DEFINITION 
userWord = 0
lengthOfWord = 0 #defining variables

# INPUT 
userWord = input("Enter the word you would like to put in a word triangle\n") #getting users input and assigning to a variable

# PROCESSING 
lengthOfWord = (len(userWord)) #getting the input words' length 


# OUTPUT 
for i in range (lengthOfWord): #gets the starting value for i 
    for j in range(i+1): #gets the next letter in the line by adding one to i

        print(userWord[j],end = '')#prints the users word by using the value of j, and ends by adding a blank space
    print() #prints the loop
