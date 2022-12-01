from constants import *
import pymysql
from connection import get_general_connection, get_connection_to_db
from queries.db_queries import delete_db_query,create_db_query
from queries.tables_creation import create_anomalies_table,create_user_statistics_table

def create_db():
    try:
        connection = get_general_connection()
        with connection.cursor() as cursor:
            cursor.execute(delete_db_query) #if db already exists.
            cursor.execute(create_db_query)
            print("db created successfully")
            connection.commit()
    except Exception as e:
        print(e)

def create_tables():
    try:
        connection = get_connection_to_db(DB_NAME)
        with connection.cursor() as cursor:
            cursor.execute(create_user_statistics_table)
            print("user statistics table created successfully")
            cursor.execute(create_anomalies_table)
            print("anomalies table created successfully")
            connection.commit()
    except Exception as e:
        print(e)

def start():
    create_db()
    create_tables()

start()