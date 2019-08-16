import platform
import os

from console.tools import request_choice
from core.playing.fake_input import FakeInput


def load_input():
    saves_path = {
        'Linux': f'{os.getenv("HOME")}/.Tundra',
        'Windows': f'{os.getenv("APPDATA")}/Tundra'
    }[platform.system()] + '/saves'

    file = request_choice([path for path in os.listdir(saves_path) if path.endswith('.txt')])

    try:
        with open(f'{saves_path}/{file}') as save_file:
            variants = [l[:-1] for l in save_file]
    except FileNotFoundError:
        variants = []

    return FakeInput(variants)


class ScenarioPlayer:
    def __init__(self):
        self.input = load_input()

    def play(self, scenario_):
        current_monologue = scenario_.root_monologue

        while True:
            for replica in current_monologue.replicas:
                replica = str(replica)

                for r in scenario_.replaces:
                    replica = replica.replace(r.shortcut, r.value)

                print(replica, end='')
                self.input()

            if len(current_monologue.choices) == 0:
                break

            if len(current_monologue.choices) == 1 and current_monologue.choices[0].text == "":
                current_monologue = current_monologue.choices[0].next_monologue
                continue

            current_monologue = request_choice(current_monologue.choices, input=self.input).next_monologue
            print()


scenario_player = ScenarioPlayer()
