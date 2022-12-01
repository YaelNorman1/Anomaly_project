import pymysql
from constants import *

def get_general_connection():
    return pymysql.connect(
        host=CONNECTION_HOST, user=CONNECTION_USER, password=CONNECTION_PASSWORD
    )

def get_connection_to_db(db_name: str):
    return pymysql.connect(
        host=CONNECTION_HOST,
        user=CONNECTION_USER,
        password=CONNECTION_PASSWORD,
        db=db_name,
        charset=CONNECTION_CHARSET,
        cursorclass=pymysql.cursors.DictCursor,
    )
