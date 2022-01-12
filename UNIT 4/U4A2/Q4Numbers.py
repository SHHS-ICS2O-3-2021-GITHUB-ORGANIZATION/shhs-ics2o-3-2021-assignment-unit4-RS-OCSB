# NAME OF AUTHOR: Ryan Swanson
# NAME OF THE PROGRAM: Q4 Numbers
# DATE OF CREATION: 1/12/2022
# PURPOSE OF PROGRAM: label and caulate the average and sum of 5 numbers

# VARIABLE DEFINITION (declare variables)
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0

finalSum = 0
finalAverage = 0

# INPUT (information from user)
num1 = int(input("Please enter your first number: "))
num2 = int(input("Please enter your second number: "))
num3 = int(input("Please enter your third number: "))
num4 = int(input("Please enter your fourth number: "))
num5 = int(input("Please enter your fifth number: "))


# PROCESSING (algorithim)

finalSum = (num1 + num2 + num3 + num4 + num5)

finalAverage = (finalSum /5)

# OUTPUT (print statement/export to file/game)
print("\nYour Selections Were...\n")

from tabulate import tabulate
data = [[num1, num2, num3, num4, num5, finalSum, finalAverage]]
print (tabulate(data, headers=["Number 1", "Number 2", "Number 3", "Number 4", 'Number 5', 'Sum', 'Average']))

