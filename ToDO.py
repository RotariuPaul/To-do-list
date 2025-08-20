def add_task(tasks):
    print("How many tasks do you want to add?")
    number_of_tasks = int(input())
    for i in range(number_of_tasks):
        temp=input(f"Enter task {i+1}: ")
        tasks.append(temp)

def remove_task(tasks):
    if not tasks:
        print("No tasks added")
        return
    print("Which task do you want to remove?")
    for i in range(len(tasks)):
        print(f"{i + 1}.", tasks[i])
    remove_task=int(input())-1
    if remove_task<0 or remove_task>=len(tasks):
        print("This task does not exist")
        return
    else:
        tasks.pop(remove_task)
        print("Task removed")

def mark_task(tasks):
    if not tasks:
        print("No tasks added")
        return
    print("What task do you want to mark?")
    for i in range(len(tasks)):
        print(f"{i + 1}.", tasks[i])
    mark=int(input())-1
    if mark>=len(tasks) or mark<0:
        print("This task doesn't exist")
        return
    else:
        tasks[mark]=tasks[mark]+"✓"
def show_tasks(tasks):
    if not tasks:
        print("No tasks added")
    else:
        for i in range(len(tasks)):
            print(f"{i+1}.",tasks[i])



tasks=[]
print("Tasks:\n1.Add task\n2.Remove task\n3.Mark task as done\n4.Show tasks\n5.Exit")

while True:
    choice=int(input("Enter your choice:"))
    if choice==1:
        add_task(tasks)
    elif choice==2:
        remove_task(tasks)
    elif choice==3:
        mark_task(tasks)
    elif choice==4:
        show_tasks(tasks)
    elif choice==5:
        break
    else:
        print("Invalid choice")