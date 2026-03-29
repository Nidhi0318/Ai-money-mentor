def calculate_tax(income):
    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = income * 0.05
    elif income <= 1000000:
        tax = income * 0.2
    else:
        tax = income * 0.3

    return {"income": income, "tax": tax}
