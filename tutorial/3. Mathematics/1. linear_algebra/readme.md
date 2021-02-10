# Linear Algebra
Linear algebra is a branch of mathematics, but the truth of it is that linear algebra is the mathematics of data. Matrices and vectors are the language of data.

Linear algebra is about linear combinations. That is, using arithmetic on columns of numbers called vectors and arrays of numbers called matrices, to create new columns and arrays of numbers. Linear algebra is the study of lines and planes, vector spaces and mappings that are required for linear transforms.

## Applications of Linear Algebra

  1. Matrices in Engineering, such as a line of springs.
  2. Graphs and Networks, such as analyzing networks.
  3. Markov Matrices, Population, and Economics, such as population growth.
  4. Linear Programming, the simplex optimization method.
  5. Fourier Series: Linear Algebra for functions, used widely in signal processing.
  6. Linear Algebra for statistics and probability, such as least squares for regression.
  7. Computer Graphics, such as the various translation, rescaling and rotation of images.
  
   - [**Simple_Algebra**](https://github.com/rjnp2/Data-Science/blob/main/tutorial/3.%20Mathematics/1.%20linear_algebra/1.%20algebra.md), [**Vectors_Spaces**](https://github.com/rjnp2/Data-Science/blob/main/tutorial/3.%20Mathematics/1.%20linear_algebra/2.%20vector.md) and **Norms** 
       

# 1. Linear Equations 
A linear equation is just a series of terms and mathematical operations where some terms are unknown.

    For example: y = 4 * x + 1
        
Equations like this are linear in that they describe a line on a two-dimensional graph. The line comes from plugging in different values into the unknown x to find out what the equation or model does to the value of y.

## 1.1 systems of Linear Equations
A system of linear equations is usually a set of two linear equations with two variables.

  - x+y=5 and 2x-y=1 are both linear equations with two variables.
  - When considered together, they form a system of linear equations.

A linear equation with two variables has an infinite number of solutions (for example, consider how (0,5), (1,4), (2,3) etc. are all solutions to the equation x+y=5. However, systems of two linear equations with two variables can have a single solution that satisfies both solutions.

		(2,3) is the only solution to both x+y=5and 2x-y=1.
    
This is solved by :

  1. Look at two ways to solve systems of linear equations algebraically: substitution and elimination.
  2. Look at systems of linear equations graphically to help us understand when systems of linear equations have one solution, no solutions, or infinitely many solutions.
  3. Explore algebraic methods of identifying the number of solutions that exist for systems with two linear equations.
  
# 2. Matrices and Vectors
A matrix is an array of numbers, symbols or expressions, made up of rows and columns. A matrix is characterized by the amount of rows, m, and the amount of columns, n, it has. 

  ##### Order of a Matrix : 
    The order of a matrix is defined in terms of its number of rows and columns. 
    Order of a matrix = No. of rows ×No. of columns , ‘m x n’ (read: “m by n”).
    
Below, we display an example 2 x 3 matrix A:

![image](https://user-images.githubusercontent.com/58425689/105944955-66b8b100-608c-11eb-99c2-912b75178365.png)

We can refer to individual elements of the matrix through its corresponding row and column. For example, A[1, 2] = 2, since in the first row and second column the number 2 is placed.

A matrix with only a single column is called a vector. For example, every column of the matrix A above is a vector. Let us take the first column of the matrix A as the vector v:

 ![image](https://user-images.githubusercontent.com/58425689/105944944-63252a00-608c-11eb-994d-be12076c5dfe.png)

## Matrix Operations
Our ability to analyze and solve particular problems within the field of linear algebra will be greatly enhanced when we can perform algebraic operations with matrices. Here, the most important basic tools for performing these operations are listed.

### (i) Matrix Sums
If A and B are m x n matrices, then the sum A+B is the m x n matrix whose columns are the sums of the corresponding columns in A and B. The sum A+B is defined only when A and B are the same size.

![image](https://user-images.githubusercontent.com/58425689/105945053-a1224e00-608c-11eb-84e9-0c7ce5ddfc49.png)

Of course, subtraction of the matrices, A-B, works in the same way, where the columns in B are subtracted from the columns in A.

### (ii) Scalar Multiples
If r is a scalar, then the scalar multiple of the matrix A is r*A, which is the matrix whose columns are r times the corresponding columns in A.

![image](https://user-images.githubusercontent.com/58425689/105945063-a4b5d500-608c-11eb-92ee-d1ad76196287.png)

### (iii) Matrix-Vector Multiplication
If the matrix A is of size m x n (thus, it has n columns), and u is a vector of size n, then the product of A and u, denoted by Au, is the linear combination of the columns of A using the corresponding entries in u as weights.

![image](https://user-images.githubusercontent.com/58425689/105945072-a8495c00-608c-11eb-9fe7-a17b69f78e6d.png)

### (iv) Matrix Multiplication
If A is an m x n matrix and B = [b1, b2, …, bp] is an n x p matrix where bi is the i-th column of the matrix B, then the matrix product AB is the m x p matrix whose columns are Ab1, Ab2, …, Abp. So, essentially, we perform the same procedure as in (iii) with matrix-vector multiplication, where each column of the matrix B is a vector.

![image](https://user-images.githubusercontent.com/58425689/105945077-ab444c80-608c-11eb-89ae-c2fe7c201c4e.png)

#### Properties of Matrix addition and multiplication: 
    1. A+B = B+A (Commutative)
    2. (A+B)+C = A+ (B+C) (Associative)
    3. AB ? BA (Not Commutative)
    4. (AB) C = A (BC) (Associative)
    5. A (B+C) = AB+AC (Distributive)

### (v) Powers of a Matrix
If A is an n x n matrix and k is a positive integer, then A^k (A to the power k) is the product of k copies of A:

![image](https://user-images.githubusercontent.com/58425689/105945086-aed7d380-608c-11eb-917c-843962719703.png)

### (vi) Matrix Transpose
Suppose we have a matrix A of size m x n, then the transpose of A (denoted by A^T) is the n x m matrix whose columns are formed from the corresponding rows of A.
if A= [aij] mxn , then AT = [bij] nxm where bij = aji.

![image](https://user-images.githubusercontent.com/58425689/105945097-b26b5a80-608c-11eb-9858-496fe164f53f.png)

### Properties of transpose of a matrix:

![image](https://user-images.githubusercontent.com/58425689/105945362-41787280-608d-11eb-95ee-3cf7bb560234.png)

## (vii) Adjoint of a square matrix:
The adjoint of a matrix A is the transpose of the cofactor matrix of A

![image](https://user-images.githubusercontent.com/58425689/105945520-88666800-608d-11eb-914a-a8ede1894c9c.png)

### Cofactor
A cofactor is the number you get when you remove the column and row of a designated element in a matrix, which is just a numerical grid in the form of a rectangle or a square. The cofactor is always preceded by a positive (+) or negative (-) sign, depending whether the element is in a + or - position.

![image](https://user-images.githubusercontent.com/58425689/105945553-99af7480-608d-11eb-9289-298d0ebceaf2.png)

### Determinant matrix
The determinant is defined as a scalar value which is associated with the square matrix. If X is a matrix, then the determinant of a matrix is represented by |X| or det (X).
Let us assume a 2×2 square matrix

![image](https://user-images.githubusercontent.com/58425689/105946919-3d018900-6090-11eb-8be9-192c533d0b22.png)

Finding Determinants for 3×3 Matrix
Now, assume the 3×3 matrix, say

![image](https://user-images.githubusercontent.com/58425689/105946929-40951000-6090-11eb-9d1b-1b977f8fbd33.png)

## (vii) Matrix Inverse
Inverse of a matrix is defined usually for square matrices. For every m × n square matrix, there exists an inverse matrix. If A is the square matrix then A-1 is the inverse of matrix A and satisfies the property:

	AA-1 = A-1A = I, where I is the Identity matrix.
Also, the determinant of the square matrix here should not be equal to zero.

![image](https://user-images.githubusercontent.com/58425689/105946938-43900080-6090-11eb-9925-9267a088cb3c.png)

![image](https://user-images.githubusercontent.com/58425689/105946944-45f25a80-6090-11eb-911e-4ca7e0077a54.png)

## Vector Norms
Vector norms measure the magnitude of a vector. Fundamentally, the size of a given variable x can be represented by its norm ||x||, and the norm represents the distance between two variables x and y, and it is represented by ||x-y||.\
The general equation of the vector norm: \
![image](https://user-images.githubusercontent.com/58425689/106708804-94b56c80-661b-11eb-9144-adf070a7d549.png)

These are the general classes of p-norms:

   - **L1 norm or Manhattan Norm.**
   The L1 norm on R^n is defined for x ∈ R^n as shown in figure: \
	![image](https://user-images.githubusercontent.com/58425689/106709005-ef4ec880-661b-11eb-9f3e-690fca1f0d08.png) \
		Figure: L1 norm or Manhattan norm equation. \
        ![image](https://user-images.githubusercontent.com/58425689/106709014-f37ae600-661b-11eb-88dd-02e6fc593ccc.png) \
		Figure: L1 norm representation.

   - **L2 norm or Euclidean Norm.**
   The L2 norm of x∈R^n is defined as: \
   	![image](https://user-images.githubusercontent.com/58425689/106709200-42288000-661c-11eb-9ff6-2be82a3efd9d.png) \
  			 Figure: L2 norm or Euclidean norm equation. \
	![image](https://user-images.githubusercontent.com/58425689/106709210-46549d80-661c-11eb-9ae4-75fe917bb511.png) \
			Figure: L2 norm representation.

# L1 and L2 norms are used in Regularization.

## Matrix Decomposition
   A matrix decomposition is a way of reducing a matrix into its constituent parts. \
   It is an approach that can simplify more complex matrix operations that can be performed on the decomposed matrix rather than on the original matrix itself. \
   A common analogy for matrix decomposition is the factoring of numbers, such as the factoring of 10 into 2 x 5. For this reason, matrix decomposition is also called matrix factorization. Like factoring real values, there are many ways to decompose a matrix, hence there are a range of different matrix decomposition techniques. \
   Two simple and widely used matrix decomposition methods are the LU matrix decomposition and the QR matrix decomposition.
   
- **LU Decomposition**
	L U decomposition of a matrix is the factorization of a given square matrix into two triangular matrices, one upper triangular matrix and one lower triangular matrix, such that the product of these two matrices gives the original matrix. \
	A square matrix A can be decomposed into two square matrices L and U such that A = L U where U is an upper triangular matrix formed as a result of applying Gauss Elimination Method on A; and L is a lower triangular matrix with diagonal elements being equal to 1. \
	For A = ![image](https://user-images.githubusercontent.com/58425689/106712190-b533f580-6620-11eb-8cf9-76057fc671da.png), 

	we have L = ![image](https://user-images.githubusercontent.com/58425689/106712226-c1b84e00-6620-11eb-8f6f-68fcbec70c03.png)
	 and U = ![image](https://user-images.githubusercontent.com/58425689/106712239-c54bd500-6620-11eb-9d5a-76fb20d3bc81.png);

	 such that A = L U. \
	 ![image](https://user-images.githubusercontent.com/58425689/106712246-c846c580-6620-11eb-872c-26857512ca0a.png)
	 
- **QR Decomposition/Factorization**
	QR decomposition, also known as QR factorization, is a method used when converting a matrix into the form A = QR. In the formula, A represents the starting matrix, Q represents an orthogonal matrix, and R represents an upper triangle matrix. An upper triangle matrix is a special kind of square matrix in which all of the entries below the main diagonal are zero. Often, QR decomposition is used in solving the linear least squares problem.
	
	- **QR Decomposition and Machine Learning**
	QR decomposition can be useful in machine learning applications. An example of using QR decomposition in machine learning is the automatic removal of an object from an image.

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
