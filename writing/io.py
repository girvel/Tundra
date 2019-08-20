from writing.fake_input import FakeInput

input_line = FakeInput([])

old_print = print


def print(text, *a, **kw):
    old_print(text, *a, end='', **kw)


def print_line(text="", *a, **kw):
    print(text + "\n", *a, **kw)
