BOOKS_FOLDER = 'assets/books'


class Book:
    def __init__(self, title):
        self.title = title

        with open(f'{BOOKS_FOLDER}/{title}.txt') as file:
            self.content = [line.replace('\n', '') for line in file if line != '\n']