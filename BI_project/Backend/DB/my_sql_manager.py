from DB.db_manager import DataBaseManager
import pymysql


class MySqlManager(DataBaseManager):
    def __init__(self) -> None:
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="anomaly_db",
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor,
        )
        self.connection.autocommit(True)

    def _execute_query(self, query):
        self.connection.ping()
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
