# NAME OF AUTHOR: Ryan Swanson
# NAME OF THE PROGRAM: Number Counter (U4Q1)
# DATE OF CREATION: 1/18/22
# PURPOSE OF PROGRAM: Count up and down to a specifiied number using a counter number identified by the user.

# VARIABLE DEFINITION 
largeNum = 0
counterNum = 0   #asssigned variables
counterTotal = 0


# INPUT 
largeNum = int(input("Please enter the large number to count to: ")) #getting user inputs
counterNum = int(input("Please enter the number to count by: "))

# PROCESSING and OUTPUT 

while counterTotal <= largeNum:     #loop if counternumber is less than large number 
  print (counterTotal)
  counterTotal = (counterTotal + counterNum)  #adding counter numbers until they match the counter total which should equal to the large number eventually

while largeNum >= 0: #loop for subtraction if the large number is greater than 0
  print(largeNum)
  largeNum = largeNum - counterNum #takes the total value and subtracts counter number until it equals 0

if largeNum <= 0:
  print("Counting Completed!") #prints complete if the large number is less than or equal to 0






