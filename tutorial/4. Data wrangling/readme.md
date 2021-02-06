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


## **1. Data Loading, Storage, and File Formats** 
- **1.1 Data Imports** \
  Accessing data is a necessary first step for using most of the tools. Input and output typically falls into a few main categories: reading text files and other
  more efficient on-disk formats, loading data from databases, and interacting with network sources like web APIs. \
  Use these commands to import data from a variety of different sources and formats. \  
     ```python
      import pandas as pd  
      #this is comma-delimited, we can use read_csv to read it into a DataFrame.
      data = pd.read_csv('examples.csv')

      # To read this file, have a couple of options.
      # we can allow pandas to assign default column names, or you can specify names yourself:

      data = pd.read_csv('examples.csv', header=None)

      data = pd.read_csv('examples.csv', names=['a', 'b', 'c', 'd'])
      ``` 
      
 - **1.2 Writing Data to Text Format** \
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


## **2: Tidy Data**
- **2.1 Initial data screening**
  - **2.1.1 data.info()** \
  Print a concise summary of a DataFrame.
  This method prints information about a DataFrame including the index dtype and columns, non-null values and memory usage.
  ``` python 
      data.info()
  ```
  - **2.1.2 data.shape** 
  we can also get them with the shape attribute; so good to have that in the cheatsheet as well.
  ``` python 
      # number of rows and columns
      data.shape
  ```
  - **2.1.3 data.columns** \
  Some datasets may have too many columns and will not fit on the computer screen. You can check column names with columns attribute instead.
  ``` python 
      # column names
      data.columns
  ```
  - **2.1.4 data[].nunique() and .unique()** \
  For categorical variables you’ll want to know how many categories are there and also the names of those categories;
  ``` python 
      # number of unique values
      data["categorical"].nunique()
      
      # name of the unique values
      data["categorical"].unique()
  ```
  - **2.1.5 data[].value_counts()** \
   the count of rows in each category.
  ``` python 
      # count of categorical data
      data["categorical"].value_counts()
  ```
- **2.2 Handling Missing Data** \
  Missing data occurs commonly in many data analysis applications. One of the goals of pandas is to make working with missing data as painless as possible. For example, all of the descriptive statistics on pandas objects exclude missing data by default. \
  The way that missing data is represented in pandas objects is somewhat imperfect, but it is functional for a lot of users. For numeric data, pandas uses the floating-point value NaN (Not a Number) to represent missing data. We call this a sentinel value that can be easily detected:
  
  Checks for null Values, Returns Boolean Arrray
  ```python
    # show NaN values per feature
    data.isnull().sum()
   ```
  - **2.2.1 Filtering Out Missing Data** \
  There are a few ways to filter out missing data. While you always have the option to do it by hand using pandas.isnull and boolean indexing, the dropna can be helpful.
  ```python
    ## Drop row/column ##

    # drop all rows containing null
    data.dropna()
    
    # drop all columns containing null
    data.dropna(axis=1)
    
    # drop columns with less than 5 NaN values
    data.dropna(axis=1, thresh=5)
   ```
  - **2.2.2 Filling In Missing Data** \
  Rather than filtering out missing data (and potentially discarding other data along with it), you may want to fill in the “holes” in any number of ways. For most purposes, the fillna method is the workhorse function to use. Calling fillna with a constant replaces missing values with that value:
  ```python
    ## Filling values ##

    # Filling all na values with -9999
    df.fillna(-9999)

    # fill na values with NaN
    df.fillna(np.NaN) 
   ``` 
- **2.3 Data Transformation** \
We’ve been concerned with rearranging data. Filtering, cleaning, and other transformations are another class of important operations.

  - **2.3.1 Removing Duplicates** \
    Duplicate rows may be found in a DataFrame for any number of reasons. \
    The DataFrame method duplicated returns a boolean Series indicating whether each row is a duplicate (has been observed in a previous row) or not:row is a duplicate (has been observed in a previous row) or not:
     ```python
    data.duplicated()
    ```

     Relatedly, drop_duplicates returns a DataFrame where the duplicated array is False 
     ```python
      data.drop_duplicates()
     ```
     Both of these methods by default consider all of the columns; alternatively, you can specify any subset of them to detect duplicates. Suppose we had an additional column of values and wanted to filter duplicates only based on the 'k1' column:
     ```python
     data.drop_duplicates(['k1'])
     ```
     duplicated and drop_duplicates by default keep the first observed value combination. Passing keep='last' will return the last one:
       ```python
       data.drop_duplicates(['k1', 'k2'], keep='last')
       ```
   - **2.3.2 Transforming Data Using a Function or Mapping** \
     For many datasets, you may wish to perform some transformation based on the values in an array, Series, or column in a DataFrame.
     ```python
     data.map(next_data)
     ```
      ![image](https://user-images.githubusercontent.com/58425689/107121672-db28f680-68bb-11eb-9055-4769db8cf995.png)
      ![image](https://user-images.githubusercontent.com/58425689/107121719-14616680-68bc-11eb-8e48-d5be4837f104.png)

   - **Replacing Values** \
     Filling in missing data with the fillna method is a special case of more general value replacement. As you’ve already seen, map can be used to modify a subset of values in an object but replace provides a simpler and more flexible way to do so.
     ```python
     data.replace(-999, np.nan)
     ```

   - **2.3.3 Discretization and Binning** \
     Continuous data is often discretized or otherwise separated into “bins” for analysis. \
     ```python
     # Bin values into discrete intervals.
     bins_data = pd.cut(data, bins)

     # bin counts for the result of pandas.cut 
     pd.value_counts(bins_data)
     ```
      ![image](https://user-images.githubusercontent.com/58425689/107122187-3f4cba00-68be-11eb-8588-9832c4d42079.png)       


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
