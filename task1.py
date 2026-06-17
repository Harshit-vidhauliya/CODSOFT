tasks = []

while True:
    print("\n==TO-DO LIST ==")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task Added Successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No Tasks Available!")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No Tasks Available!")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

            num = int(input("Enter task number to update: "))
            new_task = input("Enter new task: ")

            tasks[num - 1] = new_task
            print("Task Updated Successfully!")

    elif choice == "4":
        if len(tasks) == 0:
            print("No Tasks Available!")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

            num = int(input("Enter task number to delete: "))
            deleted = tasks.pop(num - 1)

            print(f"'{deleted}' Deleted Successfully!")

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
