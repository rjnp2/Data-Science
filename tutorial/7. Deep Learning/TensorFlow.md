# What is TensorFlow?
   TensorFlow is a powerful open source software library for numerical computation, particularly well suited and fine-tuned for large-scale Machine Learning. Its basic principle is simple: you first define in Python a graph of computations to perform, and then TensorFlow takes that graph and runs it efficiently using optimized C++ code. \
Most importantly, it is possible to break up the graph into several chunks and run them in parallel across multiple CPUs or GPUs. TensorFlow also supports distributed computing, so you can train colossal neural networks on humongous training sets in a reasonable amount of time by splitting the computations across hundreds of servers.

**The word TensorFlow is made by two words, i.e., Tensor and Flow**
1. Tensor is a multidimensional array
2. Flow is used to define the flow of data in operation.

![img](https://github.com/rjnp2/Data-Science/blob/main/tutorial/7.%20Deep%20Learning/images/tfp1.png) \
fig : A simple computation graph

![img](https://github.com/rjnp2/Data-Science/blob/main/tutorial/7.%20Deep%20Learning/images/tfp2.png) \
fig : Parallel computation on multiple CPUs/GPUs/servers


## Components of TensorFlow
- Tensor \
  The name TensorFlow is derived from its core framework, "Tensor." A tensor is a vector or a matrix of n-dimensional that represents all type of data. All values in a tensor hold similar data type with a known shape. The shape of the data is the dimension of the matrix or an array.

  A tensor can be generated from the input data or the result of a computation. In TensorFlow, all operations are conducted inside a graph. The group is a set of calculation that takes place successively. Each transaction is called an op node are connected. \
  ![img](https://github.com/rjnp2/Data-Science/blob/main/tutorial/7.%20Deep%20Learning/images/tf2.png)

- Graphs \
  TensorFlow makes use of a graph framework. The chart gathers and describes all the computations done during the training.

  Advantages
    - It was fixed to run on multiple CPUs or GPUs and mobile operating systems.
    - The portability of the graph allows to conserve the computations for current or later use. The graph can be saved because it can be executed in the future.
    - All the computation in the graph is done by connecting tensors together.
    
  Consider the following expression a= (b+c)*(c+2) \
  We can break the functions into components given below: 
  
        d=b+c 
        e=c+2 
        a=d*e

  Now, we can represent these operations graphically below: \
  ![img](https://github.com/rjnp2/Data-Science/blob/main/tutorial/7.%20Deep%20Learning/images/tf3.png)

- Session \
  A session can execute the operation from the graph. To feed the graph with the value of a tensor, we need to open a session. Inside a session, we must run an operator to create an output.

## Why is TensorFlow popular?
  TensorFlow is the better library for all because it is accessible to everyone. TensorFlow library integrates different API to create a scale deep learning architecture like CNN (Convolutional Neural Network) or RNN (Recurrent Neural Network).

  TensorFlow is based on graph computation; it can allow the developer to create the construction of the neural network with Tensorboard. This tool helps debug our program. It runs on CPU (Central Processing Unit) and GPU (Graphical Processing Unit).

## Use Cases/Applications of TensorFlow
  ![img](https://github.com/rjnp2/Data-Science/blob/main/tutorial/7.%20Deep%20Learning%20using%20TensorFlow/images/tf4.png) \
  TensorFlow provides amazing functionalities and services when compared to other popular deep learning frameworks. TensorFlow is used to create a large-scale neural network with many layers.

  ![img](https://github.com/rjnp2/Data-Science/blob/main/tutorial/7.%20Deep%20Learning%20using%20TensorFlow/images/tf5.png) \
  It is mainly used for deep learning or machine learning problems such as Classification, Perception, Understanding, Discovering Prediction, and Creation.

1. Voice/Sound Recognition \
    Voice and sound recognition applications are the most-known use cases of deep-learning. If the neural networks have proper input data feed, neural networks are capable of understanding audio signals.

    For example: 
      - Voice recognition is used in the Internet of Things, automotive, security, and UX/UI. 
      - Sentiment Analysis is mostly used in customer relationship management (CRM). 
      - Flaw Detection (engine noise) is mostly used in automotive and Aviation. 
      - Voice search is mostly used in customer relationship management (CRM)

2. Image Recognition \
    Image recognition is the first application that made deep learning and machine learning popular. Telecom, Social Media, and handset manufacturers mostly use image recognition. It is also used for face recognition, image search, motion detection, machine vision, and photo clustering.

    For example, image recognition is used to recognize and identify people and objects in from of images. Image recognition is used to understand the context and content of any image. 
    
    For object recognition, TensorFlow helps to classify and identify arbitrary objects within larger images. 
    
    This is also used in engineering application to identify shape for modeling purpose (3d reconstruction from 2d image) and by Facebook for photo tagging. 
    
    For example, deep learning uses TensorFlow for analyzing thousands of photos of cats. So a deep learning algorithm can learn to identify a cat because this algorithm is used to find general features of objects, animals, or people.

3. Time Series \
    Deep learning is using Time Series algorithms for examining the time series data to extract meaningful statistics. For example, it has used the time series to predict the stock market.

    A recommendation is the most common use case for Time Series. Amazon, Google, Facebook, and Netflix are using deep learning for the suggestion. So, the deep learning algorithm is used to analyze customer activity and compare it to millions of other users to determine what the customer may like to purchase or watch.

    For example, it can be used to recommend us TV shows or movies that people like based on TV shows or movies we already watched.

4. Video Detection \
    The deep learning algorithm is used for video detection. It is used for motion detection, real-time threat detection in gaming, security, airports, and UI/UX field.

    For example, NASA is developing a deep learning network for object clustering of asteroids and orbit classification. So, it can classify and predict NEOs (Near Earth Objects).

5. Text-Based Applications \
    Text-based application is also a popular deep learning algorithm. Sentimental analysis, social media, threat detection, and fraud detection, are the example of Text-based applications.

    For example, Google Translate supports over 100 languages.

    Some companies who are currently using TensorFlow are Google, AirBnb, eBay, Intel, DropBox, Deep Mind, Airbus, CEVA, Snapchat, SAP, Uber, Twitter, Coca-Cola, and IBM.

