# K-Nearest Neighbor(KNN) Algorithm
- K-Nearest Neighbour is one of the simplest Machine Learning algorithms based on Supervised Learning technique.
- K-NN algorithm assumes the similarity between the new case/data and available cases and put the new case into the category that is most similar to the available categories.
- K-NN algorithm stores all the available data and classifies a new data point based on the similarity. This means when new data appears then it can be easily classified into a well suite category by using K- NN algorithm.
- K-NN algorithm can be used for Regression as well as for Classification but mostly it is used for the Classification problems.
- K-NN is a non-parametric algorithm, which means it does not make any assumption on underlying data.
- It is also called a lazy learner algorithm because it does not learn from the training set immediately instead it stores the dataset and at the time of classification, it performs an action on the dataset.
- KNN algorithm at the training phase just stores the dataset and when it gets new data, then it classifies that data into a category that is much similar to the new data.

Example: Suppose, we have an image of a creature that looks similar to cat and dog, but we want to know either it is a cat or dog. So for this identification, we can use the KNN algorithm, as it works on a similarity measure. Our KNN model will find the similar features of the new data set to the cats and dogs images and based on the most similar features it will put it in either cat or dog category.

## Why do we need a K-NN Algorithm?
Suppose there are two categories, i.e., Category A and Category B, and we have a new data point x1, so this data point will lie in which of these categories. To solve this type of problem, we need a K-NN algorithm. With the help of K-NN, we can easily identify the category or class of a particular dataset. Consider the below diagram: \
![image](https://user-images.githubusercontent.com/58425689/107843791-11073700-6df6-11eb-9a84-72651af523b8.png)

How does K-NN work?
The K-NN working can be explained on the basis of the below algorithm:

Step-1: Select the number K of the neighbors \
Step-2: Calculate the Euclidean distance of K number of neighbors \
Step-3: Take the K nearest neighbors as per the calculated Euclidean distance. \
Step-4: Among these k neighbors, count the number of the data points in each category. \
Step-5: Assign the new data points to that category for which the number of the neighbor is maximum. \
Step-6: Our model is ready. \

Suppose we have a new data point and we need to put it in the required category. Consider the below image:

![image](https://user-images.githubusercontent.com/58425689/107843813-3a27c780-6df6-11eb-8557-ef0944f2d0ea.png)

Next, we will calculate the Euclidean distance between the data points. The Euclidean distance is the distance between two points, which we have already studied in geometry. It can be calculated as:

![image](https://user-images.githubusercontent.com/58425689/107843817-3c8a2180-6df6-11eb-915b-3d0b08b67059.png)

By calculating the Euclidean distance we got the nearest neighbors, as three nearest neighbors in category A and two nearest neighbors in category B. Consider the below image:

![image](https://user-images.githubusercontent.com/58425689/107843820-3eec7b80-6df6-11eb-8b4b-55af83a0f4d1.png)

As we can see the 3 nearest neighbors are from category A, hence this new data point must belong to category A.

## How to select the value of K in the K-NN Algorithm?
Below are some points to remember while selecting the value of K in the K-NN algorithm:

- There is no particular way to determine the best value for "K", so we need to try some values to find the best out of them. The most preferred value for K is 5.
- A very low value for K such as K=1 or K=2, can be noisy and lead to the effects of outliers in the model.
- Large values for K are good, but it may find some difficulties.

## Advantages of KNN Algorithm:
- It is simple to implement.
- It is robust to the noisy training data
- It can be more effective if the training data is large.  

## Disadvantages of KNN Algorithm:
- Always needs to determine the value of K which may be complex some time.
- The computation cost is high because of calculating the distance between the data points for all the training samples.

  ```python 
  #Fitting K-NN classifier to the training set  
  from sklearn.neighbors import KNeighborsClassifier  
  classifier= KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2 )  
  classifier.fit(x_train, y_train)  
  ```
