#!/usr/bin/python3
"""
This module provides a Flask application with basic authentication and JWT-based authentication,
as well as role-based access control.
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this to a more secure secret key
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Users and their hashed passwords
users = {
    "john": generate_password_hash("hello"),
    "admin": generate_password_hash("secret")
}

# User roles
roles = {
    "john": "user",
    "admin": "admin"
}

@auth.verify_password
def verify_password(username, password):
    """
    Verify the user's password against the stored hashed password.

    Args:
        username (str): The username of the user.
        password (str): The password provided by the user.

    Returns:
        bool: True if the password is correct, False otherwise.
    """
    if username in users:
        return check_password_hash(users.get(username), password)
    return False

@app.route('/login', methods=['POST'])
@auth.login_required
def login():
    """
    Authenticate the user and generate a JWT access token.

    Returns:
        dict: A JSON response containing the access token and the user's role.
    """
    username = auth.current_user()
    role = roles.get(username)
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token, role=role)

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    """
    A protected route that allows access only to administrators.

    Returns:
        dict: A JSON response with a message indicating whether access is granted or denied.
    """
    current_user = get_jwt_identity()
    role = roles.get(current_user)
    if role == 'admin':
        return jsonify(message="Access granted for administrators.")
    else:
        return jsonify(message="Access denied."), 403

@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """
    A route that allows access only to administrators.

    Returns:
        dict: A JSON response with a message indicating whether access is granted or denied.
    """
    current_user = get_jwt_identity()
    role = roles.get(current_user)
    if role == 'admin':
        return jsonify(message="Access granted for administrators only.")
    else:
        return jsonify(message="Access denied."), 403

if __name__ == '__main__':
    app.run(debug=True)
