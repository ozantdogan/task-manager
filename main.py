from task_manager import TaskManager
from db_settings import *
from menu import show_menu
import os
import time
import messages

def main():
    os.system("cls")
    messages.welcome_message()
    time.sleep(1.5)
    
    while True:
        try:
            if check_db_initials() == False:
                set_db()
            session = connect_db()
            task_manager = TaskManager(session)
            menu = show_menu(task_manager)
            if(menu == 0):
                if session:
                    session.close()
                del menu
                del task_manager
                
                set_db()

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