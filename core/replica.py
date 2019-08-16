from termcolor import colored


class Replica:
    def __init__(self, name, text):
        self.name = name
        self.text = text

    def __str__(self):
        return f'{colored(self.name, "red")}: {self.text}'
