from Models.Database import dbController
import random
import string
connection = dbController.get_connection()
TBL_NAME = "users"

# def get_users():
#     try:
#         with connection.cursor() as cursor:
#             get_table = f"SELECT * FROM {TBL_NAME}"
#             cursor.execute(get_table)
#             result = cursor.fetchall()
#             return result
#     except TypeError as e:
#         print(e)

def get_user(name):
    try:
        with connection.cursor() as cursor:
            query = f"SELECT * FROM {TBL_NAME} WHERE UserName = '{name}' LIMIT 1"
            cursor.execute(query)
            connection.commit()
            return cursor.fetchone()
    except TypeError as e:
        print(e)

def add_user(user_details):
    try:
        with connection.cursor() as cursor:
            UserName, UserPassword = user_details
            UserID = ''.join([random.choice(string.ascii_letters
            + string.digits) for n in range(10)])
            query = f"INSERT INTO {TBL_NAME}(UserID,UserName,UserPassword) values (%s,%s,%s)"
            params = (UserID,UserName, UserPassword)
            cursor.execute(query,params)
            connection.commit()
            return cursor.lastrowid
    except TypeError as e:
        print(e)

def delete_user(name):
    try:
        with connection.cursor() as cursor:
            query = f"DELETE FROM {TBL_NAME} WHERE UserName = '{name}' LIMIT 1"
            cursor.execute(query)
            connection.commit()
            return cursor.fetchall()
    except TypeError as e:
        print(e)

 
