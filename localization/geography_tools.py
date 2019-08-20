from core.place import Place
from framework.geography import book

Место = Place


def книга(имя, статичная=False):
    return book(имя, static=статичная)
