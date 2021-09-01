# simple_recommendation_engine
https://simple-movie-recommendation.herokuapp.com/


Dataset: https://www.kaggle.com/rounakbanik/the-movies-dataset/data

Simple recommendation: The central idea of this approach is that films that are more popular and highly acclaimed are more likely to be appreciated by the general public. The      IMDB Top 250 is a good example.
 
 
 Sample result: ![Alt text](https://github.com/n-e-e-l/simple_recommendation_engine/blob/main/sample_result.JPG)


Getting Ranking just based on the number of votes would mean that movies released recently would have a big disadvantage as they won't have ample number of votes at all. Moreover few movies have cult following and that is refelected in their voting numbers. To avoid this weighted average os the number of votes and the average votes is taken.

weighted rating formula as a metric/score. Mathematically, it is represented as follows:

WeightedRating(WR)=(vv+m*R)+(mv+m*C)
In the above equation,

v is the number of votes for the movie;

m is the minimum votes required to be listed in the chart;

R is the average rating of the movie;

C is the mean vote across the whole report.
