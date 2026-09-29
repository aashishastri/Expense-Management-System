import csv, json
from config import DATA_DIR, EXPENSE_FILE, BUDGET_FILE
from models import Expense, Budget

HEADERS = ['expense_id', 'date', 'category', 'amount', 'description']

def initialize_storage():
    DATA_DIR.mkdir(exist_ok=True)
    if not EXPENSE_FILE.exists():
        with EXPENSE_FILE.open('w', newline='', encoding='utf-8') as f:
            csv.DictWriter(f, fieldnames=HEADERS).writeheader()
    if not BUDGET_FILE.exists():
        BUDGET_FILE.write_text('{}', encoding='utf-8')

def load_expenses():
    initialize_storage()
    with EXPENSE_FILE.open(newline='', encoding='utf-8') as f:
        return [Expense(int(r['expense_id']), r['date'], r['category'], float(r['amount']), r['description']) for r in csv.DictReader(f)]

def save_expenses(expenses):
    initialize_storage()
    with EXPENSE_FILE.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        writer.writeheader()
        for e in expenses:
            writer.writerow({'expense_id': e.expense_id, 'date': e.date, 'category': e.category, 'amount': f'{e.amount:.2f}', 'description': e.description})

def load_budget():
    initialize_storage()
    data = json.loads(BUDGET_FILE.read_text(encoding='utf-8'))
    return {k: Budget(k, float(v)) for k, v in data.items()}

def save_budget(budgets):
    initialize_storage()
    BUDGET_FILE.write_text(json.dumps({k: v.amount for k, v in budgets.items()}, indent=2), encoding='utf-8')
