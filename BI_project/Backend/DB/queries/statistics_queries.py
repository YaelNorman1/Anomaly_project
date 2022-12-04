from DB.constants import *

def get_user_statistics_query(user_id: int):
    return f"""
        SELECT *
        FROM {USER_STATISTIC_TABLE_NAME}
        WHERE userId = {user_id} 
    """

def update_user_statistics_query(user_id, avg_num_withdraws, avg_num_deposits, avg_amount_withdraws, avg_amount_deposit):
    return f"""
        UPDATE {USER_STATISTIC_TABLE_NAME}
        SET {USER_STATISTICS_AVG_NUM_OF_WITHDRAWS}={avg_num_withdraws}, 
        {USER_STATISTICS_AVG_NUM_OF_DEPOSITS}={avg_num_deposits},
        {USER_STATISTICS_AVG_AMOUNT_WITHDRAW}={avg_amount_withdraws},
        {USER_STATISTICS_AVG_AMOUNT_DEPOSIT}={avg_amount_deposit}
        {USER_STATISTICS_NUM_OF_UPDATES}={USER_STATISTICS_NUM_OF_UPDATES}+1
        WHERE {USER_STATISTICS_USER_ID}={user_id}
    """

def insert_user_statistics_query(user_id, avg_num_withdraws, avg_num_deposits, avg_amount_withdraws, avg_amount_deposit):
    return f"""
        INSERT INTO {USER_STATISTIC_TABLE_NAME}
        VALUES {user_id},{avg_num_withdraws},{avg_num_deposits},{avg_amount_withdraws},{avg_amount_deposit},1
    """