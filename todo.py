def write_file(tasks):
    with open("tasks.txt", 'w') as f:
        for task in tasks:
            f.write(task + "\n")
            
def read_file():
    tasks = []
    with open("tasks.txt", "r") as f:
        tasks = f.readlines()
    for i in range(len(tasks)):
        tasks[i] = tasks[i].strip()
        
if __name__ == "__main__":
    tasks = read_file()
    print("Welcome to the ToDo list app.")
    while(True):
        print("Here are your ToDo list items:\n")
        for i, task in enumerate(tasks):
            print(f"  {i+1}. {task}")
        choice = input("\nSelect one of the options below:\n  (a) Add new task\n  (m) Mark task as completed \n  (d) Delete task from list \n  (q) Quit \n\nYour selection: ")
        task_choice = -1
        match choice.lower():
            case "a":
                task = input("Task name: ")
                tasks.append("[ ] " + task)
                write_file(tasks)
                print("Task successfully added")
            case "m":
                while(task_choice < 1 or task_choice > len(tasks)):
                    try:
                        task_choice = int(input("Which task number to mark completed: "))
                    except:
                        print(f"ERROR: Input must be an integer in the range {1}-{len(tasks)}")
                tasks[task_choice-1] = "[x] " + tasks[task_choice-1][4:]
                write_file(tasks)
                print("Task successfully updated")
            case "d":
                while(task_choice < 1 or task_choice > len(tasks)):
                    try:
                        task_choice = int(input("Which task number to delete: "))
                    except:
                        print(f"ERROR: Input must be an integer in the range {1}-{len(tasks)}")
                tasks.pop(task_choice-1)
                write_file(tasks)
                print("Task successfully deleted")
            case "q":
                break
            case _:
                print("Please enter one of the following as input: [a,m,d,q]")