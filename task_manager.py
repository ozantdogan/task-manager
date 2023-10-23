from sqlalchemy import asc, desc, func
from models import Task
from app_settings import *
import messages

class TaskManager:
    def __init__(self, session):
        self.task_db_ids = {}
        self.sortby = Task.createdon
        self.sort_order = asc
        self.session = session

    def get_task(self, task_index):
        if not task_index.isdigit():
            raise ValueError(messages.INVALID_CHOICE_MESSAGE)

        task_id = self.task_db_ids.get(task_index)
        if task_id:
            return True
        else:
            raise ValueError(messages.TASK_NOT_FOUND_ERROR)
        
    def get_task_count(self):
        return self.session.query(Task).count()
    
    def get_db_name(self):
        return self.session.bind.url.database
    
    def list_tasks(self):
        tasks = self.session.query(Task).order_by(self.sort_order(self.sortby)).all()
        if not tasks:
            print(messages.NO_TASKS_FOUND_MESSAGE)
        else:
            self.task_db_ids = {index: task.id for index, task in enumerate(tasks, start=1)}
            for index, task in enumerate(tasks, start=1):
                status = COMPLETED if task.is_completed else NOT_COMPLETED
                # description = f": {task.description}" if task.description.strip() else ""
                # print(f"{index}{status}  {task.title}{description}")
                description = f" [...]" if task.description.strip() else ""
                print(f"{index}{status}  {task.title}{description}")
    
    def add_task(self, title, description):
        if not title:
            raise ValueError(messages.TASK_TITLE_ERROR)
        task = Task(title=title, description=description)
        self.session.add(task)
        self.session.commit()
        print(messages.TASK_ADDED_MESSAGE.format(title=title))

    def view_task(self, task_index):
        task_id = self.task_db_ids.get(task_index)
        task = self.session.query(Task).filter_by(id=task_id).first()
        print(f"{task.title}")
        print(messages.SEPARATOR_LINE)
        if task.description == "":
            print(messages.NO_DESCRIPTION_MESSAGE)
        else:
            print(f"{task.description}") 

    def edit_task(self, task_index):
        try:
            task_id = self.task_db_ids.get(task_index)
            if task_id:
                task = self.session.query(Task).filter_by(id=task_id).first()

                print(messages.ENTER_NEW_TASK_TITLE_MESSAGE)
                title = input()
                if(title == ""):
                    title = task.title

                print(messages.ENTER_NEW_TASK_DESCRIPTION_MESSAGE)
                description = input()
                if(description == ""):
                    description = task.description
                elif(description == CLEAR):
                    description = ""

                task.title = title
                task.description = description
                task.modifiedon = func.now()

                self.session.commit()
                self.task_db_ids[task_index] = task_id
                print(messages.TASK_EDITED_MESSAGE.format(title=title))
            else:
                raise ValueError(messages.TASK_NOT_FOUND_ERROR)
        except ValueError as e:
            print(messages.ERROR_MESSAGE, e)
    
    def sort_tasks(self, index):
        try:
            current_sortby = self.sortby
            if index == 1:
                self.sortby = Task.title
            elif index == 2:
                self.sortby = Task.createdon
            elif index == 3:
                self.sortby = Task.modifiedon
            elif index == 4:
                self.sortby = Task.is_completed
            else:
                raise ValueError(messages.INVALID_CHOICE_MESSAGE)
            if current_sortby == self.sortby:
                self.sort_order = desc if self.sort_order == asc else asc
            
        except ValueError as e:
            print(messages.ERROR_MESSAGE, e)

    def mark_task(self, task_index):
        try:
            if task_index.isdigit():
                task_index = int(task_index)
                if task_index == 0:
                    raise ValueError(messages.INVALID_CHOICE_MESSAGE)
                task_id = self.task_db_ids.get(task_index)
                if task_id:
                    task = self.session.query(Task).filter_by(id=task_id).first()
                    task.is_completed = not task.is_completed
                    task.modifiedon = func.now()
                    self.session.commit()
                    print(messages.TASK_MARKED_MESSAGE.format(title=task.title, is_completed='completed' if task.is_completed else 'not completed'))
                else:
                    raise ValueError(messages.TASK_NOT_FOUND_ERROR)
            elif task_index == "-a":
                uncompleted_tasks = self.session.query(Task).filter_by(is_completed=False).all()
                if uncompleted_tasks:
                    for task in uncompleted_tasks:
                        task.is_completed = True
                        task.modifiedon = func.now()
                    self.session.commit()
                    print(messages.ALL_TASKS_MARKED_COMPLETED_MESSAGE)
                else:
                    completed_tasks = self.session.query(Task).filter_by(is_completed=True).all()
                    for task in completed_tasks:
                        task.is_completed = False
                        task.modifiedon = func.now()
                    self.session.commit()
                    print(messages.ALL_TASKS_MARKED_NOT_COMPLETED_MESSAGE)
            else:
                raise ValueError(messages.INVALID_CHOICE_MESSAGE)
        except ValueError as e:
            print(messages.ERROR_MESSAGE, e)

    def delete_task(self, task_index):
        try:
            if task_index == "-a":
                print(messages.CONFIRM_DELETE_ALL_TASKS_MESSAGE)
                confirm = input()
                if confirm.lower() == "y":
                    self.session.query(Task).delete()
                    self.session.commit()
                    self.task_db_ids.clear()
                    print(messages.ALL_TASKS_DELETED_MESSAGE)
            elif task_index.isdigit():
                task_index = int(task_index)
                if task_index == 0:
                    raise ValueError(messages.INVALID_CHOICE_MESSAGE)
                task_id = self.task_db_ids.get(task_index)
                if task_id:
                    task = self.session.query(Task).filter_by(id=task_id).first()
                    self.session.delete(task)
                    self.session.commit()
                    del self.task_db_ids[task_index]
                    print(messages.TASK_DELETED_MESSAGE.format(deleted_task=task.title))
                else:
                    raise ValueError(messages.TASK_NOT_FOUND_ERROR)
            else:
                raise ValueError(messages.INVALID_CHOICE_MESSAGE)
        except ValueError as e:
            print(messages.ERROR_MESSAGE, e)
    