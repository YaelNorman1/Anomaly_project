from fastapi import APIRouter, status, HTTPException
import pymysql as mysql
from DB.my_sql_manager import MySqlManager


route = APIRouter()
db_menager= MySqlManager()


@route.get("/categories", status_code=status.HTTP_200_OK)
def get_all_categories() -> list :
    try:
        return db_menager.get_categories()
    except mysql.MySQLError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)