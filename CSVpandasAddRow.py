import pandas

df = pandas.read_csv('hrdata_modified.csv')

newEmployee = ['Hassan Zaman','2014-07-23',61000.00,5,'00-000-0000']

df.loc[len(df.index)+1] = newEmployee

df.to_csv('hrdata_modified.csv', index=False)