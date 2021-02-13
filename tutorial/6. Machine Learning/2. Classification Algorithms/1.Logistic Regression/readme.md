# Logistic Regression           
  - Logistic regression is another supervised learning algorithm which is used to solve the classification problems. In classification problems, we have dependent variables in a binary or discrete format such as 0 or 1.
  - Logistic regression algorithm works with the categorical variable such as 0 or 1, Yes or No, True or False, Spam or not spam, etc.
  - It is a predictive analysis algorithm which works on the concept of probability.
  - Logistic regression is a type of regression, but it is different from the linear regression algorithm in the term how they are used.
  - Logistic regression uses sigmoid function or logistic function which is a complex cost function. This sigmoid function is used to model the data in logistic regression. The function can be represented as: \
   ![image](https://user-images.githubusercontent.com/58425689/107841337-1eb2c180-6de2-11eb-8cfb-3ba3650e057d.png)
   
      f(x)= Output between the 0 and 1 value.
      x= input to the function
      e= base of natural logarithm.
  - When we provide the input values (data) to the function, it gives the S-curve as follows: \
  ![image](https://user-images.githubusercontent.com/58425689/107841338-207c8500-6de2-11eb-825f-079b70534687.png)

  - It uses the concept of threshold levels, values above the threshold level are rounded up to 1, and values below the threshold level are rounded up to 0.
 
## Logistic Function (Sigmoid Function):
- The sigmoid function is a mathematical function used to map the predicted values to probabilities.
- It maps any real value into another value within a range of 0 and 1.
- The value of the logistic regression must be between 0 and 1, which cannot go beyond this limit, so it forms a curve like the "S" form. The S-form curve is called the Sigmoid function or the logistic function.
- In logistic regression, we use the concept of the threshold value, which defines the probability of either 0 or 1. Such as values above the threshold value tends to 1, and a value below the threshold values tends to 0.

## There are three types of logistic regression: 
- Binomial: In binomial Logistic regression, there can be only two possible types of the dependent variables, such as 0 or 1, Pass or Fail, etc.
- Multinomial: In multinomial Logistic regression, there can be 3 or more possible unordered types of the dependent variable, such as "cat", "dogs", or "sheep"
- Ordinal: In ordinal Logistic regression, there can be 3 or more possible ordered types of dependent variables, such as "low", "Medium", or "High".
   
   
   ```python
    #Fitting Logistic Regression to the training set  
    from sklearn.linear_model import LogisticRegression  
    classifier= LogisticRegression(random_state=0)  
    classifier.fit(x_train, y_train)  
  ```
## Project
1. [iris_predict](https://github.com/rjnp2/iris_predict/blob/master/iris%20flower.ipynb)
2. [loan_prediction](https://github.com/rjnp2/loan_prediction)
