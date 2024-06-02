#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionary to store users
users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}
}

# Route for the home page
@app.route('/')
def home():
    """
    Home route.
    Returns a welcome message.
    """
    return "Bienvenue sur l'API Flask !"

# Route to get the list of users
@app.route('/data', methods=['GET'])
def get_users():
    """
    Route to get the list of usernames.
    Returns a JSON list of usernames.
    """
    return jsonify(list(users.keys()))

# Route to check the API status
@app.route('/status', methods=['GET'])
def get_status():
    """
    Route to check the API status.
    Returns "OK".
    """
    return "OK"

# Route to get user details
@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    """
    Route to get user details.
    Returns a JSON object with user details if the user exists, otherwise returns a 404 error.
    """
    if username in users:
        return jsonify(users[username])
    else:
        return "User not found", 404

# Route to add a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Route to add a new user.
    Accepts a JSON object with user details in the request body.
    Returns the added user details with a 201 status code if successful, or a 400 error if the user already exists.
    """
    data = request.get_json()
    username = data.get('username')
    if username in users:
        return "User already exists", 400
    else:
        users[username] = data
        return jsonify(data), 201

if __name__ == '__main__':
    """
    Main function to run the Flask app.
    """
    app.run(debug=True)
