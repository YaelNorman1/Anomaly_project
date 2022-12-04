import schedule
import time
from constants import *
import bi_api_manager
import transactions_table_manager
from datetime import datetime,timedelta
import requests

async def check_amount_anomaly(user_id,quantity, category):
    stats = await bi_api_manager.get_user_statistics(user_id)
    if not stats:
        return False
    expected_value = stats[category]
    return quantity> ((1 + AMOUNT_DEVIATION_PERCENTAGE) * expected_value)
        

def check_transactions_num_anomaly():
    pass

async def update_anomalies_table():
    now = datetime.now()
    prev = now-timedelta(hours=0,minutes=0,seconds=ANOMALIES_SCHEDULER_TIME_PERIOD)
    recent_transactions = transactions_table_manager.get_recent_transactions(ANOMALIES_SCHEDULER_TIME_PERIOD)
    for transaction in recent_transactions: 
        quantity = transaction["TransactionAmount"]
        user_id = transaction["TransactionUserID"]
        category = BI_EVENT_AVG_AMOUNT_DEPOSITS if quantity>0 else BI_EVENT_AVG_AMOUNT_WITHDRAWS
        if await check_amount_anomaly(user_id,quantity, category):
            bi_api_manager.add_anomaly(user_id,category,quantity,prev,now)

def calc_amount_avg(prev, amount, num_of_updates):
    return (prev+amount)/(num_of_updates+1)

async def update_user_statistics_table():
    recent_transactions = transactions_table_manager.get_recent_transactions(USER_STATISTICS_SCHEDULER_TIME_PERIOD)
    for transaction in recent_transactions:
        user_id = transaction["TransactionUserID"]
        quantity = transaction["TransactionAmount"]
        category = BI_EVENT_AVG_AMOUNT_DEPOSITS if quantity>0 else BI_EVENT_AVG_AMOUNT_WITHDRAWS
        if (not await check_amount_anomaly(user_id,quantity, category)):
             ##We need to add and not check transactions num anomaly
            stats = bi_api_manager.get_user_statistics(user_id)
            avg_num_withdraws = 0
            avg_num_deposits = 0
            if not stats:
                avg_amount_withdraws = quantity if quantity<0 else 0
                avg_amount_deposits = quantity if quantity>0 else 0
                bi_api_manager.insert_user_statistics(user_id,avg_num_withdraws,avg_num_deposits,avg_amount_withdraws,avg_amount_deposits)
            else:
                num_of_updates = stats["numOfUpdates"]
                prev_avg_amount_withdraw = stats["avgAmountWithdraw"]
                prev_avg_amount_deposite = stats["avgAmountDeposit"]
                avg_amount_withdraws = calc_amount_avg(prev_avg_amount_withdraw, quantity, num_of_updates) if quantity<0 else avg_amount_withdraws
                avg_amount_deposits = calc_amount_avg(prev_avg_amount_deposite, quantity, num_of_updates) if quantity>0 else avg_amount_deposits
                bi_api_manager.update_user_statistics(user_id,avg_num_withdraws,avg_num_deposits,avg_amount_withdraws,avg_amount_deposits)



# schedule.every(ANOMALIES_SCHEDULER_TIME_PERIOD).seconds.do(update_anomalies_table)
schedule.every(USER_STATISTICS_SCHEDULER_TIME_PERIOD).seconds.do(update_user_statistics_table)
while True:
    schedule.run_pending()
    time.sleep(1)
    print("scheduler is running")