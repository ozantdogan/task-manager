from task_manager import TaskManager
from menu import show_menu
import os
import time
import messages

def main():
    try:
        task_manager = TaskManager()
        show_menu(task_manager)
    except KeyboardInterrupt:
        print(messages.QUIT_MESSAGE)
        time.sleep(0.5)
        os.system("cls")
        exit()
        
if __name__ == "__main__":
    main()