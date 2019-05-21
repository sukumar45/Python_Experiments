import pandas as pd

#df = pd.read_fwf('Log_May182019_061448.txt') read_fwf is a fixed width format delimiter
df1=pd.read_csv("Log_May182019_061448.txt",delimiter="\t") #use the appropriate delimeter

df1.to_csv('Log_May182019_061448.csv', header = ['time', 'data_len', 'type', 'format', 'ID:HEX', 'ID:DEC', 'Data', 'Latitude', 'Longitude'])