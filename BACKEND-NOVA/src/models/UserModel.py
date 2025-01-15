from database.db import get_connection
from .entities.User import User

class UserModel:

    def __init__(self, id, name, lastname, email, age, numberphone, address, birthdate, creationdate, isactive, password, project):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.email = email
        self.age = age
        self.numberphone = numberphone
        self.address = address
        self.birthdate = birthdate
        self.creationdate = creationdate
        self.isactive = isactive
        self.password = password
        self.project = project

    @classmethod
    def get_users(self):
        try:
            connection = get_connection()
            users = []

            columns = ["id", "name", "lastname", "email", "age", "numberphone", "address", "birthdate", "creationdate", "isactive", "password", "project"]

            with connection, connection.cursor() as cursor:
                cursor.execute(f"SELECT {', '.join(columns)} FROM usuario ORDER BY creationdate ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    user_data = dict(zip(columns, row))
                    user = User(**user_data)
                    users.append(user)

            return users

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_user(self,id):
        try:
            connection = get_connection()

            columns = ["id", "name", "lastname", "email", "age", "numberphone", "address", "birthdate", "creationdate", "isactive", "password", "project"]

            with connection, connection.cursor() as cursor:
                cursor.execute(f"SELECT {', '.join(columns)} FROM usuario WHERE id = %s",(id,))
                row = cursor.fetchone()

                user = None

                if row is not None:
                    user_data = dict(zip(columns, row))
                    user = User(**user_data)

            return user

        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def add_user(self, user):
        try:
            connection = get_connection()

            with connection, connection.cursor() as cursor:
                cursor.execute(f"INSERT INTO usuario (id, name, lastname, email, age, numberphone, address, birthdate, creationdate, isactive, password, project) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (user.id, user.name, user.lastname, user.email, user.age, user.numberphone, user.address, user.birthdate, user.creationdate, user.isactive, user.password, user.project))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows

        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def login(self, email, password):
        try:
            connection = get_connection()

            columns = ["id", "name", "lastname", "email", "age", "numberphone", "address", "birthdate", "creationdate", "isactive", "password", "project"]
            query = f"SELECT {', '.join(columns)} FROM usuario WHERE email = %s AND password = %s"

            # Create the full query string with values for printing
            full_query = query.replace("%s", "'{}'").format(email, password)

            with connection, connection.cursor() as cursor:
                cursor.execute(query, (email, password))
                row = cursor.fetchone()
                user = None

                if row is not None:
                    print('Entro al if')
                    user_data = dict(zip(columns, row))
                    user = User(**user_data)
                    print(f"User data: {user_data}")

                return user

        except Exception as ex:
            raise Exception(ex)
