# Activation Function
  The main objective of the activation function is to perform a mapping of a weighted sum upon the output. The transformation function comprises of activation functions such as tanh, ReLU, sigmoid, etc.

  The activation function is categorized into two main parts:
   - Linear Activation Function
   - Non-Linear Activation Function 

1. **Linear Activation Function** \
  In the linear activation function, the output of functions is not restricted in between any range. Its range is specified from -infinity to infinity. For each individual neuron, the inputs get multiplied with the weight of each respective neuron, which in turn leads to the creation of output signal proportional to the input. If all the input layers are linear in nature, then the final activation of the last layer will actually be the linear function of the initial layer's input. \
  ```python
    f(x)=ax
  ```
  ![image](https://user-images.githubusercontent.com/58425689/108677661-15c49d00-7512-11eb-9f20-982d8e6f5b3d.png)

2. **Non- linear function** \
  These are one of the most widely used activation function. It helps the model in generalizing and adapting any sort of data in order to perform correct differentiation among the output. It solves the following problems faced by linear activation functions:

    - Since the non-linear function comes up with derivative functions, so the problems related to backpropagation has been successfully solved.
    - For the creation of deep neural networks, it permits the stacking up of several layers of the neurons.
    
    ![image](https://user-images.githubusercontent.com/58425689/108677670-1826f700-7512-11eb-9f4a-882b3c98e93d.png)

    The non-linear activation function is further divided into the following parts:

    2.1. [**Sigmoid or Logistic Activation Function**](https://github.com/rjnp2/Data-Science/blob/main/tutorial/7.%20Deep%20Learning/Activation%20Function/Sigmoid.py) \
    It provides a smooth gradient by preventing sudden jumps in the output values. It has an output value range between 0 and 1 that helps in the normalization of each neuron's output. For X, if it has a value above 2 or below -2, then the values of y will be much steeper. In simple language, it means that even a small change in the X can bring a lot of change in Y. \
    It's value ranges between 0 and 1 due to which it is highly preferred by binary classification whose result is either 0 or 1. \
    ```python
       sigmoid(x) = 1 / (1 + np.exp(-x))
    ```
    ![image](https://user-images.githubusercontent.com/58425689/108677673-1a895100-7512-11eb-9c96-1937f10b1d96.png)

    2.2 [**Tanh or Hyperbolic Tangent Activation Function**](https://github.com/rjnp2/Data-Science/blob/main/tutorial/7.%20Deep%20Learning/Activation%20Function/tanh.py) \
    The tanh activation function works much better than that of the sigmoid function, or simply we can say it is an advanced version of the sigmoid activation function. Since it has a value range between -1 to 1, so it is utilized by the hidden layers in the neural network, and because of this reason, it has made the process of learning much easier. \
    ```python
      tanh(x) = (2/(1 + np.exp(-2*x))) -1
     ```
    ![image](https://user-images.githubusercontent.com/58425689/108677676-1c531480-7512-11eb-8058-7ef4f21fffd8.png)

    2.3 [**ReLU(Rectified Linear Unit) Activation Function**](https://github.com/rjnp2/Data-Science/blob/main/tutorial/7.%20Deep%20Learning/Activation%20Function/ReLU.py) \
    ReLU is one of the most widely used activation function by the hidden layer in the neural network. Its value ranges from 0 to infinity. It clearly helps in solving out the problem of backpropagation. It tends out to be more expensive than the sigmoid, as well as the tanh activation function. It allows only a few neurons to get activated at a particular instance that leads to effectual as well as easier computations. \
    ```python
       ReLU(x) = cp.where(x >= 0, x, 0)
    ```    
    ![image](https://user-images.githubusercontent.com/58425689/108677684-1eb56e80-7512-11eb-98ce-68025239b38d.png)
    
    2.4 [**Softmax Function**](https://github.com/rjnp2/Data-Science/blob/main/tutorial/7.%20Deep%20Learning/Activation%20Function/Softmax.py) \
    It is one of a kind of sigmoid function whereby solving the problems of classifications. It is mainly used to handle multiple classes for which it squeezes the output of each class between 0 and 1, followed by dividing it by the sum of outputs. This kind of function is specially used by the classifier in the output layer.
    ```python
       e_x = cp.exp(x)
       Softmax(x) = e_x / cp.sum(e_x, axis=-1, keepdims=True)
    ```  
