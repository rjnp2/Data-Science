# Introduction of Convolutional Neural Network

Convolutional Neural Network is one of the technique to do image classification and image recognition in neural networks. It is designed to process the data by multiple layers of arrays. This type of neural network is used in applications like image recognition or face recognition. The primary difference between CNN and other neural network is that CNN takes input as a two-dimensional array. And it operates directly on the images rather than focusing on feature extraction which other neural networks do.

Convolutional Neural Networks are a special type of feed-forward artificial neural network in which the connectivity pattern between its neuron is inspired by the visual cortex.

The visual cortex encompasses a small region of cells that are region sensitive to visual fields. In case some certain orientation edges are present then only some individual neuronal cells get fired inside the brain such as some neurons responds as and when they get exposed to the vertical edges, however some responds when they are shown to horizontal or diagonal edges, which is nothing but the motivation behind Convolutional Neural Networks.

![image](https://user-images.githubusercontent.com/58425689/108686874-1d8a3e80-751e-11eb-8b75-8ce3ae650451.png)

## How Does a Computer read an image?
The image is broken into 3 color-channels which is Red, Green, and Blue. Each of these color channels is mapped to the image's pixel.

Some neurons fires when exposed to vertices edges and some when shown horizontal or diagonal edges. CNN utilizes spatial correlations which exist with the input data. Each concurrent layer of the neural network connects some input neurons. This region is called a local receptive field. The local receptive field focuses on hidden neurons.

The hidden neuron processes the input data inside the mentioned field, not realizing the changes outside the specific boundary.

## Convolutional Neural Networks have the following 4 layers:
1. Convolutional
2. ReLU Layer
3. Pooling
4. Fully Connected

## Convolutional layer
Convolution layer is the first layer to derive features from the input image. The convolutional layer conserves the relationship between pixels by learning image features using a small square of input data. It is the mathematical operation which takes two inputs such as image matrix and kernel or any filter.

- The dimension of image matrix is h×w×d.
- The Convolutional layers encompass a set of learnable filters, such that each filter embraces small width, height as well as depth as that of the provided input volume (if the image is the input layer then probably it would be 3). The dimension of any filter is fh×fw×d.
- Suppose that we want to run the convolution over the image that comprises of 34x34x3 dimension, such that the size of a filter can be axax3. Here a can be any of the above 3, 5, 7, etc. It must be small in comparison to the dimension of the image.
- Each filter gets slide all over the input volume during the forward pass. It slides step by step, calling each individual step as a stride that encompasses a value of 2 or 3 or 4 for higher-dimensional images, followed by calculating a dot product in between filter's weights and patch from input volume.
- It will result in 2-Dimensional output for each filter as and when we slide our filters followed by stacking them together so as to achieve an output volume to have a similar depth value as that of the number of filters. And then, the network will learn all the filters.
- The dimension of output is (h-fh+1)×(w-fw+1)×1.

  ![image](https://user-images.githubusercontent.com/58425689/108687627-0bf56680-751f-11eb-9928-1ad8d0bd41be.png)
                                    
                                    Figure : Convolution
  ```python
    batch_size, _, _ ,_ = X.shape
    h_out, w_out= output_shape
    h_f, w_f = filter_shape 

    W  = cp.random.uniform( -0.1 , 0.1, (filter_shape[0],filter_shape[1],
                                  input_shape[-1],n_filters))
    output = np.zeros((batch_size, h_out, w_out, n_filters))

    for i in range(h_out):
      for j in range(w_out):

        h_start = i * self.stride
        h_end = h_start + h_f
        w_start = j * self.stride
        w_end = w_start + w_f

        output[:, i, j, :] = np.sum(
            X[:, h_start:h_end, w_start:w_end, :, np.newaxis] *
            W[np.newaxis, :, :, :], axis=(1, 2, 3))
    output = output + self.w0
  ```

## ReLU Layer
  ReLU stands for Rectified Linear Unit for a non-linear operation. The output is ƒ(x) =max (0, x). It simply removes all negative values that comes from convolutionlayers by comparing with its function and replace negative with zeros. ReLU’s purpose is to introduce non-linearity in our ConvNet. Since, the real-world data would want our ConvNet to learn would be non-negative linear values. \
  **It results in changing negatives values but unchanged size of the volume.**
  ![image](https://user-images.githubusercontent.com/58425689/108687896-5f67b480-751f-11eb-9340-b9fb4cce68ef.png)

                                  Figure : Rectification applied to Feature Maps
  ```python
  cp.where(x >= 0, x, 0)
  ```
  
## Pooling Layer
  Pooling layer plays a vital role in pre-processing of any image. Pooling layer reduces the number of the parameter when the image is too large. Pooling is "downscaling" of the image achieved from previous layers. It can be compared to shrink an image to reduce the image's density. \
  We do this by implementing the following 4 steps:
    - Pick a window size (usually 2 or 3)
    - Pick a stride (usually 2)
    - Walk your window across your filtered images
    - From each window, take the maximum value

  ![image](https://user-images.githubusercontent.com/58425689/108689135-cfc30580-7520-11eb-825f-bbc137463b94.png)
  ![image](https://user-images.githubusercontent.com/58425689/108689164-d94c6d80-7520-11eb-8e16-74882e151027.png)
  ```python
     n, h_in, w_in, c = X.shape
     h_pool, w_pool = pool_shape
     h_out , w_out = output

     output = cp.zeros((n, h_out, w_out, c))

     for i in range(h_out):
       for j in range(w_out):
          h_start = i * self.stride
          h_end = h_start + h_pool
          w_start = j * self.stride
          w_end = w_start + w_pool

              a_prev_slice = X[:, h_start:h_end, w_start:w_end, :]
              output[:, i, j, :] = np.max(a_prev_slice, axis=(1, 2)
  ```

## Fully Connected (Dense) Layer
  The layer we call as FC layer, we flattened our matrix into vector and feed it into a fully connected layer like a neural network where actual detection occurs by using high features to detect various landmarks based on labels. \
  We do this by implementing the following 3 steps:
  - Pick a neuron
  - Pick a activation function (usually relu)
  - Dot multiplies of input and neuron

    ![image](https://user-images.githubusercontent.com/58425689/108689962-de5dec80-7521-11eb-92bb-7db95e96979b.png)

## Working of CNN
![image](https://user-images.githubusercontent.com/58425689/108690131-16fdc600-7522-11eb-85b5-863b26f7665c.png)

We will start with an input image to which we will be applying multiple feature detectors, which are also called as filters to create the feature maps that comprises of a Convolution layer. Then on the top of that layer, we will be applying the ReLU or Rectified Linear Unit to remove any linearity or increase non-linearity in our images.

Next, we will apply a Pooling layer to our Convolutional layer, so that from every feature map we create a Pooled feature map as the main purpose of the pooling layer is to make sure that we have spatial invariance in our images. It also helps to reduce the size of our images as well as avoid any kind of overfitting of our data. After that, we will flatten all of our pooled images into one long vector or column of all of these values, followed by inputting these values into our artificial neural network. Lastly, we will feed it into the locally connected layer to achieve the final output.

![image](https://user-images.githubusercontent.com/58425689/108690141-19f8b680-7522-11eb-8154-84129c49810e.png)

## CNN Use Case
Steps: \
![image](https://user-images.githubusercontent.com/58425689/108690753-d0f53200-7522-11eb-82e6-5b621e5a9d33.png)

## Project
- [Facial Landmark Detection using CNN](https://github.com/rjnp2/facial_landmark_detection_using-cnn)
- [Text-Recognition-using-Deep-Learning](https://github.com/rjnp2/Text-Recognition-using-Deep-Learning)
- [neural-style-transfer](https://github.com/rjnp2/neural-style-transfer)


