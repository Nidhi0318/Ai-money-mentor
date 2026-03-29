def calculate_fire(data):
    monthly_savings = data.income - data.expenses
    yearly_savings = monthly_savings * 12

    if yearly_savings <= 0:
        return {"error": "No savings. Reduce expenses."}

    years = data.goal_amount / yearly_savings

    return {
        "monthly_savings": monthly_savings,
        "years_to_goal": round(years, 2),
        "recommended_sip": round(monthly_savings * 0.7, 2)
    }
