# NAME OF AUTHOR: Ryan Swanson
# NAME OF THE PROGRAM: Q1 Volume
# DATE OF CREATION: 1/12/2022
# PURPOSE OF PROGRAM: Calculate the volume of a rectangular prism given the length, height and width of the shape as inputs

# VARIABLE DEFINITION (declare variables)
varHeight = 0 
varLength = 0
varWidth = 0
finalVolume = 0 

# INPUT (information from user)
#prompting user for the h,l,w and then assigning to a variable

varHeight = int(input("Please enter the height: "))
varLength = int(input("Please enter the length: "))
varWidth = int(input("Please enter the width: "))

# PROCESSING (algorithim)
print("Calculating Volume...")

#calculating the final volume
finalVolume = (varHeight * varLength * varWidth)


# OUTPUT (print statement/export to file/game)
#display volume to user

print(str(finalVolume))

