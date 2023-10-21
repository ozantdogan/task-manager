import os
import time
import messages

def show_menu(task_manager):
    os.system("cls")
    for line in messages.WELCOME_MESSAGE.splitlines():
        print(line)
        time.sleep(0.1)
    ##print(messages.WELCOME_MESSAGE)
    time.sleep(1.5)

    while True:
        try:
            os.system("cls")
            task_count = task_manager.get_task_count()
            task_manager.list_tasks()
            print("_____________________")

            print(messages.CREATE_TASK)
            if(task_count > 0):
                print(messages.EDIT_TASK)
                print(messages.MARK_TASK)
                print(messages.DELETE_TASK)
                print(messages.CHANGE_TASK)
            print(messages.QUIT_PROGRAM)

            choice = input()

            if choice == "1":
                title = input(messages.ENTER_TASK_TITLE_MESSAGE)
                description = input(messages.ENTER_TASK_DESCRIPTION_MESSAGE)
                task_manager.add_task(title, description)
            elif choice == "2" and task_count > 0:
                task_index = int(input(messages.ENTER_EDIT_TASK_MESSAGE))
                task_manager.edit_task(task_index)
            elif choice == "3" and task_count > 0:
                task_index = input(messages.ENTER_MARK_TASK_MESSAGE)
                task_manager.mark_task(task_index)
            elif choice == "4" and task_count > 0:
                task_index = input(messages.ENTER_DELETE_TASK_MESSAGE)
                task_manager.delete_task(task_index)
            elif choice == "5" and task_count > 1:
                print(messages.SORT_TASKS)
                index = int(input(messages.ENTER_SORT_TASKS_MESSAGE))
                task_manager.sort_tasks(index)
            elif choice == "0":
                print(messages.QUIT_MESSAGE)
                time.sleep(0.5)
                os.system("cls")
                exit()
            else:
                print(messages.INVALID_CHOICE_MESSAGE)
            input("Press Enter to continue...")
        except ValueError as e:
            print(messages.ERROR_MESSAGE, e)
            input("Press Enter to continue...")