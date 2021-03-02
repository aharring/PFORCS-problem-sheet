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
#       2. Read the file. Pattern match 
#       3. Place the matches in a list
#       
#       Notes : Work in progress
#
#       What I learned :
#	References :
#           W3Schools Regular Expressions
#           RealPython Regular Expressions
#	    Assigned labs for week 7 
#
import re
import os

filename = "200linesaccess.log"


def extractURLs(inputFile) :

    regex = "\s/\S+"
    urlList = []

    # Open the file
    with open(inputFile, "rt") as file :
        for line in file:
            listMatchesInLine = re.findall(regex, line)
            if (len(listMatchesInLine)!= 0):
                firstMatchInLine = listMatchesInLine[0]
                urlList.append(firstMatchInLine[1:]) # Remove the leading space from the url. Append url to urlList
     
    return urlList # return urlList for further processing

def extractDictEntriesFromURLList (urlList) :

    regexResource = "[^/]\S+\?"
    regexParameterAction = "action\=\w+"
    regexParameterItemId = "itemId\=\w+-\w+"
    regexParameterProductId = "productId\=\w+-\w+-\w+"
    regexParameterSessionId = "JSESSIONID\=\S+"

    listUrlsStoredAsDicts = [] # Empty List
    url = {                    # Each Url Dict is composed of a string and another dict
        'resource': "",
        'parameters': {
            'action': "",
            'itemId': "",
            'productId': "",
            'JSESSIONID': ""
        } 
    }         
    i = 0 # Index counter

    for urlDetails in urlList :
        if urlDetails.find('action') != -1 : # This row contains the data requested
            #print(urlDetails)
            resourceList = re.findall(regexResource, urlDetails) 
            resourcename = resourceList [0]        # The result of the regex comes back in an array. We need the first entry
            resourcename = resourcename[:-1]       # Strip the ?
            url['resource'] = resourcename

            resourceList = re.findall(regexParameterAction, urlDetails)
            resourcename = resourceList[0]
            resourcename = resourcename[7:]
            url["parameters"]["action"]  = resourcename

            resourceList = re.findall(regexParameterItemId, urlDetails)
            resourcename = resourceList[0]
            resourcename = resourcename[7:]
            url["parameters"]["itemId"]  = resourcename

            resourceList = re.findall(regexParameterProductId, urlDetails)
            if resourceList != []:
                resourcename = resourceList[0]
                resourcename = resourcename[10:]
            else :
                resourcename = "Product Name Unavailable"
            url["parameters"]["productId"]  = resourcename

            resourceList = re.findall(regexParameterSessionId, urlDetails)
            resourcename = resourceList[0]
            resourcename = resourcename[11:]
            url["parameters"]["JSESSIONID"]  = resourcename

            #print(url["parameters"]["JSESSIONID"])
            #print(url["parameters"]["productId"])
            #print(url["parameters"]["itemId"])
            #print(url["parameters"]["action"])
            #print(url['resource'])
            listUrlsStoredAsDicts.append(url)
            i += 1
        print (listUrlsStoredAsDicts)


if os.path.exists(filename):
    urlList = extractURLs(filename)
    extractDictEntriesFromURLList (urlList)
else :
    print ("\nError : File does not exist")



