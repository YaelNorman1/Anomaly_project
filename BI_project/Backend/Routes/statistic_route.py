from fastapi import APIRouter, status, HTTPException, Request
import pymysql as mysql
from DB.my_sql_manager import MySqlManager


route = APIRouter()
db_menager= MySqlManager()


@route.get("/statistics/{user_id}", status_code=status.HTTP_200_OK)
def get_user_statistics(user_id) -> dict :
    try:
        return db_menager.get_user_statistics(int(user_id))[0]
    except mysql.MySQLError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)