import uuid
from datetime import datetime

class Task:
    def __init__(self,description,status="todo"):
        self.id = str(uuid.uuid4())#generate a unique id for each task
        self.description=description
        self.status=status
        self.createdAt=datetime.now().strftime("%Y-%m-%d %H:%M:%S")#record when the task was created
        self.updateAt=self.createdAt #record when the task was last updated

    def update(self,description=None,status=None):
        if description:
            self.description=description
        if status:
            self.status=status
        self.updateAt=datetime.now().strftime("%Y-%m-%d %H:%M:%S")#update self.update to current date and time

    def __str__(self):
        return f"ID: {self.id}\nDescription: {self.description}\nStatus: {self.status}\nCreated At: {self.createdAt}\nUpdated At: {self.updateAt}\n"#defines how the task is diplayed when you print it
        


tasks=[]#list task
    
def add_task():
    description= input("Enter task description: ")
    task= Task(description)#a new task object is created using the description you just gace.2
    tasks.append(task)#new task is added to list task
    print("task added")

def list_tasks():
    if not tasks:
        print("task not found!!")
    for task in tasks:#prints each task using its __str method
        print(task)


def update_task():
    tid=input("Enter task ID to update:")# the program ask to enter the current task's id of the task you want to change.
    for task in tasks:
        if task.id==tid:
            description=input("New description(leave black to keep):")
            status=input("New stats(todo/in-progress/done): ")
            task.update(description if description else None,status if status else None)
            print("task updated!!")
            return
print("task not found....")

def delete_task():
    tid = input("Enter task ID to delete: ")
    for i,task in enumerate(tasks):
        if task.id==tid:
            del tasks[i]
            print("task deleted!!!!")
            return
        print("task not found!!!")
def main():
    while True:
        print("\nTask Tracker CLI")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()





    

        

