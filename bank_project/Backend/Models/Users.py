from Models.Database import users_queries as udb
from utils.encryption import encode,decode

class Users:
    def get(self, name):
        result = udb.get_user(name)
        return result

    def get_all(self):
        result = udb.get_users()
        return result

    def add(self, user):
        user_name = user.user
        user_pwd = encode(user.pwd)
        user_ID = udb.get_user(user_name)
        if not user_ID:
            user_details = [user_name, user_pwd]
            result = udb.add_user(user_details)
            return result
        return None

    def delete(self, tr_id):
        result = udb.delete_transaction(tr_id)
        return result

    def validate(self, user_details):
        validation_entry = self.get(user_details.user)
        if validation_entry:
            if validation_entry["UserName"] == user_details.user and decode(validation_entry["UserPassword"]) == user_details.pwd:
                return True
        return False
