def write_file(tasks):
    with open("tasks.txt", 'w') as f:
        for task in tasks:
            f.write(task + "\n")
            
def read_file():
    tasks = []
    with open("tasks.txt", "r") as f:
        tasks = f.readlines()
    return tasks