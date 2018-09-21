
from flask import Flask, request, jsonify
from . import model

app = Flask(__name__)
app.config["TESTING"] = True
app.url_map.strict_slashes = False


MY_USER = model.Users()

'''user actions'''


@app.route('/subscribe', methods=['POST'])
def subscribe():
    '''endpoint to register a user'''
    data = request.get_json()
    if not data:
        return jsonify({"message": "Fields cannot be empty"})

    name = data.get('name')
    phone = data.get('phone')
    user_id = data.get('user_id')

    if name is None or not name:
        return jsonify({"message": "Enter name"}), 206

    if phone is None or not phone:
        return jsonify({"message": "Enter phone"}), 206

    if user_id is None or not user_id:
        return jsonify({"message": "Enter ID number"}), 206

    response = jsonify(MY_USER.put(name, phone, user_id))
    response.status_code = 201
    return response


@app.route('/users', methods=['GET'])
def getallusers():
    response = jsonify(MY_USER.get_all_users())
    response.status_code = 200
    return response


@app.route('/unsubscribe/<user_id>', methods=['DELETE'])
def unsubscribe(user_id):
    response = jsonify(MY_USER.delete_user(user_id))
    response.status_code = 200
    return response


if __name__ == '__main__':
    app.run(debug=True)
