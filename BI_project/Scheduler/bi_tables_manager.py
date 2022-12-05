from datetime import datetime,timedelta
import pymysql
import requests
from constants import *

connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="anomaly_db",
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor
)


def get_user_statistics(user_id):
        try:
                with connection.cursor() as cursor:
                        get_user_statistics = f"""
                        SELECT *
                        FROM user_statistics
                        WHERE userId = {user_id} 
                        """
                        cursor.execute(get_user_statistics)
                        connection.commit()
                        result = cursor.fetchall()
                        print(result)
                        return result
        except TypeError as e:
                print(e)


def add_anomaly(user_id,category,quantity,start_date,end_date):
        try:
                with connection.cursor() as cursor:
                        add_anomaly_query = f"""
                        INSERT INTO anomalies
                        (anomalyId,userId,category,quantity,startDate,endDate) 
                        VALUES (null,{user_id},'{category}',{quantity},%s,%s)
                        """
                        cursor.execute(add_anomaly_query, (start_date,end_date))
                        connection.commit()
        except TypeError as e:
                print(e)

def update_user_statistics(user_id, user_name, avg_num_withdraws, avg_num_deposits, avg_amount_withdraws, avg_amount_deposit):
        try:
                with connection.cursor() as cursor:
                        update_user_statistic_query = f"""
                        UPDATE user_statistics
                        SET userId={user_id}, 
                        userName='{user_name}',
                        avgNumOfWithdraws={avg_num_withdraws},
                        avgNumOfDeposits={avg_num_deposits},
                        avgAmountWithdraw={avg_amount_withdraws},
                        avgAmountDeposit={avg_amount_deposit},
                        numOfUpdates=numOfUpdates+1
                        WHERE userId={user_id}
                        """
                        cursor.execute(update_user_statistic_query)
                        connection.commit()
        except TypeError as e:
                print(e)

def insert_user_statistics(user_id,user_name, avg_num_withdraws, avg_num_deposits, avg_amount_withdraws, avg_amount_deposit):
        try:
                with connection.cursor() as cursor:
                        add_user_statistic_query = f"""
                        INSERT INTO user_statistics
                        VALUES ({user_id},'{user_name}',{avg_num_withdraws},{avg_num_deposits},{avg_amount_withdraws},{avg_amount_deposit},1)
                        """
                        cursor.execute(add_user_statistic_query)
                        connection.commit()
        except TypeError as e:
                print(e)