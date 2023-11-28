from flask import Blueprint, jsonify
from models.UserModel import UserModel
#from flask_cors import cross_origin

main = Blueprint('user_blueprint', __name__)

@main.route('/')
#@cross_origin(supports_credentials=True)
def get_users():
    try:
        users = UserModel.get_users()
        # Convertir la lista de objetos User a una lista de diccionarios
        users_json = [user.to_JSON() for user in users]
        return jsonify(users_json)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
        