from termcolor import colored

from core.book import Book
from core.inventory import Inventory
from core.item import Item
from game.game import player

from writing.io import print, input_line, print_line
from writing.replace import Replace
from writing.tools import request_choice

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


def description(text):
    print_line()
    phrase(text)
    print_line()


def scene(name, description):
    phrase(
        '\n\n\t{title}\n\n{description}\n'.format(
            title=colored(name.upper(), "red"),
            description=f'{description}\n' if description != '' else ''
        )
    )


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


def __take_item(place, player, item):
    place.content = [c for c in place.content if c.get_component(type(item)) is not item]
    player.get_component(Inventory).content.append(item)


def look_around(place):
    choice_ = ""
    end_choice = f"Покинуть {place.name}"

    while choice_ != end_choice:
        variants = [
            (Book, (lambda b: f"Прочитать {b.title}"), (lambda pc, pr, b: read_book(b))),
            (Item, (lambda i: f'Взять {i.name} ({i.weight} кг)'), __take_item)
        ]

        actions = {
            v[1](item.get_component(v[0])): (v[2], place, player, item.get_component(v[0]))
            for item in place.content
            for v in variants
            if item.has_component(v[0])
        }

        actions[end_choice] = (lambda x: 0, 0)

        choice_ = request_choice(list(actions.keys()))
        a = actions[choice_]
        a[0](*a[1:])


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


def goto_by_choice(*variants):
    result = request_choice(variants, input_line, print_line)
    goto(result)
    return variants.index(result) + 1
