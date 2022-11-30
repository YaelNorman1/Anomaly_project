from pydantic import BaseModel


class Transaction(BaseModel):
    amount: int
    vendor: str
    category: str
    user: str