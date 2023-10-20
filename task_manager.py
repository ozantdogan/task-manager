from task import Task
import messages

class TaskManager:
    def __init__(self):
        self.tasks = []

    def list_tasks(self):
        if len(self.tasks) == 0:
            print(messages.NO_TASKS_FOUND_MESSAGE)
        else:
            for i, task in enumerate(self.tasks, start=1):
                status = "✅" if task.is_completed else "❌"
                print(f"{i}.[{status}] {task.title}: {task.description}")

    def add_task(self, title, description):
        if not title:
            raise ValueError(messages.TASK_TITLE_ERROR)
        task = Task(title, description)
        self.tasks.append(task)
        print(messages.TASK_ADDED_MESSAGE.format(title=task.title))

    def mark_task(self, task_index):
        try:
            if 1 <= task_index <= len(self.tasks):
                task = self.tasks[task_index - 1]
                task.is_completed = not task.is_completed
                print(messages.TASK_MARKED_MESSAGE.format(title=task.title, is_completed='completed' if task.is_completed else 'not completed'))
            else:
                raise ValueError(messages.TASK_NOT_FOUND_ERROR)
        except ValueError as e:
            print(messages.ERROR_MESSAGE, e)
            
    def delete_task(self, task_index):
        try:
            if 1 <= task_index <= len(self.tasks):
                deleted_task = self.tasks.pop(task_index - 1)
                print(messages.TASK_DELETED_MESSAGE.format(deleted_task=deleted_task))
            else:
                raise Exception(messages.TASK_NOT_FOUND_ERROR)
        except Exception as e:
            print(messages.ERROR_MESSAGE, e)