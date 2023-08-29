"""
This function recommends movies based on user input
user input is in the form:
user_input = {'movie1': '3', 'movie2': '4', 'movie3': '1', 'movie4': '4', 'movie5': '2'}
The function uses this input and passes this into the model (assuming you have saved the model)
and makes recommendations
"""
import random
# Dummy model (doesn't currently exist)
model = "model.sav"

# Create a dummy database where we have all movies
movies = [f'movie_{i}' for i in range(1000)]
random.shuffle(movies)
def recommend_nmf(user_input, model=model, k=3):
    "the function does a couple of things before it recommnds"
    ...
    return movies[:k]

# Test if the function works
if __name__ == "__main__":
    user_input = {"movie_1":5,
                   "movie_2": 3,
                   "movie_3": 3,
                   "movie_4": 4,
                   "movie_5": 2,
                   }
    recs = recommend_nmf(user_input)
    print(recs)