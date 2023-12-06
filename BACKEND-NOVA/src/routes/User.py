from flask import Blueprint, jsonify, request
from models.UserModel import UserModel
import uuid 
from datetime import datetime
from utils.DateFormat import DateFormat
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

@main.route('/add', methods=['POST'])
def add_user():
    try:
        id = str(uuid.uuid4())
        name = request.json['name']
        lastname = request.json['lastname']
        email = request.json['email']
        age = request.json['age']
        numberphone = request.json['numberphone']
        address = request.json['address']
        birthdate = request.json['birthdate']
        creationdate = DateFormat.convert_date(datetime.now())
        isactive = request.json['isactive']
        user = UserModel(id,name, lastname, email, age, numberphone, address, birthdate, creationdate, isactive)
        affected_rows = UserModel.add_user(user)

        if(affected_rows > 0):
            return jsonify({'message': 'User added successfully'}),201
        else:
            return jsonify({'message': 'User not added'}),400

    except Exception as ex:
        return jsonify({'message': str(ex)}),500