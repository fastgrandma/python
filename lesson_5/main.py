# # Списки
# name_1 = "тоха"
# name_2 = "Антон"
# name_3 = "Антуан"
# mega_anton = [name_1, name_2, name_3,]  # список
# # операции со списками
# mega_anton.append("Тоша")  # добавить элемент в список
# mega_anton.pop(2)  # удалить по индексу
# mega_anton.remove("Тоха")  # удалить по значению
#
# print(mega_anton)

# Индексация несколько раз
# man = [["Антон", "Гриша"], ["компутеры", "Настолки"], "Мама"]
# print(man[0][1]) # выводим Гришу
#
#
# x = 7
# if x == 7 or x > 10:
#     print("ура")
#
#
# number = float(input("введи число"))
# print(number)
# if number < 0: # если
#      print("Отрицательное")
# elif number > 0: # иначе если
#      print("все гуд парень,положительное")
# else: # иначе
#     print("число, на которое нельзя делить")

# year = int(input("введи год: ")
# if year % 4 == 0 and year % 400 == 0 or year % 100 != 0:
#     print("ВИСОКОСНЕНЬКОООООООООООООООО😎😎😎")
# else:
#     print("не ВИСООКОСНЕНЬКО{{{(>_<)}}}😢")

# number_1 = int(input("введи первое число"))
# operation = input("введи операцию (+, -, /, *, ^):").strip()
# number_2 = int(input("введи второе число: "))
# ist = ["+", "-","/","**","|"]  # список доп операций
# if operation in ist:
#     if operation == "+":
#         print(number_1 + number_2)
#     elif operation == "-":
#         print(number_1 - number_2)
#     elif operation == "/":
#         print(number_1 / number_2)
#     elif operation == "*":
#         print(number_1 * number_2)
#     elif operation == "**":
#         print(number_1 ** number_2)
#     elif operation == "|":
#         print(abs(number_1), abs(number_2))


# number_1 = int(input("Первое число: "))
# number_2 = int(input("второе число "))
# number_3 = int(input("второе число "))
#
# spisok = [number_1, number_2, number_3]
# print("максимальное число:", max(spisok))
# print("минимальное число:", min(spisok))
# min() - поиск минимума; max() - максимум

ticket = input("введи номер билета скорее")
if len(ticket) == 6 and ticket.isdigit():
    first_half = ticket[:3] # три первых числа
    last_half = ticket[-3] # три последних числа
    first_sum = int(first_half[0]) + int(first_half[1]) + int(first_half[2])
    last_sum = int(last_half[0]) + int(last_half[1]) + int(last_half[2])
    if first_sum == last_sum:
        print("счастливый")
    else:
        print("не счастливый")
else:
    print("у тебя кепка(шляпа)")
