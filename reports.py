from collections import defaultdict
from expense_manager import ExpenseManager
from budget_manager import get_budget

class ReportService:
    def monthly_summary(self, month):
        expenses = [e for e in ExpenseManager().list_all() if e.date.startswith(month)]
        by_category = defaultdict(float)
        for e in expenses: by_category[e.category] += e.amount
        total = sum(by_category.values())
        budget = get_budget(month)
        return total, dict(sorted(by_category.items(), key=lambda x: x[1], reverse=True)), budget.amount if budget else None

    def dashboard(self, month):
        total, categories, budget = self.monthly_summary(month)
        remaining = budget - total if budget is not None else None
        return {'month': month, 'total': total, 'categories': categories, 'budget': budget, 'remaining': remaining}
