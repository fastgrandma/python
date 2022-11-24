import random
import datetime

while True:
    number = input("сколько др генерируем? (до 70) ")
    if not number.isdigit() or int(number) < 2 or int(number) > 70:
        print("БРОТАНЧИК ЭТО НЕ СМЕШНО ПИШИ НОРМАЛТНО")
        print("-" * 5)
    else:
        number = int(number)
        break

birthdays = []
start0fYear = datetime.date(2022, 1, 1)
for _  in range(number):
    sdvig = random.randint(0,364)
    randomDay = datetime.timedelta(sdvig)
    birthday = start0fYear + randomDay
    birthdays.append(birthday)

for index in range(number):
    print(f"{index + 1}) {birthdays[index].strftime('%d.%m.%y')}")

print("=" * 10)
for i in set(birthdays):
    if birthdays.count(i) > 1:
        print(f"- {i.strftime('%d.%m.%y')}встречется { birthdays.count(i)}раза")

