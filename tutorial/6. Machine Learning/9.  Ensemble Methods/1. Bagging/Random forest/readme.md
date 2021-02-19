# Random Forest Algorithm
Random Forest is a popular machine learning algorithm that belongs to the supervised learning technique. It can be used for both Classification and Regression problems in ML. It is based on the concept of ensemble learning, which is a process of combining multiple classifiers to solve a complex problem and to improve the performance of the model.

As the name suggests, "Random Forest is a classifier that contains a number of decision trees on various subsets of the given dataset and takes the average to improve the predictive accuracy of that dataset." Instead of relying on one decision tree, the random forest takes the prediction from each tree and based on the majority votes of predictions, and it predicts the final output.

The greater number of trees in the forest leads to higher accuracy and prevents the problem of overfitting.

The below diagram explains the working of the Random Forest algorithm:

![image](https://user-images.githubusercontent.com/58425689/107848670-5ab74800-6e1d-11eb-9d61-36a54989dc42.png)

## Assumptions for Random Forest
Since the random forest combines multiple trees to predict the class of the dataset, it is possible that some decision trees may predict the correct output, while others may not. But together, all the trees predict the correct output. Therefore, below are two assumptions for a better Random forest classifier:

- There should be some actual values in the feature variable of the dataset so that the classifier can predict accurate results rather than a guessed result.
- The predictions from each tree must have very low correlations.

## Why use Random Forest?
Below are some points that explain why we should use the Random Forest algorithm:

- It takes less training time as compared to other algorithms.
- It predicts output with high accuracy, even for the large dataset it runs efficiently.
- It can also maintain accuracy when a large proportion of data is missing.

## How does Random Forest algorithm work?
Random Forest works in two-phase first is to create the random forest by combining N decision tree, and second is to make predictions for each tree created in the first phase.

The Working process can be explained in the below steps and diagram:
- Step-1: Select random K data points from the training set.
- Step-2: Build the decision trees associated with the selected data points (Subsets).
- Step-3: Choose the number N for decision trees that you want to build.
- Step-4: Repeat Step 1 & 2.
- Step-5: For new data points, find the predictions of each decision tree, and assign the new data points to the category that wins the majority votes.

Example: Suppose there is a dataset that contains multiple fruit images. So, this dataset is given to the Random forest classifier. The dataset is divided into subsets and given to each decision tree. During the training phase, each decision tree produces a prediction result, and when a new data point occurs, then based on the majority of results, the Random Forest classifier predicts the final decision. Consider the below image:

![image](https://user-images.githubusercontent.com/58425689/107848713-c7cadd80-6e1d-11eb-955b-6b0243609eda.png)

## Applications of Random Forest
There are mainly four sectors where Random forest mostly used:

- Banking: Banking sector mostly uses this algorithm for the identification of loan risk.
- Medicine: With the help of this algorithm, disease trends and risks of the disease can be identified.
- Land Use: We can identify the areas of similar land use by this algorithm.
- Marketing: Marketing trends can be identified using this algorithm.

### code
```python
   from sklearn.ensemble import RandomForestClassifier
   model = RandomForestClassifier(n_estimators=100, criterion='gini', max_depth=None, min_samples_split=2, 
   min_samples_leaf=1, max_leaf_nodes=None, n_jobs=None, random_state=None, max_samples=None)
   
```
  Parameters used in the algorithms:
  - n_estimators:
    - It defines the number of decision trees to be created in a random forest.
    - Generally, a higher number makes the predictions stronger and more stable, but a very large number can result in higher training time.
  - criterion:
    - It defines the function that is to be used for splitting.
    - The function measures the quality of a split for each feature and chooses the best split.
  - max_features :
    - It defines the maximum number of features allowed for the split in each decision tree.
    - Increasing max features usually improve performance but a very high number can decrease the diversity of each tree.
  - max_depth:
    - Random forest has multiple decision trees. This parameter defines the maximum depth of the trees.
  - min_samples_split:
    - Used to define the minimum number of samples required in a leaf node before a split is attempted.
    - If the number of samples is less than the required number, the node is not split.
  - min_samples_leaf:
     - This defines the minimum number of samples required to be at a leaf node.
     - Smaller leaf size makes the model more prone to capturing noise in train data.
  - max_leaf_nodes:
     - This parameter specifies the maximum number of leaf nodes for each tree.
     - The tree stops splitting when the number of leaf nodes becomes equal to the max leaf node.
  - n_jobs:
     - This indicates the number of jobs to run in parallel.
     - Set value to -1 if you want it to run on all cores in the system.
  - random_state:
     - This parameter is used to define the random selection.
     - It is used for comparison between various models.
   
