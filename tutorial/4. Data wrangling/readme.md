

## **1. Data Loading, Storage, and File Formats** 

- **Data Imports** \
  Accessing data is a necessary first step for using most of the tools. Input and output typically falls into a few main categories: reading text files and other
  more efficient on-disk formats, loading data from databases, and interacting with network sources like web APIs.

  Use these commands to import data from a variety of different sources and formats.

      ```python

      import pandas as pd

      # this is comma-delimited, we can use read_csv to read it into a DataFrame:
      data = pd.read_csv('examples.csv')

      # To read this file, have a couple of options.
      # we can allow pandas to assign default column names, or you can specify names yourself:

      data = pd.read_csv('examples.csv', header=None)

      data = pd.read_csv('examples.csv', names=['a', 'b', 'c', 'd'])
      ```
 - **Writing Data to Text Format** \
   Data can also be exported to a delimited format. Let’s consider one of the CSV files. Using DataFrame’s to_csv method, we can write the data out to a comma-separated file:
  
    ``` python
    data.to_csv('examples/out.csv')
    
    ```

In Overall, 

  | function | Description |
  | --- | --- |
  pd.read_csv(filename) | From a CSV file
  pd.read_table(filename) | From a delimited text file (like TSV)
  pd.read_excel(filename) | From an Excel file
  pd.read_sql(query, connection_object) | Read from a SQL table/database
  pd.read_json(json_string) | Read from a JSON formatted string, URL or file.
  pd.read_html(url) | Parses an html URL, string or file and extracts tables to a list of dataframes
  pd.read_pickle('pickle')  | read any “pickled” object stored in a file
  pd.HDFStore('hdf.h5') | read any “HDF5 Format” object stored in a file
  
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
