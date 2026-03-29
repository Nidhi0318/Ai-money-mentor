from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserInput(BaseModel):
    age: int
    income: float
    expenses: float
    savings: float
    goal_amount: float

class TaxInput(BaseModel):    income: float
class HealthInput(BaseModel):
    income: float
    expenses: float
    savings: float
    debt: float
    insurance: float

class LifeEventInput(BaseModel):
    event: str
    amount: float

class ChatRequest(BaseModel):
    message: str

class CoupleInput(BaseModel):
    income1: float
    income2: float
    expenses: float
    savings: float

class MFInput(BaseModel):
    invested: float
    current: float
    years: float


@app.get("/")
def home():
    return {"message": "AI Money Mentor Running"}

@app.post("/fire")
def fire(data: UserInput):
    savings = data.income - data.expenses
    if savings <= 0:
        return {"years_to_goal": 0, "recommended_sip": 0}

    years = data.goal_amount / (savings * 12)
    sip = data.goal_amount / (years * 12)

    return {
        "years_to_goal": round(years, 1),
        "recommended_sip": round(sip, 0)
    }

@app.post("/tax")
def tax(data: TaxInput):
    income = data.income
    if income < 500000:
        tax = 0
    elif income < 1000000:
        tax = income * 0.1
    else:
        tax = income * 0.2
    return {"tax": int(tax)}

@app.post("/couple")
def couple(data: CoupleInput):
    total_income = data.income1 + data.income2
    savings = total_income - data.expenses

    return {
        "total_income": total_income,
        "monthly_savings": savings
    }

@app.post("/mf")
def mf(data: MFInput):
    xirr = ((data.current / data.invested) ** (1 / data.years)) - 1
    return {"xirr": round(xirr * 100, 2)}

@app.post("/health")
def health(data: HealthInput):
    breakdown = {}

    emergency = min((data.savings / (data.expenses * 6)) * 100, 100)
    insurance = 100 if data.insurance >= data.income * 10 else 50
    debt = 100 if (data.debt / data.income) < 0.3 else 50
    savings_rate = min(((data.income - data.expenses) / data.income) * 100, 100)
    tax = 70
    retirement = 60

    breakdown = {
        "Emergency": int(emergency),
        "Insurance": int(insurance),
        "Debt": int(debt),
        "Savings": int(savings_rate),
        "Tax": tax,
        "Retirement": retirement
    }

    score = int(sum(breakdown.values()) / 6)

    return {
        "score": score,
        "status": "🔥 Excellent" if score > 80 else "👍 Good" if score > 60 else "⚠️ Improve",
        "breakdown": breakdown
    }

@app.post("/life")
def life_event(data: LifeEventInput):
    event = data.event.lower()

    if event == "bonus":
        advice = "Invest 50%, save 30%, spend 20%"
    elif event == "marriage":
        advice = "Increase insurance + build joint savings plan"
    elif event == "baby":
        advice = "Start child fund + increase health cover"
    elif event == "inheritance":
        advice = "Avoid lump sum risk. Use staggered investing"
    else:
        advice = "Plan wisely based on goals"

    return {"advice": advice}

@app.post("/chat")
def chat(req: ChatRequest):
    msg = req.message.lower()

    # Simple rule-based financial advisor
    if "save money" in msg:
        response = "Try the 50-30-20 rule: 50% needs, 30% wants, 20% savings."
    
    elif "invest" in msg:
        response = "Start with SIP in mutual funds and diversify into index funds."
    
    elif "debt" in msg:
        response = "Pay high-interest debt first (credit cards), then lower ones."
    
    elif "budget" in msg:
        response = "Track expenses and set monthly limits for each category."
    
    elif "emergency fund" in msg:
        response = "Keep 6 months of expenses as emergency savings."
    
    else:
        response = "Focus on saving, investing wisely, and avoiding unnecessary debt."

    return {"response": response}