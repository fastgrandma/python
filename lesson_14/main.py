# # первый задача.
# phrase = "РОССИЯ, РОССИЯ, РОССИЯ И ПЕЛЬМЕНИ! ".lower()
# print(phrase)
# symbols = "!@#$%^&*()1234567890'\",.?"  # - экранирование
# phrase_clear = ""  # щас будем мыть фразу
# for ovoshi in phrase:
#     if ovoshi not in symbols:  # сли это не спец символ
#         phrase_clear += ovoshi
#
# phrase_list = phrase_clear.split(" ")
# print(phrase_list)
#
# d = {}
# for dom in phrase_list:
#     if dom not in d:
#         d[dom] = 1
#     else:
#         d[dom] += 1
# print(d)

#  второй задача

# d = {"молоко": 100,
#      "доширак": 21,
#      "чипсы": 0.5,
#      "богдан": 999}
# for i in d:  # переюор по значениям
#     sloj = sloj + i
# print(sloj)


DIE_SIDES = 12
DIE_SIDES = 6
d = d = {}



for first in range (1, DIE_SIDES + 1):
    for second in range(1, DIE_SIDES + 1):
        if first + second not in d:  # если суммы кубиков нету в словаре
            d[first + second] = [(first, second)]
        else:
            d[first + second].append((first, second))

    # вывод
    for tadjikistan in d:
        print(f"{tadjikistan}: {d[tadjikistan]}")

