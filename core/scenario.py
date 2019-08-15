from termcolor import colored

from core.monologue import Monologue
from core.replica import Replica


class Scenario:

    def __init__(self):
        self.root_monologue = None
        self.current_monologue = None
        self.current_choice_monologue = None
        self.replaces = []
        self.name = "Another one scenario"
        self.__lazy_gotos = []  # [ (from, required_name)* ]

    def __create_monologue(self, name):
        m = Monologue(name)
        for r in self.__lazy_gotos:
            if name == r[1]:
                r[0].choices.append(("", m))
        return m

    def scene(self, name):
        new_monologue = self.__create_monologue(name)

        if self.root_monologue is None:
            self.root_monologue = new_monologue
        elif self.current_choice_monologue is None:
            self.current_monologue.choices.append(("", new_monologue))

        self.current_monologue = new_monologue
        self.current_choice_monologue = None

    def choice(self, text):
        self.current_choice_monologue = self.__create_monologue(text)
        self.current_monologue.choices.append((text, self.current_choice_monologue))

    def goto(self, text):
        self.__lazy_gotos.append((
            self.current_monologue if self.current_choice_monologue is None else self.current_choice_monologue,
            text
        ))

    def replace(self, shortcut, name):
        self.replaces.append((shortcut, name))

    def replica(self, name, text):
        for n in self.replaces:
            text = text.replace(n[0], n[1])

        (self.current_monologue if self.current_choice_monologue is None else self.current_choice_monologue)\
            .replicas.append(Replica(name, text))

    def play(self):
        self.current_monologue = self.root_monologue

        while True:
            for replica in self.current_monologue.replicas:
                print(replica, end='')
                input()

            if len(self.current_monologue.choices) == 0:
                break

            if len(self.current_monologue.choices) == 1 and self.current_monologue.choices[0][0] == "":
                self.current_monologue = self.current_monologue.choices[0][1]
                continue

            for i, v in enumerate(self.current_monologue.choices):
                print(f'{i + 1}. {v[0]}')

            while True:
                choice = input()

                if choice.isdigit():
                    choice = int(choice)
                    if 0 < choice <= len(self.current_monologue.choices):
                        self.current_monologue = self.current_monologue.choices[choice - 1][1]
                        break


scenario = Scenario()
