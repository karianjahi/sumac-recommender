"""
This is the main file where flask is to be launched
"""

"""
IF you want to kill a port you can use:
fuser -n tcp -k <port number>
"""
# import our flask module
from flask import Flask, render_template, request
from recommend_some_movies import recommend_nmf
from choice_of_method_to_recommend import MovieRecommendation

# We need to actually tell flask that this is the file that launches it
app = Flask(__name__)

# We can create a home page that says hello world
# We do this by way of a decorator to a function that specifies the url
# The app.route specifies the url to whatever the function is doing
# "/" means home page.

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recommender")
def recommend_movies():
    print(request.args)
    user_input = dict(request.args)
    print(user_input)
    # nmf_movies = recommend_nmf(user_input, k=10)
    recs = MovieRecommendation(user_input).recommend_movie()
    return render_template("recommendations.html", movies=recs)
# To test if the server can open, we shall make sure that only when this file is used directly is when we can open a new web server
if __name__ == "__main__":
    app.run(debug=True, port=5001)