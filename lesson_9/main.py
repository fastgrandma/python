
# /////x = 10
# while x != 0:
#     print(x)
#     x -= 1 # то же самое , что и x = x - 1
#
# while True: # срабатывать каждый раз
#     break # остановка цикла выйти из цикла while
#
# # for
# lst = ["А", "Б", "В", "Г", "Д"]
# for letter in lst: # проитеррироваться по списку
#     print(letter)
#
# for i in range(0, 3):
#     print(i)


# word = input("введи слово быстро")
# while word: # пока слово не пустое (из-за типа строчка)
#     print(word, end=" ")
#     word = word[:-1]
#
# # x = int(input("введи число"))
# # while x:
# #     x -= 1
# #     if x % 2 == 0:
# #         print(x)
# #
# x = int(input("Введи циферку: "))
# step = 0
# while x != 1:
#     step += 1  # то же самое, что step = step + 1
#     if x % 2 == 0:
#         print(f"{step})", end=" ")
#         print(x, "* 3 + 1 =", end=" ")
#         x = x // 2
#     else:
#         print(f"{step})", end=" ")
#         print(x, " / 2 =", end=" ")
#         x = 3 * x + 1
#    print(x)
#  print("Шагов:", step)