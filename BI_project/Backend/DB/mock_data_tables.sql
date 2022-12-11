use anomaly_db;


-- INSERT INTO user_statistics (userId, userName, avgNumOfWithdraws,avgNumOfDeposits,avgAmountWithdraw,avgAmountDeposit,numOfUpdates) VALUES(856486322,"Yael Norman",1,1,100,100,1);

-- INSERT INTO anomalies (userId,category,quantity,startDate,endDate) VALUES(1,"avgNumOfWithdraws",1,"2022-04-22 10:30:00.00","2022-04-22 11:00:53.44");

-- INSERT INTO anomalies (userId,category,quantity,startDate,endDate) VALUES(856486322,"avgNumOfWithdraws",324,"2022-04-22 10:30:00.00","2022-04-22 11:00:53.44");

-- INSERT INTO anomalies (userId,category,quantity,startDate,endDate) VALUES(1,"CATEGORY2",324,"2022-04-22 10:30:00.00","2022-04-22 11:00:53.44");

-- SELECT *
-- FROM anomalies 
-- WHERE (userId=Null OR userId=1) AND (category=Null OR category='') ;
