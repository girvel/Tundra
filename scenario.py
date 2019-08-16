from localization.writing_tools import *


# Scenario
имя("Тундра")


# Characters
ГГ = Персонаж(запрос("Bаше имя"))
Вождь = Персонаж("Вождь")
Разум = Персонаж("Голос разума")
Сердце = Персонаж("Голос сердца")

замена("%ГГ%", ГГ.name)


# Scenes
сцена(
    "Пролог. Исход",
    "Иней медленно покрывал кружку с заледеневшим чаем. С глухим звуком разгерметизации отворилась круглая дверь. "
    "%ГГ% открыл глаза.")

Вождь("Мы уходим, %ГГ%. Собирай вещи.")
ГГ("Что?")
Вождь("Сердце древа охладело к нашему народу. Настало время уходить, %ГГ%.")

Разум("Уходить - нельзя. У тебя свой путь. Солги ему.")
Сердце("Здесь твой дом. Тебе надо попрощаться.")
Разум("Я не понял, ты за кого вообще?")


вариант("Я останусь.")

Вождь("Традиции превыше всего. Пора.")
Сердце("Заладил со своими традициями, сколько уже можно?")
ГГ("Я никуда не пойду.")
Вождь("Твое право. Отныне и во веки веков, %ГГ%, ты отречен от паствы и изгнан. "
      "Весь твой род, братья, сестры и собратья будут нести бремя изгнания, пока не поглотит их земля. "
      "Прочь из моего дома.")

переход("Глава I. Уход.")


вариант("Мне нужно время, чтобы собраться.")

Вождь("Таинство начнется в полночь. Поторопись.")
Разум("Инсулин.")

переход("Глава I. Уход.")


сцена(
    "Глава I. Уход.",
    "Перед %ГГ% разостлалась бескрайняя ледяная пустошь, окутанная метелью. Позади еще виднелся его былой дом, "
    "расположившийся на дне небольшой впадины, который теперь был почти полностью засыпан снегом. Впереди виднелись "
    "пики древних ледников.")

Разум("Ты не выживешь.")


if __name__ == '__main__':
    начать_игру()
