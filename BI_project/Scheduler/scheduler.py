import schedule
import time
import transactions_table_manager
from constants import *
from anomalies_logic.amount_anomaly import check_amount_anomaly
from anomalies_logic.num_anomaly import check_transactions_num_anomaly


def update_bi_database():
    recent_transactions = transactions_table_manager.get_recent_transactions(
        USER_STATISTICS_SCHEDULER_TIME_PERIOD
    )
    for transaction in recent_transactions:
        check_amount_anomaly(transaction)
    check_transactions_num_anomaly(recent_transactions)


schedule.every(USER_STATISTICS_SCHEDULER_TIME_PERIOD).seconds.do(update_bi_database)


while True:
    schedule.run_pending()
    time.sleep(1)
    print("scheduler is running")
