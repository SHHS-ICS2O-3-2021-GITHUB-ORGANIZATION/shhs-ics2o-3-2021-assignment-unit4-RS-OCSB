# NAME OF AUTHOR: Ryan Swanson
# NAME OF THE PROGRAM: School Age Checker (U4A5 - Q1 AgeChecker)
# DATE OF CREATION: 01/21/22
# PURPOSE OF PROGRAM: Take  the users age as an input and determine what level of school they are currently in

# VARIABLE DEFINITION 
userAge = 0

# INPUT 
userAge = input('please enter your age:') #gets users input and set to variable 


# PROCESSING and OUTPUT
if int(userAge) > 4 and int(userAge) < 12: 
  print("You are in elementary school!")

if int(userAge) > 11 and int(userAge) < 15:
  print('You are in intermediate school!')

if int(userAge) > 14 and int(userAge) < 19:
  print("You are in high school")

if int(userAge) >= 19:
  print("You are in university/college/workforce")

#each if statement checks if the users inputted age is between certain perameters and displays the messages accordingly, based on what age group they are in
