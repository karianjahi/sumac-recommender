"""
This is the main file where flask is to be launched
"""

# import our flask module
from flask import Flask

# We need to actually tell flask that this is the file that launches it
app = Flask(__name__)

# We can create a home page that says hello world
# We do this by way of a decorator to a function that specifies the url
# The app.route specifies the url to whatever the function is doing
# "/" means home page.

@app.route("/")
def hello_world():
    return '''<h1 style="color:green">Hello world</h1>
                <p>This application recommends movies to users! </p>'''

# To test if the server can open, we shall make sure that only when this file is used directly is when we can open a new web server
if __name__ == "__main__":
    app.run(debug=True, port=5001)