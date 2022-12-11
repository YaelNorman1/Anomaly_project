import pymysql

DB_NAME = "bank_app"
MOCK_DATA = [
    (
        -180,
        "bus",
        "transportation",
    ),
    (
        -200,
        "fuel",
        "transportation",
    ),
    (
        300,
        "cash",
        "salary",
    ),
]


def init_script():
    # drop existing DB - optional
    try:
        initial_connection = pymysql.connect(host="localhost", user="root", password="")
        print("deleting data base...")
        initial_connection.cursor().execute(f"drop database {DB_NAME}")
        print("data base deleted successfully")

    except Exception:
        print("data base dont exists!")

    # create DB
    try:
        initial_connection = pymysql.connect(host="localhost", user="root", password="")
        print("creating data base...")
        initial_connection.cursor().execute(f"create database {DB_NAME}")
        print("data base created successfully")

    except Exception:
        print("data base already exists!")

    # create tables
    try:
        initial_connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db=DB_NAME,
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor,
        )
        print("creating value table...")

        #          /// DO YOUR TABLE INITIALIZATION HERE ////         #

        query = """CREATE TABLE IF NOT EXISTS Users(
                    UserID VARCHAR(255) PRIMARY KEY,
                    UserName VARCHAR(255),
                    UserPassword VARCHAR(255))
                    """
        initial_connection.cursor().execute(query)
        initial_connection.commit()

        query = """CREATE TABLE IF NOT EXISTS Transactions(
                    TransactionID INT NOT NULL AUTO_INCREMENT,
                    TransactionAmount INT,
                    TransactionVendor VARCHAR(255),
                    TransactionCategory VARCHAR(255),
                    TransactionUserID VARCHAR(255),
                    TransactionDate DATETIME,
                    PRIMARY KEY (TransactionID),
                    FOREIGN KEY (TransactionUserID) REFERENCES Users(UserID))
                    """
        initial_connection.cursor().execute(query)
        initial_connection.commit()

        # example:
        # initial_connection.cursor().execute('create table dairy(dairy_ingredients varchar(255))')
        # initial_connection.commit()
        # initial_connection.cursor().execute('create table gluten(gluten_ingredients varchar(255))')
        # initial_connection.commit()

        print("table created successfully")
    except Exception:
        print("tables already exists!")

    # add ingridients:
    try:
        initial_connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db=DB_NAME,
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor,
        )
        with initial_connection.cursor() as cursor:
            print("inserting values...")

            #          /// DO YOUR TABLE INSERTS HERE ////         #
            # query = "INSERT INTO transactions(TransactionAmount,TransactionVendor,TransactionCategory) VALUES (%s,%s,%s)"
            # params = MOCK_DATA
            # print(params)
            # cursor.executemany(query,params)
            # initial_connection.commit()

    except Exception:
        print(Exception.args[0])
        print("coudlnt insert values!")


init_script()
