
def add_expense(expenses, date, item, amount):
    if date not in expenses:
        expenses[date] = []
    expenses[date].append({'item': item, 'amount': amount})
    print(f"Added expense: {item} of amount {amount} on {date}")

def view_expenses(expenses):
    for date, expense_list in expenses.items():
        print(f"Date: {date}")
        for expense in expense_list:
            print(f"  Item: {expense['item']}, Amount: {expense['amount']}")

def total_expense(expenses):
    total = 0
    for expense_list in expenses.values():
        for expense in expense_list:
            total += expense['amount']
    return total

def expenses_by_date(expenses, date):
    if date in expenses:
        return expenses[date]
    else:
        return []

# Example usage:
expenses = {}
add_expense(expenses, "2024-08-01", "Sandwich", 5.00)
add_expense(expenses, "2024-08-01", "Coffee", 2.50)
add_expense(expenses, "2024-08-02", "Salad", 7.00)

print("\nAll Expenses:")
view_expenses(expenses)

print("\nTotal Expense:")
print(total_expense(expenses))

print("\nExpenses on 2024-08-01:")
print(expenses_by_date(expenses, "2024-08-01"))

