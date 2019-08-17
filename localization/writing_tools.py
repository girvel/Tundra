from core.writing import \
    scene, Character, request, set_phrase_replace, choice, goto, point
from core.saving import saving_choice, checkpoint
from ecs.time import Time
from ecs.world_clocks import WorldClocks

clocks = WorldClocks(Time(minutes=1))

Персонаж = Character

выбор_сохранения = saving_choice
сцена = scene
запрос = request
замена = set_phrase_replace
точка = point
выбор = choice
переход = goto
сохранение = checkpoint


def прошло(годы=0, месяцы=0, дни=0, часы=0, минуты=0, секунды=0):
    clocks(Time(
        years=годы,
        months=месяцы,
        days=дни,
        hours=часы,
        minutes=минуты,
        seconds=секунды
    ))
