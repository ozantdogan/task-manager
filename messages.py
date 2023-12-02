from app_settings import Text, app_icons, app_commands, colors, styles
import time
from colorama import init

init(autoreset=True)

add_icon = app_icons.get("ADD")
edit_icon = app_icons.get("EDIT")
mark_icon = app_icons.get("MARK")
delete_icon = app_icons.get("DELETE")
error_icon = app_icons.get("ERROR")
not_found_icon = app_icons.get("NOT_FOUND")


welcome_message_color = colors.get("welcome_message_color")
task_manager_title_color = colors.get("task_manager_title_color")
input_selection_color = colors.get("input_selection_color")
subtask_selection_color = colors.get("subtask_selection_color")
exit_program_color = colors.get("exit_program_color")
input_messages_color = colors.get("input_messages_color")
subtask_input_messages_color = colors.get("subtask_input_messages_color")
task_messages_color = colors.get("task_messages_color")
subtask_messages_color = colors.get("subtask_messages_color")
program_messages_color = colors.get("program_messages_color")
error_color = colors.get("error_color")
line_color = colors.get("line_color")
confirm_exit_color = colors.get("confirm_exit_color")

program_messages_style = styles.get("program_messages_style")


##intro


def welcome_message():
    message = """     
    //--------------------------------------
    |                          2023-10-20  |
    |  TASK MANAGER                        |
    |  Created by: Ozan Doğan              |                         
    --------------------------------------//
    """
    for line in message.splitlines():
        print(welcome_message_color + line)
        time.sleep(0.025)


## menu
TASK_MANAGER_TITLE = task_manager_title_color + "{DB_NAME}"
SEPARATOR_LINE = Text(
    "----------------------------------------------", color=line_color
)
TERMINATE_PROGRAM = Text("(Press Ctrl+C to terminate)", color=program_messages_color)

CREATE_TASK = Text("New task", color=input_selection_color).bold()
VIEW_TASK = Text("View task", color=input_selection_color).bold()
EDIT_TASK = Text("Edit task", color=input_selection_color).bold()
MARK_TASK = Text("Mark task", color=input_selection_color).bold()
DELETE_TASK = Text("Delete task", color=input_selection_color).bold()
SORT_TASKS = Text("Sort tasks", color=input_selection_color).bold()

CREATE_SUBTASK = Text("New subtask", color=subtask_selection_color).bold()
VIEW_SUBTASK = Text("View subtask", color=subtask_selection_color).bold()
EDIT_SUBTASK = Text("Edit subtask", color=subtask_selection_color).bold()
MARK_SUBTASK = Text("Mark subtask", color=subtask_selection_color).bold()
DELETE_SUBTASK = Text("Delete subtask", color=subtask_selection_color).bold()
SORT_SUBTASKS = Text("Sort subtasks", color=subtask_selection_color).bold()

BACK = Text("Back", color=exit_program_color).bold()

EXIT = Text("Exit", color=exit_program_color).bold()

SORT_TASKS_OPTIONS = (
    task_messages_color
    + """Sort tasks by:
    1. Alphabetical order
    2. Creation date
    3. Modification date
    4. Completion status
    """
)

## database
ENTER_DATABASE_CONFIGURATION = Text(
    "Enter the database configurations (Ctrl+C to exit.)", color=input_messages_color
)
ENTER_DATABASE_NAME = Text("Database name: ", color=input_selection_color)
ENTER_DATABASE_USER = Text("Database user: ", color=input_selection_color)
ENTER_DATABASE_PASSWORD = Text("Database password: ", color=input_selection_color)
ENTER_DATABASE_HOST = Text("Database host: ", color=input_selection_color)
ENTER_DATABASE_PORT = Text("Database port: ", color=input_selection_color)

## input messages
ENTER_TASK_TITLE_MESSAGE = input_messages_color + "Enter task title (cannot be null): "
ENTER_TASK_DESCRIPTION_MESSAGE = input_messages_color + "Enter task description: "
ENTER_EDIT_TASK_MESSAGE = input_messages_color + "Enter task index to edit: "
ENTER_NEW_TASK_TITLE_MESSAGE = input_messages_color + "Enter new task title: "
ENTER_NEW_TASK_DESCRIPTION_MESSAGE = (
    input_messages_color
    + f"Enter new task description (Type {app_commands.get('CLEAR')} to clear description): "
)
ENTER_MARK_TASK_MESSAGE = (
    input_messages_color
    + f"Enter task index to mark (Type {app_commands.get('ALL')} to mark all): "
)
ENTER_DELETE_TASK_MESSAGE = (
    input_messages_color
    + f"Enter task index to delete (Type {app_commands.get('ALL')} to delete all): "
)
CONFIRM_DELETE_IF_HAS_SUBTASKS_MESSAGE = (
    input_messages_color
    + "Are you sure you want to delete this task? All subtasks will be deleted in progress. (Y/n): "
)
CONFIRM_DELETE_ALL_TASKS_MESSAGE = (
    input_messages_color + "Are you sure you want to delete all tasks? (Y/n): "
)
ENTER_SORT_TASKS_MESSAGE = input_messages_color + "Enter sort option: "
ENTER_VIEW_TASK_MESSAGE = input_messages_color + "Enter task index to view: "
CONFIRM_EXIT_MESSAGE = Text(
    "Are you sure you want to exit the program (Y/n): ", color=confirm_exit_color
).underline()

## task messages
TASK_ADDED_MESSAGE = task_messages_color + f"{add_icon} Task '{{title}}' added."
TASK_EDITED_MESSAGE = task_messages_color + f"{edit_icon} Task '{{title}}' edited."
TASK_MARKED_MESSAGE = (
    task_messages_color + f"{mark_icon} Task '{{title}}' marked as '{{is_completed}}'."
)
ALL_TASKS_MARKED_COMPLETED_MESSAGE = (
    task_messages_color + f"{mark_icon} All tasks marked as completed."
)
ALL_TASKS_MARKED_NOT_COMPLETED_MESSAGE = (
    task_messages_color + f"{mark_icon} All tasks marked as 'not completed'."
)
TASK_DELETED_MESSAGE = (
    task_messages_color + f"{delete_icon} Task '{{deleted_task}}' deleted."
)
ALL_TASKS_DELETED_MESSAGE = task_messages_color + f"{delete_icon} All tasks deleted."

## input messages (subtasks)
ENTER_SUBTASK_TITLE_MESSAGE = (
    subtask_input_messages_color + "Enter subtask title (cannot be null): "
)
ENTER_SUBTASK_DESCRIPTION_MESSAGE = (
    subtask_input_messages_color + "Enter subtask description: "
)
ENTER_EDIT_SUBTASK_MESSAGE = (
    subtask_input_messages_color + "Enter subtask index to edit: "
)
ENTER_NEW_SUBTASK_TITLE_MESSAGE = (
    subtask_input_messages_color + "Enter new subtask title: "
)
ENTER_NEW_SUBTASK_DESCRIPTION_MESSAGE = (
    subtask_input_messages_color
    + f"Enter new subtask description (Type {app_commands.get('CLEAR')} to clear description): "
)
ENTER_MARK_SUBTASK_MESSAGE = (
    subtask_input_messages_color + f"Enter subtask index to mark: "
)
ENTER_DELETE_SUBTASK_MESSAGE = (
    subtask_input_messages_color
    + f"Enter subtask index to delete (Type {app_commands.get('ALL')} to delete all): "
)
CONFIRM_DELETE_ALL_SUBTASKS_MESSAGES = (
    subtask_input_messages_color
    + "Are you sure you want to delete all subtasks? (Y/n): "
)
ENTER_VIEW_SUBTASK_MESSAGE = (
    subtask_input_messages_color + "Enter subtask index to view: "
)
ENTER_SORT_SUBTASKS_MESSAGE = subtask_input_messages_color + "Enter sort option: "

##subtask messages
SUBTASK_ADDED_MESSAGE = (
    subtask_messages_color + f"{add_icon} Subtask '{{title}}' added."
)
SUBTASK_EDITED_MESSAGE = (
    subtask_messages_color + f"{edit_icon} Subtask '{{title}}' edited."
)
SUBTASK_MARKED_MESSAGE = (
    subtask_messages_color
    + f"{mark_icon} Subtask '{{title}}' marked as '{{is_completed}}'."
)
SUBTASK_DELETED_MESSAGE = (
    subtask_messages_color + f"{delete_icon} Subtask '{{deleted_task}}' deleted."
)
ALL_SUBTASKS_DELETED_MESSAGE = (
    subtask_messages_color + f"{delete_icon} All subtasks deleted."
)


## program messages
SUBTASKS_MESSAGE = Text("Subtasks:", color=program_messages_color).bold()
CONNECTED_TO_DATABASE_MESSAGE = Text(
    "(Connected to the database successfully.)", color=program_messages_color
).italic()
NO_TASKS_FOUND_MESSAGE = Text(
    "(No tasks found.)", color=program_messages_color
).italic()
NO_DESCRIPTION_MESSAGE = Text(
    "(No description.)", color=program_messages_color
).italic()
EXIT_PROGRAM_MESSAGE = Text(
    "(Exiting the program...)", color=program_messages_color
).italic()
PRESS_ENTER_MESSAGE = Text(
    "(Press enter to continue...)", color=program_messages_color
).italic()
TERMINATING_PROGRAM_MESSAGE = Text(
    "(Terminating the program...)", color=program_messages_color
).bold_italic()

## error messages
ERROR_MESSAGE = Text(f"{error_icon} An error occured: ", color=error_color).bold()
TASK_TITLE_ERROR = Text(f"{not_found_icon} Task title cannot be empty.")
TASK_NOT_FOUND_ERROR = Text(f"{not_found_icon} Invalid task index. Task not found.")
INVALID_CHOICE_MESSAGE = Text(
    f"{not_found_icon} Invalid choice. Please select a valid option."
)
