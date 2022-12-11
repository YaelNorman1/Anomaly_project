from DB.constants import *

def get_user_statistics_query(user_id: str):
    return f"""
        SELECT *
        FROM {USER_STATISTIC_TABLE_NAME}
        WHERE userId ="{user_id}" 
    """