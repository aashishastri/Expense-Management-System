from config import CATEGORIES

def print_categories():
    print('Categories:', ', '.join(CATEGORIES))

def money(value):
    return f'₹{value:,.2f}'

def pause():
    input('\nPress Enter to continue...')
