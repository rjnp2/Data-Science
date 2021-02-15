# Dimensionality Reduction
In machine learning classification problems, there are often too many factors on the basis of which the final classification is done. These factors are basically variables called features. The higher the number of features, the harder it gets to visualize the training set and then work on it. Sometimes, most of these features are correlated, and hence redundant. This is where dimensionality reduction algorithms come into play. \
Dimensionality reduction is the process of reducing the number of random variables under consideration, by obtaining a set of principal variables. It can be divided into feature selection and feature extraction. \
It is commonly used in the fields that deal with high-dimensional data, such as **speech recognition, signal processing, bioinformatics, etc. It can also be used for data visualization, noise reduction, cluster analysis, etc.**
___

## The Curse of Dimensionality
Handling the high-dimensional data is very difficult in practice, commonly known as the curse of dimensionality. If the dimensionality of the input dataset increases, any machine learning algorithm and model becomes more complex. As the number of features increases, the number of samples also gets increased proportionally, and the chance of overfitting also increases. If the machine learning model is trained on high-dimensional data, it becomes overfitted and results in poor performance.

Hence, it is often required to reduce the number of features, which can be done with dimensionality reduction. \
![image](https://user-images.githubusercontent.com/58425689/107955528-fd122f80-6fc5-11eb-9acc-1ece92271122.png)

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

## Approaches of Dimension Reduction
There are two ways to apply the dimension reduction technique, which are given below:
___
![image](https://user-images.githubusercontent.com/58425689/107881065-8ebc6700-6f0a-11eb-8123-96ed36955f74.png)
___

1. **Feature Selection** \
  Feature selection is the process of selecting the subset of the relevant features and leaving out the irrelevant features present in a dataset to build a model of high accuracy. In other words, it is a way of selecting the optimal features from the input dataset. \
   Three methods are used for the feature selection:

    - Filters Methods \
      In this method, the dataset is filtered, and a subset that contains only the relevant features is taken. Some common techniques of filters method are:
      - Correlation
      - Chi-Square Test
      - ANOVA  
      - Information Gain, etc.

    - Wrappers Methods \
      The wrapper method has the same goal as the filter method, but it takes a machine learning model for its evaluation. In this method, some features are fed to the ML model, and evaluate the performance. The performance decides whether to add those features or remove to increase the accuracy of the model. This method is more accurate than the filtering method but complex to work. Some common techniques of wrapper methods are:
      - Forward Selection
      - Backward Selection
      - Bi-directional Elimination

    -  Embedded Methods: \
      Embedded methods check the different training iterations of the machine learning model and evaluate the importance of each feature. Some common techniques of Embedded methods are:
        - LASSO
        - Elastic Net
        - Ridge Regression, etc.

2. **Feature Extraction:** \
  Feature extraction is the process of transforming the space containing many dimensions into space with fewer dimensions. This approach is useful when we want to keep the whole information but use fewer resources while processing the information. \
  Some common feature extraction techniques are:
    - Principal Component Analysis
    - Linear Discriminant Analysis
    - Kernel PCA
    - Quadratic Discriminant Analysis 
