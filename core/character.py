from core.scenario import scenario


class Character:
    def __init__(self, name):
        self.name = name
  
    def __call__(self, text):
        scenario.replica(self.name, text)
