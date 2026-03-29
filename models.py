from pydantic import BaseModel

class UserInput(BaseModel):
    age: int
    income: float
    expenses: float
    savings: float
    goal_amount: float

class TaxInput(BaseModel):
    income: float
