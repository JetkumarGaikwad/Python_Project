class Expense:
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount

    def get_date(self):
        return self.date

    def get_description(self):
        return self.description

    def get_amount(self):
        return self.amount

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, date, description, amount):
        new_expense = Expense(date, description, amount)
        self.expenses.append(new_expense)

    def get_total_expenditure(self):
        total = 0
        for expense in self.expenses:
            total += expense.get_amount()
        return total

def main():
    tracker = ExpenseTracker()
    while True:
        print("\n1. Add Expense")
        print("2. Get Total Expenditure")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter date (dd/mm/yyyy): ")
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            tracker.add_expense(date, description, amount)

        elif choice == "2":
            total = tracker.get_total_expenditure()
            print("\nTotal Expenditure: ", total)

        elif choice == "3":
            print("Quitting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()