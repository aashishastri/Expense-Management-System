from datetime import datetime
from config import DATE_FORMAT, CATEGORIES

def valid_amount(value):
    try:
        return float(value) > 0
    except (ValueError, TypeError):
        return False

def valid_date(value):
    try:
        datetime.strptime(value, DATE_FORMAT)
        return True
    except ValueError:
        return False

def valid_category(value):
    return value.title() in CATEGORIES

def validate_expense(date, category, amount, description=''):
    errors = []
    if not valid_date(date): errors.append('Date must be in YYYY-MM-DD format.')
    if not valid_category(category): errors.append('Choose a category from the available list.')
    if not valid_amount(amount): errors.append('Amount must be a positive number.')
    if not description.strip(): errors.append('Description cannot be empty.')
    return errors
