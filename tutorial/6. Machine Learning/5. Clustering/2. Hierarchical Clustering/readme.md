# Hierarchical Clustering in Machine Learning
Hierarchical clustering is another unsupervised machine learning algorithm, which is used to group the unlabeled datasets into a cluster and also known as hierarchical cluster analysis or HCA.

In this algorithm, we develop the hierarchy of clusters in the form of a tree, and this tree-shaped structure is known as the dendrogram.

Sometimes the results of K-means clustering and hierarchical clustering may look similar, but they both differ depending on how they work. As there is no requirement to predetermine the number of clusters as we did in the K-Means algorithm.

The hierarchical clustering technique has two approaches:

1. Agglomerative: Agglomerative is a bottom-up approach, in which the algorithm starts with taking all data points as single clusters and merging them until one cluster is left.
2. Divisive: Divisive algorithm is the reverse of the agglomerative algorithm as it is a top-down approach.

## How the Agglomerative Hierarchical clustering Work?
The working of the AHC algorithm can be explained using the below steps:

Step-1: Create each data point as a single cluster. Let's say there are N data points, so the number of clusters will also be N. \
![image](https://user-images.githubusercontent.com/58425689/107866554-406f7f80-6e9a-11eb-89d8-108af8fd4958.png)

Step-2: Take two closest data points or clusters and merge them to form one cluster. So, there will now be N-1 clusters. \
![image](https://user-images.githubusercontent.com/58425689/107866558-49f8e780-6e9a-11eb-8e92-dc7567b706e1.png)

Step-3: Again, take the two closest clusters and merge them together to form one cluster. There will be N-2 clusters. \
![image](https://user-images.githubusercontent.com/58425689/107866559-4bc2ab00-6e9a-11eb-9300-bb309084982d.png)

Step-4: Repeat Step 3 until only one cluster left. So, we will get the following clusters. Consider the below images: \
![image](https://user-images.githubusercontent.com/58425689/107866562-4e250500-6e9a-11eb-9411-1cd55bdd7a7b.png)
![image](https://user-images.githubusercontent.com/58425689/107866563-50875f00-6e9a-11eb-9a81-0625ea571441.png)
![image](https://user-images.githubusercontent.com/58425689/107866564-52e9b900-6e9a-11eb-9f9e-b82fe9bd96bf.png)

Step-5: Once all the clusters are combined into one big cluster, develop the dendrogram to divide the clusters as per the problem.

## Measure for the distance between two clusters
As we have seen, the closest distance between the two clusters is crucial for the hierarchical clustering. There are various ways to calculate the distance between two clusters, and these ways decide the rule for clustering. These measures are called Linkage methods. Some of the popular linkage methods are given below:

- Single Linkage: It is the Shortest Distance between the closest points of the clusters. Consider the below image: \
![image](https://user-images.githubusercontent.com/58425689/107866623-e15e3a80-6e9a-11eb-9724-826109218382.png)

- Complete Linkage: It is the farthest distance between the two points of two different clusters. It is one of the popular linkage methods as it forms tighter clusters than single-linkage. \
![image](https://user-images.githubusercontent.com/58425689/107866625-e3c09480-6e9a-11eb-843c-fa07a494c33d.png)

- Average Linkage: It is the linkage method in which the distance between each pair of datasets is added up and then divided by the total number of datasets to calculate the average distance between two clusters. It is also one of the most popular linkage methods.
- Centroid Linkage: It is the linkage method in which the distance between the centroid of the clusters is calculated. Consider the below image: \
![image](https://user-images.githubusercontent.com/58425689/107866627-e8854880-6e9a-11eb-856b-046af4cc5a3e.png)

From the above-given approaches, we can apply any of them according to the type of problem or business requirement.

## Woking of Dendrogram in Hierarchical clustering
The dendrogram is a tree-like structure that is mainly used to store each step as a memory that the HC algorithm performs. In the dendrogram plot, the Y-axis shows the Euclidean distances between the data points, and the x-axis shows all the data points of the given dataset.

The working of the dendrogram can be explained using the below diagram: \
![image](https://user-images.githubusercontent.com/58425689/107866655-37cb7900-6e9b-11eb-93dd-74193af87375.png)

In the above diagram, the left part is showing how clusters are created in agglomerative clustering, and the right part is showing the corresponding dendrogram.
- As we have discussed above, firstly, the datapoints P2 and P3 combine together and form a cluster, correspondingly a dendrogram is created, which connects P2 and P3 with a rectangular shape. The hight is decided according to the Euclidean distance between the data points.
- In the next step, P5 and P6 form a cluster, and the corresponding dendrogram is created. It is higher than of previous, as the Euclidean distance between P5 and P6 is a little bit greater than the P2 and P3.
- Again, two new dendrograms are created that combine P1, P2, and P3 in one dendrogram, and P4, P5, and P6, in another dendrogram.
- At last, the final dendrogram is created that combines all the data points together.
- We can cut the dendrogram tree structure at any level as per our requirement.

  ```python
    #Finding the optimal number of clusters using the dendrogram  
    import scipy.cluster.hierarchy as shc  
    dendro = shc.dendrogram(shc.linkage(x, method="ward")) 

    #training the hierarchical model on dataset  
    from sklearn.cluster import AgglomerativeClustering  
    hc= AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
  ```
