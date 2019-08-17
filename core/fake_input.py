class FakeInput:
    def __init__(self, saved_lines):
        self.saved_lines = saved_lines
        self.current_index = -1

    def reset(self):
        self.saved_lines = []
        self.current_index = -1

    def __call__(self):
        self.current_index += 1

        if self.current_index >= len(self.saved_lines):
            input_ = input()
            self.saved_lines.append(input_)
            return input_

        current_line = self.saved_lines[self.current_index]
        print(current_line)
        return current_line

    def __repr__(self):
        return f'<FakeInput: saved {len(self.saved_lines)} lines, last line is {self.saved_lines[self.current_index]}>'
