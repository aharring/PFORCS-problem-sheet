# GMIT CyberSecurity : Programming for CyberSecurity, Python
# Lecturer : Andrew Beatty
# Problem Sheet Week 9 - Pandas  
#
# Task Requirement : 
#      Read access.log in to a panda dataframe. 
#      Set the time field to be the index. 
#      Use Regex to extract the SessionId from the URL & store the result in a different column
#      Use groupBy to get the sum of all the data downloaded by each sessionId.
#      Plot the result
#
# Program Name : maxData.py 
#
# Program Function : 
#      1. Read the sample log in to a panda dataframe (The program assumes the log file is in the current directory)
#      2. Use regex expression to extract the SessionId from the URL - insert this column at position 1  
#      3. Remove unused columns to make data more readable
#      4. Strip the [] from the datetime field
#      5. Make the datetime field the index
#      6. Group the data by SessionId
#      7. Create a new dataframe sums the summable fields (Response Size) by SessionId - No breakdown by time in at this point
#      8. Use matplotlib to display a graph of the results (Set some seetings regarding font, angle of x axis data so that it is readable
#      9. Print out the data so it is possible to see the response size is indeed summed by SessionId
#     10. Sample the dataframe, this time computing the Response Size per SessionId per day
#     11. Print out this structure so that it can be compared with the previous structure to ensure the grouping/summing is correct
#
#     ToDo - use full log, output comparisons to an output file since a full log will generate a lot of output - maybe
#
#	References :
#	    Assigned lab for week 9 (Pandas)  
#           https://www.kite.com/python/answers/how-to-print-an-entire-pandas-dataframe-in-python#:~:text=Use%20pandas.,to%20be%20displayed%20when%20printed.
#           https://stackoverflow.com/questions/13682044/remove-unwanted-parts-from-strings-in-a-column
#           https://www.geeksforgeeks.org/adding-new-column-to-existing-dataframe-in-pandas/ - adding a column in a specific position in the df. 
#           https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.insert.html - using the panda insert to add a col in a specific location - further reading
#           https://matplotlib.org/stable/gallery/ticks_and_spines/ticklabels_rotation.html
#           https://stackoverflow.com/questions/56816833/pandas-pd-to-datetime-only-keep-time-do-not-date
#
import pandas as pd                # Used to import log info into a panda dataframe for ease of manipulation
import re                          # RegEx needed to extract JSESSIONID specific portion of URL
import matplotlib.pyplot as plt    # To plot data

colNames =  ('Ip',                 # Name the columns expected in the dataframe - ref : Lab by lecturer Andrew Beatty
'Dash1',
'UserId',
'Time',
'URL',
'Status Code',
'Response Size',
'Referer',
'User Agent',
'Unknown'
)


pd.set_option("display.max_rows", None, "display.max_columns", None)    # https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html

df = pd.read_csv("shortlog2.log", delim_whitespace=True, header=None, names = colNames)     # Read the logfile data in to a panda dataframe
df.insert(1, 'SessionId', df['URL'].str.extract(r'((?<=JSESSIONID=)\S+)', expand = True))   # Extract SessionID using RegEx - Insert it at the beginning 

df.drop(columns=['Dash1', 'UserId', 'Ip', 'URL', 'Status Code', 'Referer', 'User Agent','Unknown'], inplace=True)       # From the lab, remove the two columns with '-' value. Removing last column too since we don't know what it is. Also removing data that doesn't 'Sum', focussing just on response size

df['Time'] = df['Time'].map(lambda x: x.lstrip('[').rstrip(']'))    # Strip leading & trailing [] from DateTime - Stackoverflow example 
df['Time'] = pd.to_datetime(df['Time'], format='%d/%b/%Y:%H:%M:%S') # Used lab guide to convert DateTime
#df['Time'] = pd.to_datetime(df['Time'], format='%d/%b/%Y:%H:%M:%S').dt.date # Extract the date portion only - pandas.org

df = df.set_index('Time')                                           # Set the Time field to be the index
df.groupby('SessionId')                                             # This will group data for each SessionId together

pdf = df.groupby(['SessionId']).sum()                               # This will sum the total responsesize  by SessionId  
print("\nTotal Response Size per SessionId \n{}" .format(pdf))      # Total Response Size per SessionId 

pdf.plot.bar(figsize=(8, 8), fontsize=5, title = "Access Logs\nTotal Response Size By SessionID") # Plot shows Total Response Size per SessionId
plt.xticks(rotation='45')                                           # Adjust the angle of the text on the x axis so it fits

# Pad margins so that markers don't get clipped by the axes
plt.margins(0.2)
# Adjust spacing to prevent clipping of tick-labels
plt.subplots_adjust(bottom=0.15)
plt.show()

pdf = df.groupby(['SessionId']).resample(rule='D').sum()            # This will sum the responsesize per day by SessionId - so there will be a total Response per session per day
print("\nResponse Size per SessionId per day\n{}" .format(pdf))     # Response Size per day per SessionId

#Just me looking at different panda options
#print (df.iloc[0])
#print(df.describe())
#print(df.head (2))
#print(df)
#print (pdf)
#print (len(df.columns))

