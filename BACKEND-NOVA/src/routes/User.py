from flask import Blueprint, jsonify
from models.UserModel import UserModel
#from flask_cors import cross_origin

main = Blueprint('user_blueprint', __name__)

@main.route('/')
def get_users():
    try:
        users = UserModel.get_users()
        # Convertir la lista de objetos User a una lista de diccionarios
        users_json = [user.to_JSON() for user in users]
        return jsonify(users_json)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

@main.route('/<id>')
def get_user(id):
    try:
        user = UserModel.get_user(id)
        print(user)
        if user is not None:
            return jsonify(user.to_JSON())
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500