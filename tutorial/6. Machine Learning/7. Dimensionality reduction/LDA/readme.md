#  LDA (Linear Discriminant Analysis)

Linear Discriminants is a statistical method of dimensionality reduction that provides the highest possible discrimination among various classes, used in machine learning to find the linear combination of features, which can separate two or more classes of objects with the best performance. The method is based on discriminant functions that are estimated based on a set of data called a training set. These discriminant functions are linear with respect to the characteristic vector.

The aim of LDA is to maximize the between-class variance and minimize the within-class variance, through a linear discriminant function, under the assumption that data in every class are described by a Gaussian probability density function with the same covariance.

It is good to understand the mathematics behind the LDA but I would not like to overwhelm anyone. We will understand by keeping things simple so it will be easy to follow for anyone.

LDA helps you find the boundaries of class clusters. This projects your data points on a line in order to differentiate the clusters as much as possible, with each cluster having a relatively close distance to a centroid.

So, the question arises-how are these clusters identified and how do we get LDA’s reduced feature set?
Basically, LDA considers a centroid of data points for each class. For example, with eleven different features, LDA will use the eleven different feature datasets to find the centroid of each of its classes. Depending on this, it now defines a new dimension which is nothing more than an axis that should fulfill two requirements.

1. Maximize the distance between each class ‘Centroid.
2. Minimize the variance within each group (which LDA calls scatter, and is represented by s2).

  Hence the essence is (mean_a — mean_b)/(S_a — S_b)
  (mean_a — mean_b) = ideally large (S_a — S_b) = ideally small
  
Here mean is nothing more than the class centroid. Variance is nothing but the spread of data across the plane. So, if the data variance is small then there will be less overlapping between the classes and the overall distinction between the different classes will be preserved.
So whatever coordinate of the new axis meets these two conditions, they form the new dataset dimension.
