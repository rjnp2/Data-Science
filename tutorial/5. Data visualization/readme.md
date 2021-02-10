#  Data visualization
Data visualization is actually a set of data points and information that are represented graphically to make it easy and quick for user to understand. Data visualization is good if it has a clear meaning, purpose, and is very easy to interpret, without requiring context. Tools of data visualization provide an accessible way to see and understand trends, outliers, and patterns in data by using visual effects or elements such as a chart, graphs, and maps.

# Categories of Data Visualization 
![image](https://user-images.githubusercontent.com/58425689/107495356-14ad7a80-6bb8-11eb-888c-1742a3def59d.png)

1. **Numerical Data** \
  Numerical data is also known as Quantitative data. Numerical data is any data where data generally represents amount such as height, weight, age of a person, etc. Numerical data visualization is easiest way to visualize data. It is generally used for helping others to digest large data sets and raw numbers in a way that makes it easier to interpret into action. Numerical data is categorized into two categories :
    - **Continuous Data** \
      It can be narrowed or categorized (Example: Height measurements). 
    - **Discrete Data** \
      This type of data is not “continuous” (Example: Number of cars or children’s a household has). \

The type of visualization techniques that are used to represent numerical data visualization is Charts and Numerical Values. Examples are Pie Charts, Bar Charts, Averages, Scorecards, etc.

2. **Categorical Data** \
Categorical data is also known as Qualitative data. Categorical data is any data where data generally represents groups. It simply consists of categorical variables that are used to represent characteristics such as a person’s ranking, a person’s gender, etc. Categorical data visualization is all about depicting key themes, establishing connections, and lending context. Categorical data is classified into three categories :
    - **Binary Data** \
      In this, classification is based on positioning (Example: Agrees or Disagrees).
    - **Nominal Data** \
      In this, classification is based on attributes (Example: Male or Female).
    - **Ordinal Data** |
      In this, classification is based on ordering of information (Example: Timeline or processes).



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

