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
