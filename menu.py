import os
import time
import messages


class Menu:
    def __init__(self, task_manager):
        self.current_view = 'list'
        self.task_manager = task_manager
        self.buttons = {}
        self.task_count = task_manager.get_task_count()
        self.selected_task = None
        self.disconnect = False

    def show_menu(self):
        while True:
            try:
                os.system("cls")
                print(messages.TASK_MANAGER_TITLE.format(DB_NAME=self.task_manager.get_db_name()) + '\n')

                if self.current_view == 'list':
                    self.list_view()
                elif self.current_view == 'task':
                    self.task_view()
                print(messages.SEPARATOR_LINE)
                self.buttons_menu()
                print(messages.EXIT_PROGRAM)
                selected_index = input()

                if selected_index.isdigit and int(selected_index) in self.buttons.keys():
                    choice = self.buttons.get(int(selected_index))
                    if choice == messages.CREATE_TASK:
                        self.task_manager.add_task()

                    elif choice == messages.VIEW_TASK:
                        print(messages.ENTER_VIEW_TASK_MESSAGE)
                        task = self.task_manager.get_task()
                        if task:
                            self.selected_task = task
                            self.current_view = 'task'
                            
                    elif choice == messages.EDIT_TASK:
                        print(messages.ENTER_EDIT_TASK_MESSAGE)
                        self.task_manager.edit_task()

                    elif choice == messages.MARK_TASK:
                        print(messages.ENTER_MARK_TASK_MESSAGE)
                        self.task_manager.mark_task()

                    elif choice == messages.DELETE_TASK:
                        print(messages.ENTER_DELETE_TASK_MESSAGE)
                        self.task_manager.delete_task()

                    elif choice == messages.SORT_TASKS:
                        print(messages.SORT_TASKS_OPTIONS)
                        print(messages.ENTER_SORT_TASKS_MESSAGE)
                        self.task_manager.sort_tasks()

                    elif choice == messages.BACK:
                        self.current_view = 'list'
                        self.selected_task = None

                    elif choice == messages.DISCONNECT_PROGRAM:
                        print(messages.DISCONNECT_MESSAGE)
                        time.sleep(0.5)
                        os.system("cls")
                        self.disconnect = True
                        return 0
                    
                    if choice == messages.VIEW_TASK or choice == messages.BACK:
                        pass
                    else:
                        print(messages.PRESS_ENTER_MESSAGE)
                        input()
                else:
                    raise ValueError(messages.INVALID_CHOICE_MESSAGE)
                
            except ValueError as e:
                print(messages.ERROR_MESSAGE, e)
                print(messages.PRESS_ENTER_MESSAGE)
                input()

    def list_view(self):
        self.task_manager.list_tasks()
        
    def task_view(self):
        self.task_manager.view_task(self.selected_task)
        
    def buttons_menu(self):
        self.buttons.clear()
        i = 1
        if self.current_view == 'list':
            self.buttons = {}
            self.buttons[i] = messages.CREATE_TASK
            if self.task_count > 0:
                i += 1
                self.buttons[i] = messages.VIEW_TASK
                i += 1
                self.buttons[i] = messages.EDIT_TASK
                i += 1
                self.buttons[i] = messages.MARK_TASK
                i += 1
                self.buttons[i] = messages.DELETE_TASK
            if self.task_count > 1:
                i += 1
                self.buttons[i] = messages.SORT_TASKS
            
        elif self.current_view == 'task':
            self.buttons[i] = messages.BACK

        self.buttons[0] = messages.DISCONNECT_PROGRAM
        for key, value in self.buttons.items():
            print(str(key) + ':' + str(value))
        
        