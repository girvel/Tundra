from termcolor import colored


class Scene:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'\n\n\t{colored(self.name.upper(), "red")}\n\n' + (f'{self.description}\n' if self.description != "" else '')
