from writing.scripting import set_phrase_replace, scene, Character, look_around, request, point, goto, choice
from writing.saving import saving_choice, checkpoint
from ecs.time import Time
from game.game import clocks, player

Персонаж = Character

выбор_сохранения = saving_choice
сцена = scene
запрос = request
замена = set_phrase_replace
точка = point
выбор = choice
переход = goto
сохранение = checkpoint
осмотреться = look_around


def прошло(годы=0, месяцы=0, дни=0, часы=0, минуты=0, секунды=0):
    clocks(Time(
        years=годы,
        months=месяцы,
        days=дни,
        hours=часы,
        minutes=минуты,
        seconds=секунды
    ))
