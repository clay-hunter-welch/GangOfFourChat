from flask import Flask, Blueprint, request, jsonify
import json

signup_blueprint = Blueprint('signup', __name__)

@signup_blueprint.route('/signup', methods=['POST'])
def signup():
    # Extract data from form data
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']  # In production, ensure this is handled securely

    # Assuming validation is successful, write to file
    user_info = {
        "username": username,
        "email": email,
        # Password handling: In a real application, store a hashed version, not the plain text
        "password": password
    }
    write_user_to_file(user_info)

    # For demonstration, print the data to the terminal
    print(f'Username: {username}, Email: {email}, Password: {password}')

    # Respond back to the client
    return jsonify({"status": "success", "message": "Signup successful"})


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

if __name__ == '__main__':
    signup_blueprint.run(debug=True)
