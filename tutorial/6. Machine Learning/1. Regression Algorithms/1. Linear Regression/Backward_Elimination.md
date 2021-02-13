## What is Backward Elimination?
Backward elimination is a feature selection technique while building a machine learning model. It is used to remove those features that do not have a significant effect on the dependent variable or prediction of output. There are various ways to build a model in Machine Learning, which are:

    1. All-in
    2. Backward Elimination
    3. Forward Selection
    4. Bidirectional Elimination
    5. Score Comparison

Above are the possible methods for building the model in Machine learning, but we will only use here the Backward Elimination process as it is the fastest method.

## Steps of Backward Elimination
Below are some main steps which are used to apply backward elimination process:

Step-1: Firstly, We need to select a significance level to stay in the model. (SL=0.05) \
Step-2: Fit the complete model with all possible predictors/independent variables. \
Step-3: Choose the predictor which has the highest P-value, such that. 

    If P-value >SL, go to step 4. 
    Else Finish, and Our model is ready. 
Step-4: Remove that predictor. \
Step-5: Rebuild and fit the model with the remaining variables.

## Need for Backward Elimination: An optimal Multiple Linear Regression model:
Unnecessary features increase the complexity of the model. Hence it is good to have only the most significant features and keep our model simple to get the better result.

So, in order to optimize the performance of the model, we will use the Backward Elimination method. This process is used to optimize the performance of the MLR model as it will only include the most affecting feature and remove the least affecting feature. Let's start to apply it to our MLR model.

