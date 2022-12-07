import Scheduler.bi_tables_manager as bi_tables_manager
from Scheduler.constants import *
from datetime import datetime, timedelta


def is_transaction_amount_anomaly(user_id, quantity, category):
    stats = bi_tables_manager.get_user_statistics(user_id)
    if not stats:
        return False
    expected_value = stats[0][category]
    is_it_anomaly = quantity > ((1 + AMOUNT_DEVIATION_PERCENTAGE) * expected_value)
    return is_it_anomaly


def calc_amount_avg(prev_avg, amount, num_of_updates):
    return (prev_avg * num_of_updates + amount) / (num_of_updates + 1)


def check_amount_anomaly(transaction):
    user_name = transaction["UserName"]
    user_id = transaction["TransactionUserID"]
    quantity = transaction["TransactionAmount"]
    category = (
        BI_EVENT_AVG_AMOUNT_DEPOSITS if quantity > 0 else BI_EVENT_AVG_AMOUNT_WITHDRAWS
    )
    if not is_transaction_amount_anomaly(user_id, quantity, category):
        ##We need to add and not check transactions num anomaly
        stats = bi_tables_manager.get_user_statistics(user_id)
        avg_num_withdraws = 0
        avg_num_deposits = 0
        if not stats:
            avg_amount_withdraws = quantity if quantity < 0 else 0
            avg_amount_deposits = quantity if quantity > 0 else 0
            bi_tables_manager.insert_user_statistics(
                user_id,
                user_name,
                avg_num_withdraws,
                avg_num_deposits,
                avg_amount_withdraws,
                avg_amount_deposits,
            )
        else:
            num_of_updates = stats[0]["numOfUpdates"]
            prev_avg_amount_withdraw = stats[0]["avgAmountWithdraw"]
            prev_avg_amount_deposite = stats[0]["avgAmountDeposit"]
            avg_amount_withdraws = (
                calc_amount_avg(prev_avg_amount_withdraw, quantity, num_of_updates)
                if quantity < 0
                else prev_avg_amount_withdraw
            )
            avg_amount_deposits = (
                calc_amount_avg(prev_avg_amount_deposite, quantity, num_of_updates)
                if quantity > 0
                else prev_avg_amount_deposite
            )
            bi_tables_manager.update_user_statistics(
                user_id,
                user_name,
                avg_num_withdraws,
                avg_num_deposits,
                avg_amount_withdraws,
                avg_amount_deposits,
            )
    else:
        now = datetime.now()
        prev = now - timedelta(
            hours=0, minutes=0, seconds=ANOMALIES_SCHEDULER_TIME_PERIOD
        )
        bi_tables_manager.add_amount_anomaly(user_id, category, quantity, prev, now)
