#  Data visualization
Data visualization is actually a set of data points and information that are represented graphically to make it easy and quick for user to understand. Data visualization is good if it has a clear meaning, purpose, and is very easy to interpret, without requiring context. Tools of data visualization provide an accessible way to see and understand trends, outliers, and patterns in data by using visual effects or elements such as a chart, graphs, and maps.

# Categories of Data Visualization 
![image](https://user-images.githubusercontent.com/58425689/107495356-14ad7a80-6bb8-11eb-888c-1742a3def59d.png)
___
1. **Numerical Data** \
  Numerical data is also known as Quantitative data. Numerical data is any data where data generally represents amount such as height, weight, age of a person, etc. Numerical data visualization is easiest way to visualize data. It is generally used for helping others to digest large data sets and raw numbers in a way that makes it easier to interpret into action. \
  Numerical data is categorized into two categories :
    - **Continuous Data** \
      It can be narrowed or categorized (Example: Height measurements). 
    - **Discrete Data** \
      This type of data is not “continuous” (Example: Number of cars or children’s a household has). \

The type of visualization techniques that are used to represent numerical data visualization is Charts and Numerical Values. Examples are Pie Charts, Bar Charts, Averages, Scorecards, etc.
___
2. **Categorical Data** \
  Categorical data is also known as Qualitative data. Categorical data is any data where data generally represents groups. It simply consists of categorical variables that are used to represent characteristics such as a person’s ranking, a person’s gender, etc. Categorical data visualization is all about depicting key themes, establishing connections, and lending context. \
  Categorical data is classified into three categories :
    - **Binary Data** \
      In this, classification is based on positioning (Example: Agrees or Disagrees).
    - **Nominal Data** \
      In this, classification is based on attributes (Example: Male or Female).
    - **Ordinal Data** |
      In this, classification is based on ordering of information (Example: Timeline or processes).
___

# Most Common Graph Types
## 1. Bar Chart

Use a bar chart for the following reasons:
- You want to compare two or more values in the same category
- You want to compare parts of a whole
- You don’t have too many groups (less than 10 works best)
- You want to understand how multiple similar data sets relate to each other
- Don’t use a bar chart for the following reasons:

The category you’re visualizing only has one value associated with it
- You want to visualize continuous data

## 2. Line Chart

Use a line chart for the following reasons:
- You want to understand trends, patterns, and fluctuations in your data
- You want to compare different yet related data sets with multiple series
- You want to make projections beyond your data

Don’t use a line chart for the following reason:
- You want to demonstrate an in-depth view of your data

## 3. Scatterplot
Use a scatterplot for the following reasons:
- You want to show the relationship between two variables
- You want a compact data visualization

Don’t use a scatterplot for the following reasons:
- You want to rapidly scan information
- You want clear and precise data points

## 4. Pie Chart
Use a pie chart for the following reasons:
- You want to compare relative values
- You want to compare parts of a whole
- You want to rapidly scan metrics

Don’t use a pie chart for the following reason:
- You want to precisely compare data

## 5. Heat Map
Use a heat map for the following reasons:
- To show a relationship between two measures
- To illustrate an important detail
- To use a rating system

Don’t use a heat map for the following reason:
- To visualize individual, unconnected metrics

## 6. Box Plot
Use a box plot for the following reasons:
- To display or compare a distribution of data
- To identify the minimum, maximum and median of data

Don’t use a box plot for the following reason:
- To visualize individual, unconnected data sets

# Importing the library
import matplotlib.pyplot as plt

# Plots and key arguments

| plot | codes | argument|
| --- |--- | --- |
| Line graph| plt.plot() | (x_data, y_data) |
Scatter plot |plt.scatter() |(x_data, y_data)
Bar chart |plt.bar()|(x_locs, bar_heights, width = int)
Histogram |plt.hist()|(data, bins = int)
Pie chart|plt.pie() |(data, labels = list)

# Optional arguments
| argument | descriptions|
|---|---|
color ="color" | Change plot color
marker = "symbol" | Change marker for line or scatter plot (".", "x", "\|", "o") |
markersize = int |Change marker size
linewidth = int |Change line width for line graph
cmap = colormap|Color plot according to a colormap

# Key functions
|function|descriptions|
|-|-|
plt.clf()|Clear figure
plt.savefig("filename")|Save figure (call before plt.sh­ow())
plt.show()|Show figure

# Axis functions
|function|descriptions|
|-|-|
plt.xlim(xmin, xmax)|Set the limits for the x axis
plt.ylim(ymin, ymax)|Set the limits for the y axis
plt.xscale("scale type")|Set scale for the x axis (ex. "log")
plt.yscale("scale type")|Set scale for the y axis (ex. "log")
plt.twinx()|Add a second y axis
plt.axis("off")|Do not show the axes
plt.gca().invert_ xaxis()|Invert the x axis
plt.gca().invert_ yaxis()|Invert the y axis
 	
# Labeling functions
|function|descriptions|
|-|-|
plt.title("title")|Add a title
plt.xlabel("x axis label")|Add a label to the x axis
plt.ylabel("y axis label")|Add a label to the y axis
plt.legend(loc = int)|Add a legend
plt.xticks(range(min, max, interval)|Modify the x axis tick marks

# Multiple plots
plt.plot(x_data1, y_data1) \
plt.plot(x_data2, y_data2) \
plt.plot(x_data3, y_data3)

plt.show()

# Using colormaps
\# Choose a colormap and assign to a variable\
cm = plt.cm.get_cmap("RdYlBu")

\# Set the color map in a plot\
plt.scatter(x_data, y_data, cmap=cm)

