FILE_NAME = "tasks.txt"

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter new task: ")

        with open(FILE_NAME, "a") as file:
            file.write(task + "\n")

        print("Task added successfully!")

    elif choice == "2":
        print("\nYour Tasks:\n")

        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()

            if not tasks:
                print("No tasks available.")
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task.strip()}")

    elif choice == "3":
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("No tasks to delete.")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task.strip()}")

            delete = int(input("Enter task number to delete: "))

            if 1 <= delete <= len(tasks):
                tasks.pop(delete - 1)

                with open(FILE_NAME, "w") as file:
                    file.writelines(tasks)

                print("Task deleted successfully!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
