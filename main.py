from task_manager import TaskManager
import os
import time
import messages

def main():
    os.system("cls")
    print(messages.WELCOME_MESSAGE)
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
                title = input(messages.ENTER_TASK_TITLE_MESSAGE)
                description = input(messages.ENTER_TASK_DESCRIPTION_MESSAGE)
                task_manager.add_task(title, description)
            elif choice == "2" and task_count > 0:
                task_index = int(input(messages.ENTER_MARK_TASK_MESSAGE))
                task_manager.mark_task(task_index)
            elif choice == "3" and task_count > 0:
                task_index = int(input(messages.ENTER_DELETE_TASK_MESSAGE))
                task_manager.delete_task(task_index)
            elif choice == "4":
                print(messages.QUIT_MESSAGE)
                break
            else:
                raise Exception(messages.INVALID_CHOICE_MESSAGE)
        except Exception as e:
            print(messages.ERROR_MESSAGE, e)
        
        input(messages.PRESS_ENTER_MESSAGE)

if __name__ == "__main__":
    main()