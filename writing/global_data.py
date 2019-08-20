import os
import platform

DATA_FOLDER_PATH = {
    'Linux': f'{os.getenv("HOME")}/.Tundra',
    'Windows': f'{os.getenv("APPDATA")}/Tundra'
}[platform.system()]
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

    def __repr__(self):
        return f'<GlobalData>'


data = GlobalData()
