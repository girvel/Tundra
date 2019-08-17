import os

from console.tools import request_choice
from core.io import *
from core.fake_input import FakeInput
from core.global_data import data, DATA_FOLDER_PATH
from core.writing import is_skipping

save_is_loaded = False

SAVES_FOLDER_PATH = f'{DATA_FOLDER_PATH}/saves'


def saving_choice():
    global input_line
    NOTHING_VARIANT = "Не загружать сохранение"

    choice_ = request_choice(
        [NOTHING_VARIANT] + [path for path in os.listdir(SAVES_FOLDER_PATH) if path.endswith('.txt')],
        enumeration_start=0
    )

    if choice_ == NOTHING_VARIANT:
        input_line.reset()
        return

    with open(f'{SAVES_FOLDER_PATH}/{choice_}') as save_file:
        variants = [l.replace('\n', '') for l in save_file]

    input_line = FakeInput(variants)


def checkpoint(*important_data):
    if is_skipping:
        return

    global save_is_loaded
    if not save_is_loaded:
        save_is_loaded = True
        return

    n = int(data.autosaves_number)
    name = 'autosave{0}{1}{2}'.format(
        n,
        ": " if len(important_data) > 0 else "",
        ", ".join(important_data)
    )

    data.autosaves_number = n + 1

    with open(f'{SAVES_FOLDER_PATH}/{name}.txt', 'w') as file:
        file.write("\n".join(input_line.saved_lines))
