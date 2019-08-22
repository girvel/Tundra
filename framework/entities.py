from core.book import Book
from core.inventory import Inventory
from core.item import Item
from ecs.entity import Entity
from framework.game import clocks, player


def __new_entity(*components):
    e = Entity(*components)

    clocks.register_entity(e)
    return e


def has_item(item_, entity=None):
    if entity is None:
        entity = player

    return any(i == item_ for i in entity.inventory.content)


def book(name, static=False):
    components = [Book(name)]

    if not static:
        components.append(Item(name, 0.3))

    return __new_entity(*components)


def item(name, weight):
    return __new_entity(Item(name, weight))


# def npc()
