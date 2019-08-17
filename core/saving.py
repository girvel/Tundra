import os

from console.tools import request_choice
from core import io
from core.fake_input import FakeInput
from core.global_data import SAVES_FOLDER_PATH, global_data
from core.io import input_line
from core.writing import is_skipping

save_is_loaded = False


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


def checkpoint(*important_data):
    if is_skipping:
        return

    global save_is_loaded
    if not save_is_loaded:
        save_is_loaded = True
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