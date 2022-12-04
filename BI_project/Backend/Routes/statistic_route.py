from fastapi import APIRouter, status, HTTPException, Request
import pymysql as mysql
from DB.my_sql_manager import MySqlManager


route = APIRouter()
db_menager= MySqlManager()


@route.get("/statistics/{user_id}", status_code=status.HTTP_200_OK)
def get_user_statistics(user_id) -> dict :
    try:
        return db_menager.get_user_statistics(user_id)
    except mysql.MySQLError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)
    
@route.put("/statistics", status_code=status.HTTP_200_OK)
async def update_user_statistics(request:Request):
    try:
        stats = await request.json()
        db_menager.update_user_statistics(stats["userId"],stats["avgNumOfWithdraws"],stats["avgNumOfDeposits"],stats["avgAmountWithdraw"],stats["avgAmountDeposit"])
    except mysql.MySQLError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)

@route.post("/statistics", status_code=status.HTTP_200_OK)
async def insert_user_statistics(request:Request):
    try:
        stats = await request.json()
        db_menager.insert_user_statistics(stats["userId"],stats["avgNumOfWithdraws"],stats["avgNumOfDeposits"],stats["avgAmountWithdraw"],stats["avgAmountDeposit"])
    except mysql.MySQLError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)