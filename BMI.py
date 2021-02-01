# GMIT CyberSecurity : Programming for CyberSecurity, Python
# Lecturer : Andrew Beatty
# Program Name : BMI.py
# Python version : 3
#
# This program prompts the user for their Weight & Height 
# In both cases it does a simple error check to verify that the input evaluates 
# to a float, just to avoid obvious errors like someone entering a non digit
#
# Niall pointed out the height is expected in cm.
# So I have attempted to do some error checking around the number entered to avoid an unrealistic answer
# I chose 272 as an upper limit for converting to m bc the tallest ever recorded height is 2.72metres
# I chose 24 as the lower limit for converting from cm to m bc guinness book of records lists 24cm as shortest ever recorded 
#
# If the input was between .24 and 2.72 I assume the value entered is already in m, tell the user and calculate accordingly
#
# If the input is greater than the tallest person in metres (2.72) or cm (272) or smaller than the smallest person in cm (24) 
# or entered a negative number just to see then I print a message indicating I think there is a problem with the height entered
#
# I make no assumptions about weight
#
# It then calculates their BMI using the formula kg/hsquared 
# and outputs the result rounded to 2 decimal places

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

BreakOutOfLoop = False # A boolean to help with the while loop

while BreakOutOfLoop == False : 	# First time in this variable is False so we enter loop
    print ("Please enter weight in Kg :") 	# Execute print statement
    try :
        Weight = float(input()) 	# Assign the input to variable Weight. If the datatype can evaluate to a float Try has worked
        BreakOutOfLoop = True         	# If the try has worked IsAFloat is set to True and we can break out of our While
    except:
        print("Weight should be entered as a number ")  # If Weight = float(input()) gave an error this statement is executed
        continue 					# Back up to the top of the loop and execute bc IsAFloat will still be False

# Reset the test variable IsAFloat because we are now going to do a similar test
# on the Height input

BreakOutOfLoop = False

while BreakOutOfLoop  == False :
    print ("Please enter height (cm) :")
    try :
        Height = float(input())
    except:
        print("Height should be entered as a number ")
        continue

    if (Height >= 24) and (Height <=272): # If the height is between 24 and 272 assume user entered cm and divide by 100 for m
        Height = Height/100 	# Divide input by 100 and reassign it to Height
        BreakOutOfLoop = True 	# If yes exit the loop
    elif (Height >= .24) and (Height <= 2.72):
        print ("Based on input value assuming the height was entered in metres not cm. Calculating accordingly")
        BreakOutOfLoop = True
    elif  (Height > 2.72 and Height < 24) or (Height > 272) or (Height <= .24 ): # Trying to catch unrealistic entries
         print("Please reconfirm your height")
         BreakOutOfLoop = False	

# Calculate the square of height & reassign it to the variable Height
Height = Height ** 2 # Set the variable Height to Height squared

# Calculate the BMI by dividing Weight by Height. Remember Height here contains the squared value
BMI = round((Weight/Height), 2) # Ed pointed out it might be tidier to round the answer

# Print the string 'Your BMI is' followed by the string conversion of the BMI value previously
print ("Your BMI is " + str(BMI))

