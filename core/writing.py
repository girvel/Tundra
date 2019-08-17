import platform
import os

from termcolor import colored

from console.tools import request_choice
from core import io
from core.io import *
from core.replace import Replace

replaces = []

is_skipping = False
skip_for = None

is_loaded = False

DATA_FOLDER_PATH = {
    'Linux': f'{os.getenv("HOME")}/.Tundra',
    'Windows': f'{os.getenv("APPDATA")}/Tundra'
}[platform.system()]

SAVES_FOLDER_PATH = f'{DATA_FOLDER_PATH}/saves'

DATA_PATH = f'{DATA_FOLDER_PATH}/global_data.ini'


class GlobalData:
    def __init__(self):
        if os.path.isfile(DATA_PATH):
            return

        self.autosaves_number = 0

    def __getattr__(self, item):
        if os.path.isfile(DATA_PATH):
            with open(DATA_PATH) as data_file:
                for l in data_file:
                    if l.startswith(f'{item}='):
                        return l[len(item) + 1:]
        raise AttributeError()

    def __setattr__(self, key, value):
        new_content = []
        value_string = f'{key}={value}'
        replaced = False

        if os.path.isfile(DATA_PATH):
            with open(DATA_PATH) as data_file:
                for l in data_file:
                    if l.startswith(f'{key}='):
                        new_content.append(value_string)
                        replaced = True
                    else:
                        new_content.append(l)

                if not replaced:
                    new_content.append(value_string)
        else:
            new_content.append(value_string)

        with open(DATA_PATH, 'w') as data_file:
            data_file.write('\n'.join(new_content))


global_data = None


def load_data():
    global global_data
    global_data = GlobalData()


def saving_choice():
    NOTHING_VARIANT = "Не загружать сохранение"

    choice_ = request_choice(
        [NOTHING_VARIANT] + [path for path in os.listdir(SAVES_FOLDER_PATH) if path.endswith('.txt')],
        enumeration_start=0
    )

    if choice_ == NOTHING_VARIANT:
        io.input_line = FakeInput([])
        return

    with open(f'{SAVES_FOLDER_PATH}/{choice_}') as save_file:
        variants = [l.replace('\n', '') for l in save_file]

    global input_line
    input_line = FakeInput(variants)


def set_phrase_replace(shortcut, value):
    replaces.append(Replace(shortcut, value))


def phrase(text):
    if is_skipping:
        return

    for replace in replaces:
        text = text.replace(replace.shortcut, replace.value)

    print(text)
    input_line()


def scene(name, description):
    phrase(
        '\n\n\t{title}\n\n{description}\n'.format(
            title=colored(name.upper(), "red"),
            description=f'{description}\n' if description != '' else ''
        )
    )


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


def choice(*variants):
    goto(request_choice(variants, input_line, print_line))


class Character:
    def __init__(self, name):
        self.name = name

    def __call__(self, text):
        phrase(f'{colored(self.name, "red")}: {text}')


def checkpoint(*important_data):
    if is_skipping:
        return

    global is_loaded
    if not is_loaded:
        is_loaded = True
        return

    n = int(global_data.autosaves_number)
    name = 'autosave{0}{1}{2}'.format(
        n,
        ": " if len(important_data) > 0 else "",
        ", ".join(important_data)
    )

    global_data.autosaves_number = n + 1

    with open(f'{SAVES_FOLDER_PATH}/{name}.txt', 'w') as file:
        file.write("\n".join(input_line.saved_lines))
