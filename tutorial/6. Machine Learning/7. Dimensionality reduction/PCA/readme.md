# Principal Component Analysis
Principal Component Analysis is an unsupervised learning algorithm that is used for the dimensionality reduction in machine learning. It is a statistical process that converts the observations of correlated features into a set of linearly uncorrelated features with the help of orthogonal transformation. These new transformed features are called the **Principal Components.** It is one of the popular tools that is used for exploratory data analysis and predictive modeling. It is a technique to draw strong patterns from the given dataset by reducing the variances.

PCA generally tries to find the lower-dimensional surface to project the high-dimensional data.

PCA works by considering the variance of each attribute because the high attribute shows the good split between the classes, and hence it reduces the dimensionality. Some real-world applications of PCA are **image processing, movie recommendation system, optimizing the power allocation in various communication channels.** It is a feature extraction technique, so it contains the important variables and drops the least important variable.

The PCA algorithm is based on some mathematical concepts such as:
- **Variance and Covariance**
- **Eigenvalues and Eigen factors**

Some common terms used in PCA algorithm:

- **Dimensionality:** \
  It is the number of features or variables present in the given dataset. More easily, it is the number of columns present in the dataset.
- **Correlation:** \
  It signifies that how strongly two variables are related to each other. Such as if one changes, the other variable also gets changed. The correlation value ranges from -1 to +1. Here, -1 occurs if variables are inversely proportional to each other, and +1 indicates that variables are directly proportional to each other.
- **Orthogonal:** \
  It defines that variables are not correlated to each other, and hence the correlation between the pair of variables is zero.
- **Eigenvectors:** \
  If there is a square matrix M, and a non-zero vector v is given. Then v will be eigenvector if Av is the scalar multiple of v.
- **Covariance Matrix:** \
  A matrix containing the covariance between the pair of variables is called the Covariance Matrix.

## Principal Components in PCA
As described above, the transformed new features or the output of PCA are the Principal Components. The number of these PCs are either equal to or less than the original features present in the dataset. Some properties of these principal components are given below:

- The principal component must be the linear combination of the original features.
- These components are orthogonal, i.e., the correlation between a pair of variables is zero.
- The importance of each component decreases when going to 1 to n, it means the 1 PC has the most importance, and n PC will have the least importance.

## Steps for PCA algorithm
[Mathematics of Eigenvalues & Eigenvectors and PCA](https://github.com/rjnp2/Data-Science/blob/main/tutorial/3.%20Mathematics/1.%20linear_algebra/5.%20Eigenvalues%20%26%20Eigenvectors.md)
1. **Getting the dataset** \
Firstly, we need to take the input dataset and divide it into two subparts X and Y, where X is the training set, and Y is the validation set.

2. **Representing data into a structure** \
Now we will represent our dataset into a structure. Such as we will represent the two-dimensional matrix of independent variable X. Here each row corresponds to the data items, and the column corresponds to the Features. The number of columns is the dimensions of the dataset.

3. **Standardizing the data** \
In this step, we will standardize our dataset. Such as in a particular column, the features with high variance are more important compared to the features with lower variance.
If the importance of features is independent of the variance of the feature, then we will divide each data item in a column with the standard deviation of the column. Here we will name the matrix as Z.

4. **Calculating the Covariance of Z** \
To calculate the covariance of Z, we will take the matrix Z, and will transpose it. After transpose, we will multiply it by Z. The output matrix will be the Covariance matrix of Z.

5. **Calculating the Eigen Values and Eigen Vectors** \
Now we need to calculate the eigenvalues and eigenvectors for the resultant covariance matrix Z. Eigenvectors or the covariance matrix are the directions of the axes with high information. And the coefficients of these eigenvectors are defined as the eigenvalues.

6. **Sorting the Eigen Vectors** \
In this step, we will take all the eigenvalues and will sort them in decreasing order, which means from largest to smallest. And simultaneously sort the eigenvectors accordingly in matrix P of eigenvalues. The resultant matrix will be named as P*.

7. **Calculating the new features Or Principal Components** \
Here we will calculate the new features. To do this, we will multiply the P* matrix to the Z. In the resultant matrix Z*, each observation is the linear combination of original features. Each column of the Z* matrix is independent of each other.

8. **Remove less or unimportant features from the new dataset.** \
The new feature set has occurred, so we will decide here what to keep and what to remove. It means, we will only keep the relevant or important features in the new dataset, and unimportant features will be removed out.

## Applications of Principal Component Analysis
- PCA is mainly used as the dimensionality reduction technique in various AI applications such as computer vision, image compression, etc.
- It can also be used for finding hidden patterns if data has high dimensions. Some fields where PCA is used are Finance, data mining, Psychology, etc.

## Code
  ```python
  
     from sklearn.decomposition import PCA
     pca = PCA(n_components)
          
     #Parameters: n_components: Number of components to keep.
                  # if n_components is not set all components are kept:
                  # n_components == min(n_samples, n_features)
  ```
  |Method|Description|
  |---|---|
  fit(X[, y])|Fit the model with X.
  fit_transform(X[, y])|Fit the model with X and apply the dimensionality reduction on X.
  get_covariance()|Compute data covariance with the generative model.
  inverse_transform(X)|Transform data back to its original space.
  transform(X)|Apply dimensionality reduction to X.
  
  - **Explained Variance Ratio** \
    Another very useful piece of information is the explained variance ratio of each principal component, available via the explained_variance_ratio_ variable. It indicates the proportion of the dataset’s variance that lies along the axis of each principal component.
    
  - **Choosing the Right Number of Dimensions** \
    Instead of arbitrarily choosing the number of dimensions to reduce down to, it is generally preferable to choose the number of dimensions that add up to a sufficiently large portion of the variance (e.g., 95%). \
    By specifying the number of principal components you want to preserve, you can set n_components to be a float between 0.0 and 1.0 , indicating the
ratio of variance you wish to preserve:
    ```python
    pca = PCA(n_components=0.95)
    X_reduced = pca.fit_transform(X)
    ```  
  ![image](https://user-images.githubusercontent.com/58425689/107972564-22aa3380-6fdc-11eb-9f01-ffe3249288e4.png)
