 
## **Section 2: Tidy Data**

| function | Description |
| --- | --- |
| pd.isnull() | Checks for null Values, Returns Boolean Arrray
| df.dropna() | Drop all rows that contain null values
| df.dropna(axis=1) | Drop all columns that contain null values
| df.dropna(axis=1,thresh=n) | Drop all rows have have less than n non null values
| df.fillna(x) | Replace all null values with x
| s.fillna(s.mean()) | Replace all null values with the mean (mean can be replaced with almost any function from the statistics module)
| s.replace(1,'one') | Replace all values equal to 1 with 'one'
| s.replace([1,3],['one','three']) | Replace all 1 with 'one' and 3 with 'three'

| function | Description |
| --- | --- |
| df[df[col] > 0.5] | Rows where the column col is greater than 0.5
| df.sort_values(col1) | Sort values by col1 in ascending order
| df.groupby(col) | Returns a groupby object for values from one column
| df.pivot_table(index=col1,values=[col2,col3],aggfunc=mean) | Create a pivot table that groups by col1 and calculates the mean of col2 and col3
| df1.append(df2) | Add the rows in df1 to the end of df2 (columns should be identical)
| pd.concat([df1, df2],axis=1) | Add the columns in df1 to the end of df2 (rows should be identical)
| df1.join(df2,on=col1,how='inner') | SQL-style join the columns in df1 with the columns on df2 where the rows for col have identical values. 'how' can be one of 'left', 'right', 'outer', 'inner'
