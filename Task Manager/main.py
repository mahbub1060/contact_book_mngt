from task_manager import add_task, view_task, remove_task, search_task

while True:
    print("\n\nWelcome to Task Manager: ")
    print("-" * 25)
    print("1. Add Task")
    print("2. View Task")
    print("3. Remove Task")
    print("4. Search Task")
    print("5. Update Task")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice=="1":
        title = input("Enter your task title: ")
        description = input("Enter your task description: ")
        due_date = input("Enter your task due date:(YYYY-MM-DD): ")
    
        add_task(title, description, due_date)
        print("Task Added Successfully")
    
    elif choice == "2":
        view_task()    
    
    elif choice =="3":
        index = int(input("Enter the index of the task to remove: "))
        remove_task(index)
        print("Task removed successfully")
        
    elif choice == "4":
        query = input("Enter the search query: ")
        print("\n\nSearch Result")
        search_task(query)
    
    
    