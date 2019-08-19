from ecs.entity import Entity
from game.book import Book
from game.item import Item
from game.place import Place
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

