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
