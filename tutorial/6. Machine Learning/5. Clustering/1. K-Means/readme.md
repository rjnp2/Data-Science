# What is K-Means Algorithm?
K-Means Clustering is an Unsupervised Learning algorithm, which groups the unlabeled dataset into different clusters. Here K defines the number of pre-defined clusters that need to be created in the process, as if K=2, there will be two clusters, and for K=3, there will be three clusters, and so on. \
It allows us to cluster the data into different groups and a convenient way to discover the categories of groups in the unlabeled dataset on its own without the need for any training.  \
It is a centroid-based algorithm, where each cluster is associated with a centroid. The main aim of this algorithm is to minimize the sum of distances between the data point and their corresponding clusters. 

The below diagram explains the working of the K-means Clustering Algorithm: \
![image](https://user-images.githubusercontent.com/58425689/107849140-5db43780-6e21-11eb-8e03-5b7a26ea0d3f.png)

## How does the K-Means Algorithm Work?
The working of the K-Means algorithm is explained in the below steps:

Step-1: Select the number K to decide the number of clusters. \
Step-2: Select random K points or centroids. (It can be other from the input dataset). \
Step-3: Assign each data point to their closest centroid, which will form the predefined K clusters. \
Step-4: Calculate the variance and place a new centroid of each cluster. \
Step-5: Repeat the third steps, which means reassign each datapoint to the new closest centroid of each cluster. \
Step-6: If any reassignment occurs, then go to step-4 else go to FINISH. \
Step-7: The model is ready.

Let's understand the above steps by considering the visual plots:

Suppose we have two variables M1 and M2. The x-y axis scatter plot of these two variables is given below: \
![image](https://user-images.githubusercontent.com/58425689/107849143-6147be80-6e21-11eb-9958-799ea8b50cb9.png)
- Let's take number k of clusters, i.e., K=2, to identify the dataset and to put them into different clusters. It means here we will try to group these datasets into two different clusters.
- We need to choose some random k points or centroid to form the cluster. These points can be either the points from the dataset or any other point. So, here we are selecting the below two points as k points, which are not the part of our dataset. Consider the below image: \
![image](https://user-images.githubusercontent.com/58425689/107849144-63118200-6e21-11eb-8215-6f2841032da1.png)

- Now we will assign each data point of the scatter plot to its closest K-point or centroid. We will compute it by applying some mathematics that we have studied to calculate the distance between two points. So, we will draw a median between both the centroids. Consider the below image: \
![image](https://user-images.githubusercontent.com/58425689/107849145-6573dc00-6e21-11eb-9f66-5ad3d736170f.png)

- From the above image, it is clear that points left side of the line is near to the K1 or blue centroid, and points to the right of the line are close to the yellow centroid. Let's color them as blue and yellow for clear visualization. \
![image](https://user-images.githubusercontent.com/58425689/107849146-67d63600-6e21-11eb-8a1c-5889c955a93d.png)

- As we need to find the closest cluster, so we will repeat the process by choosing a new centroid. To choose the new centroids, we will compute the center of gravity of these centroids, and will find new centroids as below: \
![image](https://user-images.githubusercontent.com/58425689/107849148-6a389000-6e21-11eb-88f2-075559bebbaf.png)

- Next, we will reassign each datapoint to the new centroid. For this, we will repeat the same process of finding a median line. The median will be like below image: \
![image](https://user-images.githubusercontent.com/58425689/107849149-6c025380-6e21-11eb-8d58-3bb418ca402a.png)

- From the above image, we can see, one yellow point is on the left side of the line, and two blue points are right to the line. So, these three points will be assigned to new centroids. \
![image](https://user-images.githubusercontent.com/58425689/107849150-6e64ad80-6e21-11eb-997f-1fa2ba2cd043.png)

- As reassignment has taken place, so we will again go to the step-4, which is finding new centroids or K-points.
  - We will repeat the process by finding the center of gravity of centroids, so the new centroids will be as shown in the below image: \  
  ![image](https://user-images.githubusercontent.com/58425689/107849151-70c70780-6e21-11eb-843d-895ce9ec81fb.png)

  - As we got the new centroids so again will draw the median line and reassign the data points. So, the image will be: \  
    ![image](https://user-images.githubusercontent.com/58425689/107849153-7290cb00-6e21-11eb-819a-262367ba9cfc.png)
    
- We can see in the above image; there are no dissimilar data points on either side of the line, which means our model is formed. Consider the below image: \
![image](https://user-images.githubusercontent.com/58425689/107849154-745a8e80-6e21-11eb-9021-12e35d5f3245.png)

As our model is ready, so we can now remove the assumed centroids, and the two final clusters will be as shown in the below image: \
![image](https://user-images.githubusercontent.com/58425689/107849156-791f4280-6e21-11eb-9dc6-2b4d9b43a2f1.png)

## How to choose the value of "K number of clusters" in K-means Clustering?
The performance of the K-means clustering algorithm depends upon highly efficient clusters that it forms. But choosing the optimal number of clusters is a big task. There are some different ways to find the optimal number of clusters, but here we are discussing the most appropriate method to find the number of clusters or value of K. The method is given below:

### Elbow Method
The Elbow method is one of the most popular ways to find the optimal number of clusters. This method uses the concept of WCSS value. WCSS stands for Within Cluster Sum of Squares, which defines the total variations within a cluster. The formula to calculate the value of WCSS (for 3 clusters) is given below: 

![image](https://user-images.githubusercontent.com/58425689/107849408-162eab00-6e23-11eb-80a7-152853b21a6a.png)

In the above formula of WCSS, \
∑Pi in Cluster1 distance(Pi C1)2: It is the sum of the square of the distances between each data point and its centroid within a cluster1 and the same for the other two terms.

To measure the distance between data points and centroid, we can use any method such as Euclidean distance or Manhattan distance. \
To find the optimal value of clusters, the elbow method follows the below steps:
- It executes the K-means clustering on a given dataset for different K values (ranges from 1-10).
- For each value of K, calculates the WCSS value.
- Plots a curve between calculated WCSS values and the number of clusters K.
- The sharp point of bend or a point of the plot looks like an arm, then that point is considered as the best value of K.
Since the graph shows the sharp bend, which looks like an elbow, hence it is known as the elbow method. The graph for the elbow method looks like the below image:

![image](https://user-images.githubusercontent.com/58425689/107849372-f8f9dc80-6e22-11eb-8caf-e1d759460b28.png)

#Project
[Mall_Customers_cluster](https://github.com/rjnp2/Data-Science/blob/main/tutorial/6.%20Machine%20Learning/5.%20Clustering/1.%20K-Means/Mall_Customers_cluster.ipynb)
