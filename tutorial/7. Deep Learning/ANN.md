# Neural Networks

Neural Network or artificial neural network (ANN) are modeled the same as the human brain. \
The neural network is made up many perceptrons. Perceptron is a single layer neural network. It is a binary classifier and part of supervised learning. A simple model of the biological neuron in an artificial neural network is known as the perceptron.

The artificial neuron has input and output. \
![image](https://user-images.githubusercontent.com/58425689/108676331-2c69f480-7510-11eb-9266-6a25e81cc623.png)

## Representation of perceptron model mathematically.
![image](https://user-images.githubusercontent.com/58425689/108676345-2ecc4e80-7510-11eb-8ce7-939c139629ba.png)

Human brain has neurons for passing information, similarly neural network has nodes to perform the same task. Nodes are the mathematical functions.

A neural network is based on the structure and function of biological neural networks. A neural network itself changes or learn based on input and output. The information flows through the system affect the structure of the artificial neural network because of its learning and improving the property.

Neural networks are modeled in accordance with the human brain so as to imitate their functionality. The human brain can be defined as a neural network that is made up of several neurons, so is the Artificial Neural Network is made of numerous perceptron. \
![image](https://user-images.githubusercontent.com/58425689/108676550-7fdc4280-7510-11eb-8c33-eab4ae125aab.png) \
  fig : Multiple Perceptron Network
  
A neural network comprises of three main layers, which are as follows;

- Input layer: \
  The input layer accepts all the inputs that are provided by the programmer.
- Hidden layer: \
  In between the input and output layer, there is a set of hidden layers on which computations are performed that further results in the output.
- Output layer: \
  After the input layer undergoes a series of transformations while passing through the hidden layer, it results in output that is delivered by the output layer.

## What are Artificial Neural Networks?
Artificial Neural Networks are the computing system that is designed to simulate the way the human brain analyzes and processes the information. Artificial Neural Networks have self-learning capabilities that enable it to produce a better result as more data become available. So, if the network is trained on more data, it will be more accurate because these neural networks learn from the examples. The neural network can be configured for specific applications like data classification, pattern recognition, etc.

With the help of the neural network, we can actually see that a lot of technology has been evolved from translating webpages to other languages to having a virtual assistant to order groceries online. All of these things are possible because of neural networks. So, an artificial neural network is nothing but a network of various artificial neurons.

## Working of Artificial Neural Networks
Instead of directly getting into the working of Artificial Neural Networks, lets breakdown and try to understand Neural Network's basic unit, which is called a Perceptron.

So, a perceptron can be defined as a neural network with a single layer that classifies the linear data. It further constitutes four major components, which are as follows;

  - Inputs
  - Weights and Bias
  - Summation Functions
  - Activation or transformation function \
![image](https://user-images.githubusercontent.com/58425689/108681270-11e74980-7517-11eb-928b-eddb29801a8b.png)

The main logic behind the concept of Perceptron is as follows:

The inputs (x) are fed into the input layer, which undergoes multiplication with the allotted weights (w) followed by experiencing addition in order to form weighted sums. Then these inputs weighted sums with their corresponding weights are executed on the pertinent activation function.

### Weights and Bias
As and when the input variable is fed into the network, a random value is given as a weight of that particular input, such that each individual weight represents the importance of that input in order to make correct predictions of the result.

However, bias helps in the adjustment of the curve of activation function so as to accomplish a precise output.

### Summation Function
After the weights are assigned to the input, it then computes the product of each input and weights. Then the weighted sum is calculated by the summation function in which all of the products are added.

### Activation Function
The main objective of the activation function is to perform a mapping of a weighted sum upon the output. The transformation function comprises of activation functions such as tanh, ReLU, sigmoid, etc.
[For more details and code in python with gradients](https://github.com/rjnp2/Data-Science/tree/main/tutorial/7.%20Deep%20Learning/Activation%20Function)

## Implementation of Neural Network 
 ### Dense
 ```python
 import cupy as cp # to run on gpu
 class Dense(Layer):
    """A fully-connected NN layer.
    Parameters:
    -----------
    n_units: int
        The number of neurons in the layer.
    input_shape: tuple
        The expected input shape of the layer. For dense layers a single digit specifying
        the number of features of the input. Must be specified if it is the first layer in
        the network.
    """
    
    def __init__(self, n_units : int,
                 input_shape: tuple =None):
        self.input_shape = input_shape
        self.n_units = n_units
        self.trainable = True
                
    def initialize(self, optimizer):
        # Initialize the weights
        self.W  = cp.random.normal(loc=0.0, scale = np.sqrt(2/(self.input_shape[1] + self.n_units)), 
                                        size = ( self.input_shape[1],self.n_units))
        self.w0 = cp.random.normal(loc=0.0, scale = np.sqrt(2/self.n_units), size = (self.n_units) )
        # Weight optimizers
        self.opt  = copy.copy(optimizer)

    def parameters(self):        
        '''        
        Returns parameters
        '''
        return np.prod(self.W.shape) + np.prod(self.w0.shape)

    def forward_pass(self, X : cp.array, training : str ):
        '''
        Parameters
        ----------
        X : cp.array
            array of prevoius data.
        training : str
            trainable.

        Returns
        -------
        cp.array
            output array of dense.            
        '''
        if training :
            self.layer_input = X.copy()        
        return cp.dot(X, self.W) + self.w0

    def backward_pass(self, accum_grad : cp.array ):
        '''        
        Parameters
        ----------
        accum_grad : cp.array
            gradient with respect to weight.

        Returns
        -------
        cp.array
            gradient of activation.            
        '''        
        # Save weights used during forwards pass
        W = self.W

        if self.trainable:
            n = self.layer_input.shape[0]
            
            # Calculate gradient w.r.t layer weights                       
            grad_w = cp.dot(cp.asarray(self.layer_input).T, accum_grad) / n           
            grad_w0 = cp.sum(accum_grad, axis=0, keepdims=True) / n
                                            
            # Update the layer weights , )
            self.W , self.w0 =self.W_opt.update(w=self.W, b= self.w0 , 
                                grad_wrt_w= grad_w, grad_wrt_b =grad_w0)            

        # Return accumulated gradient for next layer
        # Calculated based on the weights used during the forward pass
        return accum_grad.dot(W.T)
 ```
 By using keras,
 ```python
    keras.layers.Dense(units, activation=None, use_bias=True, kernel_initializer='glorot_uniform')  
 ```
  The dense layer can be defined as a densely-connected common Neural Network layer. \
  The output = activation(dot(input, kernel) +bias) operation is executed by the Dense layer. \
  Here an element-wise activation function is being performed by the activation, so as to pass an activation argument, a matrix of weights called kernel is built by the layer, and bias is a vector created by the layer, which is applicable only if the use_bias is True.

  It is to be noted that if the input given to the layer has a rank greater than two, it will be flattened previously to its primary dot product with the kernel.
  
  Arguments \
  units: It refers to a positive integer that acknowledges the output space dimensionality. \
  activation: It makes sure that the dense layer utilizes the element-wise activation function.It is a linear activation, which is set to none by default. Since its linearity is limited, we don't have much of its in-built activation function.

## Advantages of ANN
- It stored the information on the entire network rather than the database.
- After the training of ANN, the data may give the result even with incomplete information.
- If one or more cell is corrupt of ANN, it does not prevent ANN to generate output.
- ANN has distributed memory that helps to generate the desired output.
- ANN can make a machine learnable.
- ANN has a parallel processing capability, which means it can perform more than one task at the same time.

## Disadvantages of ANN
- It requires a processor with parallel processing power according to their structure.
- Unexplained behaviour of the network is the main problem of ANN. ANN doesn't give a clue when it produces a probing solution.
- For the determination of the structure of ANN, no specific rules are providing.
- There is no information about the duration of the network.
- It's too typical to show the problem to the network.
