from colorama import Fore, Back, Style, init

#Completed task status
#
COMPLETED = '☑️'
NOT_COMPLETED = '🔳'

#Commands
#
CLEAR = "-clr"
ALL = "-a"

colors = {
    'welcome_message_color': Fore.LIGHTMAGENTA_EX,
    'task_manager_title_color': Fore.BLACK + Back.LIGHTMAGENTA_EX,
    'input_selection_color': Fore.LIGHTYELLOW_EX,
    'exit_program_color': Fore.WHITE,
    'input_messages_color': Fore.YELLOW,
    'task_messages_color': Fore.LIGHTMAGENTA_EX,
    'program_messages_color': Fore.LIGHTBLACK_EX,
    'error_color': Fore.RED,
}

styles = {
    'program_messages_style': Style.BRIGHT
}
