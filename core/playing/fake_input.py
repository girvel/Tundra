class FakeInput:
    def __init__(self, saved_lines):
        self.saved_lines = saved_lines

    def __call__(self):
        if len(self.saved_lines) == 0:
            return input()
        else:
            current_line = self.saved_lines[0]
            self.saved_lines = self.saved_lines[1:]
            print(current_line)
            return current_line
