---
# What Is Data Wrangling?
Data wrangling is the process of gathering, selecting, and transforming data to answer an analytical question. Also known as data cleaning or “munging”, legend has it that this wrangling costs analytics professionals as much as 80% of their time, leaving only 20% for exploration and modeling. \
![image](https://user-images.githubusercontent.com/58425689/106841812-e79a2d00-66ca-11eb-95c2-3bebe6ffc3f0.png)

## Course overview 
- [**Section 1: Data Import**](https://github.com/rjnp2/Data-Science/blob/main/tutorial/4.%20Data%20wrangling/1.Data%20Loading,%20Storage,%20and%20File%20Formats.md) \
  learn how to import data from different sources.

- [**Section 2: Tidy Data**](https://github.com/rjnp2/Data-Science/blob/main/tutorial/4.%20Data%20wrangling/2.%20Tidy%20Data.md) \
  learn the first pieces of converting data into a tidy format.

- **[Section 3: String Processing**](https://github.com/rjnp2/Data-Science/blob/main/tutorial/4.%20Data%20wrangling/3.%20String%20Processing.md) \
  learn how to process strings using regular expressions (regex).

- **Section 4: Join, Combine,and Reshape** \
  learn how to combine, join, and rearrange data.

- **Section 5: Dates, Times, and Text Mining** \
  learn how to work with dates and times as file formats and how to mine text.
---
---

| function | Description |
| --- | --- |
| df[df[col] > 0.5] | Rows where the column col is greater than 0.5
| df.sort_values(col1) | Sort values by col1 in ascending order
| df.groupby(col) | Returns a groupby object for values from one column
| df.pivot_table(index=col1,values=[col2,col3],aggfunc=mean) | Create a pivot table that groups by col1 and calculates the mean of col2 and col3
| df1.append(df2) | Add the rows in df1 to the end of df2 (columns should be identical)
| pd.concat([df1, df2],axis=1) | Add the columns in df1 to the end of df2 (rows should be identical)
| df1.join(df2,on=col1,how='inner') | SQL-style join the columns in df1 with the columns on df2 where the rows for col have identical values. 'how' can be one of 'left', 'right', 'outer', 'inner'
