from database.db import get_connection
from .entities.User import User

class UserModel:

    @classmethod
    def get_users(self):
        try:
            connection = get_connection()
            users = []

            columns = ["id", "name", "lastname", "email", "age", "numberphone", "address", "birthdate", "creationdate", "isactive"]

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

            columns = ["id", "name", "lastname", "email", "age", "numberphone", "address", "birthdate", "creationdate", "isactive"]

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
