from DB.db_manager import DataBaseManager
import pymysql
from typing import List
from DB.queries.anomaly_queries import *
from DB.queries.statistics_queries import *
from DB.queries.category_quries import *


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

    def get_all_anomalies(self) -> List:
        query = get_all_anomalies_query
        anomalies = self._execute_query(query)
        return anomalies

    def get_user_statistics(self, user_id: int) -> dict:
        query = get_user_statistics_query(user_id)
        statistics = self._execute_query(query)
        return statistics

    def get_categories(self) -> list:
        query = get_all_categories_query
        categories = self._execute_query(query)
        return categories

    def add_anomaly(self, user_id, category, quantity, start_date, end_date) -> None:
        query = add_anomaly_query(user_id, category, quantity, start_date, end_date)
        self._execute_query(query)
