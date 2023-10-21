from config import CLEAR, ALL

##intro
WELCOME_MESSAGE = """**TASK MANAGER**
    By Ozan Doğan
    Created on 2023-10-20
    """

## menu 
QUIT_PROGRAM = "0. Quit"
CREATE_TASK = "1. Create new task"
EDIT_TASK = "2. Edit task"
MARK_TASK = "3. Mark task"
DELETE_TASK = "4. Delete task"
CHANGE_TASK = "5. Sort tasks"

SORT_TASKS = """Sort tasks by:
    1. Title
    2. Creation date
    3. Modification date
    4. Completion status
    """

## error messages
ERROR_MESSAGE = "⚠️ An error occurred."
TASK_TITLE_ERROR = "🚫 Task title cannot be empty."
TASK_NOT_FOUND_ERROR = "🚫 Invalid task index. Task not found."
INVALID_CHOICE_MESSAGE = "Invalid choice. Please select a valid option."

## input messages
ENTER_TASK_TITLE_MESSAGE = "Enter task title (cannot be null): "
ENTER_TASK_DESCRIPTION_MESSAGE = "Enter task description: "
ENTER_EDIT_TASK_MESSAGE = "Enter task index to edit: "
ENTER_NEW_TASK_TITLE_MESSAGE = "Enter new task title: "
ENTER_NEW_TASK_DESCRIPTION_MESSAGE = f"Enter new task description (Type {CLEAR} to clear description): "
ENTER_MARK_TASK_MESSAGE = f"Enter task index to mark (Type {ALL} to mark all): "
ENTER_DELETE_TASK_MESSAGE = f"Enter task index to delete (Type {ALL} to delete all): "
CONFIRM_DELETE_ALL_TASKS_MESSAGE = "Are you sure you want to delete all tasks? (Y/n): "
ENTER_SORT_TASKS_MESSAGE = "Enter sort option: "

## task messages
TASK_ADDED_MESSAGE = "➕  Task '{title}' added."
TASK_EDITED_MESSAGE = "✏️  Task '{title}' edited."
TASK_MARKED_MESSAGE = "✔️  Task '{title}' marked as '{is_completed}'."
ALL_TASKS_MARKED_COMPLETED_MESSAGE = "✔️  All tasks marked as completed."
ALL_TASKS_MARKED_NOT_COMPLETED_MESSAGE = "✔️  All tasks marked as 'not completed'."
TASK_DELETED_MESSAGE = "🗑️  Task '{deleted_task.title}' deleted."
ALL_TASKS_DELETED_MESSAGE = "🗑️  All tasks deleted."
TASK_INDEX_CHANGED_MESSAGE = "🔀  Task index changed from {old_index} to {new_index}."

## program messages
NO_TASKS_FOUND_MESSAGE = "(No tasks found.)"
QUIT_MESSAGE = "(Exiting the program...)"
PRESS_ENTER_MESSAGE = "(Press enter to continue...)"
