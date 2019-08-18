def Книга(имя, статичная=False):
    return Book(имя, static=статичная)


def Место(*содержание):
    return Place(*содержание)


BOOKS_FOLDER = 'assets/books'


class Book:
    def __init__(self, title, static=False):
        self.title = title
        self.static = static

        with open(f'{BOOKS_FOLDER}/{title}.txt') as file:
            self.content = [line.replace('\n', '') for line in file if line != '\n']

        if not static:
            raise NotImplementedError()


class Place:
    def __init__(self, name, content):
        self.name = name
        self.content = content
