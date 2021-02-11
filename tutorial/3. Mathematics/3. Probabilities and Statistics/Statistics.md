# Data
Data is the collected information(observations) we have about something or facts and statistics collected together for reference or analysis.
___
  Data — a collection of facts (numbers, words, measurements, observations, etc) that has been translated into a form that computers can process
___
![types-of-matrices](https://user-images.githubusercontent.com/58425689/107605139-6870a000-6c5a-11eb-9c6a-3c02e212df1b.png)

#### 1. Qualitative/Categorical data - describes qualities or characteristics, can't measures easily but can be observed subjectively, visualized by Bar Plot, Pie Chart, Pareto Chart.
 - **Nominal:** \
    Data at this level is categorized using names, labels or qualities. \
    eg: Brand Name, ZipCode, Gender. 
 - **Ordinal:** \
    Data at this level can be arranged in order or ranked and can be compared. \
    eg: Grades, Star Reviews, Position in Race, Date 

#### 2. Quantitative/Numerical data - expressing a certain quantity, amount or range, visualized by Histogram, Line Plot, Scatter Plot
  - **Continous/Interval:** \
  Data at this level can be ordered as it is in a range of values and meaningful differences between the data points can be calculated. \
  eg: Temperature in Celsius, Year of Birth, weight
  - **Discrete:** \
  Data that can only take certain values. \
  eg. no of students

# Statistics
Statistics is the discipline that concerns the collection, organization, analysis, interpretation, and presentation of data. In applying statistics to a scientific, industrial, or social problem, it is conventional to begin with a statistical population or a statistical model to be studied.

## Population or Sample Data
**Population:** Collection of all items (N) and it includes each and every unit of our study. It is hard to define and the measure of characteristic such as mean, mode is called parameter. \
**Sample:** Subset of the population (n) and it includes only a handful units of the population. It is selected at random and the measure of the characteristic is called as statistics. \
![image](https://user-images.githubusercontent.com/58425689/107606069-167d4980-6c5d-11eb-91a1-f0f0a5a77d11.png)

## Population vs Sample
The population includes all objects of interest whereas the sample is only a portion of the population. Parameters are associated with populations and statistics with samples. Parameters are usually denoted using Greek letters (mu, sigma) while statistics are usually denoted using Roman letters (x, s).

There are several reasons why we don't work with populations. They are usually large, and it is often impossible to get data for every object we're studying. Sampling does not usually occur without cost, and the more items surveyed, the larger the cost.

## Types of Sampling
There are five types of sampling: **Random, Systematic, Convenience, Cluster, and Stratified.** 
       
   **• Random sampling** is analogous to putting everyone's name into a hat and drawing out several names. Each element in the population has an equal chance of occuring. While this is the preferred way of sampling, it is often difficult to do. It requires that a complete list of every element in the population be obtained. Computer generated lists are often used with random sampling. 

   **• Systematic sampling** is easier to do than random sampling. In systematic sampling, the list of elements is "counted off". That is, every kth element is taken. 

   **• Convenience sampling** is very easy to do, but it's probably the worst technique to use. In convenience sampling, readily available data is used. That is, the first people the surveyor runs into. 

   **• Cluster sampling** is accomplished by dividing the population into groups -- usually geographically. These groups are called clusters or blocks. The clusters are randomly selected, and each element in the selected clusters are used.

   **• Stratified sampling** also divides the population into groups called strata. However, this time it is by some characteristic, not geographically. For instance, the population might be separated into males and females. A sample is taken from each of these strata using either random, systematic, or convenience sampling.
  
We compute statistics, and use them to estimate parameters. The computation is the first part of the statistics course (Descriptive Statistics) and the estimation is the second part (Inferential Statistics).


## Types of Statistics
  - **Descriptive Statistics**
Collection, organization, summarization, and presentation of data. \
![image](https://user-images.githubusercontent.com/58425689/106352129-ee125880-6308-11eb-8c1c-c5cf148a1426.png)

  - **Inferential Statistics**
Generalizing from samples to populations using probabilities. Performing hypothesis testing, determining relationships between variables, and making predictions. \
![image](https://user-images.githubusercontent.com/58425689/106352238-66791980-6309-11eb-85b0-840ccf771c49.png)

## Measures of Central Tendency
The measure of central tendency is a single value that attempts to describe a set of data by identifying the central position within that set of data. As such, measures of central tendency are sometimes called measures of central location. They are also classed as summary statistics.

 - **Mean** \
     This is what people usually intend when they say "average". It susceptible to outliers when unusual values are added it gets skewed i.e deviates from the typical central value. \
     Population Mean: ![image](https://user-images.githubusercontent.com/58425689/106349996-b7cddc80-62fa-11eb-9dc4-2f4fbebb590e.png) \
     Sample Mean: ![image](https://user-images.githubusercontent.com/58425689/106350000-bac8cd00-62fa-11eb-9f1c-5b73463087ab.png) \
     Frequency Distribution: ![image](https://user-images.githubusercontent.com/58425689/106350002-be5c5400-62fa-11eb-82a9-63276479228f.png) \
     The mean of a frequency distribution is also the weighted mean.
     
  - **Median** \
    The median is the middle value for a dataset that has been arranged in order of magnitude. Median is a better alternative to mean as it is less affected by outliers and skewness of the data. The median value is much closer than the typical central value. \
    If the total number of values is odd then \
    ![image](https://user-images.githubusercontent.com/58425689/107606607-b8e9fc80-6c5e-11eb-895f-587da648ade7.png)

    If the total number of values is even then \
    ![image](https://user-images.githubusercontent.com/58425689/107606613-bb4c5680-6c5e-11eb-9940-195168017710.png)
    
  - **Mode** \
    The mode is the most commonly occurring value in the dataset. The mode can, therefore sometimes consider the mode as being the most popular option.
    
## Measures of Asymmetry
**Skewness:** Skewness is the asymmetry in a statistical distribution, in which the curve appears distorted or skewed towards to the left or to the right. Skewness indicates whether the data is concentrated on one side. \
![image](https://user-images.githubusercontent.com/58425689/106351687-a0e0b780-6305-11eb-8226-28cc3ceb64f3.png)

**Positive Skewness:** Positive Skewness is when the mean>median>mode. The outliers are skewed to the right i.e the tail is skewed to the right. \
**Negative Skewness:** Negative Skewness is when the mean<median<mode. The outliers are skewed to the left i.e the tail is skewed to the left. \
Skewness is important as it tells us about where the data is distributed.

For eg: Global Income Distribution in 2003 is highly right-skewed.We can see the mean $3,451 in 2003(green) is greater than the median $1,090. It suggests that the global income is not evenly distributed. Most individuals incomes are less than $2,000 and less number of people with income above $14,000, so the skewness. But it seems in 2035 according to the forecast income inequality will decrease over time. \
![image](https://user-images.githubusercontent.com/58425689/107606832-7d9bfd80-6c5f-11eb-9d3c-c85a15a14d00.png)


## Measures of Variability(Dispersion)
The measure of central tendency gives a single value that represents the whole value; however, the central tendency cannot describe the observation fully. The measure of dispersion helps us to study the variability of the items i.e the spread of data. \
Remember: Population Data has N data points and Sample Data has (n-1) data points. (n-1) is called Bessel’s Correction and it is used to reduce bias.

- **Range** \
    The range is the simplest measure of variation to find. It is simply the highest value minus the lowest value. \
        
        RANGE = MAXIMUM - MINIMUM
    Since the range only uses the largest and smallest values, it is greatly affected by extreme values, that is - it is not resistant to change.
 
- **Variance** \
  Variance measures how far is the sum of squared distances from each point to the mean i.e the dispersion around the mean. \
  Variance is the average of all squared deviations.
  
  ![image](https://user-images.githubusercontent.com/58425689/106350377-24e27180-62fd-11eb-90b6-35529a1f17e5.png) \
  ![image](https://user-images.githubusercontent.com/58425689/106350381-29a72580-62fd-11eb-862b-60b12c13fc55.png)
  
- **Standard Deviation** \
   As Variance suffers from unit difference so standard deviation is used. The square root of the variance is the standard deviation. It tells about the concentration of the data around the mean of the data set. \
   ![image](https://user-images.githubusercontent.com/58425689/106350383-2d3aac80-62fd-11eb-8cae-6e5fa361eb5e.png)
   ![image](https://user-images.githubusercontent.com/58425689/106350386-30359d00-62fd-11eb-869b-889396d95141.png)

- **Coefficient of Variation(CV):** \
  It is also called as the relative standard deviation. It is the ratio of standard deviation to the mean of the dataset.
  
  ![image](https://user-images.githubusercontent.com/58425689/107607187-9e188780-6c60-11eb-90e2-7c349db47b22.png)

 - **Sum of Squares** \
     The sum of the squares of the deviations from the means is given a shortcut notation and several alternative formulas.
     ![image](https://user-images.githubusercontent.com/58425689/106350582-60317000-62fe-11eb-85aa-3a5ad12eeaa1.png) 
     
     ![image](https://user-images.githubusercontent.com/58425689/106350584-63c4f700-62fe-11eb-998e-09718d7746e6.png)
     
 - **Quartile** \
   Either the 25th, 50th, or 75th percentiles. The 50th percentile is also called the median. \
   **ungroup_data** \
   ![image](https://user-images.githubusercontent.com/58425689/106352905-c0301280-630e-11eb-96b0-496c6d29033e.png) \
   **group data** \
   ![image](https://user-images.githubusercontent.com/58425689/106352907-c32b0300-630e-11eb-8991-8803d2ef8c6c.png)

   ![image](https://user-images.githubusercontent.com/58425689/106352943-05544480-630f-11eb-9794-5176167c223b.png) \

## Measures of Position
![image](https://user-images.githubusercontent.com/58425689/106352388-dfc53c00-630a-11eb-87ec-d7a6bbc05a39.png)

 - **Standard Scores (z-scores)** \
  The standard score is obtained by subtracting the mean and dividing the difference by the standard deviation. The symbol is z, which is why it's also called a z-score. \
   ![image](https://user-images.githubusercontent.com/58425689/106350742-5f4d0e00-62ff-11eb-80a8-3a1023689150.png) \
   The mean of the standard scores is zero and the standard deviation is 1. This is the nice feature of the standard score -- no matter what the original scale      was, when the data is converted to its standard score, the mean is zero and the standard deviation is 1.
  
  - **Percentile** \
    The percent of the population which lies below that value. The data must be ranked to find percentiles. \
    The kth percentile is the number which has k% of the values below it. The data must be ranked.
    
        1. Rank the data
        2. Find k% (k /100) of the sample size, n.
        3. If this is an integer, add 0.5. If it isn't an integer round up.
        4. Find the number in this position.
     If your depth ends in 0.5, then take the midpoint between the two numbers. \
     It is sometimes easier to count from the high end rather than counting from the low end. For example, the 80th percentile is the number which has 80% below        it and 20% above it. Rather than counting 80% from the bottom, count 20% from the top.

     **Box and Whiskers Plot:**
     A graphical representation of the five number summary. A box is drawn between the lower and upper hinges with a line at the median. Whiskers (a single line,      not a box) extend from the hinges to lines at the minimum and maximum values.
     
   - **Outlier** \
      An extremely high or low value when compared to the rest of the values.
      ![boxplot-example1-l](https://user-images.githubusercontent.com/58425689/106352464-72fe7180-630b-11eb-9827-839a3c1fee1f.jpg)

   - **Mild Outliers** \
      Values which lie between 1.5 and 3.0 times the InterQuartile Range below the 1st Quartile or above the 3rd Quartile. Note, some texts use hinges instead of         Quartiles. \
      x is a mild outlier if ...
      
      **Q1 - 3 * IQR <= x < Q1 - 1.5 * IQR** \
      or \
      **Q1 + 1.5 * IQR < x <= Q3 + 3 * IQR**
      
   - **Extreme Outliers** \
      Values which lie more than 3.0 times the InterQuartile Range below the 1st Quartile or above the 3rd Quartile. Note, some texts use hinges instead of             Quartiles. \
       x is an extreme outlier if ... 
       
       **x < Q1 - 3 * IQR** \
       or \
       **x > Q3 + 3 * IQR**
       
## Measurements of Relationships between Variables
Measures of relationship are used to find the comparison between 2 variables. \
![image](https://user-images.githubusercontent.com/58425689/106352739-a510d300-630d-11eb-863b-cab2d2def20a.png)

- **Covariance:** \
Covariance is a measure of the relationship between the variability of 2 variables i.e It measures the degree of change in the variables, when one variable changes, will there be the same/a similar change in the other variable. \
If it’s positive then they tend to move in the same direction, if it’s negative then they tend to move in opposite directions, and if they’re zero, they have no relation to each other. \
![image](https://user-images.githubusercontent.com/58425689/107607765-424efe00-6c62-11eb-8b5b-c20ed028cf20.png)

  **Covariance does not give effective information about the relation between 2 variables as it is not normalized.**

- **Correlation:** \
  Correlation gives a better understanding of covariance. It is normalized covariance. Correlation tells us how correlated the variables are to each other. It is also called as Pearson Correlation Coefficient. \
  ![image](https://user-images.githubusercontent.com/58425689/107607831-77f3e700-6c62-11eb-9949-1d84799e5f45.png) \
The value of correlation ranges from -1 to 1. \
-1 indicates negative correlation i.e with an increase in 1 variable independent there is a decrease in the other dependent variable. \
 1 indicates positive correlation i.e with an increase in 1 variable independent there is an increase in the other dependent variable. \
 0 indicates that the variables are independent of each other.
