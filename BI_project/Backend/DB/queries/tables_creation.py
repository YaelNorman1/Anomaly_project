from constants import *

create_anomalies_table = f"""
            CREATE TABLE IF NOT EXISTS {ANOMALY_TABLE_NAME}(
                anomalyId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                userId INT,
                category VARCHAR(255),
                quantity INT,
                startDate DATE,
                endDate DATE,
                FOREIGN KEY(userId) REFERENCES {USER_STATISTIC_TABLE_NAME}(userId)
                );
            """

create_user_statistics_table = f"""
            CREATE TABLE IF NOT EXISTS {USER_STATISTIC_TABLE_NAME}(
                userId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                avgNumOfWithdraws FLOAT,
                avgNumOfDeposits FLOAT,
                avgAmountWithdraw FLOAT,
                avgAmountDeposit FLOAT,
                numOfUpdates INT
                );
            """

