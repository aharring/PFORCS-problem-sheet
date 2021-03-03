# GMIT CyberSecurity : Programming for CyberSecurity, Python
# Lecturer : Andrew Beatty
# Problem Sheet Week 7  
#
# Task Requirement :
#      Write a program called extract-url.py, that will extract the URLs from an access.log file.
# Program Name : extract-url.py 
#
# Program Function : 
#       1. If the file exists open it 
#       2. Open the file. 
#          a. For each line in the file extract the portion of the line corresponding to the url
#          e.g. '/cart.do?action=view&itemId=EST-6&productId=SC-MG-G10&JSESSIONID=SD5SL9FF2ADFF4958' 
#       3. Place the matches in a list
#              a. This is contained in the function extractURLs
#
#       4. For each url in the list split it in to it's component parts which should be stored as a dict
#
#          e.g.
#          [ 
#             {
#               'resource':'cart.do', 
#               'parameters':{
#                   'action':'view',
#                   'itemId':'EST-6',
#                   'productId':'SC-MG-G10'
#                   'JSESSIONID':'SD5SL9FF2ADFF4958'
#               }
#             },
#             #next dictionary object
#          ]
#             a. This is contained in the function extractDictEntriesFromURLList  
#
#        5. Print the results neatly
#             a. This is contained in the function printResults
#
#            
#       
#       Notes : I first return the list of URLs and then process that list to a second list of dicts.
#               This is to show the two distinct pieces of work 
#               In my original lognger file I noted sometimes there was an action but no product. 
#               I tried to accomodate this by putting 'Unavailable' in these situations
#               While my url List pulls out all urls my dict only pulls out entries that appeared to match
#               the sample output, i.e. rows that had 'action'. 
#
#       What I learned : I require a lot of practice on Regex
#
#	References :
#           python.org
#           W3Schools Regular Expressions
#           RealPython Regular Expressions
#	    Assigned labs for week 7 
#
import re
import os

filename = "shortlog.log" 

def extractURLs(inputFile) :

    regex = "(?<=\s)/\\S+" # Everything after the first ' /' upto the next non S which is a space
    urlList = []

    # Open the file
    with open(inputFile, "rt") as file :
        for line in file:
            listMatchesInLine = re.findall(regex, line)
            if (len(listMatchesInLine)!= 0):         # Assuming we got a result
                firstMatchInLine = listMatchesInLine[0]
                urlList.append(firstMatchInLine[1:]) # Remove the leading space from the url. Append url to urlList

    return urlList # return urlList for further processing

def extractDictEntriesFromURLList (urlList) :

    regexResource = "\S+(?=\?)"  # Will match a string if it's followed by ? which corresponds to the resource
    regexParameters = "(?<=\=)\w+-*\w+-*\w+"  # Many failed regex attempts later  

    listUrlsStoredAsDicts = []   # Empty List
    url = {}                     # Empty Dict
             
    for urlDetails in urlList :
        if urlDetails.find('action') != -1 :   # This row contains the data requested
            resource = re.findall(regexResource, urlDetails) 
            resourceName = resource [0]        # The result of the regex comes back in an array. We need the first entry
            url['resource'] = resourceName            

            parameterList = re.findall(regexParameters, urlDetails) # Array contains action, item, product & session
            url['action'] = parameterList[0]
            url['itemId'] = parameterList[1]

            if len(parameterList) > 3 :
                url['productId'] = parameterList[2]
                url['JSESSIONID'] = parameterList[3]
            else :
                url['productId'] = "Unavailable"
                url['JSESSIONID'] = parameterList[2]

            listUrlsStoredAsDicts.append(url)
    
    return listUrlsStoredAsDicts

def printResults(urlList, listUrlsStoredAsDicts) :

    print ("\nURL List \n")
    for url in urlList :
       print (url)

    for url in listUrlsStoredAsDicts :
        print ("\nResource :{}\n\n\tAction : {}\n\tItemID :{}\n\tProductID :{}\n\tJSessionID :{}". format(url['resource'], url['action'], url['itemId'], url['productId'], url['JSESSIONID']))

# Main Program

if os.path.exists(filename):
    urlList = extractURLs(filename)
    listUrlsStoredAsDicts = extractDictEntriesFromURLList (urlList)
    printResults(urlList, listUrlsStoredAsDicts)
else :
    print ("\nError : File does not exist")

