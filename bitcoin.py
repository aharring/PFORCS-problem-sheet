# GMIT CyberSecurity : Programming for CyberSecurity, Python
# Lecturer : Andrew Beatty
# Problem Sheet Week 3  
#
# Task Requirement :
# 	1. Write a program (bitcoin.py) that outputs the current bitcoin price in US
# 	Dollars. Use the supplied code snippet to get a Dict object that contains
#	the price.
#	2. Extra output all the price in the three currencies, in a neat way
#
# Program Name : bitcoin.py
#
# Prerequisites  : Executed 'pip install requests' on the command line to install the request module
#
# Program Function : bitcoin.py outputs the current bitcoin price in USD, GBP and Euro
#
# Steps in completing this program
#	1. I first executed the program as provided in the problem sheet. I of course got an error bc I forgot to import requests
#	2. With requests imported, I ran the program and printed the contents of bitCoinDict
#	3. The output was very messy so I went to the coindesk website and tried to find a defined format for the output. It was all equally messy
#	4. I then googled 'format for json files' and I came across something called jq which was defined as the 'sed' for json
#	5. I did some more reading and found jq would format json. I installed jq using brew install jq on the command line
#          I then executed the command 'cat - | jq . ' with the json text that it formatted the json structure in to 
#		a more readable format. I've copied the command and output here for reference
# 	PFORCS-problem-sheet adeleharrington$ cat - | jq .
#	{"time":{"updated":"Sep 18, 2013 17:27:00 UTC","updatedISO":"2013-09-18T17:27:00+00:00"},"disclaimer":"This data was produced from the CoinDesk #	Bitcoin Price Index. Non-USD currency data converted using hourly conversion rate from openexchangerates.org","bpi":{"USD":{"code":"USD","symbol#	":"$","rate":"126.5235","description":"United States Dollar","rate_float":126.5235},"GBP":{"code":"GBP","symbol":"£","rate":"79.2495","descripti#	on":"British Pound Sterling","rate_float":79.2495},"EUR":{"code":"EUR","symbol":"€","rate":"94.7398","description":"Euro","rate_float":94.739}}}
#	
#	The output was a much clearer view of the json strucucture and it showed that it wasn't a simple dict strucure but a nested one
#	containing a dict labelled time, a string variable labelled disclaimer and a second dict called bpi 
#
#{
#	  "time": {
#	    "updated": "Sep 18, 2013 17:27:00 UTC",
#	    "updatedISO": "2013-09-18T17:27:00+00:00"
#	  },
#	  "disclaimer": "Produced from CoinDesk Bitcoin Price Index. Non-USD data converted using hourly conversion rate from openexchangerates.org",
#	  "bpi": {
#	    "USD": {
#	      "code": "USD",
#	      "symbol": "$",
#	      "rate": "126.5235",
#	      "description": "United States Dollar",
#	      "rate_float": 126.5235
#	    },
#	    "GBP": {
#	      "code": "GBP",
#	      "symbol": "£",
#	      "rate": "79.2495",
#	      "description": "British Pound Sterling",
#	      "rate_float": 79.2495
#	    },
#	    "EUR": {
#	      "code": "EUR",
#	      "symbol": "€",
#	      "rate": "94.7398",
#	      "description": "Euro",
#	      "rate_float": 94.7398
#	    }
#	  }
#	}
#
#
#	Once I had this information I took an intermediate step adding the line bpi = bitCoinDict["bpi"] to help me figure out how to access
#	the bpi elements but once I saw I could reference bpi["USD"]["rate"] I realised bitCoinDict["bpi"]["USD"]["rate"] was likely to work so I tested
#	it and it did so I removed my earlier bpi variable
#
#	Notes : I understood "rate" to mean current price
#		I originally was printing the 'symbol' associated with a given dict entry but it didn't seem to print the euro sign correctly
#		So I just put '€' in front of the rate instead of calling format on the dict entry	
#		I had to revisit how to use positional formatting in a print statement
#		I have since realised that VSCode will also show a Json file format but I tend to write my programs on the cmdline using vi
#		The research around using jq to format a json file was worthwhile
#
#	References :
#		W3Schools
#		StackOverflow
#		RealPython (positional formatting in a print statment, multiple args)
#

import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json" # Supplied by lecturer

returnedData = requests.get(url) # Supplied by lecturer
bitCoinDict = returnedData.json() # Supplied by lecturer - places json data in a dict

# Print Newline followed by "Bitcoin is currently priced at : 
# newline, newline, tab $ bpi dict usd rate newline tab bpi dict euro rate newline tab bpi dict gbp rate
print("\nBitCoin is currently priced at : \n\n\t${0}\n\t€{1}\n\t£{2}\n" .format(bitCoinDict["bpi"]["USD"] ["rate"], bitCoinDict["bpi"]["EUR"]["rate"], bitCoinDict["bpi"]["GBP"]["rate"]))

# Split disclaimer indicating datasource so it can be printed neatly over 2 lines
# "disclaimer": "Produced from CoinDesk Bitcoin Price Index. Non-USD data converted using hourly conversion rate from openexchangerates.org",

disclaimer = bitCoinDict["disclaimer"].split(".") # The split function gives me an array of two strings

# Print source information (disclaimer). Print Line 1. NewLine. Print Line 2 with leading space stripped
print(disclaimer[0] + "\n" + disclaimer[1].lstrip() + "\n") 
