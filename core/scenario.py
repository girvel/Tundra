from core.choice import Choice
from core.lazy_goto import LazyGoto
from core.lazy_replace import LazyReplace
from core.monologue import Monologue
from core.replica import Replica
from core.scene import Scene


class Scenario:
    def __init__(self):
        self.root_monologue = None
        self.current_monologue = None
        self.current_choice_monologue = None
        self.replaces = []  # [ LazyReplace* ]
        self.name = "Another one scenario"
        self.__lazy_gotos = []  # [ LazyGoto* ]

    def __create_monologue(self, name):
        m = Monologue(name)
        for goto in self.__lazy_gotos:
            if name == goto[1]:
                goto[0].choices.append(Choice("", m))
        return m

    def scene(self, name, description=""):
        new_monologue = self.__create_monologue(name)
        new_monologue.replicas.append(Scene(name, description))

        if self.root_monologue is None:
            self.root_monologue = new_monologue
        elif self.current_choice_monologue is None:
            self.current_monologue.choices.append(Choice("", new_monologue))

        self.current_monologue = new_monologue
        self.current_choice_monologue = None

    def choice(self, text):
        self.current_choice_monologue = self.__create_monologue(text)
        self.current_monologue.choices.append(Choice(text, self.current_choice_monologue))

    def goto(self, text):
        self.__lazy_gotos.append(LazyGoto(
            self.current_monologue if self.current_choice_monologue is None else self.current_choice_monologue,
            text
        ))

    def replace(self, shortcut, name):
        self.replaces.append(LazyReplace(shortcut, name))

    def replica(self, name, text):
        (self.current_monologue if self.current_choice_monologue is None else self.current_choice_monologue)\
            .replicas.append(Replica(name, text))

    def play(self):
        self.current_monologue = self.root_monologue

        while True:
            for replica in self.current_monologue.replicas:
                replica = str(replica)

                for r in self.replaces:
                    replica = replica.replace(r.shortcut, r.value)

                print(replica, end='')
                input()

            if len(self.current_monologue.choices) == 0:
                break

            if len(self.current_monologue.choices) == 1 and self.current_monologue.choices[0].text == "":
                self.current_monologue = self.current_monologue.choices[0].next_monologue
                continue

            print()
            for i, choice in enumerate(self.current_monologue.choices):
                print(f'{i + 1}. {choice.text}')

            while True:
                choice = input()

                if choice.isdigit():
                    choice = int(choice) - 1
                    if 0 <= choice < len(self.current_monologue.choices):
                        break

            self.current_monologue = self.current_monologue.choices[choice].next_monologue
            print()


scenario = Scenario()
