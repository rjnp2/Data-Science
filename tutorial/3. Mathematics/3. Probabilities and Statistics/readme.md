# Statistics
## Counting Techniques

## 1.Factorial
A positive integer factorial is the product of each natural number up to and including the integer.
If n is a positive integer, then

     n! = n (n-1) (n-2) ... (3)(2)(1)
     n! = n (n-1)!
   
A special case is 0!

    0! = 1
   
## 2.Permutation
A permutation is an arrangement of objects without repetition where order is important.
Permutations using all the objects
A permutation of n objects, arranged into one group of size n, without repetition, and order being important is:
    
    nPn = P(n,n) = n!
Example: Find all permutations of the letters "ABC"
  
    ABC  ACB  BAC  BCA  CAB  CBA
Permutations of some of the objects
A permutation of n objects, arranged in groups of size r, without repetition, and order being important is:
  
    nPr = P(n,r) = n! / (n-r)!
   
## 3.Combinations
A combination is an arrangement of objects without repetition where order is not important.

**Note:** The difference between a permutation and a combination is not whether there is repetition or not -- there must not be repetition with either, and if there is repetition, you can not use the formulas for permutations or combinations. The only difference in the definition of a permutation and a combination is whether order is important.
A combination of n objects, arranged in groups of size r, without repetition, and order being important is:
   
    nCr = C(n,r) = n! / ( (n-r)! * r! )
   
## 4. Tree Diagram
A graphical device used to list all possibilities of a sequence of events in a systematic way.
Pascal's Triangle
Combinations are used in the binomial expansion theorem from algebra to give the coefficients of the expansion (a+b)^n. They also form a pattern known as Pascal's Triangle.

                           1
                         1   1
                       1   2   1
                     1   3   3   1
                   1   4   6   4   1
                 1   5  10   10  5   1
               1   6  15  20  15   6   1
             1   7  21  35  35  21   7   1
Each element in the table is the sum of the two elements directly above it. Each element is also a combination. The n value is the number of the row (start counting at zero) and the r value is the element in the row (start counting at zero). That would make the 20 in the next to last row C(6,3) -- it's in the row #6 (7th row) and position #3 (4th element).

## Introduction
**Definitions**

## Statistics
Collection of methods for planning experiments, obtaining data, and then organizing, summarizing, presenting, analyzing, interpreting, and drawing conclusions.

## Variable
Characteristic or attribute that can assume different values

## Random Variable
A variable whose values are determined by chance.

## Population
All subjects possessing a common characteristic that is being studied.

## Sample
A subgroup or subset of the population.

## Population vs Sample
The population includes all objects of interest whereas the sample is only a portion of the population. Parameters are associated with populations and statistics with samples. Parameters are usually denoted using Greek letters (mu, sigma) while statistics are usually denoted using Roman letters (x, s).

There are several reasons why we don't work with populations. They are usually large, and it is often impossible to get data for every object we're studying. Sampling does not usually occur without cost, and the more items surveyed, the larger the cost.

We compute statistics, and use them to estimate parameters. The computation is the first part of the statistics course (Descriptive Statistics) and the estimation is the second part (Inferential Statistics)

## Types of Sampling
There are five types of sampling: **Random, Systematic, Convenience, Cluster, and Stratified.** \
       
   **• Random sampling** is analogous to putting everyone's name into a hat and drawing out several names. Each element in the population has an equal chance of occuring. While this is the preferred way of sampling, it is often difficult to do. It requires that a complete list of every element in the population be obtained. Computer generated lists are often used with random sampling. 
   
   **• Systematic sampling** is easier to do than random sampling. In systematic sampling, the list of elements is "counted off". That is, every kth element is taken. 
   
   **• Convenience sampling** is very easy to do, but it's probably the worst technique to use. In convenience sampling, readily available data is used. That is, the first people the surveyor runs into. 
   
   **• Cluster sampling** is accomplished by dividing the population into groups -- usually geographically. These groups are called clusters or blocks. The clusters are randomly selected, and each element in the selected clusters are used.
   
   **• Stratified sampling** also divides the population into groups called strata. However, this time it is by some characteristic, not geographically. For instance, the population might be separated into males and females. A sample is taken from each of these strata using either random, systematic, or convenience sampling.
    
## Parameter
Characteristic or measure obtained from a population.
Statistic (not to be confused with Statistics)
Characteristic or measure obtained from a sample.

## Descriptive Statistics
Collection, organization, summarization, and presentation of data. \
![image](https://user-images.githubusercontent.com/58425689/106352129-ee125880-6308-11eb-8c1c-c5cf148a1426.png)

## Inferential Statistics
Generalizing from samples to populations using probabilities. Performing hypothesis testing, determining relationships between variables, and making predictions. \
![image](https://user-images.githubusercontent.com/58425689/106352238-66791980-6309-11eb-85b0-840ccf771c49.png)

## Discrete Variables
Variables which assume a finite or countable number of possible values. Usually obtained by counting.

## Continuous Variables
Variables which assume an infinite number of possible values. Usually obtained by measurement.

 ## Skewed Distribution 
 The majority of the values lie together on one side with a very few values (the tail) to the other side. In a positively skewed distribution, the tail is to the     right and the mean is larger than the median. In a negatively skewed distribution, the tail is to the left and the mean is smaller than the median.
    ![image](https://user-images.githubusercontent.com/58425689/106351687-a0e0b780-6305-11eb-8226-28cc3ceb64f3.png)

 ## Symmetric Distribution
 The data values are evenly distributed on both sides of the mean. In a symmetric distribution, the mean is the median.
  
 ## Weighted Mean
 The mean when each value is multiplied by its weight and summed. This sum is divided by the total of the weights.

## Measures of Central Tendency

  - Mean \
    This is what people usually intend when they say "average" \
    Population Mean: ![image](https://user-images.githubusercontent.com/58425689/106349996-b7cddc80-62fa-11eb-9dc4-2f4fbebb590e.png) \
    Sample Mean: ![image](https://user-images.githubusercontent.com/58425689/106350000-bac8cd00-62fa-11eb-9f1c-5b73463087ab.png) \
    Frequency Distribution: ![image](https://user-images.githubusercontent.com/58425689/106350002-be5c5400-62fa-11eb-82a9-63276479228f.png) \
    The mean of a frequency distribution is also the weighted mean.
    
  - Median \
    The data must be ranked (sorted in ascending order) first. The median is the number in the middle.
    To find the depth of the median, there are several formulas that could be used, the one that we will use is: \
        Depth of median = 0.5 * (n + 1) \
    Grouped Frequency Distribution \
    ![image](https://user-images.githubusercontent.com/58425689/106350090-52c6b680-62fb-11eb-8933-f9f6149f0c31.png)
  
  - Mode \
    The mode is the most frequent data value. There may be no mode if no one value appears more than any other. There may also be two modes (bimodal), three modes       (trimodal), or more than three modes (multi-modal).
    For grouped frequency distributions, the modal class is the class with the largest frequency.
    
  - Midrange
    The midrange is simply the midpoint between the highest and lowest values.
    
## Measures of Variation
  - Range \
    The range is the simplest measure of variation to find. It is simply the highest value minus the lowest value. \
        
        RANGE = MAXIMUM - MINIMUM
    Since the range only uses the largest and smallest values, it is greatly affected by extreme values, that is - it is not resistant to change.
    
   - Population Variance \
     The average of the squares of the distances from the population mean. \
     It is the sum of the squares of the deviations from the mean divided by the population size. \
     The units on the variance are the units of the population squared. \
     ![image](https://user-images.githubusercontent.com/58425689/106350377-24e27180-62fd-11eb-90b6-35529a1f17e5.png)
     
   - Sample Variance \
     Unbiased estimator of a population variance. \
     Instead of dividing by the population size, the sum of the squares of the deviations from the sample mean is divided by one less than the sample size. \
     The units on the variance are the units of the population squared. \
     ![image](https://user-images.githubusercontent.com/58425689/106350381-29a72580-62fd-11eb-862b-60b12c13fc55.png)

   - Standard Deviation \
     The square root of the variance. \
     The population standard deviation is the square root of the population variance and the sample standard deviation is the square root of the sample variance. \
     The sample standard deviation is not the unbiased estimator for the population standard deviation. \
     The units on the standard deviation is the same as the units of the population/sample.\
     ![image](https://user-images.githubusercontent.com/58425689/106350383-2d3aac80-62fd-11eb-8cae-6e5fa361eb5e.png)
     ![image](https://user-images.githubusercontent.com/58425689/106350386-30359d00-62fd-11eb-869b-889396d95141.png)

   - Sum of Squares \
     The sum of the squares of the deviations from the means is given a shortcut notation and several alternative formulas.
     ![image](https://user-images.githubusercontent.com/58425689/106350582-60317000-62fe-11eb-85aa-3a5ad12eeaa1.png)
      ![image](https://user-images.githubusercontent.com/58425689/106350584-63c4f700-62fe-11eb-998e-09718d7746e6.png)
      
   - Coefficient of Variation \
     Standard deviation divided by the mean, expressed as a percentage. We won't work with the Coefficient of Variation in this course. \
     ![image](https://user-images.githubusercontent.com/58425689/106352031-151c5a80-6308-11eb-8c08-1d44eb344a28.png)


## Measures of Position

  - Standard Scores (z-scores) \
  The standard score is obtained by subtracting the mean and dividing the difference by the standard deviation. The symbol is z, which is why it's also called a z-score. \
          ![image](https://user-images.githubusercontent.com/58425689/106350742-5f4d0e00-62ff-11eb-80a8-3a1023689150.png) \
The mean of the standard scores is zero and the standard deviation is 1. This is the nice feature of the standard score -- no matter what the original scale was, when the data is converted to its standard score, the mean is zero and the standard deviation is 1.
   - Percentile \
    The percent of the population which lies below that value. The data must be ranked to find percentiles. \
    The kth percentile is the number which has k% of the values below it. The data must be ranked.
        1. Rank the data
        2. Find k% (k /100) of the sample size, n.
        3. If this is an integer, add 0.5. If it isn't an integer round up.
        4. Find the number in this position. If your depth ends in 0.5, then take the midpoint between the two numbers. \
   It is sometimes easier to count from the high end rather than counting from the low end. For example, the 80th percentile is the number which has 80% below it       and 20% above it. Rather than counting 80% from the bottom, count 20% from the top.

   - Quartile \
     Either the 25th, 50th, or 75th percentiles. The 50th percentile is also called the median.
     
   - Outlier \
      An extremely high or low value when compared to the rest of the values.
      
   - Mild Outliers \
      Values which lie between 1.5 and 3.0 times the InterQuartile Range below the 1st Quartile or above the 3rd Quartile. Note, some texts use hinges instead of         Quartiles. \
      x is a mild outlier if ...
   Q1 - 3 * IQR <= x < Q1 - 1.5 * IQR
or
   Q1 + 1.5 * IQR < x <= Q3 + 3 * IQR
      
   - Extreme Outliers \
      Values which lie more than 3.0 times the InterQuartile Range below the 1st Quartile or above the 3rd Quartile. Note, some texts use hinges instead of               Quartiles. \
       x is an extreme outlier if ...
   x < Q1 - 3 * IQR       
or
   x > Q3 + 3 * IQR
      
# Measurements of Relationships between Variables

## Covariance: 
Measures the variance between two (or more) variables. \
If it’s positive then they tend to move in the same direction, if it’s negative then they tend to move in opposite directions, and if they’re zero, they have no relation to each other. \
![image](https://user-images.githubusercontent.com/58425689/106351732-f5843280-6305-11eb-9ec1-33c41f67b55b.png)

## Correlation: 
Measures the strength of a relationship between two variables and ranges from -1 to 1; the normalized version of covariance. \
Generally, a correlation of +/- 0.7 represents a strong relationship between two variables. \
On the flip side, correlations between -0.3 and 0.3 indicate that there is little to no relationship between variables. \
![image](https://user-images.githubusercontent.com/58425689/106351734-f917b980-6305-11eb-8faf-36c93e82b02b.png)
