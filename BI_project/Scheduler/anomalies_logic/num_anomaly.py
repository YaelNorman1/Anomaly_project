from collections import Counter


def check_transactions_num_anomaly(transactions):
    users = list(
        map(lambda transaction: transaction["TransactionUserID"], transactions)
    )
    users_counter = Counter(users)
    print(users_counter)
