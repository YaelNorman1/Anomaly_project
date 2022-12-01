from constants import DB_NAME

delete_db_query = f"""
            DROP DATABASE IF EXISTS {DB_NAME};
            """


create_db_query = f"""
            CREATE DATABASE IF NOT EXISTS {DB_NAME};
            """