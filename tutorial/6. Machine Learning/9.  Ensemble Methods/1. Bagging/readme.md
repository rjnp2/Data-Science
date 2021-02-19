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
    - Bagging meta-estimator
    - Random forest
