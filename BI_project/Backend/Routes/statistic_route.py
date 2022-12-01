from fastapi import APIRouter, status, HTTPException
import pymysql as mysql
from DB.my_sql_manager import MySqlManager


route = APIRouter()
db_menager= MySqlManager()


@route.get("/statistic/{user_id}/{category}", status_code=status.HTTP_200_OK)
def get_user_statistic(user_id, category) -> dict :
    num=5
    try:
        # return "hello"
        return db_menager.get_user_statistics(user_id, category)
    except mysql.MySQLError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)