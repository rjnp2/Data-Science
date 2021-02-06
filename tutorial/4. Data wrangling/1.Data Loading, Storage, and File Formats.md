## **1. Data Loading, Storage, and File Formats** 
- **1.1 Data Imports** \
    Accessing data is a necessary first step for using most of the tools. Input and output typically falls into a few main categories: reading text files and other more efficient on-disk formats, loading data from databases, and interacting with network sources like web APIs. \
    Use these commands to import data from a variety of different sources and formats. 
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
  ---
  ---
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
  
  ---
  ---
