# x = "Антон\nАнтон\nАнтон"
# x1 = """Строка 1
# Строка 2
# Строка 3"""
# print(x1)

# name_1 = "глеб"
# name_2 = "кирилл"
# name_3 = "Паша"
#
# bratva = [name_1, name_2, name_3]
# print(bratva)
# print(bratva[0])
# print(bratva[-3])
#
# alphabet = "АБВГДЕЁЖЗИКЛМН"
# print(alphabet[0])
# print(alphabet[-1])
# print(alphabet[0]) + alphabet[1] + alphabet[2])
# print(alphabet[0:3])
# print(alphabet[-3:])

# x = input("введи слово: ")
# print("первая буква:", [0])
# print("последняя буква:", x[-1])
# temp = x[-1]
# print(x.index(temp) + 1)
# print(len(x))

# path = "C:/Python3/python.exe"
# temp = path.split("/")
# print(temp)
# print("Имя файла: ", temp[-1])
# print("Расширение: ", temp[-1][-3:])
# print("ИМя каталога:", temp[1])
# print("полный путь к каталогу:", temp[0] + "/" +  temp[1])

chapter_1 = input("Глава 1: ")
page_1 = input("страница: ")

chapter_2 = input("Глава 2: ")
page_2 = input("страница: ")

print(chapter_1.ljust, page_1.rjust(15))
print(chapter_2.ljust, page_2.rjust(15))

