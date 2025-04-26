# Creating small RESTful API

# Import the Flask class from the flask module, & jsonify
from flask import Flask, jsonify, make_response

# Create an instance of Flask class, passing the name of the current module
app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route('/')
def index():
    # function thaat handles requests to the root URL
    # return JSON response
    return jsonify({"message": "hello World!"})
# Define a routw for the "\no-content" URL
@app.route("/no_content")
def no_content():
    """Return 'no content found' with a status of 204.
    Returns:
        tuple: A tuple containing a dictionary and a status code.
    """
    # Create a dictionary with a message and return it with a 204 No Content status code
    return ({"message": "No content found"}, 204)
# Define a riute for the "/exp" URL
@app.route("/exp")
def index_explicit():
    """Return 'Hello World' message with a status code of 200.
    Returns:
        response: A response object containing the message and status code 200.
    """
    # Create a response object with the message "Hello World"
    resp = make_response({"message" : "Hello World!"})
    # Set the status code of the response to 200
    resp.status_code = 200
    # Return the response Object
    return resp