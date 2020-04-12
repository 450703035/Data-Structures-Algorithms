"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
text_diff_num = []
call_diff_num = []

#O(n)
for text in texts:
    #pdb.set_trace() 
    if text[0] not in text_diff_num:
        text_diff_num.append(text[0])
    if text[1] not in text_diff_num:
        text_diff_num.append(text[1])

print('There are <{}> text different telephone numbers in the records.'.format(len(text_diff_num)))

for call in calls:
    #pdb.set_trace() 
    if call[0] not in call_diff_num:
        call_diff_num.append(call[0])
    if call[1] not in call_diff_num:
        call_diff_num.append(call[1])
        
print('There are <{}> call different telephone numbers in the records.'.format(len(call_diff_num)))