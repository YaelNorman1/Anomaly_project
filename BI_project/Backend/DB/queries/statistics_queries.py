from DB.constants import *

def get_user_statistics_query(user_id: int):
    return f"""
        SELECT *
        FROM {USER_STATISTIC_TABLE_NAME}
        WHERE userId = {user_id} 
    """