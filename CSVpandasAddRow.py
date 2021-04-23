import pandas

df = pandas.read_csv('hrdata_modified.csv')

newEmployee = ['Eren Jaeger','2015-08-23',90000.00,5,'00-000-0000']

df.loc[len(df.index)+1] = newEmployee

df.to_csv('hrdata_modified.csv', index=False)