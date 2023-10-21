from config import CLEAR, ALL

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
EXIT_PROGRAM    = exit_program_color    + "0. Exit"
CREATE_TASK     = input_selection_color + "1. Create new task"
EDIT_TASK       = input_selection_color + "2. Edit task"
MARK_TASK       = input_selection_color + "3. Mark task"
DELETE_TASK     = input_selection_color + "4. Delete task"
SORT_TASKS      = input_selection_color + "5. Sort tasks"

SORT_TASKS_OPTIONS = task_messages_color + """Sort tasks by:
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
ENTER_TASK_TITLE_MESSAGE            = input_messages_color + "Enter task title (cannot be null): "
ENTER_TASK_DESCRIPTION_MESSAGE      = input_messages_color + "Enter task description: "
ENTER_EDIT_TASK_MESSAGE             = input_messages_color + "Enter task index to edit: "
ENTER_NEW_TASK_TITLE_MESSAGE        = input_messages_color + "Enter new task title: "
ENTER_NEW_TASK_DESCRIPTION_MESSAGE  = input_messages_color + f"Enter new task description (Type {CLEAR} to clear description): "
ENTER_MARK_TASK_MESSAGE             = input_messages_color + f"Enter task index to mark (Type {ALL} to mark all): "
ENTER_DELETE_TASK_MESSAGE           = input_messages_color + f"Enter task index to delete (Type {ALL} to delete all): "
CONFIRM_DELETE_ALL_TASKS_MESSAGE    = input_messages_color + "Are you sure you want to delete all tasks? (Y/n): "
ENTER_SORT_TASKS_MESSAGE            = input_messages_color + "Enter sort option: "

## task messages
<<<<<<< Updated upstream
TASK_ADDED_MESSAGE = "➕  Task '{title}' added."
TASK_EDITED_MESSAGE = "✏️  Task '{title}' edited."
TASK_MARKED_MESSAGE = "✔️  Task '{title}' marked as '{is_completed}'."
ALL_TASKS_MARKED_COMPLETED_MESSAGE = "✔️  All tasks marked as completed."
ALL_TASKS_MARKED_NOT_COMPLETED_MESSAGE = "✔️  All tasks marked as 'not completed'."
TASK_DELETED_MESSAGE = "🗑️  Task '{deleted_task}' deleted."
ALL_TASKS_DELETED_MESSAGE = "🗑️  All tasks deleted."
TASK_INDEX_CHANGED_MESSAGE = "🔀  Task index changed from {old_index} to {new_index}."

## program messages
CONNECTED_TO_DATABASE_MESSAGE = "Connected to database successfully."
NO_TASKS_FOUND_MESSAGE = "(No tasks found.)"
QUIT_MESSAGE = "(Exiting the program...)"
PRESS_ENTER_MESSAGE = "(Press enter to continue...)"
=======
TASK_ADDED_MESSAGE                      = task_messages_color + "➕ Task '{title}' added."
TASK_EDITED_MESSAGE                     = task_messages_color + "✏️ Task '{title}' edited."
TASK_MARKED_MESSAGE                     = task_messages_color + "✔️ Task '{title}' marked as '{is_completed}'."
ALL_TASKS_MARKED_COMPLETED_MESSAGE      = task_messages_color + "✔️ All tasks marked as completed."
ALL_TASKS_MARKED_NOT_COMPLETED_MESSAGE  = task_messages_color + "✔️ All tasks marked as 'not completed'."
TASK_DELETED_MESSAGE                    = task_messages_color + "🗑️ Task '{deleted_task}' deleted."
ALL_TASKS_DELETED_MESSAGE               = task_messages_color + "🗑️ All tasks deleted."
TASKS_SORTED_MESSAGE                    = task_messages_color + "🔀 Task index changed from {old_index} to {new_index}."

## program messages
CONNECTED_TO_DATABASE_MESSAGE   = program_messages_color + "(Connected to database successfully.)"
NO_TASKS_FOUND_MESSAGE          = program_messages_color + "(No tasks found.)"
EXIT_PROGRAM_MESSAGE           = program_messages_color + "(Exiting the program...)"
PRESS_ENTER_MESSAGE             = program_messages_color + "(Press enter to continue...)"
TERMINATING_PROGRAM_MESSAGE     = program_messages_color + "(Terminating program...)"

## error messages
DATABASE_CONNECTION_ERROR   = error_color + "Error connecting to database: "
ERROR_MESSAGE               = error_color + "⚠️ An error occurred:"
TASK_TITLE_ERROR            = "🚫 Task title cannot be empty."
TASK_NOT_FOUND_ERROR        = "🚫 Invalid task index. Task not found."
INVALID_CHOICE_MESSAGE      = "Invalid choice. Please select a valid option."

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
>>>>>>> Stashed changes

## error messages
DATABASE_CONNECTION_ERROR = "Error connecting to database: {0}"
ERROR_MESSAGE = "⚠️ An error occurred."
TASK_TITLE_ERROR = "🚫 Task title cannot be empty."
TASK_NOT_FOUND_ERROR = "🚫 Invalid task index. Task not found."
INVALID_CHOICE_MESSAGE = "Invalid choice. Please select a valid option."