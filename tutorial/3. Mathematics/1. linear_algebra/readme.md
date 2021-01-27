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

