class UserStatistics:
    def __init__(
        self,
        user_id: str,
        user_name: str,
        avg_num_Of_withdraws: float,
        avg_num_Of_deposits: float,
        avg_amount_withdraw: float,
        avg_amount_deposit: float,
        num_of_withdraws: int,
        num_of_deposits: int,
        num_of_intervals: int,
    ) -> None:
        self.user_id = user_id
        self.user_name = user_name
        self.avg_num_Of_withdraws = avg_num_Of_withdraws
        self.avg_num_Of_deposits = avg_num_Of_deposits
        self.avg_amount_withdraw = avg_amount_withdraw
        self.avg_amount_deposit = avg_amount_deposit
        self.num_of_withdraws = num_of_withdraws
        self.num_of_deposits = num_of_deposits
        self.num_of_intervals = num_of_intervals
