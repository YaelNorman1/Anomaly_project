from datetime import datetime,timedelta
import pymysql

connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="bank_app",
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor,
)

def get_recent_transactions(time_cycle):
    now = datetime.now()
    prev_time_slot=now-timedelta(hours=0,minutes=0,seconds=time_cycle)
    try:
        with connection.cursor() as cursor:
            get_table = (
                f"SELECT * FROM transactions WHERE TransactionDate>={prev_time_slot}"
            )
            cursor.execute(get_table)
            result = cursor.fetchall()
            print(result)
            return result
    except TypeError as e:
        print(e)