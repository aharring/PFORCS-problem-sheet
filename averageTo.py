# GMIT CyberSecurity : Programming for CyberSecurity, Python
# Lecturer : Andrew Beatty
#
# Problem Sheet Week 10  
#
# Task Requirement : 
#    Write a (bullet proof) function called averageTo(aList, toIndex)
#    The function should take in a list and an index. 
#    The function will return the average of the numbers upto and including the toIndex in the aList.
#    The function to always return an integer, even if a error occurs (say return -1), 
#    The function will use logging to make a meaningful log warning, for any error that occurs 
#    (eg the aList contains an entry that is not a number/ toIndex is not valid)
#    The program should include test cases to verify functionality
#
# Program Name : averageTo.py 
# Program Parameters : aList, toIndex
#
# Program Function : 
#     For confirmed valid data return the average of numbers upto and including the toIndex in aList
#     Invalid data should return an int & post a meaningful error message
#     Validation Checks/Assumptions
#
#          1. A Negative toIndex will reevaluate to it's positive index position provided it is not out of bounds  
#           e.g averageTo ([1,2,3,-44, 18, 10], -4 )   toIndex -4 equates to toIndex 2
#           and averageTo ([1,2,3,-44, 18, 10], -6 )   toIndex -6 equates to toIndex 0 
#           but  averageTo ([1,2,3,-44, 18, 10], -6 )  toIndex -7 is in invalid index number
#          2. averageTo ([1,2,3,-44, 18, 10], 4 )      Negative numbers in the list do not cause a problem 
#          3. averageTo ([1,-1], 1 )                   It's ok if our list values add to 0 
#          4. averageTo ([1], 0)                       This is fine it will be 1/1
#          5. averageTo ([1,2,3,4], 4)                 toIndex out of bounds, max toIndex is 3
#          6. averageTo ([1,2,3,4], 2.5)               toIndex must be an int  
#          7. averageTo ([1,2,3,4], 3.0)               toIndex must be an int. 3.0 will be interpreted as 3
#          8. averageTo ([1,2,3,4], 'a')               toIndex must be an int 
#          9. averageTo ([], 1)                        aList may not be empty
#         10. averageTo ([1, 'b',2], 2)                aList values must be numbers
#         11. averageTo ([1,2,3,4], [])                toIndex must be an int  Empty List invalid 
#         12. averageTo (3, 0)                         3 translates to [3] 
#        12a. averageTo (3.5, 0)                       3 translates to [3.5] which will return int 3
#         13. averageTo ()                             Function requires two args. Python TypeError. Still Messy
#         14. averageTo ([1,2,3,4], a)                 toIndex must be an int  NOT WORKING YET
#         15. averageTo (a, 1)                         NameError - Not nicely dealt with yet 
#
#       What I learned :
#           int(variable) does not behave the same as int(round(variable))
#
#       Notes/Assumptions
#           The averageTo function returns a rounded int value as opposed to just an int
#           This means an average of 2.75 will be returned as 3 not 2
#
#	References :
#          Weekly recommended reading on w3schools & RealPython
#          stackoverflow examples of isinstance, & float.is_integer()
#          https://www.python.org/dev/peps/pep-0570/#positional-only-parameters
#          https://docs.python.org/3/tutorial/errors.html
#          https://stackoverflow.com/questions/19684434/best-way-to-check-function-arguments (Read but not implemented)
#          https://stackoverflow.com/questions/57713184/how-to-write-logging-messages-to-a-file
#
import logging # Lecture 3, week 9
import datetime as dt
import time

# Redirecting Debug to output averageTo.log
# Debug output shows the pre conversion to int for valid averages. Please do review the log file

LOG_FILE = "averageTo.log" # Just a straightforward log file, no timestamp, overwritten for each run
fileHandler = logging.FileHandler("{0}".format(LOG_FILE))
rootLogger = logging.getLogger()
rootLogger.addHandler(fileHandler)
rootLogger.setLevel(logging.DEBUG)             # Debug Level

def averageTo (aList, toIndex) :

    if isinstance(aList, int) or isinstance(aList, float) :
        listEntry = aList
        aList = []
        aList.append(listEntry)               # If we have just one int/float .. convert it to a list element
    elif not isinstance(aList, list) :        # Check our first argument is a list
        print ("\nError : Function averageTo expects aList, e.g., [1,2,3], as it's first argument\n")
        return -1

    lenAList = len(aList)                     # We use len(aList) a few times so assign it to a variable
    if lenAList == 0 :                        # Check the list is not empty 
        print("Please provide list values")
        return -1

    if isinstance(toIndex, float) :           # 2.5 is an error but 3.0 is ok. Only check floats bc this fails on ints
        if not(toIndex.is_integer()) :
            print ("\nParameter 2, toIndex, value {} must evaluate to an integer" .format(str(toIndex)))
            return -1
        else :
            toIndex = int(toIndex)            # Explicitly typecast in case you get a whole num float otherwise 
    elif not(isinstance(toIndex, int)) :
        print ("\nParameter 2, toIndex, value {} must evaluate to an integer" .format(str(toIndex))) # Catches 'a'
        return -1

    # Index value should be in List range
    if toIndex < 0 :
        if toIndex + lenAList < 0 :           # If the negative value cannot be indexed from the right
            print("Parameter 2, toIndex, value {} must be > 0 && < length, {}, of parameter 1, aList, {}" .format(str(toIndex), lenAList, aList))
            return -1
        else :                                # Find positive Index pos equating to negative number 
            logging.debug("Original toIndex %d", toIndex)          # Before we change index 
            toIndex = toIndex + lenAList # Set the index the right way around, so -1 is the last element
            logging.debug("Modified toIndex  %d", toIndex)         # Checking neg index eval logic 

    if toIndex >= len(aList) :                # Check toIndex is not > number of entries in the list
        print("Parameter 2, toIndex, value {} must be < length, {}, of parameter 1, aList, {}" .format(str(toIndex), lenAList, aList))
        return -1

    # The 'Everything is fine' code that calculates the sum of all values of aList <= aListIndexValue

    upperLimit = toIndex + 1   # i in range 1-n will calc to n-1. We need to include n in our calc
    logging.debug("Summing list entries %s to index %d in list len %d", str(aList), toIndex, lenAList)    # Check we are implementing correct range

    sumAListToIndex = 0                        # Define/Initialise var to store sum of aList up to upperLimit

    for listIndex in range (0, upperLimit) :
        value = aList[listIndex]
        if isinstance(value, (int, float)) :    # Verify list entries are numbers. It's ok if we have floats here
            logging.debug("CurrentArray pos %d, CurrentArray Value %s", listIndex, str(aList[listIndex]))
            sumAListToIndex += value            # Running total of sum list elemenets up to & including index element 
        else :
            print("aList entries must be numbers. aList entry \'{}\' is not a number" .format(str(value)))
            return -1

    avgSumAListToIndex = sumAListToIndex/upperLimit
    logging.debug("\n\nSum elements 0-%d in array %s  is  %d.\nThe float average is %f.\nThe int value is %d.\nThe rounded int value is %d\n", toIndex, str(aList), sumAListToIndex, avgSumAListToIndex, avgSumAListToIndex, int(round(avgSumAListToIndex)))

    return int(round(avgSumAListToIndex)) # Task condition "I would like the function to always return an integer". Ans rounded 1st

if __name__ == "__main__": # Are we in the main program
    # Tests 
    print ('averageTo ([1,2,3,4, 18, 10], 4 )')
    x = averageTo ([1,2,3,4, 18, 10], 4 )           # Perfect situation
    print (x)

    print ('averageTo ([1,2,3,-44, 18, 10], -4 )')  # toIndex -4 equates to toIndex 2
    x = averageTo ([1,2,3,-44, 18, 10], -4 )        # toIndex -4 equates to toIndex 2
    print (x)

    print ('averageTo ([1,2,3,-44, 18, 10], -6 )')  # toIndex -6 equates to toIndex 0 
    x = averageTo ([1,2,3,-44, 18, 10], -6 )        # toIndex -6 equates to toIndex 0 
    print (x)

    print ('averageTo ([1,2,3,-44, 18, 10], -6 )')  # toIndex -7 is in invalid index number
    x = averageTo ([1,2,3,-44, 18, 10], -6 )        # toIndex -7 is in invalid index number
    print (x)

    print ('averageTo ([1,2,3,-44, 18, 10], -6 )')  # toIndex -7 is in invalid index number
    x = averageTo ([1,2,3,-44, 18, 10], -6 )        # toIndex -7 is in invalid index number
    print (x)

    print ('averageTo ([1,2,3,-44, 18, 10], 4 )')   # Negative numbers in the list do not cause a problem 
    x = averageTo ([1,2,3,-44, 18, 10], 4 )         # Negative numbers in the list do not cause a problem 
    print (x)

    print ('averageTo ([1,-1], 1 )')                # It's ok if our list values add to 0 
    x = averageTo ([1,-1], 1 )                      # It's ok if our list values add to 0 
    print (x)

    print ('averageTo ([1], 0) ')                   # This is fine it will be 1/1
    x = averageTo ([1], 0)                          # This is fine it will be 1/1
    print (x)

    print ('averageTo ([1,2,3,4], 4)')              # toIndex out of bounds
    x = averageTo ([1,2,3,4], 4)                    # toIndex out of bounds
    print (x)

    print ('averageTo ([1,2,3,4, 9, 10, 15], -2)')  # toIndex out of bounds
    x = averageTo ([1,2,3,4, 9, 10, 15], -2)        # toIndex out of bounds
    print (x)

    print ('averageTo ([1,2,3,4], 2.5)')            # toIndex must be an int  
    x = averageTo ([1,2,3,4], 2.5)                  # toIndex must be an int  
    print (x)

    print('averageTo ([1,2,3,4], 3.0)')             # toIndex must be an int. 3.0 will be interpreted as 3
    x = averageTo ([1,2,3,4], 3.0)                  # toIndex must be an int. 3.0 will be interpreted as 3
    print (x)

  #  x = averageTo ([1,2,3,4], 'a')                 # toIndex must be an int 

    print('averageTo ([], 1)')                      # aList may not be empty
    x = averageTo ([], 1)                           # aList may not be empty
    print (x)

    print("averageTo ([1, 'b',2], 2)" )             # aList values must be numbers
    x = averageTo ([1, 'b',2], 2)                   # aList values must be numbers
    print (x)

    print ("averageTo ([1,2,3,4], [])")             # toIndex must be an int  Empty List invalid 
    x = averageTo ([1,2,3,4], [])                   # toIndex must be an int  Empty List invalid 
    print (x)

    print ("averageTo (3, 0)")                      # What if a single value is passed for aList  - an int
    x = averageTo (3, 0)                            # What if a single value is passed for aList  - an int
    print (x)

    print ("averageTo (3.5, 0)")                    # What if a single value is passed for aList  - a float - becomes list, averages, returns int
    x = averageTo (3.5, 0)                          # What if a single value is passed for aList  - a float - becomes list, averages, returns int
    print (x)

    print ("averageTo ('*', 1)")                    # Function expects a list as first parametere
    x = averageTo ('*', 1)                          # Function expects a list as first parametere
    print (x)

#   x = averageTo ()                         # Function requires two args. Python TypeError
#   x = averageTo ([1,2,3,4], a)              # toIndex must be an int  NOT WORKING YET
#   x = averageTo (a, 1)                      #  NameError - Not nicely dealt with yet 
