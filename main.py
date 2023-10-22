from task_manager import TaskManager
from db_settings import set_db, connect_db
from menu import show_menu
import os
import time
import messages

def main():
    os.system("cls")
    messages.welcome_message()
    time.sleep(1.5)
    
    while True:
        session = connect_db()
        try:
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
            continue
        
if __name__ == "__main__":
    main()