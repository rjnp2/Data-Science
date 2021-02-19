# Ensemble methods
Ensemble methods is a machine learning technique that combines several base models in order to produce one optimal predictive model. \
Ensembles can give us boost in the machine learning result by combining several models. Basically, ensemble models consist of several individually trained supervised learning models and their results are merged in various ways to achieve better predictive performance compared to a single model. Ensemble methods can be divided into following two groups −

- Sequential ensemble methods \
As the name implies, in these kind of ensemble methods, the base learners are generated sequentially. The motivation of such methods is to exploit the dependency among base learners.

- Parallel ensemble methods \
As the name implies, in these kind of ensemble methods, the base learners are generated in parallel. The motivation of such methods is to exploit the independence among base learners.
___
## Simple Ensemble Techniques
- **Max Voting** \
  The max voting method is generally used for classification problems. In this technique, multiple models are used to make predictions for each data point. The predictions by each model are considered as a ‘vote’. The predictions which we get from the majority of the models are used as the final prediction.

  For example, when you asked 5 of your colleagues to rate your movie (out of 5); we’ll assume three of them rated it as 4 while two of them gave it a 5. Since the majority gave a rating of 4, the final rating will be taken as 4. You can consider this as taking the mode of all the predictions.
  Sample Code:
  
  Here x_train consists of independent variables in training data, y_train is the target variable for training data. The validation set is x_test (independent variables) and y_test (target variable).
  ```python
  model1 = tree.DecisionTreeClassifier()
  model2 = KNeighborsClassifier()
  model3= LogisticRegression()

  model1.fit(x_train,y_train)
  model2.fit(x_train,y_train)
  model3.fit(x_train,y_train)

  pred1=model1.predict(x_test)
  pred2=model2.predict(x_test)
  pred3=model3.predict(x_test)

  final_pred = np.array([])
  for i in range(0,len(x_test)):
      final_pred = np.append(final_pred, mode([pred1[i], pred2[i], pred3[i]]))
  ```
  Alternatively, you can use “VotingClassifier” module in sklearn as follows:
  ```python
  from sklearn.ensemble import VotingClassifier
  
  model1 = LogisticRegression(random_state=1)
  model2 = tree.DecisionTreeClassifier(random_state=1)
  model = VotingClassifier(estimators=[('lr', model1), ('dt', model2)], voting='hard')
  
  model.fit(x_train,y_train)
  model.score(x_test,y_test)
  ```
  ___
- **Averaging** \
  Similar to the max voting technique, multiple predictions are made for each data point in averaging. In this method, we take an average of predictions from all the models and use it to make the final prediction. Averaging can be used for making predictions in regression problems or while calculating probabilities for classification problems.

  For example, in the above case, the averaging method would take the average of all the values.
  i.e. (5+4+5+4+4)/5 = 4.4
  
  Sample Code:
  ```python
  model1 = tree.DecisionTreeClassifier()
  model2 = KNeighborsClassifier()
  model3= LogisticRegression()

  model1.fit(x_train,y_train)
  model2.fit(x_train,y_train)
  model3.fit(x_train,y_train)

  pred1=model1.predict_proba(x_test)
  pred2=model2.predict_proba(x_test)
  pred3=model3.predict_proba(x_test)

  finalpred=(pred1+pred2+pred3)/3
  ```
  ___
- **Weighted Averaging** \
  This is an extension of the averaging method. All models are assigned different weights defining the importance of each model for prediction. For instance, if two of your colleagues are critics, while others have no prior experience in this field, then the answers by these two friends are given more importance as compared to the other people.

  The result is calculated as [(5*0.23) + (4*0.23) + (5*0.18) + (4*0.18) + (4*0.18)] = 4.41.

  | |Colleague 1	|Colleague 2	|Colleague 3	|Colleague 4	|Colleague 5|	
  |--|--|--|--|--|--|
  weight	|0.23	|0.23	|0.18	|0.18	|0.18	
  rating	|5|	4|	5|	4	|4	| 
  
  Sample Code:
  ```python
  model1 = tree.DecisionTreeClassifier()
  model2 = KNeighborsClassifier()
  model3= LogisticRegression()

  model1.fit(x_train,y_train)
  model2.fit(x_train,y_train)
  model3.fit(x_train,y_train)

  pred1=model1.predict_proba(x_test)
  pred2=model2.predict_proba(x_test)
  pred3=model3.predict_proba(x_test)

  finalpred=(pred1*0.3+pred2*0.3+pred3*0.4)
  ```
  ___
  ___
## Advanced Ensemble techniques
1. **Stacking** \
    Stacking is an ensemble learning technique that uses predictions from multiple models (for example decision tree, knn or svm) to build a new model. This model is used for making predictions on the test set. Below is a step-wise explanation for a simple stacked ensemble:
    - The train set is split into 10 parts. \
      ![EM](https://github.com/rjnp2/Data-Science/blob/main/tutorial/6.%20Machine%20Learning/9.%20%20Ensemble%20Methods/images/1.png) 
    - A base model (suppose a decision tree) is fitted on 9 parts and predictions are made for the 10th part. This is done for each part of the train set. \
      ![EM](https://github.com/rjnp2/Data-Science/blob/main/tutorial/6.%20Machine%20Learning/9.%20%20Ensemble%20Methods/images/2.png)
    - The base model (in this case, decision tree) is then fitted on the whole train dataset. \
    - Using this model, predictions are made on the test set. \
      ![EM](https://github.com/rjnp2/Data-Science/blob/main/tutorial/6.%20Machine%20Learning/9.%20%20Ensemble%20Methods/images/3.png)
    - Steps 2 to 4 are repeated for another base model (say knn) resulting in another set of predictions for the train set and test set. \
      ![EM](https://github.com/rjnp2/Data-Science/blob/main/tutorial/6.%20Machine%20Learning/9.%20%20Ensemble%20Methods/images/4.png)
    - The predictions from the train set are used as features to build a new model. \
      ![EM](https://github.com/rjnp2/Data-Science/blob/main/tutorial/6.%20Machine%20Learning/9.%20%20Ensemble%20Methods/images/5.png)
    - This model is used to make final predictions on the test prediction set.
  
      Sample code: \
      We first define a function to make predictions on n-folds of train and test dataset. This function returns the predictions for train and test for each model.
      ```python
       def Stacking(model,train,y,test,n_fold):
         folds=StratifiedKFold(n_splits=n_fold,random_state=1)
         test_pred=np.empty((test.shape[0],1),float)
         train_pred=np.empty((0,1),float

         for train_indices,val_indices in folds.split(train,y.values):
            x_train,x_val=train.iloc[train_indices],train.iloc[val_indices]
            y_train,y_val=y.iloc[train_indices],y.iloc[val_indices]

            model.fit(X=x_train,y=y_train)
            train_pred=np.append(train_pred,model.predict(x_val))
            test_pred=np.append(test_pred,model.predict(test))
         return test_pred.reshape(-1,1),train_pred
       ```
      Now we’ll create two base models – decision tree and knn.
      ```python
        model1 = tree.DecisionTreeClassifier(random_state=1)

        test_pred1 ,train_pred1=Stacking(model=model1,n_fold=10, train=x_train,test=x_test,y=y_train)

        train_pred1=pd.DataFrame(train_pred1)
        test_pred1=pd.DataFrame(test_pred1)
        model2 = KNeighborsClassifier()

        test_pred2 ,train_pred2=Stacking(model=model2,n_fold=10,train=x_train,test=x_test,y=y_train)

        train_pred2=pd.DataFrame(train_pred2)
        test_pred2=pd.DataFrame(test_pred2)
      ```
      Create a third model, logistic regression, on the predictions of the decision tree and knn models.
      ```python
        df = pd.concat([train_pred1, train_pred2], axis=1)
        df_test = pd.concat([test_pred1, test_pred2], axis=1)

        model = LogisticRegression(random_state=1)
        model.fit(df,y_train)
        model.score(df_test, y_test)
      ```
       In order to simplify the above explanation, the stacking model we have created has only two levels. The decision tree and knn models are built at level zero, while a logistic regression model is built at level one. Feel free to create multiple levels in a stacking model.
      ___
2. **Blending** \
    Blending follows the same approach as stacking but uses only a holdout (validation) set from the train set to make predictions. In other words, unlike stacking, the predictions are made on the holdout set only. The holdout set and the predictions are used to build a model which is run on the test set. Here is a detailed explanation of the blending process:
    - The train set is split into training and validation sets. \
      ![bl](https://github.com/rjnp2/Data-Science/blob/main/tutorial/6.%20Machine%20Learning/9.%20%20Ensemble%20Methods/images/Bl1.png)
    - Model(s) are fitted on the training set.
    - The predictions are made on the validation set and the test set. \
      ![bl](https://github.com/rjnp2/Data-Science/blob/main/tutorial/6.%20Machine%20Learning/9.%20%20Ensemble%20Methods/images/Bl2.png)
    - The validation set and its predictions are used as features to build a new model.
    - This model is used to make final predictions on the test and meta-features.
  
    Sample Code:\
    We’ll build two models, decision tree and knn, on the train set in order to make predictions on the validation set.
    ```python
    model1 = tree.DecisionTreeClassifier()
    model1.fit(x_train, y_train)
    val_pred1=model1.predict(x_val)
    test_pred1=model1.predict(x_test)
    val_pred1=pd.DataFrame(val_pred1)
    test_pred1=pd.DataFrame(test_pred1)

    model2 = KNeighborsClassifier()
    model2.fit(x_train,y_train)
    val_pred2=model2.predict(x_val)
    test_pred2=model2.predict(x_test)
    val_pred2=pd.DataFrame(val_pred2)
    test_pred2=pd.DataFrame(test_pred2)
    ```
    Combining the meta-features and the validation set, a logistic regression model is built to make predictions on the test set.
    ```python
    df_val=pd.concat([x_val, val_pred1,val_pred2],axis=1)
    df_test=pd.concat([x_test, test_pred1,test_pred2],axis=1)

    model = LogisticRegression()
    model.fit(df_val,y_val)
    model.score(df_test,y_test)
    ```
    ___
3. [**Bagging**]\(https://github.com/rjnp2/Data-Science/tree/main/tutorial/6.%20Machine%20Learning/9.%20%20Ensemble%20Methods/1.%20Bagging) \
   The idea behind bagging is combining the results of multiple models (for instance, all decision trees) to get a generalized result. \
   Bagging algorithms
    - Bagging meta-estimator
    - [Random forest](https://github.com/rjnp2/Data-Science/tree/main/tutorial/6.%20Machine%20Learning/9.%20%20Ensemble%20Methods/1.%20Bagging/Random%20forest)
   ___
5. **Boosting** \
   Boosting is a sequential process, where each subsequent model attempts to correct the errors of the previous model. The succeeding models are dependent on the previous model. \
   Boosting algorithms:
    - AdaBoost
    - GBM
    - XGBM
    - Light GBM
    - CatBoost
  ___
____
