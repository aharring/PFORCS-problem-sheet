# GMIT CyberSecurity : Programming for CyberSecurity, Python
# Lecturer : Andrew Beatty
# Problem Sheet Week 4  
#
# Task Requirement :
# 	Write a program (collatz.py) to input any positive integer and outputs the successive values of the following calculation.
#        At each step calculate the next value by taking the current value and, 
#	   if it is even, divide it by two, 
#	   but if it is odd, multiply it by three and add one.
#        Have the program end if the current value is one.
# Program Name : collatz.py
#
# Program Function : 
#	
#	1. Prompt for user input
#		A.  Verify the input is both positive and an integer
#			If it is, proceed to the next step.
#			If it isn't then ask the user again to input a positive integer
#          This will be accomplished by a while loop
#	2. Given a verified positive integer check if the value can be divided exactly by 2 without a remainder
#		If it can then your new value is the old value divided by two
#               If it cannot then your new value is the old value mulitplied by 3 and adding 1
#		If the current value is 1 then end the program
#     
#	   This will be accomplished with an if elif statement nested in a while loop that checks if the current value is 1
#	3. Print out the values  
#
#	Notes : The sample output shows all integers on one line with no brackets around it so we're not doing a print (ThisList) but we are
#		also not going to be looping through and printing each value because that puts each value on a new line
#		Option  1: 
#                   Instead of adding the successive values to an array convert them to a string and add them with a space to a variable
#		    called output. This was my first effort and I have left the code in but commented it out because I learned about
#                   print(list, end=" ") in the Wednesday Lab. I tested both methods and I could see no appreciable difference in run time but the
#                   
#              
#               Option  2: 
#                   Define an array Numbers and at the end looped through Numbers as follows
#                   for Number in Numbers :
#                       print (Number, end=" ")
#		I have left the code in for option 1 above simply for reference but commented it out because
#               I tested both methods and I could see no appreciable difference in run time but the array method looked cleaner
#
#	References :
#		W3Schools
#		Assigned labs for week 4
#

currentValue = 0
notPosInt = True
# output = "" Original solution to printing all values on one line without the brackets
outputList = [] # Array used in Option 2 above

while (notPosInt) : # Check input is both an int and positive
    try :
         currentValue = int(input("\nPlease enter a positive integer "))  # Prompt for user input. Verify the input is an integer
         if currentValue <  0 : 				        # Verify the input is positive
             print ("The input must be both an integer and positive \n")
         else :
             notPosInt = False                                          # Break out of our while loop
    except :
        print ("A positive integer is required \n")

while currentValue > 1 : 				       
    # output = output + " " + str(currentValue)                # Original solution for printing all numbers on one line with no brackets
    outputList.append(currentValue)
    if currentValue%2 == 0 :       			       # Is the number even
       currentValue = int(currentValue/2)
       # print(currentValue, output)                           # Me debugging
    else :
       currentValue = (currentValue * 3) + 1

# output = output + " " + str(currentValue) # Adding the final 1 to the output string
outputList.append(1)                        # Adding the final 1 to the output list

#print (output)
print ("\n")                                # For readability
for number in outputList :                  # Step through my array
    print (number, end=" ")
print ("\n")                                # Just to tidy things up on a large output

