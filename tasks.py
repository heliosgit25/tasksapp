print("This is a tasks app on Python.")

#dict concept used here for creating a task object
##task = {
#    "title": "Learn Python",
#    "done": False
#}
# a tasks list can store multiple task objects

tasks = []
title = input("What do you need to do?: ")
comp = int(input("Is it done? Type 0 if not done, or type 1 if done: "))
priority = input("What's the priority of this task? Enter low, med, high: ")

task = {
    "title": title,
    "done": False if comp == 0 else "True",
    "priority": priority
}

tasks.append(task)

for i, task in enumerate(tasks, 1):
    print(f"{i}. [{task['done']}] {task['title']} {task['priority']}")

#print(tasks[0]["done"])
#print(task)
#print(tasks)
#status = "✔" if task["done"] else "✘"