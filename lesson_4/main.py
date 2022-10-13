# familya = input("фамилия: ").capitalize()
# imya = input("имя: ").capitalize()
# otchestvo = input("отчество: ").capitalize()
#
# print(familya, imya[0] +  ".", otchestvo[0] + ".")
# print(f"{familya} {imya[0]}. {otchestvo[0]}.")
# word = input("введи фразочку: ")
# print("а:", word.count("а"))
# print("аб:",word.count("аб"))


# phrase = input("введи фразу, разделенную пробелами: ").strip()
# jst = phrase.split(" ")
# print(jst)
# jst.pop(0)
# jst.remove("антон")
# print(jst)


# phrase = input("введи ФраазУУ:")
# find = input("что меняем")
# replace = input("на что меняем: ")
#
# print(phrase.replace(find, replace))

# x = input()
# print(x.replace("йо", "ё"))
alphabet = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "e": "e",
    "ё": "yo",
    "ж": "zh",
    }

phrase = input("введи фразу: ")
translate = ""
for bukva in phrase:
    translate = translate +  alphabet[bukva]
print(translate)
