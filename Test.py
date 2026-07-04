expenses = {}


def add_expense(item_name, price):
    expenses[item_name] = price
    print("Item has been added successfully....")


def delete_expense(item_name):

    if item_name in expenses:
        expenses.pop(item_name)
        print("Item has been removed.")

    else:
        print("Item not found!")


def view_expense():

    if expenses:

        for item_name, price in expenses.items():
            print(f"{item_name} : Rs. {price}")

    else:
        print("First buy something.....")


def total_expense():

    if expenses:

        total = 0

        for value in expenses.values():
            total += value

        print(f"Your total expense is Rs. {total}")

    else:
        print("Total sum is Rs. 0")


def main():

    while True:

        print("\nWhat you want to do:")
        print("1. Add Expense")
        print("2. Delete Expense")
        print("3. View All Expense")
        print("4. Calculate total spending")
        print("5. Exit")


        choice = input("Enter your choice: ")


        match choice:

            case '1':

                item_name = input("Enter item name: ")
                price = int(input("Enter price: "))

                add_expense(item_name, price)


            case '2':

                item_name = input("What do you want to delete: ")

                delete_expense(item_name)


            case '3':

                view_expense()


            case '4':

                total_expense()


            case '5':

                print("Thank you!")
                break


            case _:

                print("Invalid choice")


if __name__ == "__main__":

    print("Hello! Welcome to our site....🎉")

    main()