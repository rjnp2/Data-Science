# Cross-Validation in Machine Learning
Cross-validation is a technique for validating the model efficiency by training it on the subset of input data and testing on previously unseen subset of the input data. We can also say that it is a technique to check how a statistical model generalizes to an independent dataset.

In machine learning, there is always the need to test the stability of the model. It means based only on the training dataset; we can't fit our model on the training dataset. For this purpose, we reserve a particular sample of the dataset, which was not part of the training dataset. After that, we test our model on that sample before deployment, and this complete process comes under cross-validation. This is something different from the general train-test split.

Hence the basic steps of cross-validations are: 
- Reserve a subset of the dataset as a validation set.
- Provide the training to the model using the training dataset.
- Now, evaluate model performance using the validation set. If the model performs well with the validation set, perform the further step, else check for the issues.

## Methods used for Cross-Validation
There are some common methods that are used for cross-validation. These methods are given below:

- **Validation Set Approach** \
  We divide our input dataset into a training set and test or validation set in the validation set approach. Both the subsets are given 50% of the dataset.

  But it has one of the big disadvantages that we are just using a 50% dataset to train our model, so the model may miss out to capture important information of the dataset. It also tends to give the underfitted model.
  ```python
    # sample()  function to split the set of observations into two halves.
    # data: pd dataframe
    train_df = data.sample(196, random_state = 1)
    test_df = data[~data.isin(train_df)].dropna(how = 'all')
  ```

- **Leave-P-out cross-validation** \
  In this approach, the p datasets are left out of the training data. It means, if there are total n datapoints in the original input dataset, then n-p data points will be used as the training dataset and the p data points as the validation set. This complete process is repeated for all the samples, and the average error is calculated to know the effectiveness of the model.

  There is a disadvantage of this technique; that is, it can be computationally difficult for the large p.
  
  ```python
     from sklearn.model_selection import LeavePOut
     lpo = LeavePOut(p)
  ```
  ![image](https://user-images.githubusercontent.com/58425689/107875910-b4397880-6eea-11eb-8a5c-ca2193c919b1.png)
  
- **Leave one out cross-validation** \
  This method is similar to the leave-p-out cross-validation, but instead of p, we need to take 1 dataset out of training. It means, in this approach, for each learning set, only one datapoint is reserved, and the remaining dataset is used to train the model. This process repeats for each datapoint. Hence for n samples, we get n different training set and n test set. It has the following features:

  - In this approach, the bias is minimum as all the data points are used.
  - The process is executed for n times; hence execution time is high.
  - This approach leads to high variation in testing the effectiveness of the model as we iteratively check against one data point.
  
  
  ```python
     from sklearn.model_selection import LeaveOneOut
     lpo = LeaveOneOut()
  ```
  ![image](https://user-images.githubusercontent.com/58425689/107875891-923ff600-6eea-11eb-811e-539b89430281.png)
  
- **K-fold cross-validation** \
  K-fold cross-validation approach divides the input dataset into K groups of samples of equal sizes. These samples are called folds. For each learning set, the prediction function uses k-1 folds, and the rest of the folds are used for the test set. This approach is a very popular CV approach because it is easy to understand, and the output is less biased than other methods.

  The steps for k-fold cross-validation are:
  - Split the input dataset into K groups
  - For each group:
    - Take one group as the reserve or test data set.
    - Use remaining groups as the training dataset
    - Fit the model on the training set and evaluate the performance of the model using the test set.
  Let's take an example of 5-folds cross-validation. So, the dataset is grouped into 5 folds. On 1st iteration, the first fold is reserved for test the model, and rest are used to train the model. On 2nd iteration, the second fold is used to test the model, and rest are used to train the model. This process will continue until each fold is not used for the test fold. \

  Consider the below diagram:
  ![image](https://user-images.githubusercontent.com/58425689/107875293-3de74700-6ee7-11eb-9acb-e1dbe0577259.png)
  ```python
     from sklearn.model_selection import KFold
     fk = KFold(n_splits)
  ```
  ![image](https://user-images.githubusercontent.com/58425689/107876067-a9331800-6eeb-11eb-9dbf-1ff0a18d4d0f.png)

- **Stratified k-fold cross-validation** \
  This technique is similar to k-fold cross-validation with some little changes. This approach works on stratification concept, it is a process of rearranging the data to ensure that each fold or group is a good representative of the complete dataset. To deal with the bias and variance, it is one of the best approaches.

  It can be understood with an example of housing prices, such that the price of some houses can be much high than other houses. To tackle such situations, a stratified k-fold cross-validation technique is useful.
  ```python
     from sklearn.model_selection import StratifiedKFold
     fk = StratifiedKFold(n_splits)
  ```
  ![image](https://user-images.githubusercontent.com/58425689/107876133-370f0300-6eec-11eb-9ba9-fddf82398a63.png)
