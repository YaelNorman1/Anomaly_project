from Models.Database import transactions_queries as tdb
from Models.Database import users_queries as udb


class Transactions:

    def get_all(self, user_name):
        user_ID = udb.get_user(user_name)["UserID"]
        result = tdb.get_transactions(user_ID)
        return result
    
    def add(self, transaction):
        user_name = transaction.user
        user_ID = udb.get_user(user_name)["UserID"]
        transaction_details = [transaction.amount, transaction.vendor, transaction.category, transaction.date, user_ID]
        result = tdb.add_transaction(transaction_details)
        return result

    def delete(self, tr_id):
        result = tdb.delete_transaction(tr_id)
        return result

    def get_balance(self, user_name):
        user_ID = udb.get_user(user_name)["UserID"]
        result = tdb.get_balance(user_ID)
        try:
            return int(result['balance'])
        except:
            return 0
    
    def get_breakdown(self, user_name):
        user_ID = udb.get_user(user_name)["UserID"]
        result = tdb.get_breakdown(user_ID)
        return result