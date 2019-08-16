from core.writing.scenario_writer import scenario_writer


class Character:
    def __init__(self, name):
        self.name = name
  
    def __call__(self, text):
        scenario_writer.replica(self.name, text)
