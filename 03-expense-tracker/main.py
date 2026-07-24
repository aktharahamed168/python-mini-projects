import csv

FILE_NAME = "expenses.csv"

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        category = input("Enter Category: ")
        amount = input("Enter Amount: ")

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([category, amount])

        print("Expense Added Successfully!")

    elif choice == "2":
        print("\n----- Expenses -----")

        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                print(row[0], "₹", row[1])

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
