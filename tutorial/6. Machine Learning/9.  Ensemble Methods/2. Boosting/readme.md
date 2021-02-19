# BOOSTING
Boosting is a sequential process, where each subsequent model attempts to correct the errors of the previous model. The succeeding models are dependent on the previous model. Let’s understand the way boosting works in the below steps.

1. A subset is created from the original dataset.
2. Initially, all data points are given equal weights.
3. A base model is created on this subset.
4. This model is used to make predictions on the whole dataset. \
  ![bo](https://github.com/rjnp2/Data-Science/blob/main/tutorial/6.%20Machine%20Learning/9.%20%20Ensemble%20Methods/images/bo1.png)
5. Errors are calculated using the actual values and predicted values.
6. The observations which are incorrectly predicted, are given higher weights. (Here, the three misclassified blue-plus points will be given higher weights)
7. Another model is created and predictions are made on the dataset. (This model tries to correct the errors from the previous model) \
  ![bo](https://github.com/rjnp2/Data-Science/blob/main/tutorial/6.%20Machine%20Learning/9.%20%20Ensemble%20Methods/images/bo2.png)
8. Similarly, multiple models are created, each correcting the errors of the previous model.
9. The final model (strong learner) is the weighted mean of all the models (weak learners). \
  ![bo](https://github.com/rjnp2/Data-Science/blob/main/tutorial/6.%20Machine%20Learning/9.%20%20Ensemble%20Methods/images/bo3.png)

Thus, the boosting algorithm combines a number of weak learners to form a strong learner. The individual models would not perform well on the entire dataset, but they work well for some part of the dataset. Thus, each model actually boosts the performance of the ensemble. \
  ![bo](https://github.com/rjnp2/Data-Science/blob/main/tutorial/6.%20Machine%20Learning/9.%20%20Ensemble%20Methods/images/bo4.png)

## Boosting algorithms:
- AdaBoost
- GBM
- XGBM
- Light GBM
- CatBoost
