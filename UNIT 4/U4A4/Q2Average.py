# NAME OF AUTHOR: Ryan Swanson
# NAME OF THE PROGRAM: Number Sum and Average Calculator (Q2Average)
# DATE OF CREATION: 1/18/22
# PURPOSE OF PROGRAM: Calculates the average and sum of any amount of numbers entered by the user and provides instant feedback

# VARIABLE DEFINITION 
totalSum = 0
totalAverage = 0 #defining variables
counter = 0


# INPUT 
inputNum = int(input("Enter your number (0 to Exit): ")) #getting user inputs and assigning them to inputNum variable


# PROCESSING 
while inputNum != 0:  #while the users input is not 0, the program keeps track of the amount of number with the counter, the total sum and continues to operate until 0 is typed
    totalSum = totalSum + inputNum
    inputNum = int(input("Enter your number (0 to Exit): "))
    counter = counter + 1

totalSum = totalSum + inputNum #calculates total sum
totalAverage = totalSum/counter #calculates total average


# OUTPUT 
print ("Total sum of entered number(s) is", totalSum) #outputs previously calculated information
print ("Total average of entered number(s) is" , totalAverage)
