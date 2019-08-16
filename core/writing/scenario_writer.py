from core.modelling.choice import Choice
from core.writing.lazy_goto import LazyGoto
from core.modelling.lazy_replace import LazyReplace
from core.modelling.monologue import Monologue
from core.modelling.replica import Replica
from core.modelling.scenario import scenario
from core.modelling.scene import Scene


class ScenarioWriter:
    def __init__(self):
        self.scenario = scenario
        self.current_monologue = None
        self.current_choice_monologue = None
        self.__lazy_gotos = []  # [ LazyGoto* ]
        self.all_monologues = []

    def __get_working_monologue(self):
        return self.current_monologue if self.current_choice_monologue is None else self.current_choice_monologue

    def __create_monologue(self, name):
        m = Monologue(name)
        for goto in self.__lazy_gotos:
            if name == goto.required_name:
                goto.from_.choices.append(Choice("", m))

        self.all_monologues.append(m)
        return m

    def scene(self, name, description=""):
        new_monologue = self.__create_monologue(name)
        new_monologue.replicas.append(Scene(name, description))

        if self.scenario.root_monologue is None:
            self.scenario.root_monologue = new_monologue
        elif self.current_choice_monologue is None:
            self.current_monologue.choices.append(Choice("", new_monologue))

        self.current_monologue = new_monologue
        self.current_choice_monologue = None

    def choice(self, text):
        self.current_choice_monologue = self.__create_monologue(text)
        self.current_monologue.choices.append(Choice(text, self.current_choice_monologue))

    def goto(self, text):
        for monologue in self.all_monologues:
            if monologue.name != text:
                continue

            self.__get_working_monologue().choices.append(Choice(text, monologue))
        else:
            self.__lazy_gotos.append(LazyGoto(self.__get_working_monologue(), text))

    def replace(self, shortcut, name):
        self.scenario.replaces.append(LazyReplace(shortcut, name))

    def replica(self, name, text):
        self.__get_working_monologue().replicas.append(Replica(name, text))


scenario_writer = ScenarioWriter()