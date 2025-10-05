# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import ast
import os.path

os.makedirs("expense_dir", exist_ok=True)
expense_details = list()


def main():
    option = input("Select option 1 to Add 2 to view, 3 to track , 4 to save and 5 to save and Exit :")

    try:
        load_expenses()

        while option != "5":
            if option == "1":
                add_expense()
            elif option == "2":
                view_expense()
            elif option == "3":
                budget_tracker()
            elif option == "4":
                save_expenses()

            print("Select option 1 to Add 2 to view, 3 to track , 4 to save and 5 to save and Exit :")
            option = input("Select Option to continue :")

        if option == "5":
            save_expenses()

    except Exception as e:
        print("Exception Occurred : ", e)


def add_expense():
    date_expense = input("Date Of Expense in YYYY-MM-DD format : ")
    category_of_expense = input("The category of the expense, such as Food or Travel : ")
    amount_spent = input("The amount spent ,Enter In Numeric Format Only: ")
    brief_description = input("A brief description of the expense : ")

    expense_dict = dict()
    expense_dict["date"] = date_expense
    expense_dict["category"] = category_of_expense
    expense_dict["amount"] = amount_spent
    expense_dict["description"] = brief_description
    expense_details.append(expense_dict)
    if not expense_dict["amount"].isnumeric():
        raise Exception("Please Enter Amount in Numeric Format Only For Budget Tracking Purpose")


def view_expense():
    for i in range(len(expense_details)):
        try:
            validate_expense(ast.literal_eval(str(expense_details[i])))

            print("\n")
            print("printing the expense details for expense :", str(i + 1))
            print("Date Of Expense is ", expense_details[i]['date'])
            print("The category of the expense, such as Food or Travel : ", expense_details[i]['category'])
            print("The amount spent : ", expense_details[i]['amount'])
            print("A brief description of the expense : ", expense_details[i]['description'])
        except Exception as e:
            print("Given Information is Not Correct for Expense ", i + 1, " ", e)


def validate_expense(expense_dict: dict):
    if len(expense_dict.get('date')) is None or len(expense_dict.get('date')) < 1:
        raise Exception("Date cant be Empty in Expense Details")
    if expense_dict.get('category') is None or len(expense_dict.get('category')) < 1:
        raise Exception("Category cant be Empty in Expense Details")
    if expense_dict.get('amount') is None or len(expense_dict.get('amount')) < 1:
        raise Exception("Amount cant be Empty in Expense Details")
    if expense_dict.get('description') is None or len(expense_dict.get('description')) < 1:
        raise Exception("Description cant be Empty in Expense Details")


def budget_tracker():
    monthly_budget = int(input("Monthly Budget Value : "))
    total_amount = 0
    for i in range(len(expense_details)):
        if str(expense_details[i]["amount"]).isnumeric():
            total_amount += int(expense_details[i]["amount"])
        else:
            print("Non Numeric Data is not expected under Amount Field ", expense_details[i]["amount"])

    if total_amount > monthly_budget:
        print("You have exceeded your budget!")
    else:
        print("You have ", monthly_budget - total_amount, " left for the month")


def save_expenses():
    with open(os.path.join("expense_dir", "expenses.txt"), 'w') as file:
        for i in range(len(expense_details)):
            file.write(str(expense_details[i]) + "\n")


def load_expenses():
    try:
        with open(os.path.join("expense_dir", "expenses.txt"), 'r') as file:
            for line in file:
                expense_details.append(ast.literal_eval(line.strip()))
    except FileNotFoundError:
        with open(os.path.join("expense_dir", "expenses.txt"), 'w'):
            pass


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
