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

