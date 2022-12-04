from datetime import datetime,timedelta
import pymysql
import requests
from constants import *


async def get_user_statistics(user_id):
        result = await requests.get(f"{BI_USER_STATICTICS_ADDRESS}/{user_id}")
        return result

def add_anomaly(user_id,category,quantity,start_date,end_date):
        anomaly = {
                "userId": user_id,
                "category": category,
                "quantity": quantity,
                "startDate": start_date,
                "endDate": end_date
        }
        requests.post(f"{BI_ANOMALIES_ADDRESS}",data =anomaly)

def update_user_statistics(user_id, avg_num_withdraws, avg_num_deposits, avg_amount_withdraws, avg_amount_deposit):
        stats = {
                "userId":user_id,
                "avgNumOfWithdraws":avg_num_withdraws,
                "avgNumOfDeposits":avg_num_deposits,
                "avgAmountWithdraw":avg_amount_withdraws,
                "avgAmountDeposit": avg_amount_deposit
        }
        requests.put(f"{BI_USER_STATICTICS_ADDRESS}", data=stats)

def insert_user_statistics(user_id, avg_num_withdraws, avg_num_deposits, avg_amount_withdraws, avg_amount_deposit):
        stats = {
                "userId":user_id,
                "avgNumOfWithdraws":avg_num_withdraws,
                "avgNumOfDeposits":avg_num_deposits,
                "avgAmountWithdraw":avg_amount_withdraws,
                "avgAmountDeposit": avg_amount_deposit
        }
        requests.post(f"{BI_USER_STATICTICS_ADDRESS}", data=stats)