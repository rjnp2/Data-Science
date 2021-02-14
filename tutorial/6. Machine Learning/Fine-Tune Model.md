# Fine-Tune Model
Tuning the hyper-parameters of an estimator. \
Hyper-parameters are parameters that are not directly learnt within estimators. In scikit-learn they are passed as arguments to the constructor of the estimator classes. Typical examples include C, kernel and gamma for Support Vector Classifier, alpha for Lasso, etc.

It is possible and recommended to search the hyper-parameter space for the best cross validation score.

Any parameter provided when constructing an estimator may be optimized in this manner. Specifically, to find the names and current values for all parameters for a given estimator, use:

    estimator.get_params()

A search consists of:
- an estimator (regressor or classifier such as sklearn.svm.SVC();
- a parameter space;
- a method for searching or sampling candidates;
- a cross-validation scheme; and
- a score function.

Two generic approaches to parameter search are provided in scikit-learn: for given values, **GridSearchCV exhaustively considers all parameter combinations,** while **RandomizedSearchCV can sample a given number of candidates from a parameter space with a specified distribution.** Both these tools have successive halving counterparts **HalvingGridSearchCV and HalvingRandomSearchCV**, which can be much faster at finding a good parameter combination.

## Grid Search
  One way to do that would be to fiddle with the hyperparameters manually, until you find a great combination of hyperparameter values. This would be very tedious work,and you may not have time to explore many combinations.
  Instead you should get Scikit-Learn’s GridSearchCV to search for you. All you need to do is tell it which hyperparameters you want it to experiment with, and what values to try out, and it will evaluate all the possible combinations of hyperparameter values, using cross-validation.

  ## code
  ```python
    from sklearn.model_selection import GridSearchCV
    grid_search = GridSearchCV(estimator, param_grid, scoring=None, cv=None)
    # Parameters: estimator: estimator object which is implement the scikit-learn estimator interface. 
                  #Either estimator needs to provide a score function, or scoring must be passed.
                  #param_grid: dict or list of dictionaries with parameters names as keys and
                  #lists of parameter settings to try.
                  #scoring: Strategy to evaluate the performance of the cross-validated model on the test set.
                  # Acc,mse
                  #cv: int, cross-validation generator Determines the cross-validation splitting strategy.
   ``` 
    
  ## Example
  ```python
    from sklearn.model_selection import GridSearchCV
    from sklearn.svm import SVC

    parameters = [{
          'kernel': ['linear', 'poly', 'rbf', 'sigmoid', 'precomputed'], 
          'C': [1,2,3,300,500],
          'max_iter': [1000,100000]}]

    clf = GridSearchCV(
          SVC(), parameters, scoring='accuracy'
      )
    clf.fit(X_train, y_train)
    print(clf.best_params_)
  ```

## Random Search Parameter Tuning
The grid search approach is fine when you are exploring relatively few combinations, like in the previous example, but when the hyperparameter search space is large, it is often preferable to use RandomizedSearchCV instead. This class can be used in much the same way as the GridSearchCV class, but instead of trying out all possible combinations, it evaluates a given number of random combinations by selecting a random value for each hyperparameter at every iteration.

This approach has two main benefits:
- If you let the randomized search run for, say, 1,000 iterations, this approach will explore 1,000 different values for each hyperparameter (instead of just a few values per hyperparameter with the grid search approach).
- You have more control over the computing budget you want to allocate to hyper‐parameter search, simply by setting the number of iterations.
  
  ## code
  ```python
    from sklearn.model_selection import RandomizedSearchCV
    randomized_search = RandomizedSearchCV(estimator, param_grid, scoring=None, cv=None)
    # Parameters: estimator: estimator object which is implement the scikit-learn estimator interface. 
                  #Either estimator needs to provide a score function, or scoring must be passed.
                  #param_grid: dict or list of dictionaries with parameters names as keys and
                  #lists of parameter settings to try.
                  #scoring: Strategy to evaluate the performance of the cross-validated model on the test set.
                  # Acc,mse
                  #cv: int, cross-validation generator Determines the cross-validation splitting strategy.
   ``` 
  
  ## Example
  ```python
    from sklearn.model_selection import RandomizedSearchCV
    from sklearn.linear_model import Ridge

    param_grid = {'alpha': uniform()}
    model = Ridge()

    clf = RandomizedSearchCV(model, parameters, random_state=0)
    
    clf.fit(X_train, y_train)
    print(clf.best_params_)
  ```
