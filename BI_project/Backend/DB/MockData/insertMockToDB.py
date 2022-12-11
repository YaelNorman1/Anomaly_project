import pymysql
import datetime

anomalies = [{'anomalyId': 1, 'userId': 'Px3ADejnL4', 'category': 'avgAmountDeposit', 'quantity': 60000, 'startDate': datetime.datetime(2022, 12, 11, 15, 34, 52), 'endDate': datetime.datetime(2022, 12, 11, 15, 35, 22)}, {'anomalyId': 2, 'userId': 'sjpui0UcGs', 'category': 'avgNumOfDeposits', 'quantity': 6, 'startDate': datetime.datetime(2022, 12, 11, 15, 35, 53), 'endDate': datetime.datetime(2022, 12, 11, 15, 36, 23)}, {'anomalyId': 3, 'userId': 'rkM2q8ZFo1', 'category': 
'avgNumOfWithdraws', 'quantity': 10, 'startDate': datetime.datetime(2022, 12, 11, 15, 36, 54), 'endDate': datetime.datetime(2022, 12, 11, 15, 37, 24)}, {'anomalyId': 4, 'userId': 'vgqpYn8nEf', 'category': 'avgAmountWithdraw', 'quantity': -6000, 'startDate': datetime.datetime(2022, 12, 11, 15, 38, 25), 'endDate': datetime.datetime(2022, 12, 11, 15, 38, 55)}, {'anomalyId': 5, 'userId': 'Px3ADejnL4', 'category': 'avgNumOfDeposits', 'quantity': 6, 'startDate': datetime.datetime(2022, 12, 11, 15, 42, 59), 'endDate': datetime.datetime(2022, 12, 11, 15, 43, 29)}, {'anomalyId': 6, 
'userId': 'Px3ADejnL4', 'category': 'avgAmountWithdraw', 'quantity': -15000, 'startDate': datetime.datetime(2022, 12, 11, 15, 44), 'endDate': datetime.datetime(2022, 12, 11, 15, 44, 30)}]

user_statistics = [{'userId': 'Px3ADejnL4', 'userName': 'YaelNorman', 'avgNumOfWithdraws': 1.0, 'avgNumOfDeposits': 1.5, 'avgAmountWithdraw': -100.0, 'avgAmountDeposit': 100.0, 'numOfWithdraws': 1, 'numOfDeposits': 0, 'numOfIntervals': 5}, {'userId': 'rkM2q8ZFo1', 'userName': 'TomNahum', 'avgNumOfWithdraws': 2.0, 'avgNumOfDeposits': 1.0, 'avgAmountWithdraw': -5000.0, 'avgAmountDeposit': 5000.0, 'numOfWithdraws': 12, 'numOfDeposits': 0, 'numOfIntervals': 2}, {'userId': 'sjpui0UcGs', 'userName': 'OhadHofi', 'avgNumOfWithdraws': 0.0, 'avgNumOfDeposits': 1.0, 'avgAmountWithdraw': 0.0, 'avgAmountDeposit': 100.0, 'numOfWithdraws': 0, 'numOfDeposits': 7, 'numOfIntervals': 2}, {'userId': 'vgqpYn8nEf', 'userName': 'LotemHiki', 'avgNumOfWithdraws': 1.0, 'avgNumOfDeposits': 1.0, 'avgAmountWithdraw': -100.0, 'avgAmountDeposit': 8000.0, 'numOfWithdraws': 1, 'numOfDeposits': 0, 'numOfIntervals': 3}]

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="anomaly_db",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

def insertAnomaly(anomalyId,userId,category,quantity,startDate,endDate):
    try:
        with connection.cursor() as cursor:
            query = f'INSERT INTO anomalies (anomalyId,userId,category,quantity,startDate,endDate) VALUES({anomalyId},"{userId}","{category}",{quantity},%s,%s);'
            cursor.execute(query,(startDate,endDate))
            connection.commit()
    except TypeError as e:
        print(e)

def insertUserStatistic(userId,userName,avgNumOfWithdraws,avgNumOfDeposits,avgAmountWithdraw,avgAmountDeposit,numOfWithdraws,numOfDeposits,numOfIntervals):
    try:
        with connection.cursor() as cursor:
            query = f'INSERT INTO user_statistics (userId,userName,avgNumOfWithdraws,avgNumOfDeposits,avgAmountWithdraw,avgAmountDeposit,numOfWithdraws,numOfDeposits,numOfIntervals) VALUES("{userId}","{userName}",{avgNumOfWithdraws},{avgNumOfDeposits},{avgAmountWithdraw},{avgAmountDeposit},{numOfWithdraws},{numOfDeposits},{numOfIntervals});'
            cursor.execute(query)
            connection.commit()
    except TypeError as e:
        print(e)

def insert_to_user_statistics():
    for user_statistic in user_statistics:
        insertUserStatistic(user_statistic["userId"],user_statistic["userName"],user_statistic["avgNumOfWithdraws"],user_statistic["avgNumOfDeposits"],user_statistic["avgAmountWithdraw"],user_statistic["avgAmountDeposit"],user_statistic["numOfWithdraws"],user_statistic["numOfDeposits"],user_statistic["numOfIntervals"])
def insert_to_anomalies():
    for anomaly in anomalies:
        insertAnomaly(anomaly["anomalyId"],anomaly["userId"],anomaly["category"],anomaly["quantity"],anomaly["startDate"],anomaly["endDate"])

def insert_to_db():
    insert_to_user_statistics()
    insert_to_anomalies()

insert_to_db()