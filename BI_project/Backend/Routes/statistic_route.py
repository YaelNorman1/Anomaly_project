from fastapi import APIRouter, status, HTTPException
import pymysql as mysql

route = APIRouter()

@route.get("/statistic/{user_id}/{category}", status_code=status.HTTP_200_OK)
def get_user_statistic(user_id, category) -> dict :
    try:
        return get_user_statistics(user_id, category)
    except mysql.MySQLError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)