from dataclasses import dataclass

@dataclass
class Expense:
    expense_id: int
    date: str
    category: str
    amount: float
    description: str

@dataclass
class Budget:
    month: str
    amount: float
