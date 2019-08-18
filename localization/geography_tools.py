from ecs.entity import Entity
from localization.game import clocks


def книга(имя, статичная=False):
    components = [Book(имя)]

    if статичная:
        components.append(Item(имя, 1))

    e = Entity(*components)

    clocks.register_entity(e)
    return e


def место(*содержание):
    return Place(*содержание)


BOOKS_FOLDER = 'assets/books'


class Book:
    def __init__(self, title):
        self.title = title

        with open(f'{BOOKS_FOLDER}/{title}.txt') as file:
            self.content = [line.replace('\n', '') for line in file if line != '\n']


class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Place:
    def __init__(self, name, content):
        self.name = name
        self.content = content
