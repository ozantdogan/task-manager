from app_settings import Text, app_commands, colors, styles
import time
from colorama import init

init(autoreset=True)

welcome_message_color = colors.get('welcome_message_color')
task_manager_title_color = colors.get('task_manager_title_color')
input_selection_color = colors.get('input_selection_color')
subtask_selection_color = colors.get('subtask_selection_color')
exit_program_color = colors.get('exit_program_color')
input_messages_color = colors.get('input_messages_color')
subtask_messages_color = colors.get('subtask_messages_color')
task_messages_color = colors.get('task_messages_color')
program_messages_color = colors.get('program_messages_color')
error_color = colors.get('error_color')
line_color = colors.get('line_color')
disconnect_program_color = colors.get('disconnect_program_color')

program_messages_style = styles.get('program_messages_style')


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
TASK_MANAGER_TITLE      = task_manager_title_color + '{DB_NAME}'
SEPARATOR_LINE          = Text('----------------------------------------------', color=line_color)
EXIT_PROGRAM            = Text('(Press Ctrl+C to terminate)', color=program_messages_color)
DISCONNECT_PROGRAM      = Text('Disconnect', color=exit_program_color)
CREATE_TASK             = Text('New task', color=input_selection_color).bold()
VIEW_TASK               = Text('View task', color=input_selection_color).bold()
EDIT_TASK               = Text('Edit task', color=input_selection_color).bold()
MARK_TASK               = Text('Mark task', color=input_selection_color).bold()
DELETE_TASK             = Text('Delete task', color=input_selection_color).bold()
SORT_TASKS              = Text('Sort tasks', color=input_selection_color).bold()

CREATE_SUBTASK          = Text('New subtask', color=subtask_selection_color).bold()
VIEW_SUBTASK            = Text('View subtask', color=subtask_selection_color).bold()
EDIT_SUBTASK            = Text('Edit subtask', color=subtask_selection_color).bold()
MARK_SUBTASK            = Text('Mark subtask', color=subtask_selection_color).bold()
DELETE_SUBTASK          = Text('Delete subtask', color=subtask_selection_color).bold()

BACK                    = Text('Back', color=exit_program_color).bold()

SORT_TASKS_OPTIONS = task_messages_color + """Sort tasks by:
    1. Alphabetical order
    2. Creation date
    3. Modification date
    4. Completion status
    """

## database
ENTER_DATABASE_CONFIGURATION    = Text('Enter the database configurations (Ctrl+C to exit.)', color=input_messages_color)
ENTER_DATABASE_NAME             = Text('Database name: ', color=input_selection_color)
ENTER_DATABASE_USER             = Text('Database user: ', color=input_selection_color)
ENTER_DATABASE_PASSWORD         = Text('Database password: ', color=input_selection_color)
ENTER_DATABASE_HOST             = Text('Database host: ', color=input_selection_color)
ENTER_DATABASE_PORT             = Text('Database port: ', color=input_selection_color)

## input messages
ENTER_TASK_TITLE_MESSAGE            = input_messages_color + "Enter task title (cannot be null): "
ENTER_TASK_DESCRIPTION_MESSAGE      = input_messages_color + "Enter task description: "
ENTER_EDIT_TASK_MESSAGE             = input_messages_color + "Enter task index to edit: "
ENTER_NEW_TASK_TITLE_MESSAGE        = input_messages_color + "Enter new task title: "
ENTER_NEW_TASK_DESCRIPTION_MESSAGE  = input_messages_color + f"Enter new task description (Type {app_commands.get('CLEAR')} to clear description): "
ENTER_MARK_TASK_MESSAGE             = input_messages_color + f"Enter task index to mark (Type {app_commands.get('ALL')} to mark all): "
ENTER_DELETE_TASK_MESSAGE           = input_messages_color + f"Enter task index to delete (Type {app_commands.get('ALL')} to delete all): "
CONFIRM_DELETE_ALL_TASKS_MESSAGE    = input_messages_color + "Are you sure you want to delete all tasks? (Y/n): "
ENTER_SORT_TASKS_MESSAGE            = input_messages_color + "Enter sort option: "
ENTER_VIEW_TASK_MESSAGE             = input_messages_color + "Enter task index to view: "
CONFIRM_DISCONNECT_MESSAGE          = Text("Are you sure you want to disconnect from the database? (Y/n): ", color=disconnect_program_color).underline()

## input messages (subtasks)
ENTER_SUBTASK_TITLE_MESSAGE             = subtask_messages_color + "Enter subtask title (cannot be null): "
ENTER_SUBTASK_DESCRIPTION_MESSAGE       = subtask_messages_color + "Enter subtask description: "
ENTER_EDIT_SUBTASK_MESSAGE              = subtask_messages_color + "Enter subtask index to edit: "
ENTER_NEW_SUBTASK_TITLE_MESSAGE         = subtask_messages_color + "Enter new subtask title: "
ENTER_NEW_SUBTASK_DESCRIPTION_MESSAGE   = subtask_messages_color + f"Enter new subtask description (Type {app_commands.get('CLEAR')} to clear description): "
ENTER_MARK_SUBTASK_MESSAGE              = subtask_messages_color + f"Enter subtask index to mark (Type {app_commands.get('ALL')} to mark all): "
ENTER_DELETE_SUBTASK_MESSAGE            = subtask_messages_color + f"Enter subtask index to delete (Type {app_commands.get('ALL')} to delete all): "
ENTER_VIEW_SUBTASK_MESSAGE              = subtask_messages_color + "Enter subtask index to view: "

## task messages
TASK_ADDED_MESSAGE                      = task_messages_color + "➕ Task '{title}' added."
TASK_EDITED_MESSAGE                     = task_messages_color + "✏️ Task '{title}' edited."
TASK_MARKED_MESSAGE                     = task_messages_color + "✔️ Task '{title}' marked as '{is_completed}'."
ALL_TASKS_MARKED_COMPLETED_MESSAGE      = task_messages_color + "✔️ All tasks marked as completed."
ALL_TASKS_MARKED_NOT_COMPLETED_MESSAGE  = task_messages_color + "✔️ All tasks marked as 'not completed'."
TASK_DELETED_MESSAGE                    = task_messages_color + "🗑️ Task '{deleted_task}' deleted."
ALL_TASKS_DELETED_MESSAGE               = task_messages_color + "🗑️ All tasks deleted."
TASKS_SORTED_MESSAGE                    = task_messages_color + "🔀 Task index changed from {old_index} to {new_index}."

## program messages
SUBTASKS_MESSAGE                = Text("Subtasks:", color=program_messages_color).bold()
CONNECTED_TO_DATABASE_MESSAGE   = Text("(Connected to the database successfully.)", color=program_messages_color).italic()
NO_TASKS_FOUND_MESSAGE          = Text("(No tasks found.)", color=program_messages_color).italic()
NO_DESCRIPTION_MESSAGE          = Text("(No description.)", color=program_messages_color).italic()
DISCONNECT_MESSAGE              = Text("(Disconnected from the database.)", color=program_messages_color).italic()
PRESS_ENTER_MESSAGE             = Text("(Press enter to continue...)", color=program_messages_color).italic()
TERMINATING_PROGRAM_MESSAGE     = Text("(Exiting the program...)", color=program_messages_color).bold_italic()

## error messages
DATABASE_CONNECTION_ERROR   = Text('⚠️ Error connecting to database: ', color=error_color).bold()
ERROR_MESSAGE               = Text('⚠️ An error occured: ', color=error_color).bold()
TASK_TITLE_ERROR            = Text('🚫 Task title cannot be empty.')
TASK_NOT_FOUND_ERROR        = Text('🚫 Invalid task index. Task not found.')
INVALID_CHOICE_MESSAGE      = Text('🚫 Invalid choice. Please select a valid option.')

# def database_connection_error(error):
#     message = f"Error connecting to database: {error}"
#     logging.info(f"Called database_connection_error function. Message: {message}")
#     return message

# def error_message():
#     message = "⚠️ An error occurred."
#     logging.info(f"Called error_message function. Message: {message}")
#     return message

# def task_title_error():
#     message = "🚫 Task title cannot be empty."
#     logging.info(f"Called task_title_error function. Message: {message}")
#     return message

# def task_not_found_error():
#     message = "🚫 Invalid task index. Task not found."
#     logging.info(f"Called task_not_found_error function. Message: {message}")
#     return message

# def invalid_choice_message():
#     message = "Invalid choice. Please select a valid option."
#     logging.info(f"Called invalid_choice_message function. Message: {message}")
#     return message
