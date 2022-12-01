import schedule
import time
from constants import *
import transactions_table_manager

def check_amount_anomaly(transaction):
    pass

def check_transactions_num_anomaly():
    pass

def update_BI_tables():
    recent_transactions = transactions_table_manager.get_recent_transactions(SCHEDULER_TIME_PERIOD)
    for transaction in recent_transactions:
        if check_amount_anomaly(transaction):
            pass
        else:
            pass


schedule.every(SCHEDULER_TIME_PERIOD).seconds.do(update_BI_tables)
while True:
    schedule.run_pending()
    time.sleep(1)