def task_manager():
    tasks = []

    while True:
        print('''
        === TO-DO LIST MENU ===
        1: Add Task
        2: View Tasks
        3: Mark Task as Done
        4: Delete Task
        5: Quit
        ''')

        choice = input("Choose one of the options (1–5): ")

        if choice == '1':
            task_name = input("Enter the name of the task: ")
            tasks.append({"name": task_name, "done": False})
            print(f"✅ Task '{task_name}' added!\n")

        elif choice == '2':
            if not tasks:
                print("🗒️ No tasks to show.\n")
            else:
                print("📋 Your Tasks:")
                for idx, task in enumerate(tasks):
                    status = "✅" if task["done"] else "❌"
                    print(f"{idx}: [{status}] {task['name']}")
                print()

        elif choice == '3':
            if not tasks:
                print("No tasks to mark as done!\n")
            else:
                index = int(input("Enter the index of the task to mark as done: "))
                if 0 <= index < len(tasks):
                    tasks[index]["done"] = True
                    print(f"🎉 Task '{tasks[index]['name']}' marked as done!\n")
                else:
                    print("Invalid index!\n")

        elif choice == '4':
            if not tasks:
                print("No tasks to delete!\n")
            else:
                index = int(input("Enter the index of the task to delete: "))
                if 0 <= index < len(tasks):
                    removed_task = tasks.pop(index)
                    print(f"🗑️ Task '{removed_task['name']}' deleted!\n")
                else:
                    print("Invalid index!\n")

        elif choice == '5':
            print("👋 Exiting the task manager. See you next time!")
            break

        else:
            print("⚠️ Invalid option. Please choose between 1–5.\n")

task_manager()