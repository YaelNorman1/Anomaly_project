import bi_tables_manager as bi_tables_manager
from constants import *
from datetime import datetime, timedelta
from anomalies_logic.user_statistics import UserStatistics


def is_transaction_amount_anomaly(user_id, quantity, category):
    stats = bi_tables_manager.get_user_statistics(user_id)
    if not stats:
        return False
    expected_value = stats[0][category]
    is_it_anomaly = quantity > ((1 + AMOUNT_DEVIATION_PERCENTAGE) * expected_value)
    return is_it_anomaly


def calc_amount_avg(prev_avg, amount, counter):
    return (prev_avg * counter + amount) / (counter + 1)


def check_amount_anomaly(transaction):
    user_id = transaction["TransactionUserID"]
    user_name = transaction["UserName"]
    quantity = transaction["TransactionAmount"]
    category = (
        BI_EVENT_AVG_AMOUNT_DEPOSITS if quantity > 0 else BI_EVENT_AVG_AMOUNT_WITHDRAWS
    )
    if not is_transaction_amount_anomaly(user_id, quantity, category):
        stats = bi_tables_manager.get_user_statistics(user_id)
        if not stats:
            bi_tables_manager.insert_user_statistics(
                UserStatistics(
                    user_id,
                    user_name,
                    0,
                    0,
                    quantity if quantity < 0 else 0,
                    quantity if quantity > 0 else 0,
                    1 if quantity < 0 else 0,
                    1 if quantity > 0 else 0,
                    0,
                )
            )
        else:
            prev_avg_amount_withdraw = stats[0]["avgAmountWithdraw"]
            prev_avg_amount_deposite = stats[0]["avgAmountDeposit"]
            num_of_withdraws = stats[0]["numOfWithdraws"]
            num_of_deposits = stats[0]["numOfDeposits"]
            avg_amount_withdraw = (
                calc_amount_avg(prev_avg_amount_withdraw, quantity, num_of_withdraws)
                if quantity < 0
                else prev_avg_amount_withdraw
            )
            avg_amount_deposit = (
                calc_amount_avg(prev_avg_amount_deposite, quantity, num_of_deposits)
                if quantity > 0
                else prev_avg_amount_deposite
            )
            bi_tables_manager.update_user_statistics(
                UserStatistics(
                    user_id,
                    user_name,
                    stats[0]["avgNumOfWithdraws"],
                    stats[0]["avgNumOfDeposits"],
                    avg_amount_withdraw,
                    avg_amount_deposit,
                    num_of_withdraws + 1 if quantity < 0 else 0,
                    num_of_deposits + 1 if quantity > 0 else 0,
                    stats[0]["numOfIntervals"],
                )
            )
    else:
        now = datetime.now()
        prev = now - timedelta(
            hours=0, minutes=0, seconds=ANOMALIES_SCHEDULER_TIME_PERIOD
        )
        bi_tables_manager.add_anomaly(user_id, category, quantity, prev, now)
