import os
import time
import messages

def show_menu(task_manager):
    os.system("cls")
    messages.welcome_message()
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
            if(task_count > 1):
                print(messages.SORT_TASKS)
            print(messages.EXIT_PROGRAM)

            choice = input()

            ##Create a task
            if choice == "1":
                print(messages.ENTER_TASK_TITLE_MESSAGE)
                title = input()

                print(messages.ENTER_TASK_DESCRIPTION_MESSAGE)
                description = input()

                task_manager.add_task(title, description)

            ##Edit a task
            elif choice == "2" and task_count > 0:
                print(messages.ENTER_EDIT_TASK_MESSAGE)
                task_index = int(input())
                task_manager.edit_task(task_index)

            ##Mark a task
            elif choice == "3" and task_count > 0:
                print(messages.ENTER_MARK_TASK_MESSAGE)
                task_index = input()
                task_manager.mark_task(task_index)

            ##Delete a task
            elif choice == "4" and task_count > 0:
                print(messages.ENTER_DELETE_TASK_MESSAGE)
                task_index = input()
                task_manager.delete_task(task_index)

            ##Sort tasks
            elif choice == "5" and task_count > 1:
                print(messages.SORT_TASKS_OPTIONS)
                print(messages.ENTER_SORT_TASKS_MESSAGE)
                index = int(input())
                task_manager.sort_tasks(index)
            
            ##Exit program
            elif choice == "0":
                print(messages.EXIT_PROGRAM_MESSAGE)
                time.sleep(0.5)
                os.system("cls")
                exit()

            else:
                print(messages.INVALID_CHOICE_MESSAGE)
            print(messages.PRESS_ENTER_MESSAGE)
            input()

        except ValueError as e:
            print(messages.ERROR_MESSAGE, e)
            print(messages.PRESS_ENTER_MESSAGE)
            input()