# Long Short-Term Memory Networks (LSTMs)
Long Short-Term Memory networks, which are commonly known as "LSTMs," are a special kind of Recurrent Neural Networks that are capable enough of learning long-term dependencies.

For example, LSTM is an application to tasks such as unsegmented, connected handwriting recognition, or speech recognition.

A general LSTM unit is composed of a cell, an input gate, an output gate, and a forget gate. The cell remembers values over arbitrary time intervals, and three gates regulate the flow of information into and out of the cell. LSTM is well-suited to classify, process, and predict the time series given of unknown duration.

![110087685-0ff57400-7dbc-11eb-836b-70018e76ff76](https://user-images.githubusercontent.com/58425689/110088028-77132880-7dbc-11eb-920b-d985b6c45269.png)

## What are long-term dependencies?
It has happened many times that we only require recent data in order to perform questions in a model. But at the same time, we may also need data that has been previously obtained.

Consider the following example to have a better understanding of it.

Let's suppose there is a language model, which is trying to predict the next word on the basis of the previous ones. Assume that we are trying to predict the last word in the sentence say, "The car runs on the road".

Here the context is quite simple because the last word always ends up being a road. By incorporating Recurrent Neural Networks, the gap present between the former information and the existing necessities can be easily associated.

That is the reason why Vanishing and Exploding Gradient problems do not exist, followed by making this LSTM networks to easily handle long-term dependencies.

LSTM encompasses a layer of neural network in the form of a chain. In a standard recurrent neural network, the repeating module consists of one single function as shown in the image given below:

![image](https://user-images.githubusercontent.com/58425689/110089158-db82b780-7dbd-11eb-8fb8-212a4aeaf354.png)

From the image given above, it can be seen that there is a tanh function in the layer, which is called as squashing function. So, what is a squashing function?

The squashing function is mainly used in between the range of -1 to +1 so that the values can be manipulated on the basis of inputs.

Now, let us consider the structure of an LSTM network:

![image](https://user-images.githubusercontent.com/58425689/110090336-454f9100-7dbf-11eb-8c1d-e5cf193a0c7c.png)

Here all those functions that are present in the layers have their own structures as and when it comes to LSTM networks. The cell state is represented by the horizontal line, acts as a conveyer belt that carries the data linearly crossways the data channel.

Let us consider a step-by-step approach to understand LSTM networks better.

Step 1:

The first step in the LSTM is to identify that information which is not required and will be thrown away from the cell state. This decision is made by a sigmoid layer, which called the forget gate layer.

![image](https://user-images.githubusercontent.com/58425689/110090380-51d3e980-7dbf-11eb-8a6b-5100b4dab4dc.png)

The highlighted layer in the above is the sigmoid layer which is previously mentioned.

The calculation is done by considering the new input, and the previous timestamp is, which eventually leads to the output of a number between 0 and 1 for each number in that cell state.

As a typical binary, 1 represents to keep the cell state while 0 represents to trash it.

      ft = σ(wf [ht-1, xt] + bf)
        where, wf = Weight
              ht-1 = Output from previous timestamp
              xt = New input
              bf = Bias

Considering a gender classification problem, it necessitates observing the correct gender when we are using the network.

Step 2:

Next, we will decide which information we will store in the cell state. It further consists of the following steps:

- The sigmoid layer, which is also known as the "input gate layer," will make decisions about those values that are needed to be updated.
- A vector of new candidate values is created so that they can be added to the state by the tanh layer.

![image](https://user-images.githubusercontent.com/58425689/110090602-919ad100-7dbf-11eb-9ce9-7e7855280320.png)

Then the new input, as well as the preceding timestamp's input, will get passed through a sigmoid function that will result in the value i(t), which will then be multiplied by c(t) followed by adding it to the cell state.

In the next step, we will combine both of them so as to update the state.

Step 3:

In the 3rd step, the previous cell state Ct-1 will get updated into the new cell state Ct.

And for that, we will need to multiply the old state (Ct-1) by f(t), keeping the things aside that we thought that we earlier decided to leave.

![image](https://user-images.githubusercontent.com/58425689/110090647-9e1f2980-7dbf-11eb-84c7-ce76e621c2f4.png)

Next, we will add i_t* c˜_t, which is the new candidate values. It has been actually scaled by how much we wanted to update each state value.

In the second step, we decided to do make use of the data, which is only required at that stage. However, in the third step, we have executed it.

Step 4:

In the 4th step, we will run the sigmoid layer that will decide for those parts of the cell state that will result in the output.

Next, we will put the cell state through tanh, which means we will be pushing the values in between the range of -1 and 1.

And then, further, we will multiply it with the sigmoid gate's output so that only the decided parts results in the output.

![image](https://user-images.githubusercontent.com/58425689/110090693-a8d9be80-7dbf-11eb-9290-70c31b8b992d.png)

In this step, we will be doing some calculations that will result in the output.

However, the output consists of only the outputs there were decided to be carry forwarded in the previous steps and not all the outputs at once.

