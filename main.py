from task_manager import TaskManager
import os
import time

def main():
    os.system("cls")
    print("""TASK MANAGER
    Author: Ozan Doğan
    """)
    time.sleep(1.5)

    task_manager = TaskManager()
    while True:
        try:
            os.system("cls")
            task_count = len(task_manager.tasks)
            task_manager.list_tasks()
            print("_____________________")

            print("1. Add Task")
            if(task_count > 0):
                print("2. Mark Task")
                print("3. Delete Task")
            print("4. Quit")

            choice = input()

            if choice == "1":
                title = input("Enter task title: ")
                description = input("Enter task description: ")
                task_manager.add_task(title, description)
            elif choice == "2" and task_count > 0:
                task_index = int(input("Enter the task number to remark: "))
                task_manager.mark_task(task_index)
            elif choice == "3" and task_count > 0:
                task_index = int(input("Enter the task number to delete: "))
                task_manager.delete_task(task_index)
            elif choice == "4":
                print("Exiting the program...")
                break
            else:
                raise Exception("Invalid choice. Please select a valid option.")
        except Exception as e:
            print(f"⚠️  An error occurred: {e}")
        
        input("(Press Enter to continue...)")

if __name__ == "__main__":
    main()