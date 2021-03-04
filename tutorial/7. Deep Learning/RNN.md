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

