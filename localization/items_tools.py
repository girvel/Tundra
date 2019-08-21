from core.place import Place
from framework.items import book, item, has_item

Место = Place
предмет = item
есть_предмет = has_item


def книга(имя, статичная=False):
    return book(имя, static=статичная)

