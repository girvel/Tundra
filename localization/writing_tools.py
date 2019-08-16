from console.tools import request
from core.character import Character
from core.scenario import scenario

Персонаж = Character
запрос = request

сценарий = scenario

сцена = scenario.scene
играть = scenario.play
замена = scenario.replace
вариант = scenario.choice
переход = scenario.goto


def имя(значение):
    scenario.name = значение
