from sqlalchemy import asc, desc, func
from models import Task
from app_settings import *
import messages
import textwrap

class TaskManager:
    def __init__(self, session):
        self.task_db_ids = {}
        self.sortby = Task.createdon
        self.sort_order = asc
        self.session = session

    def get_task(self, commands=False):
        task_index = input()

        if commands:
            if task_index in app_commands.values():
                return task_index

        if not task_index.isdigit():
            raise ValueError(messages.INVALID_CHOICE_MESSAGE)

        task_id = self.task_db_ids.get(int(task_index))
        task = self.session.query(Task).filter_by(id=task_id).first()

        if task:
            return task
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
                status = app_icons.get('COMPLETED') if task.is_completed else app_icons.get('NOT_COMPLETED')
                description = f" [...]" if task.description.strip() else ""
                print(f"{index}{status}  {task.title}{description}")
    
    def add_task(self):
        print(messages.ENTER_TASK_TITLE_MESSAGE)
        title = input()
        print(messages.ENTER_TASK_DESCRIPTION_MESSAGE)
        description = input()
        if title == "":
            raise ValueError(messages.TASK_TITLE_ERROR)
        self.session.add(Task(title=title, description=description))

    def view_task(self, task):
        status = app_icons.get('COMPLETED') if task.is_completed else app_icons.get('NOT_COMPLETED')
        task_title = Text(str(task.title)).bold()
        task_description = Text(str(task.description))
        createdon_text = Text(f"Created on: {task.createdon.strftime('%d %b %Y %I:%M %p')}", color=colors.get('program_messages_color')).bold_italic()

        print(f"{status} {task_title}")
        print(messages.SEPARATOR_LINE)
        print(messages.NO_DESCRIPTION_MESSAGE) if str(task_description) == "" else [print(line) for line in textwrap.wrap(str(task_description), width=len(messages.SEPARATOR_LINE))]
        print(messages.SEPARATOR_LINE)
        print(f"{createdon_text}")
        
        if task.modifiedon is not None:
            modifiedon_text = Text(f"Last modified: {task.modifiedon.strftime('%d %b %Y %I:%M %p')}", color=colors.get('program_messages_color')).bold_italic()
            print(f"{modifiedon_text}")

    def edit_task(self):
        task = self.get_task()

        previous_title = task.title
        print(messages.ENTER_NEW_TASK_TITLE_MESSAGE)
        title = input()
        if(title == ""):
            title = task.title
        
        print(messages.ENTER_NEW_TASK_DESCRIPTION_MESSAGE)
        description = input()
        if(description == ""):
            description = task.description
        elif(description == app_commands.get('CLEAR')):
            description = ""
        
        task.title = title
        task.description = description
        task.modifiedon = func.now()

        self.session.commit()
        print(messages.TASK_EDITED_MESSAGE.format(title=previous_title))

    def mark_task(self):
        task = self.get_task(commands=True)
        if task == app_commands.get('ALL'):
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
        
        elif isinstance(task, Task):
            task.is_completed = not task.is_completed
            task.modifiedon = func.now()
            self.session.commit()
            print(messages.TASK_MARKED_MESSAGE.format(title=task.title, is_completed='completed' if task.is_completed else 'not completed'))

        else:
            raise ValueError(messages.INVALID_CHOICE_MESSAGE)
            
    def delete_task(self):
        task = self.get_task(commands=True)
        if task == app_commands.get('ALL'):
            print(messages.CONFIRM_DELETE_ALL_TASKS_MESSAGE)
            confirm = input()
            if confirm.lower() == "y":
                self.session.query(Task).delete()
                self.session.commit()
                self.task_db_ids.clear()
                print(messages.ALL_TASKS_DELETED_MESSAGE)

        elif isinstance(task, Task):
            self.session.delete(task)
            self.session.commit()
            print(messages.TASK_DELETED_MESSAGE.format(deleted_task=task.title))
        
        else:
            raise ValueError(messages.INVALID_CHOICE_MESSAGE)

    def sort_tasks(self):
        index = int(input())
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
        self.sort_order = desc if self.sort_order == asc else asc
            