import os
import time
import messages

class Menu:
    def __init__(self, task_manager):
        self.view = 'list'
        self.task_manager = task_manager
        self.buttons = {}
        self.task_buttons = {}
        self.subtask_buttons = {}
        self.exit_buttons = {}
        self.selected_task = None
        self.exit = False

    def show_menu(self):
        while True:
            try:
                os.system("cls")

                if self.view == 'list':
                    self.list_view()
                elif self.view == 'task':
                    self.task_view()
                print("")
                self.buttons_menu()
                print(messages.TERMINATE_PROGRAM)
                selected_index = input()

                if selected_index.isdigit():
                    if int(selected_index) in self.buttons.keys():
                        choice = self.buttons.get(int(selected_index))
                        if choice == messages.CREATE_TASK or choice == messages.CREATE_SUBTASK:
                            self.task_manager.add_task(get_task=self.selected_task)

                        elif choice == messages.VIEW_TASK:
                            print(messages.ENTER_VIEW_TASK_MESSAGE)
                            task = self.task_manager.get_task(get_task=self.selected_task)
                            if task:
                                self.selected_task = task
                                self.view = 'task'
                                
                        elif choice == messages.EDIT_TASK:
                            self.task_manager.edit_task(get_task=self.selected_task)

                        elif choice == messages.MARK_TASK:
                            self.task_manager.mark_task(get_task=self.selected_task)

                        elif choice == messages.DELETE_TASK:
                            self.task_manager.delete_task(get_task=self.selected_task)
                            if(self.selected_task != None and self.selected_task.parent_id is not None):
                                self.selected_task = self.task_manager.get_task_by_id(self.selected_task.parent_id)
                            else:
                                self.view = 'list'
                                self.selected_task = None

                        elif choice == messages.SORT_TASKS:
                            print(messages.SORT_TASKS_OPTIONS)
                            print(messages.ENTER_SORT_TASKS_MESSAGE)
                            self.task_manager.sort_tasks()

                        elif choice == messages.VIEW_SUBTASK:
                            print(messages.ENTER_VIEW_SUBTASK_MESSAGE)
                            task = self.task_manager.get_task(get_task=self.selected_task)
                            if task:
                                self.selected_task = task
                                self.view = 'task'
                        
                        elif choice == messages.EDIT_SUBTASK:
                            self.task_manager.edit_subtask(get_task=self.selected_task)

                        elif choice == messages.MARK_SUBTASK:
                            self.task_manager.mark_subtask(get_task=self.selected_task)

                        elif choice == messages.DELETE_SUBTASK:
                            self.task_manager.delete_subtask(get_task=self.selected_task)

                        elif choice == messages.SORT_SUBTASKS:
                            print(messages.SORT_TASKS_OPTIONS)
                            print(messages.ENTER_SORT_SUBTASKS_MESSAGE)
                            self.task_manager.sort_subtasks()

                        elif choice == messages.BACK:
                            if self.selected_task.parent_id is not None:
                                self.selected_task = self.task_manager.get_task_by_id(self.selected_task.parent_id)
                            else:
                                self.view = 'list'
                                self.selected_task = None

                        elif choice == messages.EXIT:
                            print(messages.CONFIRM_EXIT_MESSAGE)
                            confirm = input()
                            if confirm.lower() == 'y':
                                self.exit = True
                                break
                            else:
                                pass

                        if choice == messages.VIEW_TASK or choice == messages.VIEW_SUBTASK or choice == messages.BACK:
                            pass
                        else:
                            print(messages.PRESS_ENTER_MESSAGE)
                            input()
                    else:
                        raise ValueError(messages.INVALID_CHOICE_MESSAGE)
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
        task_count = self.task_manager.get_task_count()
        
        i = 1
        if self.view == 'list':
            self.task_buttons = {}
            self.task_buttons[i] = messages.CREATE_TASK
            if task_count > 0:
                i += 1
                self.task_buttons[i] = messages.VIEW_TASK
                i += 1
                self.task_buttons[i] = messages.EDIT_TASK
                i += 1
                self.task_buttons[i] = messages.MARK_TASK
                i += 1
                self.task_buttons[i] = messages.DELETE_TASK
            if task_count > 1:
                i += 1
                self.task_buttons[i] = messages.SORT_TASKS
            self.exit_buttons[0] = messages.EXIT
            
        elif self.view == 'task':
            
            self.task_buttons[i] = messages.EDIT_TASK
            i += 1
            self.task_buttons[i] = messages.MARK_TASK
            i += 1
            self.task_buttons[i] = messages.DELETE_TASK
            i += 1
            
            self.subtask_buttons[i] = messages.CREATE_SUBTASK
            i += 1

            subtask_count = self.task_manager.get_subtask_count(self.selected_task)
            if subtask_count > 0:
                
                self.subtask_buttons[i] = messages.VIEW_SUBTASK
                i += 1
                self.subtask_buttons[i] = messages.EDIT_SUBTASK
                i += 1
                self.subtask_buttons[i] = messages.MARK_SUBTASK
                i += 1
                self.subtask_buttons[i] = messages.DELETE_SUBTASK
                i += 1
                if subtask_count > 1:
                    self.subtask_buttons[i] = messages.SORT_SUBTASKS
                    i += 1

            self.exit_buttons[0] = messages.BACK
        
        for key, value in self.task_buttons.items():
            print(str(key) + ':' + str(value))
        print("")    
        for key, value in self.subtask_buttons.items():
            print(str(key) + ':' + str(value))
        print("")
        for key, value in self.exit_buttons.items():
            print(str(key) + ':' + str(value))
        
        self.buttons.update(self.task_buttons)
        self.buttons.update(self.subtask_buttons)
        self.buttons.update(self.exit_buttons)

        self.task_buttons.clear()
        self.subtask_buttons.clear()
        self.exit_buttons.clear()

        