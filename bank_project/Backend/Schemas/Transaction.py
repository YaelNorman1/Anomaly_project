from pydantic import BaseModel, Field
import datetime


class Transaction(BaseModel):
    amount: int
    vendor: str
    category: str
    user: str
    date: datetime.datetime = Field(default=None)

    def set_date(self, date: datetime.datetime):
        self.date = date
