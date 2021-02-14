# Gradient Descent
Gradient descent is an optimization algorithm that's used when training a machine learning model. It's based on a convex function and tweaks its parameters iteratively to minimize a given function to its local minimum.

## WHAT IS A GRADIENT?
"A gradient measures how much the output of a function changes if you change the inputs a little bit."

A gradient simply measures the change in all weights with regard to the change in error. You can also think of a gradient as the slope of a function. The higher the gradient, the steeper the slope and the faster a model can learn. But if the slope is zero, the model stops learning. In mathematical terms, a gradient is a partial derivative with respect to its inputs.

![image](https://user-images.githubusercontent.com/58425689/107880242-b78e2d80-6f05-11eb-94b0-d88dcce99106.png) \
               Figure . Gradient Descent
               
## HOW GRADIENT DESCENT WORKS
Think of gradient descent as hiking down to the bottom of a valley. This is a better analogy because it is a minimization algorithm that minimizes a given function.

The equation below describes what gradient descent does: b is the next position of our climber, while a represents his current position. The minus sign refers to the minimization part of gradient descent. The gamma in the middle is a waiting factor and the gradient term ( Δf(a) ) is simply the direction of the steepest descent.

![image](https://user-images.githubusercontent.com/58425689/107880306-05a33100-6f06-11eb-9c89-cc505e34b54c.png)

Imagine you have a machine learning problem and want to train your algorithm with gradient descent to minimize your cost-function J(w, b) and reach its local minimum by tweaking its parameters (w and b). The image below shows the horizontal axes represent the parameters (w and b), while the cost function J(w, b) is represented on the vertical axes. Gradient descent is a convex function.

![image](https://user-images.githubusercontent.com/58425689/107880324-1c498800-6f06-11eb-9d6a-784a2bcbb80b.png)

We know we want to find the values of w and b that correspond to the minimum of the cost function (marked with the red arrow). To start finding the right values we initialize w and b with some random numbers. Gradient descent then starts at that point (somewhere around the top of our illustration), and it takes one step after another in the steepest downside direction (i.e., from the top to the bottom of the illustration) until it reaches the point where the cost function is as small as possible.

## IMPORTANCE OF THE LEARNING RATE
How big the steps are gradient descent takes into the direction of the local minimum are determined by the learning rate, which figures out how fast or slow we will move towards the optimal weights.

For gradient descent to reach the local minimum we must set the learning rate to an appropriate value, which is neither too low nor too high. This is important because if the steps it takes are too big, it may not reach the local minimum because it bounces back and forth between the convex function of gradient descent (see left image below). If we set the learning rate to a very small value, gradient descent will eventually reach the local minimum but that may take a while (see the right image). 

![image](https://user-images.githubusercontent.com/58425689/107880344-371bfc80-6f06-11eb-93a7-2c61c361e65c.png)

So, the learning rate should never be too high or too low for this reason. You can check if you’re learning rate is doing well by plotting it on a graph.

## HOW TO MAKE SURE IT WORKS PROPERLY
A good way to make sure gradient descent runs properly is by plotting the cost function as the optimization runs. Put the number of iterations on the x-axis and the value of the cost-function on the y-axis. This helps you see the value of your cost function after each iteration of gradient descent, and provides a way to easily spot how appropriate your learning rate is. You can just try different values for it and plot them all together. The left image below shows such a plot, while the image on the right illustrates the difference between good and bad learning rates.

![image](https://user-images.githubusercontent.com/58425689/107880368-5d419c80-6f06-11eb-8799-90f86fa44a6e.png)

If gradient descent is working properly, the cost function should decrease after every iteration.

## TYPES OF GRADIENT DESCENT
There are three popular types of gradient descent that mainly differ in the amount of data they use: 

### BATCH GRADIENT DESCENT
Batch gradient descent, also called vanilla gradient descent, calculates the error for each example within the training dataset, but only after all training examples have been evaluated does the model get updated. This whole process is like a cycle and it's called a training epoch.

To implement Gradient Descent, you need to compute the gradient of the cost function with regards to each model parameter θ j . In other words, you need to calculate how much the cost function will change if you change θj just a little bit. This is called a partial derivative.

The partial derivative of the cost function with regards to **parameter θj , noted (∂ MSE(θ)/ ∂θj).**
              ![image](https://user-images.githubusercontent.com/58425689/107880534-772faf00-6f07-11eb-9fea-bd58e2b0264f.png)
              
Let’s look at a quick implementation of this algorithm:

   ```python
      eta = 0.1 # learning rate
      n_iterations = 1000
      m = 100

      theta = np.random.randn(2,1)     # random initialization

      for iteration in range(n_iterations):
        gradients = 2/m * X_b.T.dot(X_b.dot(theta) - y)
        theta = theta - eta * gradients
   ```

Some advantages of batch gradient descent are its computational efficient, it produces a stable error gradient and a stable convergence. Some disadvantages are the stable error gradient can sometimes result in a state of convergence that isn’t the best the model can achieve. It also requires the entire training dataset be in memory and available to the algorithm.

### STOCHASTIC GRADIENT DESCENT
By contrast, stochastic gradient descent (SGD) does this for each training example within the dataset, meaning it updates the parameters for each training example one by one. Depending on the problem, this can make SGD faster than batch gradient descent. One advantage is the frequent updates allow us to have a pretty detailed rate of improvement.

Let’s look at a quick implementation of this algorithm:

   ```python
      n_epochs = 50
      t0, t1 = 5, 50 # learning schedule hyperparameters
      def learning_schedule(t):
        return t0 / (t + t1)

      theta = np.random.randn(2,1)     # random initialization

      for epoch in range(n_epochs):
        for i in range(m):
          random_index = np.random.randint(m)
          xi = X_b[random_index:random_index+1]
          yi = y[random_index:random_index+1]
          gradients = 2 * xi.T.dot(xi.dot(theta) - yi)
          eta = learning_schedule(epoch * m + i)
          theta = theta - eta * gradients
   ```
   
The frequent updates, however, are more computationally expensive than the batch gradient descent approach. Additionally, the frequency of those updates can result in noisy gradients, which may cause the error rate to jump around instead of slowly decreasing.

### MINI-BATCH GRADIENT DESCENT
Mini-batch gradient descent is the go-to method since it’s a combination of the concepts of SGD and batch gradient descent. It simply splits the training dataset into small batches and performs an update for each of those batches. This creates a balance between the robustness of stochastic gradient descent and the efficiency of batch gradient descent.

Common mini-batch sizes range between 50 and 256, but like any other machine learning technique, there is no clear rule because it varies for different applications. This is the go-to algorithm when training a neural network and it is the most common type of gradient descent within deep learning.
