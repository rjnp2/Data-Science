# What Is Data Wrangling?
Data wrangling is the process of gathering, selecting, and transforming data to answer an analytical question. Also known as data cleaning or “munging”, legend has it that this wrangling costs analytics professionals as much as 80% of their time, leaving only 20% for exploration and modeling. \
![image](https://user-images.githubusercontent.com/58425689/106841812-e79a2d00-66ca-11eb-95c2-3bebe6ffc3f0.png)

## Course overview 
- **Section 1: Data Import** \
  learn how to import data from different sources.

- **Section 2: Tidy Data** \
  learn the first pieces of converting data into a tidy format.

- **Section 3: String Processing** \
  learn how to process strings using regular expressions (regex).

- **Section 4: Dates, Times, and Text Mining** \
  learn how to work with dates and times as file formats and how to mine text.

## **Section 1: Data Import** 
Use these commands to import data from a variety of different sources and formats.

| function | Description |
| --- | --- |
pd.read_csv(filename) | From a CSV file
pd.read_table(filename) | From a delimited text file (like TSV)
pd.read_excel(filename) | From an Excel file
pd.read_sql(query, connection_object) | Read from a SQL table/database
pd.read_json(json_string) | Read from a JSON formatted string, URL or file.
pd.read_html(url) | Parses an html URL, string or file and extracts tables to a list of dataframes

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
