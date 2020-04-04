"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import pdb

import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

time_call = {}
#O(n)
for call in calls:
    #pdb.set_trace() 
    val = int(call[3])
    if (call[0] not in time_call):
        time_call[call[0]] = val
    else:
        #pdb.set_trace() 
        time_call[call[0]] += val
    
    if (call[1] not in time_call):
        time_call[call[1]] = val
    else:
        time_call[call[1]] += val
        
mak_key = max(time_call,key=time_call.get)
        
print('{} spent the longest time, {} seconds, \
      on the phone during September 2016.'.format(mak_key, time_call[mak_key]))