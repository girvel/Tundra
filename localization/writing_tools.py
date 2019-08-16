from console.tools import request
from core.playing.scenario_player import scenario_player
from core.writing.character import Character
from core.modelling.scenario import scenario
from core.writing.scenario_writer import scenario_writer


Персонаж = Character
запрос = request

сценарий = scenario

сцена = scenario_writer.scene
замена = scenario_writer.replace
вариант = scenario_writer.choice
переход = scenario_writer.goto


def имя(значение):
    scenario.name = значение


def начать_игру():
    scenario_player.play(scenario)
