class Replace:
    def __init__(self, shortcut, value):
        self.value = value
        self.shortcut = shortcut

    def __repr__(self):
        return f'<Replace: "{self.shortcut}" -> "{self.value}">'
