from termcolor import colored

from core.replica import Replica


class Scenario:
    replicas = []
    names = []
    name = "Another one scenario"

    def scene(self, name):
        pass

    def replace(self, shortcut, name):
        self.names.append((shortcut, name))

    def replica(self, name, text):
        for n in self.names:
            text = text.replace(n[0], n[1])

        self.replicas.append(Replica(name, text))

    def play(self):
        for replica in self.replicas:
            print(f'{colored(replica.name, "red")}: {replica.text}', end='')
            input()


scenario = Scenario()
