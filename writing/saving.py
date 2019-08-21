import os

from writing.scripting import is_skipping
from writing.tools import request_choice
from writing.io import input_line
from writing.global_data import data, DATA_FOLDER_PATH


save_is_loaded = False

SAVES_FOLDER_PATH = f'{DATA_FOLDER_PATH}/saves'


def saving_choice():
    NOTHING_VARIANT = "Не загружать сохранение"

    if not os.path.isdir(SAVES_FOLDER_PATH):
        os.mkdir(SAVES_FOLDER_PATH)

    choice_ = request_choice(
        [NOTHING_VARIANT] + [path for path in os.listdir(SAVES_FOLDER_PATH) if path.endswith('.txt')],
        enumeration_start=0
    )

    if choice_ == NOTHING_VARIANT:
        input_line.reset()
        return

    with open(f'{SAVES_FOLDER_PATH}/{choice_}') as save_file:
        lines = [l.replace('\n', '') for l in save_file]

    input_line.reset()
    input_line.saved_lines = lines

    global save_is_loaded
    save_is_loaded = True


def checkpoint(*important_data):
    if is_skipping:
        return

    global save_is_loaded
    if save_is_loaded:
        save_is_loaded = False
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
