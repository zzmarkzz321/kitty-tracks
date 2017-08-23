# Parse entire file of bus schedule and make appropiate documents 
# Read a txt file containing text of schedule
# Read line by line
    # delimit by ' ' (space)
    # for each index in array
        # if index type is not a number
            # stop_name += index + " "
        # else append time to array c
import re 

f = open('AB Line Fall 2017')

jsonD = {
    'line': 'fastcat',
    'availability': 'Mon-Fri',
    'stops': {}
}

stop = ""
stops = {}
times = []
toggle = False
for line in f:
    line = re.split(' ', line)
    for i in line:
        if toggle == False:
            stop += i + " "
        else:
            times.append(i)
        
        if i == '|':
            toggle = True

    # create the json
    stops[stop] = times
    # reset everything
    stop = ""
    toggle = False
    times = []

jsonD['stops'] = stops
f.close()

file = open("ab","w") 
file.writelines(str(jsonD))
file.close() 