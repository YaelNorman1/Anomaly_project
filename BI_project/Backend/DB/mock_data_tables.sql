use anomaly_db;


INSERT INTO user_statistics (avgNumOfWithdraws,avgNumOfDeposits,avgAmountWithdraw,avgAmountDeposit,numOfUpdates) VALUES(1,1,100,100,1);

INSERT INTO anomalies (userId,category,quantity,startDate,endDate) VALUES(1,"avgNumOfWithdraws",1,"2022-04-22 10:30:00.00","2022-04-22 11:00:53.44");

INSERT INTO anomalies (userId,category,quantity,startDate,endDate) VALUES(1,"avgNumOfWithdraws",324,"2022-04-22 10:30:00.00","2022-04-22 11:00:53.44");

INSERT INTO anomalies (userId,category,quantity,startDate,endDate) VALUES(1,"CATEGORY2",324,"2022-04-22 10:30:00.00","2022-04-22 11:00:53.44");

