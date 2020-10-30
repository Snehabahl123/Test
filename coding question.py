import pandas as pd
df = pd.read_csv('file.csv')
#getting the columns 
columns = df.columns

#Finding duplicate values

#based on combination of all columns
#returning all the rows that is all the rows which have a duplicate along with first appearance
duplicates = df[df.duplicated(keep = False)]
#just returning duplicates that keeping/not considering the first appearance
duplicates = df[df.duplicated()]

#based on a specific column, consoidering the first column
duplicates = df[df.duplicated(columns[0])]

#based on a subset of columns, taking the subset of first and second column
duplicates = df[df.duplicated([columns[0], columns[1]])]


#Removing the duplicates

#based on combination of all columns
df.drop_duplicates(inplace=True)

#based on a specific column, consoidering the first column
df.drop_duplicates(columns[0], inplace=True)

#based on a subset of columns, taking the subset of first and second column
df.drop_duplicates([columns[0], columns[1]], inplace=True)

