# Dimensionality Reduction
In machine learning classification problems, there are often too many factors on the basis of which the final classification is done. These factors are basically variables called features. The higher the number of features, the harder it gets to visualize the training set and then work on it. Sometimes, most of these features are correlated, and hence redundant. This is where dimensionality reduction algorithms come into play. \
Dimensionality reduction is the process of reducing the number of random variables under consideration, by obtaining a set of principal variables. It can be divided into feature selection and feature extraction. \
It is commonly used in the fields that deal with high-dimensional data, such as **speech recognition, signal processing, bioinformatics, etc. It can also be used for data visualization, noise reduction, cluster analysis, etc.**
___

## The Curse of Dimensionality
Handling the high-dimensional data is very difficult in practice, commonly known as the curse of dimensionality. If the dimensionality of the input dataset increases, any machine learning algorithm and model becomes more complex. As the number of features increases, the number of samples also gets increased proportionally, and the chance of overfitting also increases. If the machine learning model is trained on high-dimensional data, it becomes overfitted and results in poor performance.

Hence, it is often required to reduce the number of features, which can be done with dimensionality reduction. \
![image](https://user-images.githubusercontent.com/58425689/107955528-fd122f80-6fc5-11eb-9acc-1ece92271122.png)
___
## Main Approaches for Dimensionality Reduction
Before we dive into specific dimensionality reduction algorithms, let’s take a look at the two main approaches to reducing dimensionality: projection and Manifold Learning.

- **Projection** \
  In most real-world problems, training instances are not spread out uniformly across all dimensions. Many features are almost constant, while others are highly correlated. As a result, all training instances actually lie within (or close to) a much lower-dimensional subspace of the high-dimensional space. \
  ![r](https://user-images.githubusercontent.com/58425689/107967830-b9272680-6fd5-11eb-970a-5b8f284c1838.png) \
  Figure. A 3D dataset lying close to a 2D subspace \
  Notice that all training instances lie close to a plane: this is a lower-dimensional (2D) subspace of the high-dimensional (3D) space. Now if we project every training instance perpendicularly onto this subspace, we get the new 2D dataset. We have just reduced the dataset’s dimensionality from 3D to 2D. Note that the axes correspond to new features z 1 and z 2 (the coordinates of the projections on the plane). \
  ![r](https://user-images.githubusercontent.com/58425689/107968142-18853680-6fd6-11eb-8960-7a7135215574.png) \
  Figure. The new 2D dataset after projection
  
However, projection is not always the best approach to dimensionality reduction. In many cases the subspace may twist and turn, such as in the famous Swiss roll toy dataset. \
![r](https://user-images.githubusercontent.com/58425689/107968937-1ff90f80-6fd7-11eb-9022-fa0dcb0c92cd.png)
![rr](https://user-images.githubusercontent.com/58425689/107968941-212a3c80-6fd7-11eb-8e57-5e04d01532fb.png) \
Figure. Swiss roll dataset(left), Squashing by projecting onto a plane(middle) versus unrolling the Swiss roll(right).

- **Manifold Learning** \
  Put simply, a 2D manifold is a 2D shape that can be bent and twisted in a higher-dimensional space. More generally, a d-dimensional manifold is a part of an n-dimensional space (where d < n) that locally resembles a d-dimensional hyperplane. In the case of the Swiss roll, d = 2 and n = 3: it locally resembles a 2D plane, but it is rolled in the third dimension. 
  
  Many dimensionality reduction algorithms work by modeling the manifold on which the training instances lie; this is called Manifold Learning. It relies on the manifold assumption, also called the manifold hypothesis, which holds that most real-world high-dimensional datasets lie close to a much lower-dimensional manifold. This assumption is very often empirically observed. 
  
  Once again, think about the MNIST dataset: all handwritten digit images have some similarities. They are made of connected lines, the borders are white, they are more or less centered, and so on. If you randomly generated images, only a ridiculously tiny fraction of them would look like handwritten digits. In other words, the degrees of freedom available to you if you try to create a digit image are dramatically lower than the degrees of freedom you would have if you were allowed to generate any image you wanted. These constraints tend to squeeze the dataset into a lower-dimensional manifold. 
  
  ![r](https://user-images.githubusercontent.com/58425689/107969746-466b7a80-6fd8-11eb-946c-07be682de16c.png) \
  Figure. The decision boundary may not always be simpler with lower dimensions
___

## Benefits of applying Dimensionality Reduction
Some benefits of applying dimensionality reduction technique to the given dataset are given below:
- By reducing the dimensions of the features, the space required to store the dataset also gets reduced.
- Less Computation training time is required for reduced dimensions of features.
- Reduced dimensions of features of the dataset help in visualizing the data quickly.
- It removes the redundant features (if present) by taking care of multicollinearity.

## Disadvantages of dimensionality Reduction
There are also some disadvantages of applying the dimensionality reduction, which are given below:
- Some data may be lost due to dimensionality reduction.
- In the PCA dimensionality reduction technique, sometimes the principal components required to consider are unknown.
___
## Approaches of Dimension Reduction
There are two ways to apply the dimension reduction technique, which are given below:
___
![image](https://user-images.githubusercontent.com/58425689/107881065-8ebc6700-6f0a-11eb-8123-96ed36955f74.png)
___

1. **Feature Selection** \
  Feature selection is the process of selecting the subset of the relevant features and leaving out the irrelevant features present in a dataset to build a model of high accuracy. In other words, it is a way of selecting the optimal features from the input dataset. \
   Three methods are used for the feature selection:

    - Filters Methods \
      In this method, the dataset is filtered, and a subset that contains only the relevant features is taken.
      
    - Wrappers Methods \
      The wrapper method has the same goal as the filter method, but it takes a machine learning model for its evaluation. In this method, some features are fed to the ML model, and evaluate the performance. The performance decides whether to add those features or remove to increase the accuracy of the model. This method is more accurate than the filtering method but complex to work. 

    -  Embedded Methods: \
      Embedded methods check the different training iterations of the machine learning model and evaluate the importance of each feature. 

2. **Feature Extraction:** \
  Feature extraction is the process of transforming the space containing many dimensions into space with fewer dimensions. This approach is useful when we want to keep the whole information but use fewer resources while processing the information. \
  Some common feature extraction techniques are:
    - [Principal Component Analysis](https://github.com/rjnp2/Data-Science/tree/main/tutorial/6.%20Machine%20Learning/7.%20Dimensionality%20reduction/PCA)
    - Linear Discriminant Analysis
    - [Kernel PCA](https://github.com/rjnp2/Data-Science/blob/main/tutorial/6.%20Machine%20Learning/7.%20Dimensionality%20reduction/Kernel%20PCA/readme.md)
