from pydantic import BaseModel
import datetime


class Transaction(BaseModel):
    amount: int
    vendor: str
    category: str
    user: str
    date: datetime.datetime

    def set_date(self, date: datetime.datetime):
        self.date = date
