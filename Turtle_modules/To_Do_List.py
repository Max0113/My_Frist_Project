def add_task() :
    enter = input("enter your task : ")
    status = {"task":enter , "completed":False}
    tasks.append(status)
    print("add task he is succes")

def mark_task() :
    #get list to task incompeted 
    incompleted_task = []
    for task in tasks :
        if task["completed"] == False :
            incompleted_task.append(task)
    # view task
    for i , task in enumerate(incompleted_task) :
        n = i + 1
        print(f"{n} - {task['task']}")
    print("-"*30)
    #choice 
    completed_task = []
    choice_nomber = input("choice in task for completed")
    for i , task in enumerate(incompleted_task) :
        n = i + 1
        if n == f"{choice_nomber}" :
            task["completed"] = True
   

            

def view_task() :
    pass

message = """
   1-add task
   2-mark task he is complete
   3-view tasks
   4-quit """

tasks = []


while True :
    print (message)
    choice = input("Enter your choice :")

    if choice =="1" :
        add_task()
    elif choice =="2" :
        mark_task()
    elif choice =="3" :
        view_task()
    elif choice =="4" : 
        quit()
    else :
        print("your choice is false enter number enter 1 and 4")


