from database.db import get_connection
from .entities.User import User

class UserModel():

    @classmethod
    def get_users(self):
        try:
            connection = get_connection()
            users = []

            with connection.cursor() as cursor:
                # Se puede usar tambien un procedimiento almacenado
                cursor.execute("SELECT id, name, lastname, email, age, numberphone, address, birthdate, creationdate, isactive FROM usuario ORDER BY creationdate ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    user = User(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8], row[9])
                    users.append(user)

            connection.close()
            return users

        except Exception as ex :
            raise Exception(ex)