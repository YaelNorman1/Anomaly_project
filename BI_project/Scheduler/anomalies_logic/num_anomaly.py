from collections import Counter
import bi_tables_manager
import bi_tables_manager as bi_tables_manager
from constants import TRANSACTIONS_NUM_DEVIATION, ANOMALIES_SCHEDULER_TIME_PERIOD
from datetime import datetime, timedelta


def get_user_counter(transactions):
    users = list(
        map(lambda transaction: transaction["TransactionUserID"], transactions)
    )
    return Counter(users)


def calc_avg_num(prev_avg, cur_num, num_of_intervals):
    if prev_avg == 0:
        return cur_num
    return (prev_avg * num_of_intervals + cur_num) / (num_of_intervals + 1)


def is_num_anomaly(prev_avg, num_of_transactions):
    return num_of_transactions > ((1 + TRANSACTIONS_NUM_DEVIATION) * prev_avg)


def check_num_anomaly_per_type(type, user_transactions):
    for user_id in user_transactions:
        stats = bi_tables_manager.get_user_statistics(user_id)
        prev_avg = stats[0][type]
        num_of_transactions = user_transactions[user_id]
        new_avg = calc_avg_num(
            prev_avg,
            num_of_transactions,
            stats[0]["numOfIntervals"],
        )
        if prev_avg != 0 and is_num_anomaly(prev_avg, num_of_transactions):
            now = datetime.now()
            prev = now - timedelta(
                hours=0, minutes=0, seconds=ANOMALIES_SCHEDULER_TIME_PERIOD
            )
            bi_tables_manager.add_anomaly(user_id, type, num_of_transactions, prev, now)
        else:
            bi_tables_manager.update_avg_num(user_id, type, new_avg)


def check_transactions_num_anomaly(transactions):
    all_withdraws = list(
        filter(lambda transaction: transaction["TransactionAmount"] < 0, transactions)
    )
    all_deposits = list(
        filter(lambda transaction: transaction["TransactionAmount"] > 0, transactions)
    )
    users_withdraws = get_user_counter(all_withdraws)
    users_deposits = get_user_counter(all_deposits)

    check_num_anomaly_per_type("avgNumOfWithdraws", users_withdraws)
    check_num_anomaly_per_type("avgNumOfDeposits", users_deposits)

    for user_id in get_user_counter(transactions):
        bi_tables_manager.update_num_of_intervals(user_id)
