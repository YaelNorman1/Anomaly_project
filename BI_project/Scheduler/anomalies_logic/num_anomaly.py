from collections import Counter
from bi_tables_manager import update_num_of_intervals, update_avg_num
import bi_tables_manager as bi_tables_manager


def get_user_counter(transactions):
    users = list(
        map(lambda transaction: transaction["TransactionUserID"], transactions)
    )
    return Counter(users)


def calc_avg_num(prev_avg, cur_num, num_of_intervals):
    if prev_avg == 0:
        return cur_num
    return (prev_avg * num_of_intervals + cur_num) / (num_of_intervals + 1)


def check_num_anomaly_per_type(type, user_transactions):
    for user_id in user_transactions:
        stats = bi_tables_manager.get_user_statistics(user_id)
        new_avg = calc_avg_num(
            stats[0][type],
            user_transactions[user_id],
            stats[0]["numOfIntervals"],
        )
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
        update_num_of_intervals(user_id)
