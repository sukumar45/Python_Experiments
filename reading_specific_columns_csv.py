import pandas as pd

#use specic column names
df = pd.read_csv('Log_May182019_061448.csv', usecols = ['Latitude','Longitude'])

#you can specify new column names while writing to a new file
df.to_csv('Log_May182019_061448_stripped.csv', header = ['Latitude', 'Longitude']) 