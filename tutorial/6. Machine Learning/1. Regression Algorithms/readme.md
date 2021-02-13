# Regression Analysis in Machine learning
Regression analysis is a statistical method to model the relationship between a dependent (target) and independent (predictor) variables with one or more independent variables. More specifically, Regression analysis helps us to understand how the value of the dependent variable is changing corresponding to an independent variable when other independent variables are held fixed. It predicts continuous/real values such as temperature, age, salary, price, etc.

## Terminologies Related to the Regression Analysis:

- Dependent Variable: The main factor in Regression analysis which we want to predict or understand is called the dependent variable. It is also called target variable.
- Independent Variable: The factors which affect the dependent variables or which are used to predict the values of the dependent variables are called independent variable, also called as a predictor.
- Outliers: Outlier is an observation which contains either very low value or very high value in comparison to other observed values. An outlier may hamper the result, so it should be avoided.
- Multicollinearity: If the independent variables are highly correlated with each other than other variables, then such condition is called Multicollinearity. It should not be present in the dataset, because it creates problem while ranking the most affecting variable.
- Underfitting and Overfitting: If our algorithm works well with the training dataset but not well with test dataset, then such problem is called Overfitting. And if our algorithm does not perform well even with training dataset, then such problem is called underfitting.      

## Types of Regression
- [Linear Regression](https://github.com/rjnp2/Data-Science/tree/main/tutorial/6.%20Machine%20Learning/1.%20Regression%20Algorithms/1.%20Linear%20Regression)     
    ```python
    #Fitting the Linear Regression to the dataset  
    from sklearn.linear_model import LinearRegression  
    lin_regs= LinearRegression()  
    lin_regs.fit(x,y)
    ```
    
- Ridge Regression     
    - Ridge regression is one of the most robust versions of linear regression in which a small amount of bias is introduced so that we can get better long term predictions.
    - The amount of bias added to the model is known as Ridge Regression penalty. We can compute this penalty term by multiplying with the lambda to the squared weight of each individual features.
    - The equation for ridge regression will be: \
      ![image](https://user-images.githubusercontent.com/58425689/107841369-781af080-6de2-11eb-884b-daa995e19b86.png)

    - A general linear or polynomial regression will fail if there is high collinearity between the independent variables, so to solve such problems, Ridge regression can be used.
    - Ridge regression is a regularization technique, which is used to reduce the complexity of the model. It is also called as L2 regularization.
    - It helps to solve the problems if we have more parameters than samples.
    ```python
       from sklearn.linear_model import Ridge
       ridge=Ridge()
       ridge.fit(X, y)
    ```

- Lasso Regression 
   - Lasso regression is another regularization technique to reduce the complexity of the model.
   - It is similar to the Ridge Regression except that penalty term contains only the absolute weights instead of a square of weights.
   - Since it takes absolute values, hence, it can shrink the slope to 0, whereas Ridge Regression can only shrink it near to 0.
   - It is also called as L1 regularization. The equation for Lasso regression will be: \
   ![image](https://user-images.githubusercontent.com/58425689/107841419-b6181480-6de2-11eb-9d8d-88181321e18b.png)
    ```python
       from sklearn.linear_model import Lasso
       ridge=Lasso()
       ridge.fit(X, y)
    ```
    
- Polynomial Regression
   - Polynomial Regression is a type of regression which models the non-linear dataset using a linear model.
   - It is similar to multiple linear regression, but it fits a non-linear curve between the value of x and corresponding conditional values of y.
   - Suppose there is a dataset which consists of datapoints which are present in a non-linear fashion, so for such case, linear regression will not best fit to those datapoints. To cover such datapoints, we need Polynomial regression.
   - In Polynomial regression, the original features are transformed into polynomial features of given degree and then modeled using a linear model. Which means the datapoints are best fitted using a polynomial line. \
   ![image](https://user-images.githubusercontent.com/58425689/107841255-8c122280-6de1-11eb-9619-b59d34f38766.png)

   - The equation for polynomial regression also derived from linear regression equation that means Linear regression equation Y= b0+ b1x, is transformed into Polynomial regression equation Y= b0+b1x+ b2x2+ b3x3+.....+ bnxn.
   - Here Y is the predicted/target output, b0, b1,... bn are the regression coefficients. x is our independent/input variable.
   - The model is still linear as the coefficients are still linear with quadratic.
   ```python
    #Fitting the Polynomial regression to the dataset  
    from sklearn.preprocessing import PolynomialFeatures  
    poly_regs= PolynomialFeatures(degree= 2)  
    x_poly= poly_regs.fit_transform(x)  
    lin_reg_2 =LinearRegression()  
    lin_reg_2.fit(x_poly, y)  
    ```

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
   Ordinal(low, medium, high) 
   ```python
    #Fitting Logistic Regression to the training set  
    from sklearn.linear_model import LogisticRegression  
    classifier= LogisticRegression(random_state=0)  
    classifier.fit(x_train, y_train)  
    ```
