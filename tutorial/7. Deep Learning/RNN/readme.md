# Recurrent Neural Networks

## Why not Feedforward Networks?
Feedforward networks are used to classify images. Let us understand the concept of a feedforward network with an example given below in which we trained our network for classifying various images of animals. If we feed an image of a cat, it will identify that image and provide a relevant label to that particular image. Similarly, if you feed an image of a dog, it will provide a relevant label to that image a particular image as well.

Consider the following diagram:

![image](https://user-images.githubusercontent.com/58425689/109961949-b8e79480-7d12-11eb-8e3e-8f89b255f8a7.png)

And if you notice the new output that we have got is classifying, a dog has no relation to the previous output that is of a cat, or you can say that the output at the time 't' is independent of output at a time 't-1'. It can be clearly seen that there is no relation between the new output and the previous output. So, we can say that in feedforward networks, the outputs are independent of each other.

There are a few scenarios where we will actually need the previous output to get the new output. Let us discuss one such scenario where we will necessitate using the output that has been previously obtained.

![image](https://user-images.githubusercontent.com/58425689/109961935-b422e080-7d12-11eb-821b-f03bbf5eae17.png)

Now, what happens when you read a book. You will understand that book only on the understanding of the previous words. So, if we use a feedforward network and try to predict the next word in the sentence, then in such a case, we will not be able to do that because our output will actually depend on previous outputs. But in the feedforward network, the new output is independent of the previous outputs, i.e., output at 't+1' has no relation with the output at 't-2', 't-1', and 't.' Therefore, it can be concluded that we cannot use feedforward networks for predicting the next word in the sentence. Similarly, many other examples can also be taken where we need the previous output or some information from the previous output, so as to infer the new output.

## How to overcome this challenge?

Consider the following diagram:

![image](https://user-images.githubusercontent.com/58425689/109962201-0106b700-7d13-11eb-93ab-a5949864975b.png)

We have input at 't-1', which we will feed to the network, and then we will get the output at 't-1'. Then at the next timestamp that is at a time 't', we have an input at a time 't', which will be again given to the network along with the information from the previous timestamp, i.e., 't-1' and that will further help us to get the output at 't'. Similarly, at the output for 't+1', we have two inputs; one is the new input that we give, and the other is the information coming from the previous timestamps, i.e., 't' in order to get the output at a time 't+1'. In the same way, it will go on further like this. Here we have embodied in a more generalized way to represent it. There is a loop where the information from the previous timestamp is flowing, and this is how we can solve a particular challenge.

## What are Recurrent Neural Networks?
A recurrent neural network (RNN) is a kind of artificial neural network mainly used in speech recognition and natural language processing (NLP). RNN is used in deep learning and in the development of models that imitate the activity of neurons in the human brain.

Recurrent Networks are designed to recognize patterns in sequences of data, such as text, genomes, handwriting, the spoken word, and numerical time series data emanating from sensors, stock markets, and government agencies.

A recurrent neural network looks similar to a traditional neural network except that a memory-state is added to the neurons. The computation is to include a simple memory.

The recurrent neural network is a type of deep learning-oriented algorithm, which follows a sequential approach. In neural networks, we always assume that each input and output is dependent on all other layers. These types of neural networks are called recurrent because they sequentially perform mathematical computations.

![image](https://user-images.githubusercontent.com/58425689/109964340-a6228f00-7d15-11eb-82be-640a5a60a83b.png)

Let's understand the math behind the Recurrent Neural Network by simply having a look at the image given below.

![image](https://user-images.githubusercontent.com/58425689/109965279-d7e82580-7d16-11eb-9831-f5a257d81f71.png)

Assume that 'w' is the weight matrix, and 'b' is the bias. Consider at time t=0, our input is 'xo', and we need to figure out what exactly is the 'ho'. We will substitute t=0 in the equation, as shown in the image, so as to procure the function ht value.

After that, we will find out the value of 'yo' by using values that were previously calculated when we applied it to the new formula.

The same process is repeated again and again through all the timestamps within the model so as to train it. So, this how a Recurrent Neural Networks works.

## Training Recurrent Neural Networks
Recurrent Neural Networks use a backpropagation algorithm for training, but it is applied for each timestamp. It is commonly known as Back-propagation by Time (BTT).

   - **Backpropagation Through Time (BPTT)** \
     Training an RNN is done by defining a loss function (L) that measures the error between the true label and the output, and minimizes it by using forward pass and backward pass. The following simple RNN architecture summarizes the entire backpropagation through time idea. \
     For a single time step, the following procedure is done: first, the input arrives, then it processes trough a hidden layer/state, and the estimated label is calculated. In this phase, the loss function is computed to evaluate the difference between the true label and the estimated label. The total loss function, L, is computed, and by that, the forward pass is finished. The second part is the backward pass, where the various derivatives are calculated.
     ![image](https://user-images.githubusercontent.com/58425689/109966769-bb4ced00-7d18-11eb-9b47-e9b88633bf6a.png)
     
     Two common problems that occur during the backpropagation of time-series data are the vanishing and exploding gradients. The equation above has two problematic cases:
     - Vanishing Gradient
     - Exploding Gradient

## Application of RNN
1. Machine Translation
2. Speech Recognition
3. Sentiment Analysis
4. Automatic Image Tagger

## Training through RNN
- The network takes a single time-step of the input. 
- We can calculate the current state through the current input and the previous state. 
- Now, the current state through ht-1 for the next state.
- There is n number of steps, and in the end, all the information can be joined.
- After completion of all the steps, the final step is for calculating the output.
- At last, we compute the error by calculating the difference between actual output and the predicted output.
- The error is backpropagated to the network to adjust the weights and produce a better outcome.

