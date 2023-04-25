#import dataset insurance.csv
import pandas as pd

df = pd.read_csv('insurance.csv')
#print(df)

print(df.info())
# RangeIndex: 1338 entries, 0 to 1337
# Data Columns (Total 7 Columns)
# No missing Data
# int, obt, float


#save dataset via python variables
column_names = df.columns

insurance_data = {}
for name in column_names:
    insurance_data[name] = df[name]
#print(insurance_data)

#Build out analysis functions

