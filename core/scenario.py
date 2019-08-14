from termcolor import colored

from core.monologue import Monologue
from core.replica import Replica


class Scenario:
    root_monologue = None
    current_monologue = None
    current_choice_monologue = None
    names = []
    name = "Another one scenario"

    def scene(self, name):
        new_monologue = Monologue(name)

        if self.root_monologue is None:
            self.root_monologue = new_monologue
        else:
            self.current_monologue.choices.append(new_monologue)

        self.current_monologue = new_monologue
        self.current_choice_monologue = None

    def replace(self, shortcut, name):
        self.names.append((shortcut, name))

    def replica(self, name, text):
        for n in self.names:
            text = text.replace(n[0], n[1])

        (self.current_monologue if self.current_choice_monologue is None else self.current_choice_monologue)\
            .replicas.append(Replica(name, text))

    def choice(self, text):
        self.current_choice_monologue = Monologue(text)
        self.current_monologue.choices.append((text, self.current_choice_monologue))

    def play(self):
        self.current_monologue = self.root_monologue

        while True:
            for replica in self.current_monologue.replicas:
                print(f'{colored(replica.name, "red")}: {replica.text}', end='')
                input()

            if len(self.current_monologue.choices) == 0:
                break

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
