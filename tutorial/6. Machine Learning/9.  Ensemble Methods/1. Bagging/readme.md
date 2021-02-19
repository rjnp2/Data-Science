# Bagging
The idea behind bagging is combining the results of multiple models (for instance, all decision trees) to get a generalized result. Here’s a question: If you create all the models on the same set of data and combine it, will it be useful? There is a high chance that these models will give the same result since they are getting the same input. So how can we solve this problem? One of the techniques is **bootstrapping.**

**Bootstrapping** is a sampling technique in which we create subsets of observations from the original dataset, with replacement. The size of the subsets is the same as the size of the original set.

Bagging (or Bootstrap Aggregating) technique uses these subsets (bags) to get a fair idea of the distribution (complete set). The size of subsets created for bagging may be less than the original set. \
![BA](https://github.com/rjnp2/Data-Science/blob/main/tutorial/6.%20Machine%20Learning/9.%20%20Ensemble%20Methods/images/BA1.png)

  1. Multiple subsets are created from the original dataset, selecting observations with replacement.
  2. A base model (weak model) is created on each of these subsets.
  3. The models run in parallel and are independent of each other.
  4. The final predictions are determined by combining the predictions from all the models.
  ![BA](https://github.com/rjnp2/Data-Science/blob/main/tutorial/6.%20Machine%20Learning/9.%20%20Ensemble%20Methods/images/BA2.png)

## Bagging algorithms
1. **Bagging meta-estimator**
  Bagging meta-estimator is an ensembling algorithm that can be used for both classification (BaggingClassifier) and regression (BaggingRegressor) problems. It follows the typical bagging technique to make predictions. Following are the steps for the bagging meta-estimator algorithm:

   - Random subsets are created from the original dataset (Bootstrapping).
   - The subset of the dataset includes all features.
   - A user-specified base estimator is fitted on each of these smaller sets.
   - Predictions from each model are combined to get the final result.
   Code:
   ```python
   from sklearn.ensemble import BaggingClassifier,BaggingRegressor
   from sklearn import tree

   model = BaggingClassifier(tree.DecisionTreeClassifier(random_state=1))
   model.fit(x_train, y_train)
   model.score(x_test,y_test)
   ```
   Parameters used in the  algorithms: 
    - base_estimator: 
      - It defines the base estimator to fit on random subsets of the dataset.
      - When nothing is specified, the base estimator is a decision tree.
    - n_estimators: 
      - It is the number of base estimators to be created.
      - The number of estimators should be carefully tuned as a large number would take a very long time to run, while a very small number might not provide the best results.
    - max_samples:
      - This parameter controls the size of the subsets.
      - It is the maximum number of samples to train each base estimator.
    - max_features:
      - Controls the number of features to draw from the whole dataset.
      - It defines the maximum number of features required to train each base estimator.
    - n_jobs:
      - The number of jobs to run in parallel.
      - Set this value equal to the cores in your system.
      - If -1, the number of jobs is set to the number of cores.
    - random_state:
      - It specifies the method of random split. When random state value is same for two models, the random selection is same for both models.
      - This parameter is useful when you want to compare different models.

2. **Random forest**
