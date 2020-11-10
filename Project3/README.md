
# May Employee Activity Log
project members: Jim Chen

The goal of this project is to be able to parse a user log file and generate insights.
The primary focus of these insights are irregular and suspicious behaviors for the purpose
of user accountability and overseeing system errors.

The flow of approach would be to first have each user's information parsed into a dictionary.
This dictionary is then passed into various functions returning information containing a
specific insight. Each of these insights are then passed into a function where they are
formatted and written to various created report files.

The general flow is - get data -> pass data into various functions and return wanted data -> write data to files

# Notes/Updates
. A function for parsing the log file is used and the flowchart is in the flow chart.

. The length of the value of each date key from the returned dictionaries in each behavior report function
gives the quantity of issues for that day.

. Instead of having users as key values it seems to be easier to handle the data if each
date was a key value for the main dictionary.

. Commonly using triple for loop pattern. Probably inneficient. Due to time constraints, I just rolled with it.
Maybe in the future to better plan out data structures, methods for handling the data.

. The write_report function was a hassle. It did not pan out as expected from the flow chart.Since my
data was sorted by date, and the specification was by members then date, my solution was to create a dictionary containing users  with a list of strings
that followed the specification and joined them in writing to the file report. Similar troubles in getting the day problem day couts for a user
so I used the same dictionary concept. Updated write_report flowchart.

. Another error I ran into was an improper if statement placement. It placed all users and their session in a problem dictionary.
It took me little bit of time to figure it out and move it out of the for loop.

. A slight annoyance was the formatting for the unique domains report. The count for each domain wasn't justified in the text.
I used rjust() to right align the counts.

# Additional Insights
Normal Behavior Function - Tests to see if at least 1 of the users exhibits normal behavior. Normal behavior
meaning that a user is not part of system glitch, irresponsible behavior, or suspicious activities. The flowchart
and report file are in their resspective folders.
