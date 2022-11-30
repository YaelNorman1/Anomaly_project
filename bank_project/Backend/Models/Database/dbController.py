import pymysql
# from Models.Database import dbInitializer
from utils.decorators import run_once

DB_NAME = "bank_app"


# @run_once
def run_init_script():
    print("init db")
    # dbInitializer.init_script()


def get_connection():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db=DB_NAME,
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor,
    )
    return connection


def close_connection():
    connection = get_connection()
    connection.close()
