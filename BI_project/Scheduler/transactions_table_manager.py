from datetime import datetime, timedelta
import pymysql
import requests
from constants import *

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="bank_app",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor,
)


def get_recent_transactions(time_cycle):
    now = datetime.now()
    prev_time_slot = now - timedelta(hours=0, minutes=0, seconds=time_cycle)
    try:
        with connection.cursor() as cursor:
            get_table = f"""
            SELECT * 
            FROM transactions AS t JOIN users AS u
            ON t.TransactionUserID = u.UserID
            WHERE TransactionDate >= %s
            """
            cursor.execute(get_table, (prev_time_slot,))
            connection.commit()
            result = cursor.fetchall()
            return result
    except TypeError as e:
        print(e)
