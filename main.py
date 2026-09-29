from datetime import date
from expense_manager import ExpenseManager
from budget_manager import set_budget
from reports import ReportService
from utils import money, print_categories, pause
from storage import initialize_storage

expenses = ExpenseManager(); reports = ReportService()

def add_expense():
    d = input(f'Date [{date.today()}]: ').strip() or str(date.today())
    print_categories(); c = input('Category: ').strip()
    a = input('Amount (₹): ').strip(); desc = input('Description: ').strip()
    ok, result = expenses.add(d, c, a, desc)
    print('Expense added successfully. ID:', result if ok else '') if ok else print('Errors:', *result, sep='\n- ')

def view_expenses():
    items = expenses.list_all()
    if not items: print('No expenses recorded.'); return
    print(f'\n{"ID":<5}{"Date":<12}{"Category":<16}{"Amount":>12}  Description')
    print('-'*70)
    for e in items: print(f'{e.expense_id:<5}{e.date:<12}{e.category:<16}{money(e.amount):>12}  {e.description}')

def delete_expense():
    try: i = int(input('Expense ID to delete: ')); print('Deleted.' if expenses.delete(i) else 'ID not found.')
    except ValueError: print('Enter a valid numeric ID.')

def budget_menu():
    month = input('Month (YYYY-MM): ').strip(); amount = input('Monthly budget (₹): ').strip()
    try: set_budget(month, amount); print('Budget saved.')
    except ValueError as e: print('Error:', e)

def report_menu():
    month = input('Month (YYYY-MM): ').strip(); d = reports.dashboard(month)
    print(f'\nREPORT — {month}\nTotal spent: {money(d["total"])}')
    if d['budget'] is not None: print(f'Budget: {money(d["budget"])}\nRemaining: {money(d["remaining"])}')
    print('\nCategory-wise spending:')
    for c, v in d['categories'].items(): print(f'  {c:<16} {money(v)}')

def main():
    initialize_storage()
    while True:
        print('\n=== PERSONAL EXPENSE TRACKER ===\n1. Add expense\n2. View expenses\n3. Delete expense\n4. Set monthly budget\n5. Monthly report\n6. Exit')
        choice = input('Choose an option: ').strip()
        if choice == '1': add_expense()
        elif choice == '2': view_expenses()
        elif choice == '3': delete_expense()
        elif choice == '4': budget_menu()
        elif choice == '5': report_menu()
        elif choice == '6': print('Thank you for using Expense Tracker.'); break
        else: print('Invalid choice. Please select 1-6.')

if __name__ == '__main__': main()
