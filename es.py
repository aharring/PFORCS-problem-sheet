# GMIT CyberSecurity : Programming for CyberSecurity, Python
# Lecturer : Andrew Beatty
# Problem Sheet Week 6  
#
# Task Requirement :
#       Write a program that reads in a text file and outputs the number of e's it contains.
#       The program should take the filename from an argument on the command line.
# Program Name : es.py 
#
# Program Function : 
#       
#       1. Check command line params - we expect two, the program name and the input file
#          If we have less than two arguments print an error and exit
#       2. Check the file supplied exists
#          If it doesn't then print an error message
#       3. If the file exists call a function that opens the file for reading
#       4. The function looks at two methods for approaching the question
#          The first is in the inbuilt count function. This is case sensitive so if count('e') gives a different answer to count('E'). I left this code in just so you could see it
#          The second is the more traditional method - assign the fileinput to an array then loop through each character checking if it is an 'e' or 'E' and incrementing a counter
#       5. Print the output
#
#       Notes : 
#           I assigned a the output of the read to a variable and then printed the variable to see what a read stored
#           I did note you could read the file line by line but it seemed as handy to read the whole thing in one go - I'm not sure what would happen if the file was massive
#           I think you could read 536,870,912 on a 32 bit system before you'd encounter a problem using the method I used
#
#       What I learned :
#           How to read command line arguments passed to a python program
#           How to check if a file exists
#           How to open a file for reading
#           How to read in the content of a file
#	References :
#           tutorialspoint.com "Python Command Line Arguments" - module sys & command line arguments
#	    Assigned labs for week 6 
#
import sys
import os 

if len(sys.argv) < 2 :
    print("\npython3 es.py expects a filename as a parameter\n")
    quit()
else :
    filename = str(sys.argv[1])

def readFile (filename) :

# This method uses the inbuilt function 'count' but it will only count lower case e's not upper case e's
# This was actually a guess on my part. I subequently googled and read examples 
# Our lecturer also mentioned it in passing when referring to W3 listed string methods in a subsequent
# lecture
# Once I realised the count was case sensitive I tried hit and miss count('e','E'), ('e' or 'E'), count.capitalize etc which all failed
# I left the code in for reference

    with open(filename, "rt") as file :
        justE  = file.read().count('e') 
        print("\nThere are {} lowercase e's in {}\nThis was calculated using the inbuilt 'count' function\n" .format(justE, filename))

# Mar 1st. A third way of approaching the question

    with open(filename, "rt") as file :
        allTheTextInTheFile  = file.read() 
        allTheTextInTheFile = allTheTextInTheFile.lower()
        allTheTextInTheFile = allTheTextInTheFile.count('e')
        print("\nThere are {} e's in {}\nThis was calculated first reading in the file, converting to lowercase and then applying count function\n" .format(allTheTextInTheFile, filename))


# This is an alternative method for counting the E's - I split it in to upp and lower case just for practice 
# I also wanted to check if I was getting the same answer as the shorter method above

    numLowerE = 0
    numUpperE = 0
    with open(filename, "rt") as file :
        allContent = file.read()
        for letter in allContent :
            if letter == 'e' :
                numLowerE += 1
            elif letter == 'E' :
                numUpperE +=1

        totalE = numLowerE + numUpperE
        print ("There are a total of {} e's, {} lowercase and {} uppercase in {}\nThis method loops through and counts each occurrence individually\n" .format(totalE, numLowerE, numUpperE, filename) )

if os.path.exists(filename):
    readFile(filename)
else :
    print ("\nError : File does not exist \n")


