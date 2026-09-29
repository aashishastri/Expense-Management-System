from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / 'data'
EXPENSE_FILE = DATA_DIR / 'expenses.csv'
BUDGET_FILE = DATA_DIR / 'budget.json'
CATEGORIES = ['Food', 'Travel', 'Education', 'Shopping', 'Entertainment', 'Bills', 'Health', 'Other']
DATE_FORMAT = '%Y-%m-%d'
