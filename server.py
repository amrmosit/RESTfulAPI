# Creating small RESTful API

# Import the Flask class from the flask module, & jsonify
from flask import Flask, jsonify

# Create an instance of Flask class, passing the name of the current module
app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route('/')
def index():
    # function thaat handles requests to the root URL
    # return JSON response
    return jsonify({"hello World!"})
