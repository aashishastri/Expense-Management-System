from models import Budget
from storage import load_budget, save_budget

def set_budget(month, amount):
    if len(month) != 7 or month[4] != '-' or not month[:4].isdigit() or not month[5:].isdigit():
        raise ValueError('Month must be YYYY-MM.')
    amount = float(amount)
    if amount <= 0: raise ValueError('Budget must be positive.')
    budgets = load_budget(); budgets[month] = Budget(month, amount); save_budget(budgets)

def get_budget(month):
    return load_budget().get(month)
