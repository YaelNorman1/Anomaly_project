get_all_anomalies_query = f"""
    SELECT *
    FROM anomalies
"""
def add_anomaly_query(user_id,category,quantity,start_date,end_date):
    add_anomaly_query = f"""
    INSERT INTO anomalies 
    VALUES (null,{user_id},{category},{quantity},{start_date},{end_date})
    """
    return add_anomaly_query
