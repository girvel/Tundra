from termcolor import colored

from core.book import Book
from core.item import Item
from core.place import Place
from framework.game import player

from writing.io import print, input_line, print_line
from writing.replace import Replace
from writing.tools import request_choice

replaces = []

testing = False
is_skipping = False
skip_for = None


def testing_mode():
    global testing
    testing = True


def set_phrase_replace(shortcut, value):
    replaces.append(Replace(shortcut, value))


def phrase(text):
    if is_skipping:
        return

    for replace in replaces:
        text = text.replace(replace.shortcut, replace.value)

    print(text)

    (print_line if testing else input_line)()


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
    place.content = [c for c in place.content if c is not item]
    player.inventory.content.append(item)


def look_around(place):
    choice_ = ""
    end_choice = "\0"

    variants = [
        (Book, (lambda b: f"Прочитать {b.title}"), (lambda pc, pr, e: read_book(e.book))),
        (Item, (lambda i: f'Взять {i.name} ({i.weight} кг)'), __take_item)
    ]

    while choice_ != end_choice:
        if not place.explored:
            description(place.description)
            place.explored = True

        actions = {
            v[1](entity.get_component(v[0])): (v[2], place, player, entity)
            for entity in place.content
            for v in variants
            if entity.has_component(v[0])
        }

        for connected in place.connected_places:
            actions[f'Пойти в {connected.name}'] = (lambda x: 0, connected)

        end_choice = f"Покинуть {place.name}"
        actions[end_choice] = (lambda: 0, )

        choice_ = request_choice(list(actions.keys()))
        a = actions[choice_]
        a[0](*a[1:])

        if len(a) == 2 and isinstance(a[1], Place):
            place = a[1]


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
