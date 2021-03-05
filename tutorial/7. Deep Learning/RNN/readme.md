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
     Training an RNN is done by defining a loss function (L) that measures the error between the true label and the output, and minimizes it by using forward pass and backward pass. The following simple RNN architecture summarizes the entire backpropagation through time idea.
     
     For a single time step, the following procedure is done: first, the input arrives, then it processes trough a hidden layer/state, and the estimated label is calculated. In this phase, the loss function is computed to evaluate the difference between the true label and the estimated label. The total loss function, L, is computed, and by that, the forward pass is finished. The second part is the backward pass, where the various derivatives are calculated.
     ![image](https://user-images.githubusercontent.com/58425689/109966769-bb4ced00-7d18-11eb-9b47-e9b88633bf6a.png)
     
     The training of RNN is not trivial, as we backpropagate gradients through layers and also through time. Hence, in each time step we have to sum up all the previous contributions until the current one, as given in the equation:
     
     ![image](https://user-images.githubusercontent.com/58425689/109967125-23033800-7d19-11eb-9118-2630efc33e07.png)

      In this equation, the contribution of a state at time step k to the gradient of the entire loss function L, at time step t=T is calculated. The challenge during the training is in the ratio of the hidden state:
      
      ![image](https://user-images.githubusercontent.com/58425689/109967149-2991af80-7d19-11eb-9fab-fe96afbbc88b.png)
     
     Two common problems that occur during the backpropagation of time-series data are the vanishing and exploding gradients. The equation above has two problematic cases:
     - Vanishing Gradient
     - Exploding Gradient
   
     ![image](https://user-images.githubusercontent.com/58425689/109967486-986f0880-7d19-11eb-8c52-94a568033f14.png) \   
     In the first case, the term goes to zero exponentially fast, which makes it difficult to learn some long period dependencies. This problem is called the vanishing gradient. In the second case, the term goes to infinity exponentially fast, and their value becomes a NaN due to the unstable process. This problem is called the exploding gradient. In the following two sections, we review two approaches to deal with these problems.
     
     |Exploding gradients	|Vanishing gradients|
     |--|--|
     |Truncated BTT Instead of starting backpropagation at the last timestamp, we can choose a smaller timestamp like 10 | ReLU activation function. We can use activation like ReLU, which gives output one while calculating the gradient|
     |Clip gradients at the threshold Clip the gradient when it goes more than a threshold|RMSprop Clip the gradient when it goes higher than a threshold|
     |RMSprop to adjusting the learning rate|LSTM, GRUs The different network architecture that has been specially designed can be used to combat this problem|

## Types of RNN
The main reason that the recurrent nets are more exciting is that they allow us to operate over sequences of vectors: Sequence in the input, the output, or in the most general case, both. A few examples may this more concrete:

![image](https://user-images.githubusercontent.com/58425689/109969355-e71da200-7d1b-11eb-8dce-0499c15c0b81.png)

Each rectangle in the above image represents vectors, and arrows represent functions. Input vectors are Red, output vectors are blue, and green holds RNN's state.

- **One-to-one:** \
   This is also called Plain Neural networks. It deals with a fixed size of the input to the fixed size of output, where they are independent of previous information/output. \
   Example: Image classification.

- **One-to-Many:** \
   It deals with a fixed size of information as input that gives a sequence of data as output. \
   Example: Image Captioning takes the image as input and outputs a sentence of words.

- **Many-to-One:** \
   It takes a sequence of information as input and outputs a fixed size of the output. \
   Example: sentiment analysis where any sentence is classified as expressing the positive or negative sentiment.

- **Many-to-Many:** \
   It takes a Sequence of information as input and processes the recurrently outputs as a Sequence of data. \
   Example: Machine Translation, where the RNN reads any sentence in English and then outputs the sentence in French.

- **Bidirectional Many-to-Many:** \
   Synced sequence input and output. Notice that in every case are no pre-specified constraints on the lengths sequences because the recurrent transformation (green) is fixed and can be applied as many times as we like. \
   Example: Video classification where we wish to label every frame of the video.

## Application of RNN
1. Machine Translation
2. Speech Recognition
3. Sentiment Analysis
4. Automatic Image Tagger
