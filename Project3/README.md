
# May Employee Activity Log
project members: Jim Chen

The goal of this project is to be able to parse a user log file and generate insights.
The primary focus of these insights are irregular and suspicious behaviors for the purpose
of user accountability and overseeing system errors.

The flow of approach would be to first have each user's information parsed into a dictionary.
This dictionary is then passed into various functions returning information containing a
specific insight. Each of these insights are then passed into a function where they are
formatted and written to various created report files. 
