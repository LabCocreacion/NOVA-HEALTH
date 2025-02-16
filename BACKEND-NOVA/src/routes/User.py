from flask import Blueprint, jsonify, request
from models.UserModel import UserModel
import uuid 
from datetime import datetime, timedelta
from utils.DateFormat import DateFormat
import jwt
from decouple import config

SECRET_KEY = config('SECRET_KEY')
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
        identificacion = request.json['identificacion']
        numberphone = request.json['numberphone']
        address = request.json['address']
        creationdate = DateFormat.convert_date(datetime.now())
        isactive = request.json['isactive']
        password = request.json['password']
        project = request.json['project']
        rol = request.json['rol']
        instituto = request.json['instituto']
        user = UserModel(id,name, lastname, email, identificacion, numberphone, address, creationdate, isactive, password, project, rol, instituto)
        affected_rows = UserModel.add_user(user)

        if(affected_rows > 0):
            return jsonify({'message': 'User added successfully'}),201
        else:
            return jsonify({'message': 'User not added'}),400

    except Exception as ex:
        return jsonify({'message': str(ex)}),500

@main.route('/check-email', methods=['GET'])
def check_email():
    email = request.args.get('email')
    try:
        user = UserModel.get_user_by_email(email)
        if user:
            return jsonify({'exists': True}), 200
        else:
            return jsonify({'exists': False}), 200
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    user = UserModel.login(email, password)
    
    if user:
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.utcnow() + timedelta(hours=1)
        }, SECRET_KEY, algorithm='HS256')
        
        return jsonify({"message": "Login successful", "token": token, "userName": user.name, "userProject": user.project, "userRol": user.rol, "userIdent": user.identificacion, "userInstitucion": user.instituto, "userEmail": email}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401