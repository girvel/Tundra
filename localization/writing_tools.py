from writing.scripting import set_phrase_replace, scene, Character, look_around, request, point, goto, \
    goto_by_choice, description, testing_mode
from writing.saving import saving_choice, checkpoint
from ecs.time import Time
from game.game import clocks, player
from writing.tools import request_choice_index

Персонаж = Character

режим_тестирования = testing_mode
выбор_сохранения = saving_choice
сцена = scene
запрос = request
замена = set_phrase_replace
точка = point
выбор_перехода = goto_by_choice
переход = goto
сохранение = checkpoint
осмотреться = look_around
описание = description


def прошло(годы=0, месяцы=0, дни=0, часы=0, минуты=0, секунды=0):
    clocks(Time(
        years=годы,
        months=месяцы,
        days=дни,
        hours=часы,
        minutes=минуты,
        seconds=секунды
    ))


def выбор(*варианты):
    return request_choice_index(варианты, enumeration_start=1) + 1
