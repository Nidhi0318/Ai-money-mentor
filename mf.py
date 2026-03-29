from pyxirr import xirr

def calculate_xirr():
    cashflows = {
        "2022-01-01": -10000,
        "2023-01-01": -10000,
        "2024-01-01": 25000
    }
    return {"xirr": xirr(cashflows)}
