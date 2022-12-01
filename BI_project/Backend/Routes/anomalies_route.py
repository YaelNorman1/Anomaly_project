from fastapi import APIRouter, status, HTTPException
import pymysql as mysql

route = APIRouter()

@route.get("/anomalies", status_code=status.HTTP_200_OK)
def get_anomalies() -> list :
    try:
        return get_all_anomalies() 
    except mysql.MySQLError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)