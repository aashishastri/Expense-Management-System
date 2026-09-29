# Personal Expense Tracker (Python, File-Based)

## 1. Overview
A console-based Personal Expense Tracker that helps a student record daily expenses, maintain a monthly budget, delete incorrect entries, and generate category-wise monthly spending reports.

**Important:** This version deliberately uses **NO database and NO external libraries**. Data is stored locally in `data/expenses.csv` and `data/budget.json`.

## 2. Main Features
1. Add an expense with date, category, amount and description.
2. View all saved expenses.
3. Delete an expense by ID.
4. Set/update a monthly budget.
5. Generate a monthly spending report with category totals, budget and remaining amount.
6. Validate dates, categories, descriptions and positive amounts.
7. Persist data between program runs using CSV/JSON files.

## 3. Requirements
- Python 3.10 or newer recommended.
- No MySQL.
- No database server.
- No pip installation is required.

## 4. Folder Structure
```text
Expense_Tracker_NoDB/
├── main.py
├── models.py
├── config.py
├── validators.py
├── storage.py
├── expense_manager.py
├── budget_manager.py
├── reports.py
├── utils.py
├── requirements.txt
├── README.md
├── statement.md
├── data/
│   ├── expenses.csv
│   └── budget.json
├── tests/
│   └── test_project.py
└── docs/
    └── diagrams.md
```

## 5. How to Run — Windows
### Step 1: Install Python
Install Python from the official Python website if it is not already installed. During installation, select **Add Python to PATH**.

### Step 2: Extract the ZIP
Right-click the downloaded project ZIP → **Extract All**.

### Step 3: Open the project folder
Open the extracted `Expense_Tracker_NoDB` folder.

### Step 4: Open Command Prompt / PowerShell
In File Explorer, click the address bar, type `cmd`, and press Enter. Or right-click inside the folder and choose **Open in Terminal**.

### Step 5: Check Python
```bash
python --version
```
If Windows uses `py` instead:
```bash
py --version
```

### Step 6: Run the project
```bash
python main.py
```
Or:
```bash
py main.py
```

### Step 7: Use the menu
```text
=== PERSONAL EXPENSE TRACKER ===
1. Add expense
2. View expenses
3. Delete expense
4. Set monthly budget
5. Monthly report
6. Exit
```
Enter the number of the required operation.

## 6. Example
Choose `1` and enter:
```text
Date: 2026-09-26
Category: Food
Amount: 150
Description: Lunch
```
The application creates a new record in `data/expenses.csv`.

Then choose `5` and enter `2026-09` to see the monthly report.

## 7. Testing
From the project root:
```bash
python -m unittest discover -s tests -v
```

## 8. Resetting the project data
To start with an empty tracker, open `data/expenses.csv` and keep only:
```csv
expense_id,date,category,amount,description
```
For budgets, replace `data/budget.json` with:
```json
{}
```

## 9. GitHub
```bash
git init
git add .
git commit -m "Initial Expense Tracker project"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```
