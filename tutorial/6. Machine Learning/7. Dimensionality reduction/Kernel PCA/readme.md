[PCA](https://github.com/rjnp2/Data-Science/tree/main/tutorial/6.%20Machine%20Learning/7.%20Dimensionality%20reduction/PCA)

# Kernel PCA
We know the kernel trick, a mathematical technique that implicitlymaps instances into a very high-dimensional space (called the feature space), enabling nonlinear classification and regression with Support Vector Machines. Recall that a linear decision boundary in the high-dimensional feature space corresponds to a complex nonlinear decision boundary in the original space.

It turns out that the same trick can be applied to PCA, making it possible to perform complex nonlinear projections for dimensionality reduction. This is called Kernel PCA (kPCA). It is often good at preserving clusters of instances after projection, or sometimes even unrolling datasets that lie close to a twisted manifold.

For example, the following code uses Scikit-Learn’s KernelPCA class to perform kPCA with an RBF kernel:
```python
  from sklearn.decomposition import KernelPCA
  rbf_pca = KernelPCA(n_components = 2, kernel="rbf", gamma=0.04)
  X_reduced = rbf_pca.fit_transform(X)
```
In below Figure shows the Swiss roll, reduced to two dimensions using a linear kernel (equivalent to simply using the PCA class), an RBF kernel, and a sigmoid kernel (Logistic).

![image](https://user-images.githubusercontent.com/58425689/108450660-acccf300-728d-11eb-8188-6d04242be5d5.png)
Figure. Swiss roll reduced to 2D using kPCA with various kernels
