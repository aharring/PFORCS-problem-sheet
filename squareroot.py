# GMIT CyberSecurity : Programming for CyberSecurity, Python
# Lecturer : Andrew Beatty
# Problem Sheet Week 5  
#
# Task Requirement :
#      Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
#      You should create a function called <tt>sqrt</tt> that does this.
#
# Program Name : squareroot.py 
#
# Program Function : 
#	Prompt user for a positive number
#       Pass the inputted number to a function 
#       Calculate & return the approximate square root
#       print the returned value
#
#       Newton's method is calculated using the following 
#        
#           .5(X + N/X) where N is the number we want the square root of and X is any number between 1 & X
#           It is a recursive calculation
#           X is initially a randomly selected number
#           If the value calculated is not within a tolerable level make your new 'X' equal to the calculated approximation
#           It's approximate so you have to define a tolerance within which you are willing to accept the answer
#           Also,the example shows the answer rounded to 1 decimal place	
#
#       Notes
#           The sample output provided with the assignment gives an answer rounded to one decimal place so I rounded to one decimal place
#           This means for an input of 99 the output is 9.9 whereas in fact 9.94987437 is far more accurate
#           
#	References :
#           Multiple YouTube Videos explaining Newton's method
#           stackoverflow
#	    W3Schools
#	    Assigned labs for week 5 
#

def sqrt(numToFindSquareRootOf) :
    
    acceptableTolerance = .01 # I made this up. There didn't seem to be a notable difference between .01 and say .00000001
    fingerInTheAirGuess = (numToFindSquareRootOf/2) # This really did seem to be a finger in the air number so I chose the middle
    while True :
        approxSquareRoot = .5 * (fingerInTheAirGuess + (numToFindSquareRootOf/fingerInTheAirGuess)) # Guess = 1/2* (X + N/X)
        if (abs(fingerInTheAirGuess - approxSquareRoot) < acceptableTolerance) : # If the absolute diff between guess & calc is < .01 return
            return round(approxSquareRoot, 1)
        else :
            fingerInTheAirGuess = approxSquareRoot # We need a new finger in the air 

numToFindSquareRootOf = float(input ("\nPlease enter a positive number :")) # Prompt for input, cast to float & assign to variable

while numToFindSquareRootOf <= 0 :
    numToFindSquareRootOf = float(input ("\nPlease enter a positive number :"))

approxSquareRoot = sqrt(numToFindSquareRootOf)

print("\nThe square root of {} is approx. {}.\n" .format (numToFindSquareRootOf, approxSquareRoot))
