from fastapi import APIRouter, status, HTTPException, Request
import pymysql as mysql
from DB.my_sql_manager import MySqlManager

route = APIRouter()
db_menager= MySqlManager()

@route.get("/anomalies", status_code=status.HTTP_200_OK)
def get_anomalies() -> list :
    try:
        return db_menager.get_all_anomalies() 
    except mysql.MySQLError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)

@route.post("/anomalies",status_code=status.HTTP_201_CREATED)
async def add_anomaly(request: Request):
    anomaly = await request.json()
    try:
        db_menager.add_anomaly(anomaly["userId"],anomaly["category"],anomaly["quantity"],anomaly["startDate"],anomaly["endDate"])
    except mysql.MySQLError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)