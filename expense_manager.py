from models import Expense
from storage import load_expenses, save_expenses
from validators import validate_expense

class ExpenseManager:
    def add(self, date, category, amount, description):
        errors = validate_expense(date, category, amount, description)
        if errors: return False, errors
        expenses = load_expenses()
        next_id = max((e.expense_id for e in expenses), default=0) + 1
        expenses.append(Expense(next_id, date, category.title(), float(amount), description.strip()))
        save_expenses(expenses)
        return True, next_id

    def delete(self, expense_id):
        expenses = load_expenses()
        updated = [e for e in expenses if e.expense_id != expense_id]
        if len(updated) == len(expenses): return False
        save_expenses(updated); return True

    def list_all(self):
        return sorted(load_expenses(), key=lambda e: (e.date, e.expense_id), reverse=True)
