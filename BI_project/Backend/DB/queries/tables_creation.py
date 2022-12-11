from constants import *

create_anomalies_table = f"""
            CREATE TABLE IF NOT EXISTS {ANOMALY_TABLE_NAME}(
                anomalyId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                userId VARCHAR(255),
                category VARCHAR(255),
                quantity INT,
                startDate DATETIME,
                endDate DATETIME,
                FOREIGN KEY(userId) REFERENCES {USER_STATISTIC_TABLE_NAME}(userId)
                );
            """

create_user_statistics_table = f"""
            CREATE TABLE IF NOT EXISTS {USER_STATISTIC_TABLE_NAME}(
                userId VARCHAR(255) PRIMARY KEY,
                userName VARCHAR(255),
                avgNumOfWithdraws FLOAT,
                avgNumOfDeposits FLOAT,
                avgAmountWithdraw FLOAT,
                avgAmountDeposit FLOAT,
                numOfWithdraws INT,
                numOfDeposits INT,
                numOfIntervals INT
                );
            """
