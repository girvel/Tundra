from core.book import Book
from core.item import Item
from ecs.entity import Entity
from game.game import clocks


def book(name, static=False):
    components = [Book(name)]

    if not static:
        components.append(Item(name, 1))

    e = Entity(*components)

    clocks.register_entity(e)
    return e
