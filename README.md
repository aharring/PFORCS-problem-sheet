# PFORCS-problem-sheet
GMIT Python Weekly Assignments &amp; Problem Sheet Solutions
Problem Sheet Assignment : BMI.py
1. Write a program that calculates somebody's Body Mass Index (BMI).

The inputs are the person's height in centimetres and weight in kilograms.
The output  is their weight divided by their height in metres squared.
$ python bmi.py
Enter weight: 65
Enter height: 180
BMI is 20.06.

Notes, Assumptions & Error Checks

# 1. For both Height & Weight the program does a simple error check to verify that the input evaluates
# to a float, just to avoid obvious errors like someone entering a non digit
#
# 2. Given the height is expected in cm.
# I have attempted to do some error checking around the number entered to avoid an unrealistic answer
# I chose 272 as an upper limit for converting to metres bc the tallest ever recorded height is 2.72metres
# I chose 24 as the lower limit for converting from cm to metres bc guinness book of records lists 24cm as shortest ever recorded
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

What I learned :

How to prompt for user input
How to assign variables
How to construct a while loop
How to test a condition using try & except
How to do simple calculations using operators
How to cast a variable to another type
How to output a calculation

Resources :
W3Schools
Stackoverflow.com





