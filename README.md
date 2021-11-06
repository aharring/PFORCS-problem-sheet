GMIT Cybersecurity Python Weekly Assignments &amp; 

Lecturer : Andrew Beatty
Student  : Adele Harrington

PFORCS-problem-sheet - 
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

GMIT CyberSecurity : Programming for CyberSecurity, Python
Lecturer : Andrew Beatty
Problem Sheet Week 7  

Task Requirement :
     Write a program called extract-url.py, that will extract the URLs from an access.log file.
Program Name : extract-url.py 

Program Function : 
       1. If the file exists open it 
       2. Open the file. 
          a. For each line in the file extract the portion of the line corresponding to the url
          e.g. '/cart.do?action=view&itemId=EST-6&productId=SC-MG-G10&JSESSIONID=SD5SL9FF2ADFF4958' 
       3. Place the matches in a list
              a. This is contained in the function extractURLs

       4. For each url in the list split it in to it's component parts which should be stored as a dict

          e.g.
          [ 
             {
               'resource':'cart.do', 
               'parameters':{
                   'action':'view',
                   'itemId':'EST-6',
                   'productId':'SC-MG-G10'
                   'JSESSIONID':'SD5SL9FF2ADFF4958'
               }
             },
             #next dictionary object
          ]
             a. This is contained in the function extractDictEntriesFromURLList  

        5. Print the results neatly
             a. This is contained in the function printResults
       
Notes : I first return the list of URLs and then process that list to a second list of dicts.
        This is to show the two distinct pieces of work 
        I noticed some resource lines did not have a leading '/' so I changed the orig url extraction regex to look for everything after 'GET|POST'
        In my original longer file I noted sometimes there was an action but no product. 
        I tried to accomodate this by putting 'Unavailable' in these situations
        While my url List pulls out all urls my dict only pulls out entries that appeared to match

        My first attempt at completing this task is stored in extract-urlAtt1.py
        My second attempt at completing this task is stored in extract-urlAtt2.py
        
What I learned : I require a lot of practice on Regex

References :
       python.org
       W3Schools Regular Expressions
       RealPython Regular Expressions
       Assigned labs for week 7 

GMIT CyberSecurity : Programming for CyberSecurity, Python
Lecturer : Andrew Beatty

Problem Sheet Week 8

Task Requirement :
      Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

Program Name : plottask.py

Program Function :
      Using imported module numpy the program creates 3 arrays, x is a numpy array in the range of 0-4, y2 is x squared, y3 is x cubed
      Plot each, with markers, in relation to x using the module matplotlib.
      Label the axes, make Y horizontal
      Create a title, a centered legend and a grid.
      Display the graph
      Save the graph image to file

What I learned :
      How to manipulate numpy arrays
      How to plot graphs using matplotlib
      I've a way to go before the OO version on RealPython makes sense

References :
      Weekly recommended reading on w3schools & RealPython
      https://www.tutorialspoint.com/numpy/numpy_array_from_numerical_ranges.htm - how to define a numpy range
      stackoverflow - annotate, title spanning 2 lines, superscripts

GMIT CyberSecurity : Programming for CyberSecurity, Python
Lecturer : Andrew Beatty

Problem Sheet Week 10

Task Requirement :
   Write a (bullet proof) function called averageTo(aList, toIndex)
   The function should take in a list and an index.
   The function will return the average of the numbers upto and including the toIndex in the aList.
   The function to always return an integer, even if a error occurs (say return -1),
   The function will use logging to make a meaningful log warning, for any error that occurs
   (eg the aList contains an entry that is not a number/ toIndex is not valid)
   The program should include test cases to verify functionality

Program Name : averageTo.py
Program Parameters : aList, toIndex

Program Function :
    For confirmed valid data return the average of numbers upto and including the toIndex in aList
    Invalid data should return an int & post a meaningful error message
    Validation Checks/Assumptions

         1. A Negative toIndex will reevaluate to it's positive index position provided it is not out of bounds
          e.g averageTo ([1,2,3,-44, 18, 10], -4 )   toIndex -4 equates to toIndex 2
          and averageTo ([1,2,3,-44, 18, 10], -6 )   toIndex -6 equates to toIndex 0
          but  averageTo ([1,2,3,-44, 18, 10], -6 )  toIndex -7 is in invalid index number
         2. averageTo ([1,2,3,-44, 18, 10], 4 )      Negative numbers in the list do not cause a problem
         3. averageTo ([1,-1], 1 )                   It's ok if our list values add to 0
         4. averageTo ([1], 0)                       This is fine it will be 1/1
         5. averageTo ([1,2,3,4], 4)                 toIndex out of bounds, max toIndex is 3
         6. averageTo ([1,2,3,4], 2.5)               toIndex must be an int
         7. averageTo ([1,2,3,4], 3.0)               toIndex must be an int. 3.0 will be interpreted as 3
         8. averageTo ([1,2,3,4], 'a')               toIndex must be an int
         9. averageTo ([], 1)                        aList may not be empty
        10. averageTo ([1, 'b',2], 2)                aList values must be numbers
        11. averageTo ([1,2,3,4], [])                toIndex must be an int  Empty List invalid
        12. averageTo (3, 0)                         This will c
       12a. averageTo (3.5, 0)                       3 translates to [3.5] which will return int 3
        13. averageTo ()                             Function requires two args. Python TypeError. Still Messy
        14. averageTo ([1,2,3,4], a)                 toIndex must be an int  NOT WORKING YET
        15. averageTo (a, 1)                         NameError - Not nicely dealt with yet  

       What I learned :
           int(variable) does not behave the same as int(round(variable))

Notes/Assumptions
    The averageTo function returns a rounded int value as opposed to just an int
    This means an average of 2.75 will be returned as 3 not 2
References :
    Weekly recommended reading on w3schools & RealPython
    stackoverflow examples of isinstance, & float.is_integer()
    https://www.python.org/dev/peps/pep-0570/#positional-only-parameters
    https://docs.python.org/3/tutorial/errors.html
    https://stackoverflow.com/questions/19684434/best-way-to-check-function-arguments (Read but not implemented)w 

GMIT CyberSecurity : Programming for CyberSecurity, Python
Lecturer : Andrew Beatty
Problem Sheet Week 9 - Pandas  

Task Requirement : 
     Read access.log in to a panda dataframe. 
     Set the time field to be the index. 
     Use Regex to extract the SessionId from the URL & store the result in a different column
     Use groupBy to get the sum of all the data downloaded by each sessionId.
     Plot the result

Program Name : maxData.py 

Program Function : 
     1. Read the sample log in to a panda dataframe (The program assumes the log file is in the current directory)
     2. Use regex expression to extract the SessionId from the URL - insert this column at position 1  
     3. Remove unused columns to make data more readable
     4. Strip the [] from the datetime field
     5. Make the datetime field the index
     6. Group the data by SessionId
     7. Create a new dataframe sums the summable fields (Response Size) by SessionId - No breakdown by time in at this point
     8. Use matplotlib to display a graph of the results (Set some seetings regarding font, angle of x axis data so that it is readable
     9. Print out the data so it is possible to see the response size is indeed summed by SessionId
    10. Sample the dataframe, this time computing the Response Size per SessionId per day
    11. Print out this structure so that it can be compared with the previous structure to ensure the grouping/summing is correct

ToDo - use full log, output comparisons to an output file since a full log will generate a lot of output - maybe

References :
    Assigned lab for week 9 (Pandas)  
    https://www.kite.com/python/answers/how-to-print-an-entire-pandas-dataframe-in-python#:~:text=Use%20pandas.,to%20be%20displayed%20when%20printed.
    https://stackoverflow.com/questions/13682044/remove-unwanted-parts-from-strings-in-a-column
    https://www.geeksforgeeks.org/adding-new-column-to-existing-dataframe-in-pandas/ - adding a column in a specific position in the df. 
    https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.insert.html - using the panda insert to add a col in a specific location - further reading
    https://matplotlib.org/stable/gallery/ticks_and_spines/ticklabels_rotation.html
    https://stackoverflow.com/questions/56816833/pandas-pd-to-datetime-only-keep-time-do-not-date

GMIT CyberSecurity : Programming for CyberSecurity, Python
Lecturer : Andrew Beatty

Term #2 Week 5. Data Analysis

Task Requirement : Analyse a data set of your choosing using any python packages

Data set chosen & reason :
I chose the iris dataset because it is apparently the training wheels dataset of data science & analytics
Comparing the data in the iris data set to some of the idr csv files provided in the incidenet, detection & response module there are obvious advantages to the iris dataset
as a dataset for learning. The data is clean.
If the goal is to learn the capabilities for python packages such as pandas, numpy, matplotlib or seaborn then there is no distraction trying to eliminate bad data or outliers.
Additionally, the dataset is quite small and easily reviewed manually
It's a well analysed and reviewed data set within the data science community so it's easy to check results

Finally, during the summer, I set myself the task of calculating averages, medians, modes and ranges for individual varieties and all varieties without using python packages
I was trying to get a better handle on how lists/dictionaries worked. I wanted in this program to look at how similar or better information could be calculated using
python packages. The program written in the summer is called Iris4.py. To practice modules I changed this file to be a function then imported the py as a module & gave it as an
 option on my menu

Program Name : plotiris.py

Program Function :
      This program
           Checks for the existence of the Iris.csv file
           If the file exists a menu is displayed offering the following options
              1. View Iris stats generated by pandas
              2. View Iris stats using code that does not use python inbuilt packages,
                 i.e. dats is loaded in to dicts and functions were written to calculate mean, median, range & mode
               3. View selection of panda plots
               4. View the ultimate seaborn plot - 3 lines of code. Love it.

       References :
               w3schools - pandas
               https://pandas.pydata.org/docs/getting_started/intro_tutorials/04_plotting.html
               https://stackoverflow.com/questions/32244753/how-to-save-a-seaborn-plot-into-a-file (I didn't use this in the end)
               https://docs.python.org/3/tutorial/modules.html
               https://towardsdatascience.com/seaborn-python-8563c3d0ad41#:~:text=Seaborn%20is%20a%20data%20visualization,Pandas%20to%20learn%20about%20Seaborn.

       Additional Reading :
               https://machinelearningmastery.com/difference-test-validation-datasets/
               https://towardsdatascience.com/exploring-classifiers-with-python-scikit-learn-iris-dataset-2bcb490d2e1b

       Conclusion :
               Writing the code by hand to generate the mean, mode, range and median was interesting but I started to lose the will to live by the time I got to standard deviation
               I think I wrote the code such that if I had extra coffee doing standard deviation should be a neat function
               Pandas are great for doing the dog work that was required to calculate stats without packages
               Seaborn seems to give you quite a lot of information with very little code required
               You could spend a lifetime analysing datasets with different functions and plots
