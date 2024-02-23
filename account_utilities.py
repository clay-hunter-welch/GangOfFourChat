from flask import Flask, Blueprint, request, jsonify, session
import json
from users import AbstractUserFactory
import bcrypt

# TO DO:
# -log out button support

signup_blueprint = Blueprint('signup', __name__)
login_blueprint = Blueprint('login', __name__)
logout_blueprint = Blueprint('logout', __name__)

def hash_password(password):
    # Convert the password to bytes
    password_bytes = password.encode('utf-8')
    # Generate a salt
    salt = bcrypt.gensalt()
    # Generate a hash for the password with the salt
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password


@signup_blueprint.route('/signup', methods=['POST'])
def signup():
    # Extract data from form data
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']  # In production, ensure this is handled securely
    role = request.form['role']

    # Hash the password here (not shown for brevity)
    hashed_password = hash_password(password)
    hashed_password_hex = hashed_password.hex()

    # build user here using abstract factory => factory => builders
    user = create_user(username=username, email=email, hashed_password_hex=hashed_password_hex, role=role)
    # factory = AbstractUserFactory.get_user_builder(role)  # Get the concrete factory based on role
    if user:
        # Convert user object to a dict or similar for JSON serialization
        user_data = user.to_dict()
        print(
            f'Signup Request processed for Username: {username}, Email: {email}, Password: {hashed_password_hex}, Role: {role}')

        # Write user_data to JSON file
        write_user_to_file(user_data)

        # To do: Log in user here, need to modify login() to accept data not POST generated

        return jsonify({"message": "User Signup successful"}), 200
    else:
        return jsonify({"error": "User Signup FAILED"}), 400


def create_user(username='None', email='None', hashed_password_hex='None', role='None'):
    user_builder = AbstractUserFactory.get_user_builder(role)
    user = user_builder.configure(username, email, role, hashed_password_hex).build()

    return user


@login_blueprint.route('/login', methods=['POST'])
def login():
    # Extract data from form data
    username = request.form['username']
    password = request.form['password']  # In production, ensure this is handled securely

    user_data = get_user_data(username)
    hashed_password = bytes.fromhex(user_data['password'])

    if user_data and bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        session['username'] = username
        return jsonify({"message": "Login successful", "username": username}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401


@logout_blueprint.route('/logout', methods=['POST'])
def logout():
    session.clear()  # This clears all data stored in the session
    return jsonify({'success': 'Logged out successfully'}), 200


def write_user_to_file(user_info):
    # Path to the file where user data will be stored
    file_path = 'users.json'

    # Load existing users
    try:
        with open(file_path, 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []

    # Append the new user
    users.append(user_info)

    # Write the updated list back to the file
    with open(file_path, 'w') as file:
        json.dump(users, file, indent=4)


def get_user_data(username):
    # Path to your JSON file
    filepath = 'users.json'

    try:
        # Open the JSON file and load the data
        with open(filepath, 'r') as file:
            users = json.load(file)

        # Search for the user by username
        for user in users:
            if user['username'] == username:
                return user  # Return the user data if found
    except FileNotFoundError:
        print("The user data file was not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON from the user data file.")

    return None  # Return None if the user was not found or if there's an error

if __name__ == '__main__':
    pass
    # signup_blueprint.run(debug=True)
