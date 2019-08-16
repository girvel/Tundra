class Choice:
    def __init__(self, text, next_monologue):
        self.text = text
        self.next_monologue = next_monologue

    def __str__(self):
        return self.text
