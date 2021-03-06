# Recommendation Systems
A recommendation engine filters the data using different algorithms and recommends the most relevant items to users. It first captures the past behavior of a customer and based on that, recommends products which the users might be likely to buy.

There are also popular recommender systems for domains like restaurants, movies, and online dating. Recommender systems have also been developed to explore research articles and experts, collaborators, and financial services. YouTube uses the recommendation system at a large scale to suggest you videos based on your history. For example, if you watch a lot of educational videos, it would suggest those types of videos.

HOW DO THEY WORK ? 
- Data Collection \
This is the first and most crucial step for building a recommendation engine. The data can be collected by two means: explicitly and implicitly. 
Explicit data is information that is provided intentionally, i.e. input from the users such as movie ratings.
Implicit data is information that is not provided intentionally but gathered from available data streams like search history, clicks, order history, etc.

- Filtering the data \
  After collecting and storing the data, we have to filter it so as to extract the relevant information required to make the final recommendations.

  ![1](https://github.com/rjnp2/Data-Science/blob/main/tutorial/8.%20Recommendation%20Systems/images/1.png)

    1. Content-based recommenders \
        This type of filter does not involve other users if not ourselves. Based on what we like, the algorithm will simply pick items with similar content to recommend us.
        A major drawback of this algorithm is that it is limited to recommending items that are of the same type. It will never recommend products which the user has not bought or liked in the past. So if a user has watched or liked only action movies in the past, the system will recommend only action movies. It’s a very narrow way of building an engine.

        How to measure the similarity? there are different measures of similarity :
        1. Euclidean Distance
        2. Cosine similarity :
          It defines the linear relationship b/w two vectors.

          ![1](https://github.com/rjnp2/Data-Science/blob/main/tutorial/8.%20Recommendation%20Systems/images/2.png)

        3. Pearson’s Correlation: It tells us how much two items are correlated. Higher the correlation, more will be the similarity. Pearson’s correlation can be calculated for user u and v using the following formula:

            ![1](https://github.com/rjnp2/Data-Science/blob/main/tutorial/8.%20Recommendation%20Systems/images/3.png)

                here ,
                    • rᵤᵢ = rating given by user (u ) to item (i )
                    • rᵥᵢ = rating given by user (v ) to item (i )
                    • rᵥ (mean) =mean of al rating given by user (v)

    2. Collaborative filtering
      The collaborative filtering algorithm uses “User Behavior” for recommending items. This is one of the most commonly used algorithms in the industry as it is not dependent on any additional information. \
      There are different types of collaborating filtering techniques. \
      2.1 User-User collaborative filtering
      This algorithm first finds the similarity score between users. Based on this similarity score, it then picks out the most similar users and recommends products which these similar users have liked or bought previously. \
       ![1](https://github.com/rjnp2/Data-Science/blob/main/tutorial/8.%20Recommendation%20Systems/images/4.png) \
       In terms of movies example, this algorithm finds the similarity between each user based on the ratings they have previously given to different movies. The prediction of an item for a user u is calculated by computing the weighted sum of the user ratings given by other users to an item i.
    The prediction Pu,i is given by:
       ![1](https://github.com/rjnp2/Data-Science/blob/main/tutorial/8.%20Recommendation%20Systems/images/5.png)

            Here,
                • Pu,i is the prediction of an item
                • Rv,i is the rating given by a user v to a movie i
                • Su,v is the similarity between users

    Now, we have the ratings for users in profile vector and based on that we have to predict the ratings for other users. 
    Following steps are followed to do so:
        1. For predictions we need the similarity between the user u and v. We can make use of Pearson correlation.
        2. First we find the items rated by both the users and based on the ratings, correlation between the users is calculated.
        3. The predictions can be calculated using the similarity values. This algorithm, first of all calculates the similarity between each user and then based on each similarity calculates the predictions. Users having higher correlation will tend to be similar.
        4. Based on these prediction values, recommendations are made. 

    This algorithm is quite time consuming as it involves calculating the similarity for each user and then calculating prediction for each similarity score. One way of handling this problem is to select only a few users (neighbors). There are various ways to select the neighbors:
        • Select a threshold similarity and choose all the users above that value
        • Randomly select the users
        • Arrange the neighbors in descending order of their similarity value and choose top-N users
        • Use clustering for choosing neighbors
    This algorithm is useful when the number of users is less. This leads us to item-item collaborative filtering, which is effective when the number of users is more than the items being recommended.

    2.2 Item-Item collaborative filtering
    In this algorithm, we compute the similarity between each pair of items.

      ![1](https://github.com/rjnp2/Data-Science/blob/main/tutorial/8.%20Recommendation%20Systems/images/6.png)

    So in our case we will find the similarity between each movie pair and based on that, we will recommend similar movies which are liked by the users in the past. This algorithm works similar to user-user collaborative filtering with just a little change — instead of taking the weighted sum of ratings of “user-neighbors”, we take the weighted sum of ratings of “item-neighbors”. 

    The prediction is given by:

      ![1](https://github.com/rjnp2/Data-Science/blob/main/tutorial/8.%20Recommendation%20Systems/images/7.png)

    Now we will find the similarity between items. \
      ![1](https://github.com/rjnp2/Data-Science/blob/main/tutorial/8.%20Recommendation%20Systems/images/8.png)


     Before going further and implementing these concepts, there is a question which we must know the answer to — what will happen if a new user or a new item is added in the dataset? It is called a Cold Start. There can be two types of cold start:

        1. Visitor Cold Start
        2. Product Cold Start

    Visitor Cold Start means that a new user is introduced in the dataset. Since there is no history of that user, the system does not know the preferences of that user. It becomes harder to recommend products to that user. So, how can we solve this problem? One basic approach could be to apply a popularity based strategy, i.e. recommend the most popular products. These can be determined by what has been popular recently overall or regionally. Once we know the preferences of the user, recommending products will be easier.

    On the other hand, Product Cold Start means that a new product is launched in the market or added to the system. User action is most important to determine the value of any product. More the interaction a product receives, the easier it is for our model to recommend that product to the right user. We can make use of Content based filtering to solve this problem. The system first uses the content of the new product for recommendations and then eventually the user actions on that product.
