# Regression Analysis in Machine learning
Regression analysis is a statistical method to model the relationship between a dependent (target) and independent (predictor) variables with one or more independent variables. More specifically, Regression analysis helps us to understand how the value of the dependent variable is changing corresponding to an independent variable when other independent variables are held fixed. It predicts continuous/real values such as temperature, age, salary, price, etc.

## Terminologies Related to the Regression Analysis:

- Dependent Variable: The main factor in Regression analysis which we want to predict or understand is called the dependent variable. It is also called target variable.
- Independent Variable: The factors which affect the dependent variables or which are used to predict the values of the dependent variables are called independent variable, also called as a predictor.
- Outliers: Outlier is an observation which contains either very low value or very high value in comparison to other observed values. An outlier may hamper the result, so it should be avoided.
- Multicollinearity: If the independent variables are highly correlated with each other than other variables, then such condition is called Multicollinearity. It should not be present in the dataset, because it creates problem while ranking the most affecting variable.
- Underfitting and Overfitting: If our algorithm works well with the training dataset but not well with test dataset, then such problem is called Overfitting. And if our algorithm does not perform well even with training dataset, then such problem is called underfitting.      

## Types of Regression
- Linear Regression     
- Ridge Regression      
- Lasso Regression      
- Polynomial Regression
   - Polynomial Regression is a type of regression which models the non-linear dataset using a linear model.
   - It is similar to multiple linear regression, but it fits a non-linear curve between the value of x and corresponding conditional values of y.
   - Suppose there is a dataset which consists of datapoints which are present in a non-linear fashion, so for such case, linear regression will not best fit to those datapoints. To cover such datapoints, we need Polynomial regression.
   - In Polynomial regression, the original features are transformed into polynomial features of given degree and then modeled using a linear model. Which means the datapoints are best fitted using a polynomial line. \
   ![image](https://user-images.githubusercontent.com/58425689/107841255-8c122280-6de1-11eb-9619-b59d34f38766.png)

   - The equation for polynomial regression also derived from linear regression equation that means Linear regression equation Y= b0+ b1x, is transformed into Polynomial regression equation Y= b0+b1x+ b2x2+ b3x3+.....+ bnxn.
   - Here Y is the predicted/target output, b0, b1,... bn are the regression coefficients. x is our independent/input variable.
   - The model is still linear as the coefficients are still linear with quadratic

- Logistic Regression           
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
  - There are three types of logistic regression: \
   Binary(0/1, pass/fail) \
   Multi(cats, dogs, lions) \
   Ordinal(low, medium, high) \
