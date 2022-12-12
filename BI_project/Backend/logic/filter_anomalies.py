from Routes.category_route import get_all_categories
from datetime import datetime

def filtered_anomalies(anomalies, userId:str, category,fromDate, toDate) -> list:
    filtered_anomalies_list = anomalies
    if userId != '' and userId != None:
        filtered_anomalies_list= generic_filtering("userId", userId, anomalies)
    
    if category in get_all_categories() :
        filtered_anomalies_list= generic_filtering("category", category, filtered_anomalies_list)
    
    if fromDate != '' and userId != None:
        filtered_anomalies_list= fromDate_filtering(fromDate, filtered_anomalies_list)
    
    if toDate != '' and userId != None:
        filtered_anomalies_list= toDate_filtering(toDate, filtered_anomalies_list)

    return filtered_anomalies_list

def generic_filtering(filter_category, filter_value, anomalies_list):
    if filter_value is not None:
        anomalies_list = list(filter(lambda x: str(x[filter_category])== filter_value, anomalies_list))
    return anomalies_list

def fromDate_filtering(filter_value, anomalies_list):
    if filter_value is not None:
        anomalies_list = list(filter(lambda anomaly: anomaly['endDate'].date()  >= datetime.strptime(filter_value, '%Y-%m-%d').date() , anomalies_list))
    return anomalies_list

def toDate_filtering(filter_value, anomalies_list):
    if filter_value is not None:
        anomalies_list = list(filter(lambda anomaly: anomaly['startDate'].date()  <= datetime.strptime(filter_value, '%Y-%m-%d').date() , anomalies_list))
    return anomalies_list



