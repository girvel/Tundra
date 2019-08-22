class Interaction:
    def __init__(self, action):
        self.action = action

    def interact(self):
        self.action()
