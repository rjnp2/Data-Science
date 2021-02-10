## Eigenvalues and Eigenvectors

- **Eigenvalues** \
	A scalar associated with a given linear transformation of a vector space and having the property that there is some nonzero vector which when multiplied by the scalar is equal to the vector obtained by letting the transformation operate on the vector

- **Eigenvectors** \
	In linear algebra, an eigenvector or characteristic vector of a linear transformation is a nonzero vector that changes by a scalar factor when that linear transformation is applied to it. The corresponding eigenvalue, often denoted by \lambda, is the factor by which the eigenvector is scaled. 

- **Eigenvalues & Eigenvectors Equation** \
	If A be an n×n matrix. A scalar λ is called the eigenvalue of A if there exists a non-zero vector x in R^n such that
	
			 Ax = λx. 
	and for Eigenvector: \
	     The vector x is called an eigenvector corresponding to λ.

	If I be the identity matrix of same order as A, then 
	
			(A−λI)x=0 

- **Calculation of Eigenvalues & Eigenvectors** \
	In order to find eigenvectors of a matrix, one needs to follow the following given steps: \
	Step 1: Determine the eigenvalues of given matrix A using the equation 
	
		det(A – λ I) = 0, 
	Denote each eigenvalue of λ1, λ2, λ3, … \
	Step 2: Substitute the value of λ1 in equation AX = λ1.X or (A – λ1.I) X = O. \ 
	Step 3: Calculate the value of eigenvector X which is associated with eigenvalue λ1. \
	Step 4: Repeat steps 3 and 4 for other eigenvalues λ2, λ3, … as well.
	
- **Example:**
	Calculate eigenvalues and eigenvectors of given matrix m: \
	![image](https://user-images.githubusercontent.com/58425689/106710949-e01d4a00-661e-11eb-9aeb-bb88fdf4db48.png) \
	Figure: Matrix m. \
	![image](https://user-images.githubusercontent.com/58425689/106711010-fa572800-661e-11eb-9d78-d0d3ea4ca5eb.png) \
	Figure: Derivation’s first step. \
	![image](https://user-images.githubusercontent.com/58425689/106711029-ff1bdc00-661e-11eb-84eb-6fd2be4e8b3e.png) \
	Figure: Derivation’s second step. \
	![image](https://user-images.githubusercontent.com/58425689/106711045-03e09000-661f-11eb-9b18-230724de5094.png) \
	Figure: Derivation’s third step. \
	![image](https://user-images.githubusercontent.com/58425689/106711053-06db8080-661f-11eb-9507-0c9ca9ada631.png) \
	Figure: Derivation’s fourth step. \
	![image](https://user-images.githubusercontent.com/58425689/106711063-0a6f0780-661f-11eb-81af-758860da464b.png) \
	Figure: Derivation’s fifth step. \
	![image](https://user-images.githubusercontent.com/58425689/106711068-0cd16180-661f-11eb-80d1-7aa0856bbdee.png) \
	Figure: Derivation’s sixth step. \
	Here, the Eigenvalues of m are 2 and -1. \
	There are multiple eigenvectors available to each eigenvalue

### Eigenvector Applications:  Eigenvalues In Principal Component Analysis
   PCA endeavors a projection that processes as much knowledge in the data as reasonable. It is a dimensionality reduction technique. It finds the directions of the highest variance and projects the data with them to decrease the dimensions. 
   
   **Calculation steps of PCA:** \
   Let there is an N*1 vector with values x1, x2, ….., xm. \
   Calculate the sample mean: \
	![image](https://user-images.githubusercontent.com/58425689/106730252-77da6280-6636-11eb-84bc-ad9fc2f26414.png) \
	Figure: Equation of sample mean. \
	Subtract sample mean with vector value: \
	![image](https://user-images.githubusercontent.com/58425689/106730285-7a3cbc80-6636-11eb-9d14-975e64065f0d.png) \
	Figure: Subtracting the sample mean. \
	Calculate the sample covariance matrix: \
	![image](https://user-images.githubusercontent.com/58425689/106730331-7c9f1680-6636-11eb-812e-7983035672f3.png) \
	Figure: Equation of the covariance matrix. \ 
	Calculate the eigenvalues and eigenvectors of the covariance matrix \
	![image](https://user-images.githubusercontent.com/58425689/106730382-7f9a0700-6636-11eb-8c11-4e142051a6a1.png) \
	Figure : Eigenvalues and eigenvetors. \
	Dimensionality reduction: approximate x using only the first k eigenvectors (k< N).

### Singular Value Decomposition (SVD)
Singular value decomposition is a method of decomposing a matrix into three other matrices:
 
![image](https://user-images.githubusercontent.com/58425689/105994325-99d06400-60cf-11eb-9811-0ddec63ba0c4.png)

Where:
A is an m × n matrix \
U is an m × n orthogonal matrix \
S is an n × n diagonal matrix \
V is an n × n orthogonal matrix
