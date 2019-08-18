from termcolor import colored

from console.tools import request_choice
from core.io import *
from core.replace import Replace
from localization.geography_tools import Book, Item

replaces = []

is_skipping = False
skip_for = None


def set_phrase_replace(shortcut, value):
    replaces.append(Replace(shortcut, value))


def phrase(text):
    if is_skipping:
        return

    for replace in replaces:
        text = text.replace(replace.shortcut, replace.value)

    print(text)
    input_line()


def scene(name, description):
    phrase(
        '\n\n\t{title}\n\n{description}\n'.format(
            title=colored(name.upper(), "red"),
            description=f'{description}\n' if description != '' else ''
        )
    )


def request(text):
    print(f'{text} ')
    return input_line()


def point(text):
    global is_skipping

    if is_skipping and skip_for == text:
        is_skipping = False


def goto(point_text):
    global is_skipping, skip_for

    if is_skipping:
        return

    is_skipping = True
    skip_for = point_text


def choice(*variants):
    goto(request_choice(variants, input_line, print_line))


class Character:
    def __init__(self, name):
        self.name = name

    def __call__(self, text):
        phrase(f'{colored(self.name, "red")}: {text}')

    def __repr__(self):
        return f'<Character: name="{self.name}">'


def read_book(book):
    phrase(book.title + "\n")

    for paragraph in book.content:
        phrase(paragraph + "\n")


def look_around(place):
    choice_ = ""
    end_choice = f"Покинуть {place.name}"

    while choice_ != end_choice:
        variants = [
            (Book, lambda b: f"Прочитать {b.title}", read_book),
            (Item, lambda i: f'Взять {i.name} ({i.weight} кг)', lambda b: 0)
        ]

        actions = {
            v[1](item.get_component(v[0])): (v[2], item.get_component(v[0]))
            for item in place.content
            for v in variants
            if item.has_component(v[0])
        }

        actions[end_choice] = (lambda x: 0, 0)

        choice_ = request_choice(list(actions.keys()))
        a = actions[choice_]
        a[0](a[1])
