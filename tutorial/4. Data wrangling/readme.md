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

## Data Meant to Be Read by Machines
Data can be stored in many different formats and file types. Some formats store data in a way easily handled by machines, while others store data in a way meant to be easily readable by a human. Microsoft Word documents are an example of the latter, while CSV, JSON, and XML are examples of the former.

- **CSV Data**
  The first machine-readable file type we will learn about is CSV. CSV files, or CSVs for short, are files that separate data columns with commas. The files themselves have a .csv extension. Another type of data, called tab-separated values (TSV) data, sometimes gets classified with CSVs. TSVs differ only in that they separate data columns with tabs and not commas. The files themselves usually have a .tsv extension, but sometimes have a .csv extension. Essentially, .tsv and .csv files will act the same in Python. \
  
  ``` python
  import csv
  csvfile = open('data-text.csv', 'rb')
  reader = csv.csv.reader(csvfile)
  ```
  ![image](https://user-images.githubusercontent.com/58425689/106841666-a7d34580-66ca-11eb-8672-1a85f2049ab8.png)

- **JSON Data**
  JSON data is one of the most commonly used formats for data transfers. It is preferred, because it is clean, easy to read, and easy to parse. It is also one of the most popular data formats that websites use when transmitting data to the JavaScript on the page. \
![image](https://user-images.githubusercontent.com/58425689/106841915-25975100-66cb-11eb-984a-1e63412a9b09.png) \
  ``` python
  import json
  json_data = open('data-text.json').read()
  data = json.loads(json_data)
  ```

- **XML Data**
  XML is often formatted to be both human and machine readable. However, the CSV and JSON examples were a lot easier to preview and understand than the XML file for this dataset. \
  ![image](https://user-images.githubusercontent.com/58425689/106842134-83c43400-66cb-11eb-9e96-19308756d4db.png)

## Working with Excel Files

- **Installing Python Packages**
  pip install xlrd


  
  
  
