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

