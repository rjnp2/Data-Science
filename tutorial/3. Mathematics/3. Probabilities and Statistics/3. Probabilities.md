# Probability

## Definitions

- **Sample Spaces** \
    A sample space is the set of all possible outcomes. However, some sample spaces are better than others.

    Consider the experiment of flipping two coins. It is possible to get 0 heads, 1 head, or 2 heads. Thus, the sample space could be {0, 1, 2}. Another way to look     at it is flip { HH, HT, TH, TT }. The second way is better because each event is as equally likely to occur as any other.

- **Probability** \
  The probability of an event occurring is the number in the event divided by the number in the sample space. Again, this is only true when the events are equally likely. 
  
       P(E) = n(E) / n(S)
       
- **Probability Rules** 
  - All probabilities are between 0 and 1 inclusive

        0 <= P(E) <= 1    
  - The sum of all the probabilities in the sample space is 1
  - The probability of an event not occurring is one minus the probability of it occurring.\
       
        P(E') = 1 - P(E)
     
- **Mutually Exclusive Events** \
  Two events are mutually exclusive if they cannot occur at the same time. Another word that means mutually exclusive is disjoint. \
  If two events are disjoint, then the probability of them both occurring at the same time is 0.

     Disjoint:  P(A and B) = 0
     
   If two events are mutually exclusive, then the probability of either occurring is the sum of the probabilities of each occurring.

- **Specific Addition Rule** \
Only valid when the events are mutually exclusive.

       P(A or B) = P(A) + P(B)
    
- **Non-Mutually Exclusive Events**
In events which aren't mutually exclusive, there is some overlap. When P(A) and P(B) are added, the probability of the intersection (and) is added twice. To compensate for that double addition, the intersection needs to be subtracted.

       P(A or B) = P(A) + P(B) - P(A and B)

- **Independent Events**
  Two events are independent if the occurrence of one does not change the probability of the other occurring.
  If events are independent, then the probability of them both occurring is the product of the probabilities of each occurring.

  Specific Multiplication Rule \ 
  Only valid for independent events

       P(A and B) = P(A) * P(B)
 
- **Conditional Probability** \
Recall that the probability of an event occurring given that another event has already occurred is called a conditional probability.
The probability that event B occurs, given that event A has already occurred is

    P(B|A) = P(A and B) / P(A)
    
- **Bayes' Theorem**
    A formula which allows one to find the probability that an event occurred as the result of a particular previous event.
    a mathematical formula for determining conditional probability. “The probability of A given B is equal to the probability of B given A times the probability of A over the probability of B”  

    ![image](https://user-images.githubusercontent.com/58425689/106353924-12286680-6316-11eb-9d92-fb11fc7dc2e7.png)

- **Probability Mass Function (PMF):** \
A function for discrete data which gives the probability of a given value occurring.

- **Cumulative Density Function (CDF):** \
A function that tells us the probability that a random variable is less than a certain value; the integral of the PDF.

- **Expected value**
    The expected value of a random variable, also known as the mean value or the first moment, is often noted E[X] or μ and is the value that we would obtain by averaging
    the results of the experiment infinitely many times. It is computed as follows:

    ![image](https://user-images.githubusercontent.com/58425689/106355936-89182c00-6323-11eb-8fba-46fbb35fc69c.png)


## Discrete Data Distributions

- **Binomial Distribution** \
    A binomial experiment is an experiment which satisfies these four conditions

    A fixed number of trials
    Each trial is independent of the others
    There are only two outcomes
    The probability of each outcome remains constant from trial to trial.

    These can be summarized as: An experiment with a fixed number of independent trials, each of which can only have two possible outcomes.

    The fact that each trial is independent actually means that the probabilities remain constant.

    The probability of getting exactly x success in n trials, with the probability of success on a single trial being p is:

    ![image](https://user-images.githubusercontent.com/58425689/106354060-2751c500-6317-11eb-8629-72ff67ee7ab0.png)

    Mean, Variance, and Standard Deviation
    The mean, variance, and standard deviation of a binomial distribution are extremely easy to find.

    ![image](https://user-images.githubusercontent.com/58425689/106354035-00938e80-6317-11eb-9c05-30a7b87e3fa2.png)

- **Poisson Distribution** \
    Poisson probabilities are useful when there are a large number of independent trials with a small probability of success on a single trial and the variables occur over a period of time. It can also be used when a density of items is distributed over a given area or volume.
    
    ![image](https://user-images.githubusercontent.com/58425689/106354113-81528a80-6317-11eb-8764-9bb821016755.png)

- **Normal Distribution** \
   - Bell-shaped
   - Symmetric about mean
   - Continuous
   - Never touches the x-axis
   - Total area under curve is 1.00
   - Approximately 68% lies within 1 standard deviation of the mean, 95% within 2 standard deviations, and 99.7% within 3 standard deviations of the mean. This is the Empirical Rule mentioned earlier.
   - Data values represented by x which has mean mu and standard deviation sigma.
   - Probability Function given by
   
   ![image](https://user-images.githubusercontent.com/58425689/106354235-4d2b9980-6318-11eb-8cb0-aa0025e900f8.png)
   ![image](https://user-images.githubusercontent.com/58425689/106354248-646a8700-6318-11eb-9d95-7d9303c229a5.png)

# Estimation

## Definitions

- **Estimation** \
    Estimation statistics is a data analysis framework that uses a combination of effect sizes, confidence intervals, precision planning, and meta-analysis to plan experiments, analyze data and interpret results. It is distinct from null hypothesis significance testing, which is considered to be less informative. \
    Data from the sample are then used to develop estimates of the characteristics of the larger population. The process of using a sample to make inferences about a population is called **statistical inference**. 
    
    **Characteristics** such as 
    - **the population mean, the population variance, and the population proportion are called parameters of the population.** 
    - **the sample such as the sample mean, the sample variance, and the sample proportion are called sample statistics.** 

    ## There are two types of estimates: point and interval. 
    - **A point estimate** is a value of a sample statistic that is used as a single estimate of a population parameter. No statements are made about the quality or precision of a point estimate.
    - **A interval estimates** are accompanied by a statement concerning the degree of confidence that the interval contains the population parameter being estimated. Interval estimates of population parameters are called confidence intervals.

- **Confidence Interval** \
An interval estimate with a specific level of confidence

- **Confidence Level** \
The percent of the time the true mean will lie in the interval estimate given.

- **Consistent Estimator** \
An estimator which gets closer to the value of the parameter as the sample size increases.

- **Degrees of Freedom** \
The number of data values which are allowed to vary once a statistic has been determined.

- **Estimator** \
A sample statistic which is used to estimate a population parameter. It must be unbiased, consistent, and relatively efficient.

- **Interval Estimate** \
A range of values used to estimate a parameter.

- **Maximum Error of the Estimate** \
The maximum difference between the point estimate and the actual parameter. The Maximum Error of the Estimate is 0.5 the width of the confidence interval for means and proportions.

- **Point Estimate** \
A single value used to estimate a parameter.

- **Relatively Efficient Estimator** \
The estimator for a parameter with the smallest variance.

- **T distribution** \
A distribution used when the population variance is unknown.

- **Unbiased Estimator** \
An estimator whose expected value is the mean of the parameter being estimated.

![Statistical Inference Reference Sheet_page-0001](https://user-images.githubusercontent.com/58425689/106356118-38093780-6325-11eb-87a2-006ebf281c0a.jpg)
![Statistical Inference Reference Sheet_page-0002](https://user-images.githubusercontent.com/58425689/106356119-393a6480-6325-11eb-98df-2df1f8909c9f.jpg)

# Hypothesis

## Definitions

- **Null Hypothesis ( H0 )**
Statement of zero or no change. If the original claim includes equality (<=, =, or >=), it is the null hypothesis. If the original claim does not include equality (<, not equal, >) then the null hypothesis is the complement of the original claim. The null hypothesis always includes the equal sign. The decision is based on the null hypothesis.

- **Alternative Hypothesis ( H1 or Ha )**
Statement which is true if the null hypothesis is false. The type of test (left, right, or two-tail) is based on the alternative hypothesis.

- **Type I error**
Rejecting the null hypothesis when it is true (saying false when true). Usually the more serious error.

- **Type II error**
Failing to reject the null hypothesis when it is false (saying true when false).

- **alpha**
Probability of committing a Type I error.

- **beta**
Probability of committing a Type II error.

- **Test statistic**
Sample statistic used to decide whether to reject or fail to reject the null hypothesis.

- **Critical region**
Set of all values which would cause us to reject H0

- **Critical value(s)**
The value(s) which separate the critical region from the non-critical region. The critical values are determined independently of the sample statistics.

- **Significance level ( alpha )**
The probability of rejecting the null hypothesis when it is true. alpha = 0.05 and alpha = 0.01 are common. If no level of significance is given, use alpha = 0.05. The level of significance is the complement of the level of confidence in estimation.

- **Decision**
A statement based upon the null hypothesis. It is either "reject the null hypothesis" or "fail to reject the null hypothesis". We will never accept the null hypothesis.

- **Conclusion**
A statement which indicates the level of evidence (sufficient or insufficient), at what level of significance, and whether the original claim is rejected (null) or supported (alternative).
