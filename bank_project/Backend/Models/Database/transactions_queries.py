from Models.Database import dbController
from datetime import datetime,timedelta
connection = dbController.get_connection()
TBL_NAME = "transactions"


def get_transactions(user_id):
    try:
        with connection.cursor() as cursor:
            get_table = (
                f"SELECT * FROM {TBL_NAME} WHERE TransactionUserID = '{user_id}'"
            )
            cursor.execute(get_table)
            result = cursor.fetchall()
            print(result)
            return result
    except TypeError as e:
        print(e)


def get_breakdown(user_id):
    try:
        with connection.cursor() as cursor:
            get_categories_sum = f"SELECT TransactionCategory,SUM(TransactionAmount) AS categorySum FROM {TBL_NAME} WHERE TransactionUserID = '{user_id}' GROUP BY TransactionCategory;"
            cursor.execute(get_categories_sum)
            result = cursor.fetchall()
            return result
    except TypeError as e:
        print(e)


def get_balance(user_id):
    try:
        with connection.cursor() as cursor:
            get_categories_sum = f"SELECT SUM(TransactionAmount) AS balance FROM {TBL_NAME} WHERE TransactionUserID = '{user_id}' GROUP BY TransactionUserID;"
            cursor.execute(get_categories_sum)
            result = cursor.fetchone()
            return result
    except TypeError as e:
        print(e)


def add_transaction(transaction_details):
    try:
        with connection.cursor() as cursor:
            amount, vendor, category, date, userID = transaction_details
            query = f"INSERT INTO {TBL_NAME}(TransactionAmount,TransactionVendor,TransactionCategory,TransactionUserID, TransactionDate) values (%s,%s,%s,%s,%s)"
            params = (amount, vendor, category, userID, date)
            cursor.execute(query, params)
            connection.commit()
    except TypeError as e:
        print(e)


def delete_transaction(id):
    try:
        with connection.cursor() as cursor:
            query = f"DELETE FROM {TBL_NAME} WHERE TransactionID = '{id}' LIMIT 1"
            cursor.execute(query)
            connection.commit()
            return cursor.fetchall()
    except TypeError as e:
        print(e)