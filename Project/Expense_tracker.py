# Features:

# Add expense
# Delete expense
# View all expenses
# Calculate total spending
# Save data in .txt or .json file

def add_expense(item_name , price):
    expense.update({item_name:price})
    # expense[item_name] = price  
    print("Item has been added successfully....")


def delete_expense(item_name):
    if expense !='NULL':
        expense.pop(item_name)
        print("Item has been removed.")
    
    else:
        print("Invalid Operation !")


def view_expense():
    if expense !='NULL':
        for item_name , price in expense.items():
          print(f"1. {item_name} : Rs. {price}")

    else:
        print("First buy somethings.....")


def total_expense():
    if expense !='NULL':
        for values in expense.values():
            total_sum +=values
            print(f"Your total expense is Rs. {sum}")

        else:
            print("Total sum is Rs. 0 ")




def main():
    global expense
    expense = {}

    while True:
        print("What u want to do :")
        print("1. Add Expense")
        print("2. Delete Expense")
        print("3. View All Expense")
        print("4. Calculate total expending")
        print("5. Exit")

        choice = input("Enter your choice :")

        match choice:
            case '1' :
                item_name = input('Enter your item name : ')
                price = int(input('Enter your item price : '))
                add_expense(item_name , price)

            case '2' :
                item_name = input('What do you want to delete : ')
                delete_expense(item_name )

            case '3' :
                view_expense()

            case '4' :
                total_expense()
            case '5':
                break
    






if __name__ == "__main__":
    print("Hello! Welcome to our site....🎉")
    main()