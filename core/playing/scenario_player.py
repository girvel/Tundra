import platform
import os
from core.playing.fake_input import FakeInput


class ScenarioPlayer:
    @staticmethod
    def load_input():
        data_path = {
            'Linux': f'{os.getenv("HOME")}/.Tundra',
            'Windows': f'{os.getenv("APPDATA")}/Tundra'
        }[platform.system()]

        try:
            with open(f'{data_path}/saves/default.txt') as save_file:
                return FakeInput([l[:-1] for l in save_file])
        except FileNotFoundError:
            return FakeInput([])

    @staticmethod
    def play(scenario_):
        input = ScenarioPlayer.load_input()
        current_monologue = scenario_.root_monologue

        while True:
            for replica in current_monologue.replicas:
                replica = str(replica)

                for r in scenario_.replaces:
                    replica = replica.replace(r.shortcut, r.value)

                print(replica, end='')
                input()

            if len(current_monologue.choices) == 0:
                break

            if len(current_monologue.choices) == 1 and current_monologue.choices[0].text == "":
                current_monologue = current_monologue.choices[0].next_monologue
                continue

            print()
            for i, choice in enumerate(current_monologue.choices):
                print(f'{i + 1}. {choice.text}')

            while True:
                choice = input()

                if choice.isdigit():
                    choice = int(choice) - 1
                    if 0 <= choice < len(current_monologue.choices):
                        break

            current_monologue = current_monologue.choices[choice].next_monologue
            print()


scenario_player = ScenarioPlayer()
