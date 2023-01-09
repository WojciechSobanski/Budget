expenses = []
type_of_expense = []

# Function showing all monthly expenses.
def show_expenses(month):
    for expense_amount, expense_type, expense_month in expenses:
        if expense_month == month:
            print(f'{expense_amount} - {expense_type}')

# Function to add new expense.
def add_expense(month):
    print()
    expense_amount = int(input('Enter the amount [PLN]: '))
    expense_type = input(f'Enter the type of expense {type_of_expense}')

    expense = (expense_amount, expense_type, month)
    expenses.append(expense)

# Function show a statsistic.
def show_stats(month):
    total_amount_this_month = sum(expense_amount for expense_amount, _, expense_month in expenses if expense_month == month) # Total amount this month 
    number_of_expenses_this_month = sum(1 for _, _, expense_month in expenses if expense_month == month) # Numbers of expenses this month
    average_expense_this_month = total_amount_this_month / number_of_expenses_this_month # Average expense this month

    total_amount_all = sum(expense_amount for expense_amount, _, _ in expenses) # Total amount all
    average_expense_all = total_amount_all / len(expenses) # Average expanse all

    print()
    print('Statistics')
    print('Total amount this montht [PLN]:', total_amount_this_month)
    print('Average expense this month [PLN]:', average_expense_this_month)
    print('Total amount all [PLN]:', total_amount_all)
    print('Average expanse all [PLN]:', average_expense_all)

# Function to add new expense type.
def new_expense_type():
    print()
    new_expense_type = input('Enter the new expense type: ')
    type_of_expense.append(new_expense_type)

    
while True:
    print()
    print('0, End aplication')
    print('1, Select month')
    print('2, Application settings')
    choice_1 = int(input('Select option: '))

    if choice_1 == 0:
        break

    if choice_1 > 2:
        print('Number is to high')

    if choice_1 == 1:
        month = int(input('Select month [1-12]: '))
        if month == 0 or month > 12:
            break
        while True:
            print()
            print('0, Back')
            print('1, Viev all expenses')
            print('2, Add new expenses')
            print('3, Statistics')
            choice_2 = int(input('Select option: '))

            if choice_2 == 0:
                break

            if choice_2 > 3:
                print('Number is to high')

            if choice_2 == 1:
                show_expenses(month)
    
            if choice_2== 2:
                add_expense(month)
        
            if choice_2 == 3:
                show_stats(month)

    if choice_1 == 2:
        while True:
            print()
            print('0, Back')
            print('1, Type of Expense')
            print('2, Other')
            choice_3 = int(input('Select option: '))

            if choice_3 == 0:
                break

            if choice_3 > 2:
                print('Number is to high')

            if choice_3 == 1:
                while True:
                    print()
                    print('0, Back')
                    print('1, Add a new type of expense')
                    print('2, Show list types of expense')
                    choice_4 = int(input('Select option: '))

                    if choice_4 == 0:
                        break

                    if choice_4 > 2:
                        print('Number is to high')
                
                    if choice_4 == 1:
                        new_expense_type()
                
                    if choice_4 == 2:
                        print()
                        print(type_of_expense)
                    
            if choice_3 == 2:
                print('2, Other')

    
