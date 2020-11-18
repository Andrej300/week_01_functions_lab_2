tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]
#1. Print a list of uncompleted tasks
for task in tasks:
    if task["completed"] == False:
        print(task)

#2. Print a list of completed tasks

for task in tasks:
    if task["completed"] == True:
        print(task)


#3. Print a list of all task descriptions
list_of_tasks = []
for task in tasks:
    list_of_tasks.append(task["description"])
    
print(list_of_tasks)


#4. Print a list of tasks where time_taken is at least a given time
time_taken_list = []
def time_taken(given_time):
    for task in tasks:
        if task["time_taken"] >= given_time:
            time_taken_list.append(task)
    print(time_taken_list)
time_taken(30)


#5. Print any task with a given description
# def task_1(task_name):
#     if task_name == "Wash Dishes":
#         print(tasks[0])
#     elif task_name == "Clean Windows":
#         print(tasks[1])
#     elif task_name == "Make Dinner":
#         print(tasks[2])
#     elif task_name == "Feed Cat":
#         print(tasks[3])
#     elif task_name == "Walk Dog":
#         print(tasks[4])
        
# task_1("Walk Dog")
def find_task_by_description( given_description):
    for task in tasks:
        if task["description"] == given_description:
            print(task)

find_task_by_description("Walk Dog")

# 6. Given a description update that task to mark it as complete.
def update_task(given_description):
    for task in tasks:
        if task["description"] == given_description:
            task["completed"] = True

update_task("Wash Dishes")
print(tasks[0])

# 7. Add a task to the list
new_task = {"description": "Go To Bed", "completed": False, "time_taken": 400}
tasks.append(new_task)
print(tasks)