from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def list_tasks(self):
        if len(self.tasks) == 0:
            print("🚫 No tasks found.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                status = "✅" if task.is_completed else "❌"
                print(f"{i}.[{status}] {task.title}: {task.description}")

    def add_task(self, title, description):
        if not title:
            raise ValueError("🚫 Task title cannot be empty.")
        task = Task(title, description)
        self.tasks.append(task)

    def mark_task(self, task_index):
        try:
            if 1 <= task_index <= len(self.tasks):
                task = self.tasks[task_index - 1]
                task.is_completed = not task.is_completed
                print(f"✅ Task '{task.title}' marked as {'completed' if task.is_completed else 'not completed'}.")
            else:
                raise ValueError("🚫 Invalid task index. Task not found.")
        except ValueError as e:
            print(f"❌ An error occurred: {e}")
            
    def delete_task(self, task_index):
        try:
            if 1 <= task_index <= len(self.tasks):
                deleted_task = self.tasks.pop(task_index - 1)
                print(f"✅ Task '{deleted_task.description}' deleted.")
            else:
                raise Exception("🚫 Invalid task index. Task not found.")
        except Exception as e:
            print(f"❌ An error occurred: {e}")