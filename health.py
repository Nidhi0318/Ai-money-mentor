def calculate_health(data):
    score = 0

    if data.savings >= 6 * data.expenses:
        score += 20
    if data.income > data.expenses:
        score += 20
    if data.goal_amount > 0:
        score += 20
    if data.income > 50000:
        score += 20

    return {
        "score": score,
        "status": "Excellent" if score > 70 else "Average" if score > 40 else "Poor"
    }
