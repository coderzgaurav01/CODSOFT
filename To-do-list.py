tasks = []

def addtask():
    task = input("Enter the task:")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def listTasks():  
    print("Tasks are:")
    for task in tasks:
        print(task)
        
def deletetask():
   task=input("Enter a Task to delete: ")
   if task in tasks:
       tasks.remove(task)
       print(f"Task '{task}' removed from the lists")
   else:
       print(f"Task is not present in the list") 

if __name__=="__main__":
    #create a loop to run the app
    print("welcome to the to-do-list app :)")
    while True:
        print("\n")
        print("Please select the desired options")
        print("---------------------------------")
        print("1. Add Task")
        print("2. List Task")
        print("3. Delete Task ")
        print("4. Quit")
        
        choice=int(input("Enter your choice:"))
        
        if(choice == 1):
           addtask()
            
        elif(choice == 2):
            listTasks()
            
        elif(choice == 3):
            deletetask()
            
        elif(choice == 4):
            break
        else:
            print("Invalid Input")
            
    print("Thank you!")