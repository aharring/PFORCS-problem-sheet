# GMIT CyberSecurity : Programming for CyberSecurity, Python
# Lecturer : Andrew Beatty
# Program Name : BMI.py
# Python version : 3
#
# This program prompts the user for their Weight & Height 
# In both cases it does a simple error check to verify that the input evaluates 
# to a float, just to avoid obvious errors like someone entering a non digit
# 
# It then calculates their BMI using the formula kg/hsquared 
# and outputs the result

IsAFloat = False # A boolean to help with the while loop

# First prompt the user to enter their weight
# A simple check is done to see if the value entered evaluates to a float
# This is a basic check just to be sure the user didn't enter an alpha
# If the try condition succeeds then the program will exit the while loop
# Otherwise it will enter the exception and print the exception statement
# I referenced both W3Schools and Stackoverflow to see how to code a try/except 
# within a while loop. I used these constructs because they were what popped up 
# on google when I searched for how to verify an input is a float - well, lots
# of suggestions came up but this looked like the best for what I was trying to 
# accomplish


while IsAFloat == False : 		# First time in this variable is False so we enter loop
    print ("Please enter weight :") 	# Execute print statement
    try :
        Weight = float(input()) 	# Assign the input to variable Weight. If the datatype can evaluate to a float Try has worked
        IsAFloat = True         	# If the try has worked IsAFloat is set to True and we can break out of our While
    except:
        print("Weight should be entered as a number ")  # If Weight = float(input()) gave an error this statement is executed
        continue 					# Back up to the top of the loop and execute bc IsAFloat will still be False

# Reset the test variable IsAFloat because we are now going to do a similar test
# on the Height input

IsAFloat = False

while IsAFloat == False :
    print ("Please enter height :")
    try :
        Height = float(input())
        IsAFloat = True 
    except:
        print("Height should be entered as a number ")
        continue

# Calculate the square of height & reassign it to the variable Height
Height = Height ** 2 # Set the variable Height to Height squared

# Calculate the BMI by dividing Weight by Height. Remember Height here contains the squared value
BMI = Weight/Height

# Print the string 'Your BMI is' followed by the string conversion of the BMI value previously
print ("Your BMI is " + str(BMI))

