from app_settings import clear_console
from task_handler import TaskHandler
from db_settings import *
from menu import Menu
import os
import time
import messages

def main():
    clear_console()
    messages.welcome_message()
    time.sleep(1.5)

    while True:
        try:
            session = connect_db()
            task_handler = TaskHandler(session)
            menu = Menu(task_handler)
            menu.show_menu()
            if menu.exit:
                print(messages.EXIT_PROGRAM_MESSAGE)
                time.sleep(0.5)
                clear_console()
                exit()

        except KeyboardInterrupt:
            print(messages.TERMINATING_PROGRAM_MESSAGE)
            time.sleep(0.5)
            clear_console()
            exit()

        except Exception as e:
            clear_console()
            continue


if __name__ == "__main__":
    main()
