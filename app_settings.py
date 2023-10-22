from colorama import Fore, Back, Style, init

#Completed task status
#
COMPLETED = '☑️'
NOT_COMPLETED = '🔳'

#Commands
#
CLEAR = "-clr"
ALL = "-a"

class Text:
    def __init__(self, text, color=None):
        self.text = text
        self.color = color

    def __str__(self):
        if self.color:
            return f"{self.color}{self.text}{Fore.RESET}"
        else:
            return self.text

    def bold(self):
        return Text(f"\033[1m{self.text}\033[0m", self.color)

    def italic(self):
        return Text(f"\033[3m{self.text}\033[0m", self.color)

    def bold_italic(self):
        return Text(f"\033[1;3m{self.text}\033[0m", self.color)

    def underline(self):
        return Text(f"\033[4m{self.text}\033[0m", self.color)
    

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

