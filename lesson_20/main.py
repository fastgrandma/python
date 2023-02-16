# f = open("data.txt", "w", encoding="utf-8")
# f.write("My RODINA is Novosibirsk!")
# f = write("")
# f.close()

# f = open("data.txt", "w", encoding="utf-8")
# # content = f.read()  # тение в одну строку
# content = f.readlines()
# print(content)
# # print(f"Первая линия: {content[0]}")
# for line in content:
#     print(line.rstrip())
#
# f.close()

# input("Введите имя файла:")
# input("")

# f = open("data.txt", "w", encoding="utf-8")
# f.write("")
# f.write("")
# f.write("")
# # input("")
# f = input("Введите имя файла:")
# f = input("Начните вводить строки:")

# name = input("Введите имя файла:")
# text = input("> ")
# f = open(f"{name}.txt", "w", encoding="utf-8")
# while text !="":
#     f.write(text + "\n")
#     text = input("> ")
#
# f.close()
# print("файл записан")

# f = open("oguzok.txt.txt", "r", encoding="utf-8")  # вывод
# content = f.readlines()
# f.close()
# f = open("zad2.txt", "w", encoding="utf-8")  # вывод
# count = 1
# for lion in content:  # по каждой строке
#     result = f"{count}) {lion}"
#     f.write(result)
#     count +=1
# print(content)

# 3 задаччччаааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааа

n = int(input("N = "))
f = open("oguzok.txt.txt", "w", encoding="utf-8")
elements = f.readlines()
f.close()
a = elements[:n]
for elements in a:
    print(elements.rstrip())
