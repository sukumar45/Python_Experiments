'''import csv

with open('Log_May182019_061448.txt', 'r') as in_file:
	print (type(in_file))
	stripped = (line.strip() for line in in_file)
	print (type(stripped))
	lines = (line.split(" /t ") for line in stripped if line)
	print (type(lines))
	with open('Log_May182019_061448.csv', 'w') as out_file:
		writer = csv.writer(out_file)
		writer.writerow(('time', 'data_len', 'type', 'format', 'ID:HEX', 'ID:DEC', 'Data', 'Latitude', 'Longitude'))
		writer.writerows(lines)
'''

# use the above code snip if you need column headers

import pandas as pd
#df = pd.read_fwf('Log_May182019_061448.txt') read_fwf is a fixed width format delimiter
df1=pd.read_csv("Log_May182019_061448.txt",delimiter="\t") #use the appropriate delimeter

df1.to_csv('Log_May182019_061448.csv')