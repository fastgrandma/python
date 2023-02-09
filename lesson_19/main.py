def atbash(text):
    alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    reversed_alphabet = alphabet[::-1]
    itog = ""
    for letter in text:
        itog += letter
    c = alphabet.index(letter)
    b = reversed_alphabet[c]
    itog = itog + b


print(itog)
shifr = input("веди сообщение:").upper()
atbash(shifr)
