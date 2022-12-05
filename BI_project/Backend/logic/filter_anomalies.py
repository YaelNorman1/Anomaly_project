def filtered_anomalies(anomalies, userId, category,fromDate, toDate) -> list:
    filtered_anomalies_list= generic_filtering("userId", userId, anomalies)
    filtered_anomalies_list= generic_filtering("category", category, filtered_anomalies_list)
    filtered_anomalies_list= generic_filtering("fromDate", fromDate, filtered_anomalies_list)
    filtered_anomalies_list= generic_filtering("toDate", toDate, filtered_anomalies_list)
    print(filtered_anomalies_list)

def generic_filtering(filter_category, filter_value, anomalies_list):
    if filter_value is not None:
        anomalies_list = list(filter(lambda x: x[filter_category]== filter_value, anomalies_list))
    return anomalies_list

# filtered_anomalies([
#     {
#         "anomalyId": 2,
#         "userName": "yael",
#         "category": "avgNumOfWithdraws",
#         "quantity": 1,
#         "startDate": "2022-04-22T10:30:00",
#         "endDate": "2022-04-22T11:00:53"
#     },
#     {
#         "anomalyId": 2,
#         "userName": "ohad",
#         "category": "avgNumOfWithdraws",
#         "quantity": 1,
#         "startDate": "2022-04-22T10:30:00",
#         "endDate": "2022-04-22T11:00:53"
#     }], "yael", None, None, None)