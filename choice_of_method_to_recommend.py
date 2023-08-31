# This is our database for movies
# In your case, you can get all movies from the 'movies.csv' file
import random
MOVIES = [f"movie_{i}" for i in range(5000)]
random.shuffle(MOVIES)

"""
Aim is to have a class that we can use to recommend movies 
based on some chosen method
- clustering
- nmf
- popular
- random
"""

class MovieRecommendation:
    def __init__(self, user_input, k=5):
        self.user_input = user_input
        self.k = k
    
    def recommend_movie(self):
        if self.user_input["method"] == "random":
            """
            Write a function that recommends movies by random
            """
            ...
            return MOVIES[:self.k]
        
        if self.user_input["method"] == "popular":
            """
            Write the function down here
            """
            ...
            return MOVIES[:self.k]
        
        if self.user_input["method"] == "nmf":
            """
            Write the function down here
            """
            ...
            return MOVIES[:self.k]
        
        if self.user_input["method"] == "cluster":
            """
            Write the function down here
            """
            ...
            return MOVIES[:self.k]

if __name__ == "__main__":
    user_input = {"method": "popular", "movie_1":3, "movie_2": 4}
    inst = MovieRecommendation(user_input=user_input)
    recs = inst.recommend_movie()
    print(recs)



