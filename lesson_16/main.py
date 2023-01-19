# # def plus_one(a, b):  # обьявление функции с 2 аргументами
# #     return a + b + 1
# #
# # print(plus_one(5, 4))
# #
# #
# #
# # # Лямбда(lambda) функции
# # plus_one2 = lambda a, b: a + b + 1
# # print(plus_one2(5, 4))
#
# # result = lambda answer: if answer == "Д"
#
#
#
# # List comprehenshion (генератор списка)
# spisok = []
# for i in range(5):
#     spisok.append(i)
# print(spisok)
#
# spisok2 = [n for n in range(1, 6)]
# # 1. list comprehension
# # 2. for n in  range(1, 6) обычный цикл for
# # 3. все что слева от for -> элемент списка
# print(spisok2)

# 1 zadachka
# c2f = lambda c:c * 9/5 + 32
# f2c = lambda f:(f - 32) * 5/9
# c2k = lambda c:c + 273.15
# k2 = lambda k:k - 273.15
# f2k = lambda f:c2k(f2c(f))
# print(c2k(203))


# задача 2
# from random import randint
# banana = lambda zxc: True if zxc == "Д"
# arbuz = int(input('слыш сколько раз бросаешь?'))
# dies = [randint(1, 6) for n in range(1, 7)]
# print(dies)
# kivi = input("выходищьь?да/нит ").upper()
#
# if banana(kivi):
#     break

from random import choice
# chars =
#
#
#
#
#
#
#
#
#
#
# cot = [choice(choice(chars) for n in range(6)]
# cotik = "".join(cot)
# dictionarry
# print("ссылка уже есть в базе вот ее кот :")
# print(dic)

# задача 3
u = lambda a, b:a / b
print(u(6, 3))
u3 = lambda a, b:a // b
print(u3(6,3))
u4 = lambda a, b:a**b
print(u4(6, 3))
u5 = lambda a:-a if a < 0 else a
# то мен
print(u5(6, 3))