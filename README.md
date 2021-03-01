# PFORCS-problem-sheet
GMIT Python Weekly Assignments &amp; 
Problem Sheet Solutions

Problem Sheet Assignment Week02 : BMI.py
Task Requirement :

	1. Write a program that calculates somebody's Body Mass Index (BMI).

	The inputs are the person's height in centimetres and weight in kilograms.
	The output  is their weight divided by their height in metres squared.
	$ python bmi.py
	Enter weight: 65
	Enter height: 180
	BMI is 20.06.

Notes, Assumptions & Error Checks

1. For both Height & Weight the program does a simple error check to verify that the input evaluates to a float, just to avoid obvious errors like someone entering a non digit

2. Given the height is expected in cm.

	I have attempted to do some error checking around the number entered to avoid an 			unrealistic answer

	I chose 272 as an upper limit for converting to metres bc the tallest ever recorded height is 	2.72metres

	I chose 24 as the lower limit for converting from cm to metres bc guinness book of records 	lists 24cm as shortest ever recorded

	If the input was between .24 and 2.72 I assume the value entered is already in m, tell the 		user and calculate accordingly

	If the input is greater than the tallest person in metres (2.72) or cm (272) or smaller than the 	smallest person in cm (24)
	or entered a negative number just to see then I print a message indicating I think there is a 		problem with the height entered

3. I make no assumptions about weight

The program then calculates their BMI using the formula kg/hsquared and outputs the result rounded to 2 decimal places

What I learned :

	1. How to prompt for user input
	2. How to assign variables
	3. How to construct a while loop
	4. How to test a condition using try & except
	5. How to do simple calculations using operators
	6. How to cast a variable to another type
	7. How to output a calculation

Resources :
	1. W3Schools
	2. Stackoverflow.com

GMIT Python Weekly Assignments & Problem Sheet Solutions

Problem Sheet Assignment Week03 : bitcoin.py
Task Requirement :
	1. Write a program (bitcoin.py) that outputs the current bitcoin price in US
	Dollars. Use the supplied code snippet to get a Dict object that contains
        the price.
	2. Extra output all the price in the three currencies, in a neat way
	
Notes : 
	The url supplying the json data as well as the code to read & assign that data to a python object was supplied by the lecturer, Andrew Beatty
	The command cat - | jq . jsonstring was used to display the json data in an eye readable format 
	
What I learned :

	 1. Json Definition (wikipedia) :is an open standard file format, and data interchange format, 
	 that uses human-readable text to store and transmit data objects consisting of attribute–value pairs and array data types (or any other serializable value.
	 2. How to read a json url & assign it to a python object
	 3. How to parse the python object to access the data I wanted
	 
Resources :
	1. Google - to find a json formatting command (jq)
	2. Wikipedia - what exactly is 'json'
	3. W3Schools - Understanding Dicts
	4. StackOverflow - More about Dicts
	
	
GMIT Python Weekly Assignments & Problem Sheet Solutions

Problem Sheet Assignment Week04 : collatz.py
Task Requirement :
	Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.

	At each step calculate the next value by taking the current value and, 
	if it is even, divide it by two, 
	but if it is odd, multiply it by three and add one.

	Have the program end if the current value is one.

What I learned :
	1. How to handle while loops, if statements and for loops
	2. How to print the contents of aa list without [], all on one line with spaces between each entry

Resources :
	1. Wednesday Lunchtime tutorial - print (list, end = " ") introduced by lecturer Andrew Beatty
	2. w3schools for conditional statements & try/except statements
	3. Example program on lecturers github showing how to manage multiple exceptions in a try/except statement. Didn't use this yet though.


GMIT Python Weekly Assignments & Problem Sheet Solutions

Problem Sheet Assignment Week05 : squareroot.py
Task Requirement :
        Write a program that takes a positive number as input, passes it to a function which attempts to approximate the square root
        of the inputted value and returns that value to be printed to the terminal. The task stiplulated we must not use python inbuilt
        functions but instead write our own square root function based on Newton's method 

What I learned :
	1. How to define a function 
	2. How to pass values to a function
        3. How to return a value from a function
 
Resources :
	1. Google "What is Newton's method for calculating a square root" 
	2. Lecture Week 05 & Live tutorial - understanding functions 


GMIT CyberSecurity : Programming for CyberSecurity, Python
 Lecturer : Andrew Beatty
 Problem Sheet Week 6  

 Task Requirement :
       Write a program that reads in a text file and outputs the number of e's it contains.
       The program should take the filename from an argument on the command line.
 Program Name : es.py 

 Program Function : 
       
       1. Check command line params - we expect two, the program name and the input file
          If we have less than two arguments print an error and exit
       2. Check the file supplied exists
          If it doesn't then print an error message
       3. If the file exists call a function that opens the file for reading
       4. The function looks at two methods for approaching the question
          The first is in the inbuilt count function. This is case sensitive so if count('e') gives a different answer to count('E'). I left this code in just so you could see it
          The second is the more traditional method - assign the fileinput to an array then loop through each character checking if it is an 'e' or 'E' and incrementing a counter
          A third method - reading in all the input, converting it to lower case & applying the count
          function was added March 1st
       5. Print the output

Notes : 
     I assigned a the output of the read to a variable and then printed the variable to see what a read stored
     I did note you could read the file line by line but it seemed as handy to read the whole thing in one go - I'm not sure what would happen if the file was massive
     I think you could read 536,870,912 on a 32 bit system before you'd encounter a problem using the method I used
     In week 07 the lecturer referenced python strings methods in passing & I revisted W3schools
     I saw I would read the whole file in, convert it to lower case then apply the count function
     I have included this code for reference

 What I learned :
     How to read command line arguments passed to a python program.
     How to check if a file exists
     How to open a file for reading
     How to read in the content of a file
         
References :
     tutorialspoint.com "Python Command Line Arguments" - module sys & command line arguments
     Assigned labs for week 6 





