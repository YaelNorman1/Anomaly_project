from datetime import datetime, timedelta
import pymysql
import requests
from constants import *
from anomalies_logic.user_statistics import UserStatistics

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="anomaly_db",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor,
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
            return result
    except TypeError as e:
        print(e)


def add_anomaly(user_id, category, quantity, start_date, end_date):
    try:
        with connection.cursor() as cursor:
            add_anomaly_query = f"""
                        INSERT INTO anomalies
                        (anomalyId,userId,category,quantity,startDate,endDate) 
                        VALUES (null,{user_id},'{category}',{quantity},%s,%s)
                        """
            cursor.execute(add_anomaly_query, (start_date, end_date))
            connection.commit()
    except TypeError as e:
        print(e)


def update_user_statistics(userStatistics: UserStatistics):
    try:
        with connection.cursor() as cursor:
            update_user_statistic_query = f"""
                        UPDATE user_statistics
                        SET 
                            userId={userStatistics.user_id}, 
                            userName='{userStatistics.user_name}',
                            avgNumOfWithdraws={userStatistics.avg_num_Of_withdraws},
                            avgNumOfDeposits={userStatistics.avg_num_Of_deposits},
                            avgAmountWithdraw={userStatistics.avg_amount_withdraw},
                            avgAmountDeposit={userStatistics.avg_amount_deposit},
                            numOfWithdraws={userStatistics.num_of_withdraws},
                            numOfDeposits={userStatistics.num_of_deposits},
                            numOfIntervals={userStatistics.num_of_intervals}
                        WHERE userId={userStatistics.user_id}
                        """
            cursor.execute(update_user_statistic_query)
            connection.commit()
    except TypeError as e:
        print(e)


def insert_user_statistics(userStatistics: UserStatistics):
    try:
        with connection.cursor() as cursor:
            add_user_statistic_query = f"""
                        INSERT INTO user_statistics
                        VALUES (
                            {userStatistics.user_id},
                            '{userStatistics.user_name}',
                            {userStatistics.avg_num_Of_withdraws},
                            {userStatistics.avg_num_Of_deposits},
                            {userStatistics.avg_amount_withdraw},
                            {userStatistics.avg_amount_deposit},
                            {userStatistics.num_of_withdraws},
                            {userStatistics.num_of_deposits},
                            {userStatistics.num_of_intervals}
                            )
                        """
            cursor.execute(add_user_statistic_query)
            connection.commit()
    except TypeError as e:
        print(e)


def update_num_of_intervals(user_id):
    try:
        with connection.cursor() as cursor:
            update_num_of_intervals_query = f"""
                        UPDATE user_statistics
                        SET 
                            numOfIntervals=numOfIntervals+1
                        WHERE userId={user_id}
                        """
            cursor.execute(update_num_of_intervals_query)
            connection.commit()
    except TypeError as e:
        print(e)


def update_avg_num(user_id, type, new_avg):
    try:
        with connection.cursor() as cursor:
            update_avg_num_query = f"""
                        UPDATE user_statistics
                        SET 
                            {type}={new_avg}
                        WHERE userId={user_id}
                        """
            cursor.execute(update_avg_num_query)
            connection.commit()
    except TypeError as e:
        print(e)
