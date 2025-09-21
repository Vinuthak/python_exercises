tasks = []
print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")
print("")
while True:
    print("")
    print("")
    print("-- ToDo List --")
    print("1.View tasks")
    print("2.Add task")
    print("3.Update task")
    print("4.Remove task")
    print("5.Exit")
    print("")
    print("")
    choice = input("Choose an option (1-5): ")

    if choice == "1": #view
        if not tasks:
            print("")
            print("")
            print("No tasks yet!")
            print("")
            print("")
            print("Please create a task to view")
            task = input("Enter a new task: ")
            tasks.append(task)
            print(f"Added task: -----> {task}")
        else:
            for i , task in enumerate(tasks,start=1):
                print(f"{i}.{task}")
        print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")
    elif choice == "2": #Add
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f"Added task: -----> {task}")
        print("")
        print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")
    elif choice == "3": #update
        if not tasks:
            print("")
            print("The list is empty. Please add a task before updating.")
            print("")
            task = input("Enter a new task: ")
            tasks.append(task)
            print(f"Added task: -----> {task}")
            print("")
            print("")

        else:
            for i , task in enumerate(tasks,start=1):
                print(f"{i}.{task}")
            task_num = int(input("Enter a task number to update: "))
            
            if 1 <= task_num <= len(tasks):
                new_task = input("Enter the new task description: ")
                old_task = tasks[task_num-1]
                tasks[task_num-1] = new_task
                print(f"updated the task from: {old_task} ------> {new_task}")
            else:
                print("")
                print("Invalid task number.Please check the list above.")

            print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")
    elif choice == "4": #remove
        for i,task in enumerate(tasks,start=1):
            print(f"{i}.{task}")
            print("")
        task_num = int(input("Enter a task number to remove: "))
        if not tasks:
            print("")
            print("The list is empty. There are no tasks to remove")
        elif 1<= task_num <= len(tasks):
            removed = tasks.pop(task_num -1)
            print(f"Removed the task:----> {removed}")
            if len(tasks) == 0:
                print("No more tasks to remove")
        else:
            print("Invalid Number")
        print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")
    elif choice == "5":#Exit
        print("Goodbye")
        break