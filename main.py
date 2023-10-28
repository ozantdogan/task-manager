from task_manager import TaskManager
from db_settings import *
from menu import Menu
import os
import time
import messages

def main():
    os.system("cls")
    messages.welcome_message()
    time.sleep(1.5)
    
    while True:
        try:
            session = connect_db()
            task_manager = TaskManager(session)
            menu = Menu(task_manager)
            menu.show_menu()
            if menu.exit:
                print(messages.EXIT_PROGRAM_MESSAGE)
                time.sleep(0.5)
                os.system("cls")
                exit()

        except KeyboardInterrupt:
            print(messages.TERMINATING_PROGRAM_MESSAGE)
            time.sleep(0.5)
            os.system("cls")
            exit()

        except Exception as e:
            os.system("cls")
            continue
        
if __name__ == "__main__":
    main()